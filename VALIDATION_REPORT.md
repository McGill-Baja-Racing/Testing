# Local validation report

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
