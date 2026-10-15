#!/usr/bin/env python3
"""Offline pilot validation. Ruby/Psych parses YAML; Python standard library does the rest."""
import argparse
import csv
from datetime import datetime
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = '''README.md IMPLEMENTATION_CHECKLIST.md PILOT_TEST_PLAN.md
.github/ISSUE_TEMPLATE/test-request.yml .github/ISSUE_TEMPLATE/preparation-task.yml .github/ISSUE_TEMPLATE/config.yml
config/labels.json config/project.json
templates/approval-record.md templates/test-plan.md templates/readiness-checklist.md templates/run-log.csv
templates/results-summary.md templates/test-report.md templates/dvp-r.md templates/sensor-record.md
docs/standards/testing-lifecycle.md docs/standards/technical-testing.md docs/standards/verification-strategy.md
docs/guides/approvals.md docs/guides/testing-day.md docs/guides/closure.md docs/project-setup.md docs/data-storage.md docs/walkthrough.md
verification/vehicle.md verification/subsystems/drivetrain.md verification/subsystems/suspension.md
instrumentation/inventory.md examples/README.md examples/requests/engine-rpm.md examples/requests/brake-pressure.md
examples/requests/half-shaft-strain.md examples/preparation/brake-adaptation.md examples/preparation/strain-feasibility.md examples/follow-up.md examples/run-log.csv'''.split()
CSV_FIELDS = 'test_id run_id started_at ended_at configuration_ref conditions observations deviations raw_data_ref calibration_ref operator data_quality'.split()
STATUSES = ['Submitted','Screening','Awaiting Approval','Awaiting Capacity','Preparing','Ready','Scheduled','Executed','Analyzing','Closed']
REQUIRED_FORM = {
 'test-request.yml': {'subsystem','purpose','question','measurements','decision','consequences'},
 'preparation-task.yml': {'parent','resource','scope','dependencies','effort','estimate','evidence'},
}
# Reject duplicate YAML keys before safe_load; YAML parsers commonly silently overwrite them.
RUBY_PARSE = r'''
require 'yaml'
require 'json'
s = STDIN.read
walk = lambda do |node|
  if node.is_a?(Psych::Nodes::Mapping)
    keys = node.children.each_slice(2).map { |k,v| k.value }
    raise 'duplicate YAML key' unless keys.uniq.length == keys.length
  end
  (node.children || []).each { |c| walk.call(c) }
end
walk.call(Psych.parse_stream(s))
puts JSON.generate(YAML.safe_load(s, permitted_classes: [], permitted_symbols: [], aliases: false))
'''

