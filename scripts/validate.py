#!/usr/bin/env python3
"""Offline repository checks; Python 3.9+ and Ruby/Psych, no packages or network."""
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
from urllib.parse import unquote, urlsplit, parse_qs

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = '''README.md HANDOFF.md VALIDATION_REPORT.md IMPLEMENTATION_CHECKLIST.md PILOT_TEST_PLAN.md
.github/ISSUE_TEMPLATE/test-request.yml .github/ISSUE_TEMPLATE/preparation-task.yml .github/ISSUE_TEMPLATE/config.yml
config/labels.json config/project.json
scripts/validate.py templates/approval-record.md templates/test-plan.md templates/readiness-checklist.md templates/run-log.csv
templates/results-summary.md templates/test-report.md templates/dvp-r.md templates/sensor-record.md templates/calibration-record.md
docs/standards/testing-lifecycle.md docs/standards/technical-testing.md docs/standards/verification-strategy.md
docs/guides/subsystem-lead.md docs/guides/managers.md docs/guides/testing-manager.md docs/guides/test-lead.md docs/guides/instrumentation.md
docs/guides/approvals.md docs/guides/testing-day.md docs/guides/closure.md docs/project-setup.md docs/data-storage.md docs/walkthrough.md docs/repository-audit.md
verification/README.md verification/vehicle.md verification/subsystems/drivetrain.md verification/subsystems/suspension.md
instrumentation/inventory.md examples/README.md examples/requests/engine-rpm.md examples/requests/brake-pressure.md
examples/requests/half-shaft-strain.md examples/preparation/brake-adaptation.md examples/preparation/strain-feasibility.md
examples/preparation/strain-integration.md examples/follow-up.md examples/run-log.csv examples/instrumentation.md examples/vehicle-validation.md examples/data/README.md'''.split()
CSV_FIELDS = 'test_id run_id started_at ended_at configuration_ref conditions observations deviations raw_data_ref calibration_ref operator data_quality'.split()
STATUSES = ['Submitted','Screening','Awaiting Approval','Awaiting Capacity','Preparing','Ready','Scheduled','Executed','Analyzing','Closed']
VIEWS = {'Pipeline','Preparation workload','Confirmed testing','Analysis backlog','Subsystem/DVP&R overview'}
REQUIRED_FORM = {
 'test-request.yml': {'subsystem','purpose','question','measurements','decision','consequences','timing'},
 'preparation-task.yml': {'parent','resource','scope','dependencies','effort','estimate','evidence'},
}
ATTRIBUTES = {
 'markdown': {'value'}, 'input': {'label','description','placeholder','value'},
 'textarea': {'label','description','placeholder','value','render'},
 'dropdown': {'label','description','options','multiple','default'},
}
# Detect duplicate keys before safe_load, which otherwise silently overwrites them.
RUBY_PARSE = r'''
require 'yaml'
require 'json'
walk = lambda do |node|
  if node.is_a?(Psych::Nodes::Mapping)
    keys = node.children.each_slice(2).map { |k,v| k.value }
    raise 'duplicate YAML key' unless keys.uniq.length == keys.length
  end
  (node.children || []).each { |c| walk.call(c) }
end
s = STDIN.read
walk.call(Psych.parse_stream(s))
puts JSON.generate(YAML.safe_load(s, permitted_classes: [], permitted_symbols: [], aliases: false))
'''

def tracked_files(root):
    return sorted(p for p in root.rglob('*') if p.is_file() and not any(x in {'.git','__pycache__'} for x in p.relative_to(root).parts))

def without_code(text):
    lines, fence = [], None
    for line in text.splitlines():
        mark = re.match(r'^\s*(`{3,}|~{3,})',line)
        if mark:
            if fence is None: fence = mark[1]
            elif mark[1][0] == fence[0] and len(mark[1]) >= len(fence): fence = None
            continue
        if fence is None: lines.append(line)
    return re.sub(r'(`+).*?\1','', '\n'.join(lines))

def anchors(text):
    seen, result = {}, set()
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$',without_code(text),re.M):
        slug = re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-')
        n = seen.get(slug,0); seen[slug] = n+1
        result.add(slug if not n else f'{slug}-{n}')
    return result

def destinations(text):
    """Repository Markdown subset: inline/image links, explicit/collapsed references."""
    text = without_code(text)
    refs = {k.strip().casefold():v for k,v in re.findall(r'^\[([^\]]+)\]:\s*(<[^>]+>|\S+)',text,re.M)}
    targets = re.findall(r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+["\x27][^\n]*?["\x27])?\s*\)',text)
    missing = []
    for label, key in re.findall(r'!?\[([^\]\n]+)\]\[([^\]\n]*)\]',text):
        key = (key or label).strip().casefold()
        if key in refs: targets.append(refs[key])
        else: missing.append(key)
    targets += list(refs.values())
    return targets, missing

