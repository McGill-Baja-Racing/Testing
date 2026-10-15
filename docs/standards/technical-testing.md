# Test design and measurement quality

## Define useful evidence

Every test states an engineering question, physical measurements, intended outputs/decision and sufficient evidence. Use quantitative pass/fail criteria only when relevant, with the requirement, calculation, simulation, reference or reasoned engineering basis recorded **before interpreting results**. Exploratory/diagnostic work needs a definite question, not a forced threshold.

The **Subsystem Lead** owns the objective and criteria. The **Testing Manager** reviews completeness/testability and may return a plan for revision, but cannot change objectives unilaterally. Alternative methods must answer the original question; unexpected observations needing new investigations use linked requests.

## Match measurement to the decision

The subsystem defines physical need and conditions. Electronics/technical owners, consulting the Subsystem Lead, determine sensor placement, range, accuracy/uncertainty, temporal response/bandwidth, sample rate, interface, environment, calibration and recording method. There is no universal sampling rate, uncertainty, repetition count or calibration recipe.

Use the [one common plan](../../templates/test-plan.md). Its core covers configuration, equipment, environment, people, procedure, runs/repeats, controls, observations, stop conditions and data checks. Add complexity, elevated-safety and design-of-experiments sections when appropriate. Technical complexity and operational safety risk are separate assessments.

## Validate the installed chain

Readiness covers secure mounting/wiring, calibration/reference validity, logging channels, scaling/units, timestamps/timebase and successful integrated verification in the installed configuration where applicable. If a check is unsafe/inapplicable, document why, alternate evidence and relevant clearance. The **Instrumentation Owner** signs for the intended use; a model being available does not establish readiness. Configuration changes trigger reassessment with the Testing Manager and relevant technical/safety owners. [Checklist](../../templates/readiness-checklist.md).

## Keep evidence usable

Use stable test/run IDs to connect raw files, run logs, configurations, equipment/calibration versions, analysis code and reports. Retain raw originals, including rejected runs. Check data during testing where feasible and before leaving where practicable. [Storage conventions](../data-storage.md).

Post a [results summary](../../templates/results-summary.md) on the original issue; link a [detailed report](../../templates/test-report.md) for complex tests. Describe actual method, deviations, metrics, uncertainty/limitations, conclusions and follow-up. The subsystem owns interpretation; Electronics/Instrumentation Owner supports data-quality judgments. [Inventory](../../instrumentation/inventory.md) separates capability, unit calibration, installation and contextual readiness.