def anchors(text):
    result, seen = set(), {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        slug = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        index = seen.get(slug, 0)
        seen[slug] = index + 1
        result.add(slug if not index else f'{slug}-{index}')
    return result

def validate(root):
    errors, counts = [], {'yaml':0, 'json':0, 'csv':0, 'markdown':0, 'local_links':0, 'forms':0, 'demo_requests':0}
    def check(condition, message):
        if not condition: errors.append(message)
    for name in REQUIRED:
        check((root/name).is_file(), f'Missing deliverable: {name}')
    parsed = {}
    for path in sorted(root.rglob('*')):
        if not path.is_file(): continue
        rel = str(path.relative_to(root))
        if path.suffix in ('.yml', '.yaml'):
            counts['yaml'] += 1
            try:
                result = subprocess.run(['ruby','-e',RUBY_PARSE],input=path.read_text(),text=True,capture_output=True)
                if result.returncode: raise ValueError(result.stderr.splitlines()[0])
                parsed[rel] = json.loads(result.stdout)
            except (ValueError, OSError) as e:
                errors.append(f'{rel}: YAML parse failed: {e}')
        elif path.suffix == '.json':
            counts['json'] += 1
            try:
                def pairs(items):
                    d = {}
                    for k,v in items:
                        if k in d: raise ValueError(f'duplicate JSON key {k}')
                        d[k] = v
                    return d
                parsed[rel] = json.loads(path.read_text(),object_pairs_hook=pairs)
            except ValueError as e: errors.append(f'{rel}: JSON parse failed: {e}')
    labels = parsed.get('config/labels.json', [])
    check(isinstance(labels,list), 'Label configuration must be an array')
    label_names = {x.get('name') for x in labels if isinstance(x,dict)} if isinstance(labels,list) else set()
    check(len(label_names)==len(labels), 'Labels must have unique names')
    for label in labels if isinstance(labels,list) else []:
        check(isinstance(label,dict) and bool(re.fullmatch(r'[0-9A-Fa-f]{6}',str(label.get('color','')))), 'Label color must have six hex digits')
    for name, required in REQUIRED_FORM.items():
        form = parsed.get('.github/ISSUE_TEMPLATE/'+name)
        if not isinstance(form,dict):
            errors.append(f'{name}: missing form object'); continue
        counts['forms'] += 1
        check(set(form) <= {'name','description','title','labels','assignees','projects','type','body'}, f'{name}: unknown top-level keys')
        for key in ('name','description','title'):
            check(isinstance(form.get(key),str) and bool(form[key].strip()), f'{name}: invalid {key}')
        check(set(form.get('labels',[])) <= label_names, f'{name}: undeclared label')
        body = form.get('body',[])
        check(isinstance(body,list) and bool(body), f'{name}: empty body')
        ids, labels_seen, found = set(), set(), set()
        for element in body if isinstance(body,list) else []:
            if not isinstance(element,dict):
                errors.append(f'{name}: form element must be object'); continue
            typ = element.get('type')
            check(typ in {'markdown','input','textarea','dropdown','checkboxes'}, f'{name}: unsupported element {typ}')
            check(set(element) <= {'type','id','attributes','validations'}, f'{name}: unsupported element keys')
            attrs = element.get('attributes',{})
            if not isinstance(attrs,dict):
                errors.append(f'{name}: attributes must be object'); continue
            if typ == 'markdown':
                check(isinstance(attrs.get('value'),str) and bool(attrs['value']), f'{name}: markdown requires value')
                continue
            eid, label = element.get('id',''), attrs.get('label','')
            check(isinstance(eid,str) and bool(re.fullmatch(r'[A-Za-z0-9_-]+',eid)) and eid not in ids, f'{name}: invalid/duplicate id {eid}')
            ids.add(eid)
            check(isinstance(label,str) and bool(label) and label not in labels_seen, f'{name}: invalid/duplicate label')
            labels_seen.add(label)
            validations = element.get('validations',{})
            check(isinstance(validations,dict) and set(validations) <= {'required'}, f'{name}: unsupported validations')
            if isinstance(validations,dict) and 'required' in validations:
                check(type(validations['required']) is bool, f'{name}: required must be boolean')
                if validations['required'] is True: found.add(eid)
            if typ == 'dropdown':
                options = attrs.get('options',[])
                check(isinstance(options,list) and bool(options) and all(isinstance(o,str) for o in options) and len(set(options))==len(options), f'{name}: invalid dropdown options')
        check(required <= found, f'{name}: required requester fields missing: {required-found}')
        if name == 'test-request.yml':
            check(not ({'requirements','timing','context'} & found), f'{name}: optional references/timing/context became required')
    check(parsed.get('.github/ISSUE_TEMPLATE/config.yml') == {'blank_issues_enabled':False}, 'Issue chooser config incorrect')
    project = parsed.get('config/project.json',{})
    check(isinstance(project,dict), 'Project specification must be object')
    if isinstance(project,dict):
        fields = {f['name']:f for f in project.get('fields',[])}
        check(fields.get('Status',{}).get('options') == STATUSES, 'Project Status options mismatch')
        check(fields.get('Disposition',{}).get('options') == ['Active','Clarification','Deferred','Declined','Cancelled'], 'Disposition options mismatch')
        check(len(fields) == len(project.get('fields',[])), 'Duplicate Project fields')
        check({v.get('name') for v in project.get('views',[])} == {'Pipeline','Preparation workload','Next testing day','Analysis & closure','Subsystem/DVP&R overview'}, 'Missing Project views')
    for path in sorted(root.rglob('*.csv')):
        counts['csv'] += 1
        rel = str(path.relative_to(root))
        try:
            with path.open(newline='') as f:
                reader = csv.DictReader(f,strict=True)
                check(reader.fieldnames == CSV_FIELDS, f'{rel}: CSV header mismatch')
                seen = set()
                for index,row in enumerate(reader,2):
                    check(set(row)==set(CSV_FIELDS) and all(row.get(k) for k in CSV_FIELDS), f'{rel}:{index}: missing/extra CSV values')
                    rid,tid = row.get('run_id',''),row.get('test_id','')
                    check(rid not in seen and bool(re.fullmatch(re.escape(tid)+r'-R\d{3}',rid)), f'{rel}:{index}: invalid/duplicate run ID')
                    seen.add(rid)
                    start,end = (datetime.fromisoformat(row[k].replace('Z','+00:00')) for k in ('started_at','ended_at'))
                    check(start.tzinfo is not None and end.tzinfo is not None and end >= start, f'{rel}:{index}: invalid time interval/offset')
        except (csv.Error,ValueError,TypeError,KeyError) as e: errors.append(f'{rel}: CSV error: {e}')
    # Check inline and reference-style relative Markdown links, including fragments; skip code fences.
    for path in sorted(root.rglob('*.md')):
        counts['markdown'] += 1
        text = re.sub(r'^```.*?^```\s*$', '', path.read_text(), flags=re.M|re.S)
        destinations = re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)',text)
        destinations += re.findall(r'^\[[^\]]+\]:\s*(\S+)',text,re.M)
        for destination in destinations:
            destination = unquote(destination.strip('<>'))
            if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',destination): continue
            counts['local_links'] += 1
            target,_,fragment = destination.partition('#')
            local = (path.parent/target).resolve() if target else path.resolve()
            check(local.is_relative_to(root.resolve()), f'{path.relative_to(root)}: link escapes package {destination}')
            check(local.exists(), f'{path.relative_to(root)}: broken link {destination}')
            if fragment and local.is_file() and local.suffix=='.md':
                check(fragment in anchors(local.read_text()), f'{path.relative_to(root)}: missing anchor {destination}')
    form = parsed.get('.github/ISSUE_TEMPLATE/test-request.yml',{})
    required_labels = [x['attributes']['label'] for x in form.get('body',[]) if x.get('validations',{}).get('required')] if isinstance(form,dict) else []
    purpose_options = next((x['attributes']['options'] for x in form.get('body',[]) if x.get('id')=='purpose'),[]) if isinstance(form,dict) else []
    for path in sorted((root/'examples/requests').glob('*.md')):
        counts['demo_requests'] += 1
        text = path.read_text()
        check('DEMO' in text and 'Hypothetical' in text, f'{path.name}: missing DEMO disclaimer')
        for label in required_labels:
            check(f'### {label}\n' in text, f'{path.name}: missing required form answer {label}')
        match = re.search(r'### Test purpose\n(.+)',text)
        check(bool(match) and match[1] in purpose_options, f'{path.name}: invalid purpose option')
    check(counts['demo_requests']==3,'Exactly three core DEMO request examples required')
    for path in sorted((root/'verification').rglob('*.md')):
        text = path.read_text()
        check('DEMO' in text,'DVP&R missing DEMO marker')
        rows = [x for x in text.splitlines() if x.startswith('| DEMO-')]
        check(bool(rows),f'{path.name}: no DVP&R entries')
        for row in rows:
            cells = [x.strip() for x in row.strip('|').split('|')]
            check(len(cells)==10 and cells[-1]=='not planned',f'{path.name}: demonstration claims status or malformed DVP&R')
    check(not (root/'.github/workflows').exists(),'Pilot must not ship live workflows')
    return errors,counts