def answers(text):
    return {label:content.strip() for label,content in re.findall(r'^### ([^\n]+)\n(.*?)(?=^#{1,3} |\Z)',text,re.M|re.S)}

def validate(root):
    root = root.resolve()
    errors = []
    counts = dict.fromkeys(('files','yaml','json','forms','markdown','local_links','form_routes','csv','runs','request_examples','preparation_examples','dvp_rows'),0)
    def check(ok,msg):
        if not ok: errors.append(msg)
    for path in REQUIRED: check((root/path).is_file(),f'Missing deliverable: {path}')
    files = tracked_files(root); counts['files'] = len(files)
    parsed = {}
    for p in files:
        rel = str(p.relative_to(root))
        check(not p.is_symlink(),f'{rel}: symlinks are not allowed in the package')
        if p.suffix in {'.yml','.yaml','.json'}:
            kind = 'json' if p.suffix=='.json' else 'yaml'; counts[kind] += 1
            try:
                if kind=='yaml':
                    result = subprocess.run(['ruby','-e',RUBY_PARSE],input=p.read_text(),text=True,capture_output=True,timeout=15)
                    if result.returncode: raise ValueError(result.stderr.splitlines()[0])
                    parsed[rel] = json.loads(result.stdout)
                else:
                    def unique(items):
                        d = {}
                        for k,v in items:
                            if k in d: raise ValueError(f'duplicate key {k}')
                            d[k] = v
                        return d
                    parsed[rel] = json.loads(p.read_text(),object_pairs_hook=unique)
            except (ValueError,OSError,subprocess.TimeoutExpired) as e: errors.append(f'{rel}: {kind.upper()} parse failed: {e}')
        text = p.read_text()
        if p.suffix in {'.md','.yml','.json'}: check(not re.search(r'\bleadership\b',text,re.I),f'{rel}: use Managers terminology')
        if p.suffix in {'.md','.yml','.json'}:
            for role in ('Subsystem Lead','Instrumentation Owner','Analysis Owner','Electronics Manager','Test Lead','Testing Manager'):
                check(not any(m[0]!=role and m[0]!=role+'s' for m in re.finditer(r'\b'+role+r's?\b',text,re.I)),f'{rel}: inconsistent role capitalization: {role}')
        for rule in (r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'\bgh[pousr]_[A-Za-z0-9]{20,}\b',r'\bgithub_pat_[A-Za-z0-9_]{20,}\b',r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',r'/Users/[A-Za-z][A-Za-z0-9._-]+/'):
            check(not re.search(rule,text),f'{rel}: potential secret/private path; inspect locally')
    labels = parsed.get('config/labels.json',[])
    if not isinstance(labels,list): errors.append('Label config must be a list'); labels=[]
    names = [x.get('name') for x in labels if isinstance(x,dict)]
    check(len(names)==len(labels)==len(set(names)),'Labels must have unique names/objects')
    for label in labels:
        check(isinstance(label,dict) and bool(re.fullmatch('[0-9A-Fa-f]{6}',str(label.get('color','')))),'Label color must be six hexadecimal digits')
    forms = {}
    for name,required in REQUIRED_FORM.items():
        form = parsed.get('.github/ISSUE_TEMPLATE/'+name)
        if not isinstance(form,dict): errors.append(f'{name}: form must be an object'); continue
        forms[name] = form; counts['forms'] += 1
        check(set(form) <= {'name','description','title','labels','body'},f'{name}: unsupported/automation top-level keys')
        for key in ('name','description','title'): check(isinstance(form.get(key),str) and bool(form[key].strip()),f'{name}: {key} must be a nonempty string')
        check(len(str(form.get('name',''))) > 3,f'{name}: name too short for chooser')
        label_list = form.get('labels',[])
        check(isinstance(label_list,list) and all(x in names for x in label_list),f'{name}: invalid/undeclared labels')
        body = form.get('body')
        if not isinstance(body,list): errors.append(f'{name}: body must be a list'); continue
        ids,field_labels,found = set(),set(),set()
        for e in body:
            if not isinstance(e,dict): errors.append(f'{name}: element must be object'); continue
            typ = e.get('type'); attrs = e.get('attributes')
            check(set(e) <= {'type','id','attributes','validations'},f'{name}: invalid element keys')
            if typ not in ATTRIBUTES or not isinstance(attrs,dict): errors.append(f'{name}: unsupported element/attributes'); continue
            check(set(attrs) <= ATTRIBUTES[typ],f'{name}: unknown {typ} attribute')
            for k,v in attrs.items():
                if k not in {'options','default','multiple'}: check(isinstance(v,str),f'{name}: {k} must be string')
            if typ=='markdown':
                check(bool(attrs.get('value')) and 'validations' not in e,f'{name}: invalid markdown element'); continue
            eid,label = e.get('id'),attrs.get('label')
            check(isinstance(eid,str) and bool(re.fullmatch(r'[A-Za-z0-9_-]+',eid)) and eid not in ids,f'{name}: invalid/duplicate element ID')
            check(isinstance(label,str) and bool(label.strip()) and label not in field_labels,f'{name}: invalid/duplicate label')
            if isinstance(eid,str): ids.add(eid)
            if isinstance(label,str): field_labels.add(label)
            validations = e.get('validations',{})
            if not isinstance(validations,dict): errors.append(f'{name}: validations must be object'); validations={}
            check(set(validations) <= {'required'},f'{name}: unsupported validations')
            if 'required' in validations:
                check(type(validations['required']) is bool,f'{name}: required must be boolean')
                if validations['required'] is True: found.add(eid)
            if typ=='dropdown':
                opts = attrs.get('options')
                valid = isinstance(opts,list) and bool(opts) and all(isinstance(o,str) and o.strip() for o in opts)
                check(valid and len(set(opts))==len(opts),f'{name}: invalid/duplicate dropdown options')
                if 'default' in attrs: check(type(attrs['default']) is int and valid and 0 <= attrs['default'] < len(opts),f'{name}: invalid dropdown default')
                if 'multiple' in attrs: check(type(attrs['multiple']) is bool,f'{name}: multiple must be boolean')
        check(found==required,f'{name}: required fields mismatch: {found.symmetric_difference(required)}')
    check(len({f.get('name') for f in forms.values()})==len(forms),'Issue form names must be unique')
    check(parsed.get('.github/ISSUE_TEMPLATE/config.yml')=={'blank_issues_enabled':False},'Issue chooser config mismatch')
    def link(source,destination):
        destination = unquote(destination.strip('<>'))
        parts = urlsplit(destination)
        if parts.scheme or parts.netloc:
            if parts.netloc=='github.com' and parts.path=='/McGill-Baja-Racing/Testing/issues/new':
                template = parse_qs(parts.query).get('template',[''])[0]
                counts['form_routes'] += 1
                check(template in forms,f'{source.relative_to(root)}: invalid GitHub form route')
            return
        counts['local_links'] += 1
        target = (source.parent/parts.path).resolve() if parts.path else source.resolve()
        check(target.is_relative_to(root),f'{source.relative_to(root)}: path escapes package')
        check(target.exists(),f'{source.relative_to(root)}: broken link {destination}')
        if parts.fragment and target.is_file() and target.suffix=='.md': check(parts.fragment in anchors(target.read_text()),f'{source.relative_to(root)}: broken anchor {destination}')
    for p in (x for x in files if x.suffix=='.md'):
        counts['markdown'] += 1
        targets,missing = destinations(p.read_text())
        for ref in missing: errors.append(f'{p.relative_to(root)}: undefined reference {ref}')
        for dest in targets: link(p,dest)
    project = parsed.get('config/project.json',{})
    if not isinstance(project,dict): errors.append('Project config must be object'); project={}
    fs,vs = project.get('fields',[]),project.get('views',[])
    fields = {f['name']:f for f in fs if isinstance(f,dict) and isinstance(f.get('name'),str)} if isinstance(fs,list) else {}
    views = {v['name']:v for v in vs if isinstance(v,dict) and isinstance(v.get('name'),str)} if isinstance(vs,list) else {}
    check(len(fields)==len(fs),'Duplicate or malformed Project fields')
    check(fields.get('Status',{}).get('options')==STATUSES,'Project Status mismatch')
    check(fields.get('Disposition',{}).get('options')==['Active','Clarification','Deferred','Declined','Cancelled'],'Disposition mismatch')
    check(set(views)==VIEWS,'Project views mismatch')
    setup = (root/'docs/project-setup.md').read_text() if (root/'docs/project-setup.md').exists() else ''
    for field in fields.values():
        check(field.get('type') in {'single_select','text','date'} and bool(field.get('owner')),'Invalid Project field type/owner')
        if field.get('type')=='single_select':
            opts=field.get('options',[])
            check(isinstance(opts,list) and all(isinstance(x,str) for x in opts) and bool(opts) and len(set(opts))==len(opts),'Invalid field options')
    for view in views.values():
        check(view.get('layout') in {'board','table'},'Invalid view layout')
        for k in ('group_by','sort_by'):
            if k in view: check(view[k] in fields,f'{view["name"]}: unknown grouping/sorting field')
        check('-label:demo' in view.get('filter',''),f'{view["name"]}: DEMO must be excluded')
        check(view.get('filter','MISSING') in setup,f'{view["name"]}: guide/config filter drift')
    confirmed=views.get('Confirmed testing',{}).get('filter','')
    check('status:Scheduled' in confirmed and 'Ready' not in confirmed,'Confirmed view must exclude Ready backlog')
    requirement_ids=set()
    for p in [*(root/'verification/subsystems').glob('*.md'),root/'examples/vehicle-validation.md']:
        if not p.exists(): continue
        text=p.read_text();check('EXAMPLE' in text and 'fictional' in text.lower(),f'{p.name}: missing fictional disclaimer')
        for row in text.splitlines():
            if not re.match(r'^\| (?:DEMO|EXAMPLE)-(?:DT|SUS|VEH)-\d+',row): continue
            counts['dvp_rows']+=1;cells=[c.strip() for c in row.strip('|').split('|')]
            check(len(cells)==10 and all(cells),f'{p.name}: incomplete DVP&R row')
            if len(cells)!=10: continue
            check(cells[0] not in requirement_ids,f'{p.name}: duplicate requirement ID');requirement_ids.add(cells[0])
            check(cells[-1] in {'not planned','planned','in progress','insufficient evidence','reverification required','N/A with reason'},f'{p.name}: example claims verification/failure or invalid status')
            check(not re.search(r'\bTBD\b|PENDING_AUTHORIZATION',row),f'{p.name}: unfinished example row')
    request_paths=[*(root/'examples/requests').glob('*.md'),root/'examples/follow-up.md']
    test_ids=set()
    for name,paths,counter in [('test-request.yml',request_paths,'request_examples'),('preparation-task.yml',list((root/'examples/preparation').glob('*.md')),'preparation_examples')]:
        for p in paths:
            if not p.exists(): continue
            counts[counter]+=1;text=p.read_text();filled=answers(text)
            check('DEMO' in text and re.search('hypothetical',text,re.I),f'{p.name}: missing example disclaimer')
            check(not re.search(r'\bTBD\b|PENDING_AUTHORIZATION',text),f'{p.name}: unfinished example')
            for e in forms.get(name,{}).get('body',[]):
                if e.get('type')=='markdown': continue
                label=e['attributes']['label'];answer=filled.get(label,'')
                if e.get('validations',{}).get('required'): check(bool(answer),f'{p.name}: missing/empty required answer: {label}')
                if e.get('type')=='dropdown' and answer: check(answer in e['attributes']['options'],f'{p.name}: invalid dropdown answer')
            for rid in re.findall(r'\b(?:DEMO|EXAMPLE)-(?:DT|SUS|VEH)-\d+\b',text): check(rid in requirement_ids,f'{p.name}: unknown requirement {rid}')
            if name=='test-request.yml':
                match=re.search(r'\bTST-DEMO-\d{3}\b',text)
                check(bool(match),f'{p.name}: missing stable example test ID')
                if match:check(match[0] not in test_ids,'Duplicate example test ID');test_ids.add(match[0])
    all_run_ids=set()
    for p in (x for x in files if x.suffix=='.csv'):
        counts['csv']+=1
        try:
            with p.open(newline='') as f:
                reader=csv.DictReader(f,strict=True);check(reader.fieldnames==CSV_FIELDS,f'{p.name}: CSV header mismatch')
                for row in reader:
                    counts['runs']+=1
                    check(set(row)==set(CSV_FIELDS) and all(row.get(k) for k in CSV_FIELDS),f'{p.name}: incomplete/extra CSV values')
                    tid,rid=row.get('test_id',''),row.get('run_id','')
                    check(tid in test_ids,f'{p.name}: unknown test ID')
                    check(bool(re.fullmatch(re.escape(tid)+r'-R\d{3}',rid)) and rid not in all_run_ids,f'{p.name}: invalid/duplicate run ID');all_run_ids.add(rid)
                    start,end=(datetime.fromisoformat(row[k].replace('Z','+00:00')) for k in ('started_at','ended_at'))
                    check(start.tzinfo is not None and end.tzinfo is not None and end>=start,f'{p.name}: invalid time interval/offset')
                    for k in ('configuration_ref','raw_data_ref','calibration_ref'):link(p,row.get(k,''))
        except (csv.Error,ValueError,TypeError,KeyError) as e:errors.append(f'{p.name}: CSV parse error: {e}')
    check(not (root/'.github/workflows').exists(),'No unapproved Actions workflows may ship')
    return errors,counts

def self_test(root):
    def edit(relative,old,new):
        def apply(r):
            p=r/relative;p.write_text(p.read_text().replace(old,new,1))
        return apply
    def set_json(relative,mutate):
        def apply(r):
            p=r/relative;data=json.loads(p.read_text());mutate(data);p.write_text(json.dumps(data))
        return apply
    mutations=[
      ('required form field',edit('.github/ISSUE_TEMPLATE/test-request.yml','required: true','required: false')),
      ('wrong form attribute',edit('.github/ISSUE_TEMPLATE/test-request.yml','placeholder:','nonsense:') if 'placeholder:' in (root/'.github/ISSUE_TEMPLATE/test-request.yml').read_text() else edit('.github/ISSUE_TEMPLATE/test-request.yml','description: Name','nonsense: Name')),
      ('string required flag',edit('.github/ISSUE_TEMPLATE/test-request.yml','required: true','required: "true"')),
      ('CSV schema',edit('examples/run-log.csv','run_id','wrong_header')),
      ('CSV duplicate run',edit('examples/run-log.csv','TST-DEMO-001-R002','TST-DEMO-001-R001')),
      ('CSV naive time',edit('examples/run-log.csv','2099-01-01T14:00:00Z','2099-01-01T14:00:00')),
      ('YAML syntax',lambda r:(r/'.github/ISSUE_TEMPLATE/config.yml').write_text('invalid: [\n')),
      ('duplicate YAML key',lambda r:(r/'.github/ISSUE_TEMPLATE/config.yml').write_text('blank_issues_enabled: false\nblank_issues_enabled: true\n')),
      ('relative link',lambda r:(r/'README.md').write_text((r/'README.md').read_text()+'\n[broken](missing.md)\n')),
      ('image link',lambda r:(r/'README.md').write_text((r/'README.md').read_text()+'\n![broken](missing.png)\n')),
      ('reference link',lambda r:(r/'README.md').write_text((r/'README.md').read_text()+'\n[broken][unknown-ref]\n')),
      ('Markdown anchor',lambda r:(r/'README.md').write_text((r/'README.md').read_text()+'\n[broken](README.md#missing-anchor)\n')),
      ('GitHub form route',edit('README.md','template=test-request.yml','template=missing.yml')),
      ('empty example answer',edit('examples/requests/engine-rpm.md','Diagnostics\n','\n')),
      ('unknown requirement',edit('examples/requests/engine-rpm.md','DEMO-DT-01','DEMO-DT-99')),
      ('unjustified example verification',edit('verification/subsystems/drivetrain.md','| planned |','| verified |')),
      ('Ready in confirmed view',set_json('config/project.json',lambda d:next(v for v in d['views'] if v['name']=='Confirmed testing').update(filter='status:Ready,Scheduled'))),
      ('role terminology',edit('docs/guides/managers.md','Managers decide','Leadership decides')),
      ('missing role guide',lambda r:(r/'docs/guides/test-lead.md').unlink()),
    ]
    for name,mutate in mutations:
        with tempfile.TemporaryDirectory(prefix='baja-validation-') as tmp:
            copy=Path(tmp)/'repository';shutil.copytree(root,copy,ignore=shutil.ignore_patterns('.git','__pycache__'))
            mutate(copy);errors,_=validate(copy)
            if not errors:print('FAIL: did not reject '+name);return 1
            print('PASS: rejected '+name)
    print(f'PASS: {len(mutations)} negative cases rejected; no live system was exercised.')
    return 0

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test',action='store_true')
    parser.add_argument('--json',action='store_true',help='Machine-readable validation result')
    args=parser.parse_args()
    if args.self_test:sys.exit(self_test(ROOT))
    errors,counts=validate(ROOT)
    if args.json:print(json.dumps({'counts':counts,'errors':errors,'passed':not errors},indent=2))
    else:
        print(json.dumps(counts,sort_keys=True))
        for error in errors:print('ERROR: '+error)
        print(f'{"PASS" if not errors else "FAIL"}: {len(errors)} error(s). Browser/Project/adoption checks remain manual.')
    sys.exit(bool(errors))
