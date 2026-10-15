# Validation report — production revision

Run date: 2026-10-15. Local checks only; no GitHub, organization, permission, browser setting or Drive mutations were made for this revision.

## Executed checks

From repository root:

```sh
python3 scripts/validate.py
python3 scripts/validate.py --self-test
git diff --check
```

Final measured counts are recorded below. Validation covers every shipped YAML/JSON file, used Issue Form syntax/attribute subset, required fields, labels, private-repository form URL targets, Project guide/filter consistency, complete fictional request/preparation answers, requirement references, DVP&R columns/states, CSV fields/unique IDs/offset timestamps/local references, role terminology and Markdown paths/fragments.

The original 41 file paths remain. Twelve files add the five role guides, calibration template, verification index, repository audit and complete supporting examples. No files were moved or deleted.

## Results

- **PASS:** 53 files; 3 YAML and 2 JSON configurations; 2 Issue Forms.
- **PASS:** 44 Markdown files; 243 local links/anchors and 3 known GitHub form routes.
- **PASS:** 4 filled request examples (including follow-up), 3 filled preparation examples and 6 complete fictional DVP&R rows.
- **PASS:** 2 CSV files, including 4 fictional runs with unique IDs, offset timestamps and resolvable local record references.
- **PASS:** all 19 negative validator cases rejected; positive baseline has zero errors.
- **PASS:** `git diff --check` produced no whitespace errors.
- **NOT RUN:** live form rendering, Project configuration, Drive access and a timed human onboarding trial.

The baseline repository is itself the positive case. Negative tests mutate temporary copies and must be rejected: missing required field, invalid form attribute, string required flag, wrong CSV header, duplicate run ID, naive timestamp, malformed/duplicate-key YAML, broken relative/image/reference/anchor links, invalid form URL, empty example answer, unknown requirement, unsupported fictional verification claim, Ready in the confirmed schedule, inconsistent role terminology and missing role guide.

## Limits and remaining practical checks

The validator uses Ruby/Psych plus Python's standard library (Python 3.9+); no network or third-party package installation. It checks the Markdown forms used here (inline/image links, explicit/collapsed references and heading anchors), not arbitrary embedded HTML or all CommonMark syntax. Private/external URLs are not fetched; known GitHub form routes are checked against packaged filenames. It is a maintainable local check, not GitHub's full server-side validator.

This revision's form rendering/required-field enforcement, Project UI filters/permissions and Drive access are **not tested live**. It does not enforce approval gates, authenticate requester roles, prove two-minute human usability, validate sensor physics or certify engineering evidence. Known prior browser/Project blockers and exact remaining actions are in [handoff](HANDOFF.md) and [acceptance scenarios](PILOT_TEST_PLAN.md).
