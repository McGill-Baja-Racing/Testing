# Electronics and instrumentation quick start

**Translate physical needs into a defensible measurement system.** The Subsystem Lead supplies the question and operating context. Data acquisition (DAQ) covers the signal chain through recording. The Instrumentation Owner owns measurement quality; the Electronics Manager commits Electronics capacity.

1. Screen before prioritization: category **Ready / Existing needs adaptation / New development / Unknown feasibility / No instrumentation support**, preparation effort low/medium/high, main tasks, dependencies, uncertainty and rough lead time. Ask precise clarification. A screen is not a commitment. “No instrumentation support” must say whether no instrumentation is needed or support is unavailable; it never waives evidence.
2. Estimate defined work and availability with the resource manager, including current commitments and a limit on simultaneous work. Confirm capacity **before Managers authorize preparation**. After rollout use [New Preparation Task](https://github.com/McGill-Baja-Racing/Testing/issues/new?template=preparation-task.yml) for medium/high effort ([local fields](../../.github/ISSUE_TEMPLATE/preparation-task.yml)). Unknown feasibility starts with a capped investigation, not full development.
3. Consult the [inventory](../../instrumentation/inventory.md). Available equipment is not necessarily ready for this test. Identify the physical unit, installation and intended use, not only the sensor model.
4. With the Subsystem Lead, specify placement, range, uncertainty, temporal response/bandwidth, sample rate, interface, environment and method for this decision. No universal sampling rate or accuracy applies. [Technical standard](../standards/technical-testing.md).
5. Record [device/installation](../../templates/sensor-record.md) and [calibration](../../templates/calibration-record.md) evidence: reference validity/traceability, procedure, points, conditions, uncertainty, coefficients, limits and validity triggers. Check wiring/mounting, channels, scaling/units, timestamps and the installed end-to-end chain.
6. Sign [readiness](../../templates/readiness-checklist.md) for the actual configuration/intended use. After relevant changes, work with the Testing Manager and technical/safety owners to define and repeat affected checks. Support run-level data checks and analysis limitations.

Pending work is visible in [preparation workload or linked issues](../project-setup.md); the commitment record, not effort class or assignee, states capacity. [Fictional equipment example](../../examples/instrumentation.md).

[Start here](../../README.md#start-here)
