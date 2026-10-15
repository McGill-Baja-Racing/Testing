# Baja Testing — local pilot

**Reviewable pilot only.** Stages 1–3 in the implementation brief are approved methodology. Repository layout, fields, labels, ID conventions, reminder cadence and Project setup are proposed Stage 4 defaults. Nothing here records actual approval, scheduling, hardware capability or verification. All examples are DEMO.

This standalone directory is outside ESP32DataLogger. No existing Baja repository, issue, organization Project, permission or Drive folder was changed. The GitHub connector returned no accessible repositories for McGill-Baja-Racing; organization access and deployment capability are unconfirmed.

## Five-minute onboarding

1. **Subsystem lead:** choose New issue → Test request after authorized sandbox installation. State the question, physical measurements, outputs, decision, evidence sufficiency and consequence of not testing. Add requirement references and requested/last useful timing if known. Confirm completeness. A request is not approval. Start locally with [engine RPM](examples/requests/engine-rpm.md).
2. **Testing Manager:** allocate a stable test ID; obtain quick technical screening before leadership prioritizes. Copy [gate records](templates/approval-record.md) into the same issue. Record each test's leadership decision. Screening is not a resource commitment. Name Test Lead, instrumentation owner, analysis owner and analysis due date in the [plan](templates/test-plan.md).
3. **Instrumentation/resource owner:** categorize readiness/effort, state uncertainty and lead time, and acknowledge capacity explicitly. For unknown feasibility seek bounded investigation authorization. Medium/high preparation uses [linked preparation issues](.github/ISSUE_TEMPLATE/preparation-task.yml); low effort can use a parent checklist. Specify viable instrumentation and sign installed-configuration readiness with [evidence](templates/readiness-checklist.md).
4. **Test Lead:** use the approved plan and [run log](templates/run-log.csv). Only technically prepared tests enter a confirmed day. On site, requesting lead and Testing Manager jointly decide go/no-go subject to safety/technical clearance. Anyone can stop. Check data during runs and before leaving when practical.
5. **Analysis owner + subsystem lead:** put [results](templates/results-summary.md) on the original issue; use a [technical report](templates/test-report.md) for complex/critical work. Subsystem lead approves conclusions; Testing Manager checks closure records. Record attempt validity separately from design outcome. Update [DVP&R](templates/dvp-r.md) deliberately; closing an issue does not verify a requirement.

## Navigate the pilot

| Area | Start here |
| --- | --- |
| Local walkthrough and fictional requests | [Walkthrough](docs/walkthrough.md), [all examples](examples/README.md) |
| Approved process | [Lifecycle](docs/standards/testing-lifecycle.md), [technical standards](docs/standards/technical-testing.md), [V&V](docs/standards/verification-strategy.md) |
| Working instructions | [Approvals](docs/guides/approvals.md), [test day](docs/guides/testing-day.md), [closure](docs/guides/closure.md) |
| GitHub implementation | [Project setup](docs/project-setup.md), [labels](config/labels.json), [field/view specification](config/project.json) |
| Engineering records | [Vehicle overview](verification/vehicle.md), [drivetrain](verification/subsystems/drivetrain.md), [suspension](verification/subsystems/suspension.md), [sensor inventory](instrumentation/inventory.md) |
| Data and validation | [Storage](docs/data-storage.md), [acceptance scenarios](PILOT_TEST_PLAN.md), [implementation checklist](IMPLEMENTATION_CHECKLIST.md) |

## Validate and preview locally

From this directory run `python3 scripts/validate.py`. Python 3 and Ruby with its standard YAML library are required; no third-party packages or network access. Read [walkthrough](docs/walkthrough.md) in any Markdown viewer. This is a file-based pilot: GitHub renders the forms only after an authorized repository installation; no Project exists yet.

For live deployment follow [the approval boundary and exact setup steps](docs/project-setup.md). A ZIP sibling of this directory contains the portable deliverable. Keep approvals, plans and results together on the parent test issue; linked preparation issues contain work execution details. Do not create a second results issue by default.
