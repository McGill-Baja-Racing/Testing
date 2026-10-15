# EXAMPLE — bounded strain feasibility and later preparation

**DEMO / Hypothetical training material only.** All people, dates, specifications, decisions and outcomes below are fabricated; none approve real work. Stable historical example test ID: **TST-DEMO-003**.

## Filled request

### Requesting subsystem and Subsystem Lead
Drivetrain — EXAMPLE Drivetrain Subsystem Lead.

### Test purpose
Characterization

### Engineering question
Can a half-shaft strain measurement support a defensible torque/load-history estimate under defined bench conditions?

### Physical measurements and expected outputs
Strain at specialist-defined locations, reference torque and temperature/context where needed; output feasibility/uncertainty assessment and, only if feasible, a calibrated load-history method.

### Intended engineering decision and sufficient evidence
Decide whether to fund full measurement preparation for an example strength/fatigue assessment. Evidence must establish safe installation, signal transfer, traceable strain-to-torque mapping and uncertainty. A negative feasibility outcome is useful; no load verification is claimed without applicable evidence.

### Consequences of not testing
Sizing may rely on unvalidated loads, while open-ended instrumentation development can consume capacity without a workable calibration method.

### Requirement IDs and references
[DEMO-DT-02 and EXAMPLE-DT-03](../../verification/subsystems/drivetrain.md). Numeric criteria there are entirely fabricated engineering allocations.

### Requested and last useful timing
Preferred EXAMPLE feasibility session 2098-12-15; latest useful before the fictional 2099-01-15 design review. Significant testing normally plans three to four weeks ahead; no actual deadline.

### Known hazards, constraints and context
Rotating parts, bonding and reference-load fixture risks require competent technical/safety controls. High technical complexity is separate from operational risk. Use a safe bench feasibility investigation before considering installed work.


## Screening and bounded phase

**Unknown feasibility**, high preparation effort/high technical complexity. Uncertainties: bonding/repeatability, rotating interface, temperature effects, calibration fixture and strain-to-torque uncertainty. Rough full-preparation estimate is a fictional 12 Electronics hours + 6 mechanical hours over three weeks; uncertainty is explicitly high.

After individual Manager value approval, the Electronics Manager must commit the [bounded feasibility task](../preparation/strain-feasibility.md): one 90-minute bench session, a method/fixture concept and blocker note. Managers then authorize only that bounded scope. Stop at the cap and review; this is not permission for full development or vehicle operation.

## Working plan

1. **Identity/people:** TST-DEMO-003; EXAMPLE-config-C/proposed; fictional author EXAMPLE Test Lead 2098-12-12. EXAMPLE Drivetrain Subsystem Lead, Testing Manager, Electronics/specialist Instrumentation Owner and Drivetrain Analysis Owner; feasibility note due 2098-12-16. Full-test analysis due date must be agreed before that separately authorized phase (example proposed date 2099-01-05, not committed).
2. **Configuration/conditions:** EXAMPLE-DEV-S-01 and proposed EXAMPLE-INST-S-01; nonrotating surrogate/reference fixture for initial feasibility. No existing calibration is claimed. Record fixture geometry, bridge/conditioning settings and temperature.
3. **Feasibility procedure:** competent owners review fixture/energy risks, establish safe controls and stop conditions, inspect installation concept and reference-load mapping feasibility, record observations/uncertainty blockers; stop at 90 minutes. No installed vehicle run is authorized by the feasibility plan.
4. **Measurement detail:** specialist determines bridge layout/range, bandwidth/sampling, signal transfer, environmental/temperature compensation, reference traceability and uncertainty after feasibility. These values are intentionally not invented before investigation; unresolved technical outputs are the point of the bounded task.
5. **Conditional full phase:** if the method is feasible, resource managers freshly commit defined development/calibration/integration work before Managers authorize [full preparation](../preparation/strain-integration.md). The fictional DVP&R allocation is 5% of a 0–100 N·m example calibration span; it is not a universal criterion. Controlled load points, repetition rationale and uncertainty budget must be agreed for that method before any interpretation.
6. **Readiness/data:** complete device/calibration versions and installed end-to-end verification, including synchronization, scaling and limitations. The current example remains **not ready**. A valid standalone bridge is insufficient. Record run IDs/raw evidence/code/settings and use the common results format; no run data are fabricated for this unfinished method.

## Outcomes to review

A feasibility note may recommend proceed, revise, defer or stop. Any of these can close the bounded preparation task with its record; it cannot mark the parent test Ready. Full preparation, schedule and execution still require their own gates. DEMO-DT-02 remains unverified. [Calibration pattern](../instrumentation.md) · [Common plan](../../templates/test-plan.md).
