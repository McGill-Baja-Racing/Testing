# Local validation report

> This document preserves the initial local-pilot baseline and setup instructions. **The new private repository and three DEMO issues are now deployed with authorization.** See [current deployment status](README.md). Project configuration and browser form-rendering checks remain pending; no permissions were changed. Do not repeat repository creation.

Run date: 2026-10-15. This report covers local artifacts; all live GitHub and archive-access acceptance scenarios remain pending explicit authorization.

Commands: `python3 scripts/validate.py` and `python3 scripts/validate.py --self-test` from pilot root. Final recorded results: both commands exited 0.

Scope: parse all YAML/JSON; check the used GitHub form-schema subset, mandatory fields and optional intake fields; declared labels; Project statuses/views; CSV headers, complete values, unique run IDs and timezone-aware intervals; DEMO request field coverage; Markdown local paths/fragments; required files; DEMO DVP&R states; absence of Actions workflows.

The validator does not contact GitHub, resolve external/private URLs, prove permissions/roles, assess engineering correctness, render forms or enforce human approval gates. It requires Python 3.9+ and Ruby with the standard YAML library. No packages need installing. Local Markdown validation covers inline/reference-style paths; external URLs and data-link placeholders are intentionally not dereferenced.

## Final results

- YAML: 3 parsed; JSON: 2 parsed.
- GitHub Issue Forms: 2 checked; DEMO requester field sets: 3 checked.
- CSV files: 2 checked (blank run-log template and two-row DEMO run log).
- Markdown files: 32 checked; local links: 112 resolved; zero errors.
- Seven temporary-copy mutation tests passed: missing required form field, wrong CSV schema, malformed YAML, missing relative target, missing Markdown anchor, duplicate YAML key and missing required deliverable were each rejected.
- Existing ESP32DataLogger working tree remained clean; no live GitHub or Drive mutations were performed.

The Project setup guide references current official GitHub form-schema, Projects API and filtering documentation. Configuration specifications were inspected locally; they were not applied to a live Project. All manual scenarios remain pending as recorded in PILOT_TEST_PLAN.md.

## Post-deployment documentation validation — 2026-10-15

Five existing documentation files were updated to reflect the authorized private repository and DEMO issues, without changing forms, examples or engineering standards. The package remains 41 files. Revalidation passed: 3 YAML, 2 JSON, 2 CSV, 2 forms, 3 DEMO field sets, 32 Markdown files and 117 local links; zero errors. All seven mutation self-tests also passed. Browser rendering and Project configuration remain pending for the reasons recorded in the README.
