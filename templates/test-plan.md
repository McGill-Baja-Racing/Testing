# Common test plan

Use on the parent issue or as a linked versioned document. **Complete the core for every test; link existing request/decision/equipment records rather than copy them.** A simple test can use one short paragraph per item. [Filled simple plan](../examples/requests/engine-rpm.md#working-plan).

## Core — required

1. **Identity and objective:** test ID, parent issue, plan revision/author/date; link the question, physical measurements, outputs/decision, sufficient evidence and relevant requirements. Record applicable criteria/basis before interpreting results, or explain the exploratory question.
2. **People and timing:** Subsystem Lead, Testing Manager, Test Lead, Instrumentation Owner (or justified N/A), Analysis Owner and agreed analysis due date; equipment/personnel availability; tentative versus confirmed day.
3. **Configuration and conditions:** component/vehicle and firmware/settings revisions; physical device, installation/calibration references; environment/operating envelope, controlled and recorded uncontrolled conditions.
4. **Risk and procedure:** separate technical complexity and operational safety risk; required technical/safety owners, hazards/controls, stop/resume conditions; numbered steps; runs/repeats and rationale; expected observations/records.
5. **Measurement quality:** placement/range, uncertainty/basis, temporal response/bandwidth/sample rate, interface/units/timebase/logging as relevant; specialist-owned specification; calibration/reference and installed integrated verification method. Link existing equipment records.
6. **Preparation and readiness:** low-effort checklist OR medium/high linked tasks; dependencies; parent gate-record link; [readiness evidence](readiness-checklist.md); any unsafe/inapplicable check's reason, alternate evidence and clearance.
7. **Data and analysis:** [run log](run-log.csv) and raw archive location/custodian; per-run/site-exit data checks; analysis method, limitations and reporting depth; [results summary](results-summary.md). Reuse named owner/due date from item 2.

## Optional — complex integration

Use when uncertainty/integration warrants it: bounded feasibility cap/review; staged technical milestones; error budget; synchronization; saturation/dropout; calibration transfer; environment effects; integration dependency owners; configuration freeze/reassessment triggers and recovery. No generic sample rate or accuracy is assumed.

## Optional — elevated operational risk

Complete regardless of technical complexity when justified: detailed hazard assessment, barriers/exclusion zones, communications, emergency/vehicle securing reference, competent clearance owners and preflight checks. Numeric operating/stop limits require an engineering basis; an unfilled template is not a safe operating procedure.

## Optional — experiment/comparison design

Factors/levels; confounders/controls; run order/randomization; replication and precision rationale; stopping rule and analysis approach. Do not impose universal repeats or force a pass/fail threshold on exploratory work.