def self_test():
    def corrupt_form(root):
        p=root/'.github/ISSUE_TEMPLATE/test-request.yml'
        p.write_text(p.read_text().replace('required: true','required: false',1))
    def corrupt_csv(root):
        p=root/'examples/run-log.csv';p.write_text(p.read_text().replace('run_id','wrong_header',1))
    def corrupt_yaml(root):
        (root/'.github/ISSUE_TEMPLATE/config.yml').write_text('invalid: [\n')
    def corrupt_link(root):
        p=root/'README.md';p.write_text(p.read_text()+'\n[broken](missing.md)\n')
    def corrupt_anchor(root):
        p=root/'README.md';p.write_text(p.read_text()+'\n[broken anchor](README.md#missing-anchor)\n')
    def corrupt_duplicate(root):
        (root/'.github/ISSUE_TEMPLATE/config.yml').write_text('blank_issues_enabled: false\nblank_issues_enabled: true\n')
    mutations=[('required form field',corrupt_form),('CSV schema',corrupt_csv),('YAML syntax',corrupt_yaml),('relative link',corrupt_link),('Markdown anchor',corrupt_anchor),('duplicate YAML key',corrupt_duplicate),('missing deliverable',lambda r:(r/'templates/test-plan.md').unlink())]
    for name, mutate in mutations:
        with tempfile.TemporaryDirectory(prefix='baja-validator-test-') as tmp:
            r=Path(tmp)/'pilot';shutil.copytree(ROOT,r)
            mutate(r)
            errors,_=validate(r)
            if not errors:
                print(f'FAIL: validator did not reject {name}');return 1
            print(f'PASS: rejected {name}')
    return 0

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    if args.self_test: sys.exit(self_test())
    errors,counts=validate(ROOT)
    print(json.dumps(counts,sort_keys=True))
    for error in errors: print('ERROR:',error)
    print(f'{"PASS" if not errors else "FAIL"}: {len(errors)} error(s). Live GitHub/manual checks remain pending.')
    sys.exit(bool(errors))
