# Implementation coverage

| Requirement | Implemented artifact |
| --- | --- |
| Two-minute onboarding and precise roles | [README](README.md), five [role guides](docs/guides/subsystem-lead.md) linked from it |
| Approved process and five decisions | [Lifecycle](docs/standards/testing-lifecycle.md), [technical standard](docs/standards/technical-testing.md), [verification](docs/standards/verification-strategy.md), [decision index](templates/approval-record.md) |
| Short intake and progressive detail | Existing [request](.github/ISSUE_TEMPLATE/test-request.yml) and [preparation](.github/ISSUE_TEMPLATE/preparation-task.yml) form paths retained; timing now explicit; no sensor specification demanded at intake |
| Lightweight templates | [Plan](templates/test-plan.md), [readiness](templates/readiness-checklist.md), [CSV](templates/run-log.csv), [results](templates/results-summary.md), [report](templates/test-report.md), [equipment](templates/sensor-record.md), [calibration](templates/calibration-record.md) |
| Verification and inventory without fake production data | [Verification index](verification/README.md), complete fictional DVP&Rs, [operational inventory](instrumentation/inventory.md), [fictional equipment](examples/instrumentation.md) |
| Functional worked examples | [Four journeys](examples/README.md), including separately bounded/full strain preparation and invalid-run follow-up |
| Native GitHub and Drive conventions | [Project/fallback setup](docs/project-setup.md), [data naming/retention](docs/data-storage.md), machine-readable field/label specs |
| Repeatable validation and review | [Validator](scripts/validate.py), [acceptance scenarios](PILOT_TEST_PLAN.md), [results](VALIDATION_REPORT.md), [audit](docs/repository-audit.md) |

Existing paths remain valid; new files extend the original repository. No Actions workflows, database, approval bot or custom tracking application were added. Pending publication, browser checks, Project setup, real records and adoption authorization are owned by the [deployment handoff](HANDOFF.md), not hidden in completed checklist items.
