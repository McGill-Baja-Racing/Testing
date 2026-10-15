# DEMO request — half shaft strain

**Hypothetical exercise only; no real approval, date, device capability or result.** Stable test ID: TST-DEMO-003.

## Requester fields

### Requesting subsystem and lead
Drivetrain — DEMO lead

### Test purpose
Characterization

### Engineering question
Can installed half-shaft strain measurements support a defensible estimate of torque/load history under defined conditions?

### Physical measurements and expected outputs
Strain at specialist-defined locations plus temperature/operating context as needed; output calibrated torque/load estimate and uncertainty assessment if feasible.

### Intended engineering decision and sufficient evidence
Decide whether evidence can support a strength/fatigue assessment. Evidence must establish bridge behavior, calibration/load mapping and uncertainty; if feasibility fails, do not claim load verification.

### Consequences of not testing
Sizing may rely on unvalidated load assumptions; development effort could be committed without feasibility evidence.

### Requirement IDs and references
DEMO-DT-02; [DVP&R index](../../verification/vehicle.md) and [drivetrain](../../verification/subsystems/drivetrain.md).

### Requested and last useful timing
Requested: DEMO longer-term backlog; last useful: before DEMO design review; significant preparation normally needs 3–4 weeks or owner estimate.

### Known hazards, constraints and context
Technical complexity high; rotating-equipment operational risk independently assessed. DEMO drivetrain lead, Testing Manager, Test Lead, electronics/specialist instrumentation owner; DEMO drivetrain analyst due DEMO eventual execution + 7 days (real date agreed during planning).

## Illustrative subsequent issue records — DEMO only

Quick screening: Unknown feasibility leading potentially to new development; high effort; gauge selection/bonding, rotating interface/telemetry, bridge/conditioning, calibration fixture, temperature and installed integration; uncertain lead time and dependencies.


1. DEMO leadership evaluates test value after screening. It can authorize only a bounded feasibility investigation before deciding on full development.
2. [Feasibility task](../preparation/strain-feasibility.md): illustrative cap of one DEMO bench session, with safe fixture concept and calibration/load-mapping viability note as deliverables. Resource manager separately commits investigation capacity; stop at cap and review.
3. If evidence supports proceeding, separately authorize full preparation, obtain all managers' commitments and create medium/high linked development/calibration/integration tasks with dependencies and due dates. No feasibility approval implies that commitment.
4. Plan bridge bonding and environmental effects, traceable load/reference calibration, uncertainty including torque conversion, signal chain and installed safe integrated verification. Do not invent gauge capability or calibration recipes.
5. Technical readiness may still be blocked despite a calibrated standalone bridge. Configuration changes require reassessment. No Ready, confirmed schedule or execution until the respective gates are satisfied; this example stays a proposal without real evidence.


Real decisions require the identity/date/scope/evidence records in [gate template](../../templates/approval-record.md). The sequences above are narrative examples, not completed sign-offs. [Modular plan](../../templates/test-plan.md) and [readiness](../../templates/readiness-checklist.md) must be completed with real evidence before authorized execution.
