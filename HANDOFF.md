# Pilot handoff

Start with [README](README.md) and [walkthrough](docs/walkthrough.md). The implementation brief supplied by the user was the requirements source; the attached prototype was inspected as reference only. No actions suggested by the prototype were treated as permission to deploy. Prototype included basic request/preparation/report forms, a static preview, starter inventory/DVP&R/templates and a short setup guide. This pilot replaces those with the complete methodology and retains a Markdown walkthrough rather than a separate web interface/report issue.

Existing workspace: ESP32DataLogger, clean at inspection; no repository files changed. GitHub read-only organization lookup returned no accessible repositories; this does not establish organization absence or lack of membership. No live state was created. Pilot lives independently in `/private/tmp/baja-testing-pilot`; copy or extract the ZIP to a durable location before temporary-file cleanup.

```text
.github/ISSUE_TEMPLATE/     test-request.yml, preparation-task.yml, config.yml
config/                    labels.json, project.json
docs/standards/            lifecycle, technical standards, V&V
docs/guides/               approvals, testing day, closure
docs/                      Project setup, data storage, walkthrough
examples/requests/         RPM, brake pressure, half-shaft strain (all DEMO)
examples/preparation/      pressure adaptation, strain feasibility
examples/                  invalid-run follow-up and CSV
templates/                 plan, gates, readiness, run CSV, results, report, DVP&R, sensor record
instrumentation/           model/device/install/calibration inventory
verification/              vehicle + drivetrain/suspension DEMO DVP&Rs
scripts/                   offline validator and mutation self-tests
README.md                  role-based onboarding
IMPLEMENTATION_CHECKLIST.md PILOT_TEST_PLAN.md VALIDATION_REPORT.md
```

Review exercise: read example A for low-effort handling, B for adaptation/capacity and invalid data follow-up, C for bounded feasibility. Use the actual form fields, gate comments, plan/readiness templates and run CSV. The [acceptance plan](PILOT_TEST_PLAN.md) separates automated checks from pending manual scenarios. Run `python3 scripts/validate.py` from the package root.

Remaining authorization boundary: creating/uploading/merging into a selected private sandbox repository; creating/configuring a private Project and DEMO issues; later production rollout. Permission changes, invitations, organization workflows and Drive changes require separate explicit approval. [Exact setup steps](docs/project-setup.md) list UI actions and scriptable API capabilities. No approval request is needed to review this completed local pilot.
