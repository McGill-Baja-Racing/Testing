# McGill Baja Racing — Testing

Plan tests, prepare reliable measurements, and turn evidence into engineering decisions. This repository connects test requests, preparation, procedures, results, and requirement verification. GitHub tracks the work; the team's existing Google Drive holds large recordings and videos. A request or Project status never authorizes vehicle operation.

**Adoption status:** this revision is ready for team review; rollout awaits Manager authorization and the [deployment checks](HANDOFF.md). The existing private GitHub repository contains DEMO requests. A testing Project has not been configured. No example is an approved test or real evidence.

## Start here

| Your role | First action |
| --- | --- |
| New member | Follow the [example journey](docs/walkthrough.md); suggest test ideas to your Subsystem Lead. |
| Subsystem Lead | [Request a test and maintain verification](docs/guides/subsystem-lead.md). |
| Manager | [Review priorities, capacity and authorizations](docs/guides/managers.md). |
| Testing Manager | [Coordinate screening, preparation and scheduling](docs/guides/testing-manager.md). |
| Test Lead | [Plan the test, record runs and hand off data](docs/guides/test-lead.md). |
| Electronics / Instrumentation Owner | [Assess measurement needs and prepare systems](docs/guides/instrumentation.md). |
| Analysis Owner | [Analyze, report and support closure](docs/guides/closure.md). |

## Request a test

1. **Subsystem Leads submit formal requests.** Other members bring ideas to their lead.
2. Read the [simple RPM example](examples/requests/engine-rpm.md), then open [New Test Request](https://github.com/McGill-Baja-Racing/Testing/issues/new?template=test-request.yml) after rollout. Reviewing locally? Read the [form fields](.github/ISSUE_TEMPLATE/test-request.yml).
3. Explain the question, physical measurements, expected outputs, engineering decision, sufficient evidence, consequences of not testing, and preferred/latest useful timing. Add requirement references if available. Sensor selection and sampling details come later.
4. Confirm completeness and respond to screening questions. The Testing Manager coordinates review; Managers decide priority and approve each test individually. **Submission is not approval.**

## Lifecycle at a glance

Request → screen feasibility → Managers review → prepare → confirm readiness → schedule → execute → analyze → close the attempt and update verification.

Five decisions stay separate: **test-value approval; bounded feasibility authorization when needed; preparation authorization after capacity commitments; technical readiness; final joint go/no-go.** Ready tests may be scheduled. Execution still requires the Subsystem Lead and Testing Manager's joint decision plus mandatory technical/safety clearance. Anyone can stop unsafe work. [Process and responsibilities](docs/standards/testing-lifecycle.md).

## Find the records

| You need | Go to |
| --- | --- |
| Active requests and preparation | [GitHub issues](https://github.com/McGill-Baja-Racing/Testing/issues); [Project setup and current fallback](docs/project-setup.md) |
| Design Verification Plan and Report (DVP&R) | [Verification index](verification/README.md) and [blank template](templates/dvp-r.md) |
| Sensor availability and readiness | [Equipment inventory](instrumentation/inventory.md) |
| Procedures and run records | [Test plan](templates/test-plan.md), [readiness checks](templates/readiness-checklist.md), [run log](templates/run-log.csv) |
| Data, analysis and conclusions | [Storage conventions](docs/data-storage.md), [results summary](templates/results-summary.md), [detailed report](templates/test-report.md) |

Need help? Ask your Subsystem Lead about objectives, the Electronics Manager about measurement capacity, and the Testing Manager about coordination. Managers resolve priorities and testing-time conflicts.
