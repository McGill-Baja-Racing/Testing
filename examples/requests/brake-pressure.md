# DEMO request — brake pressure

**Hypothetical exercise only; no real approval, date, device capability or result.** Stable test ID: TST-DEMO-002.

## Requester fields

### Requesting subsystem and lead
Brakes — DEMO lead

### Test purpose
Characterization

### Engineering question
How does brake pressure evolve during owner-defined controlled actuation, and is the intended comparison supported?

### Physical measurements and expected outputs
Brake pressure versus time at owner-defined location, actuation/context; output trace with limitations and comparison basis.

### Intended engineering decision and sufficient evidence
Decide whether further brake-system investigation is justified. Pressure range/dynamics, acceptable uncertainty and sufficient comparisons must be agreed by lead/specialist before execution.

### Consequences of not testing
A design change could rely on unknown pressure behavior and hide a safety concern.

### Requirement IDs and references
DEMO-VEH-05; [DVP&R index](../../verification/vehicle.md) and [drivetrain](../../verification/subsystems/drivetrain.md).

### Requested and last useful timing
Requested: DEMO future day; last useful: before DEMO brake review; planning expectation allows adaptation time.

### Known hazards, constraints and context
Technical complexity medium; brake-system safety risk independently reviewed, with competent clearance required. DEMO brakes lead, Testing Manager, Test Lead and electronics owner are placeholders; DEMO brakes analyst due DEMO execution + 3 days, to be agreed as a real date.

## Illustrative subsequent issue records — DEMO only

Quick screening: Existing needs adaptation; medium effort; mechanical interface/fluid compatibility, installation, reference checks, DAQ scaling and installed verification; lead time TBD by owners; no commitment from screen.


1. DEMO completeness and quick screen precede individual leadership approval. Leadership approval does not commit electronics or mechanical work.
2. DEMO preparation authority is recorded separately. Both resource managers must commit owners/time windows/due dates before adaptation begins; otherwise Awaiting Capacity.
3. Link the [medium-effort preparation task](../preparation/brake-adaptation.md). Specialist specifies range, dynamic response/sampling, uncertainty, reference method and compatibility; no generic pressure/rate is assumed.
4. Complete calibration, installation and end-to-end verification with technical/safety owner evidence. Only then Ready → Scheduled; final joint on-site decision still required.
5. DEMO R001 has a hypothetical scaling/configuration mismatch: preserve raw, classify invalid, never infer design FAIL. Open the [linked follow-up](../follow-up.md), keep the requirement unverified and document conclusions/closure. DEMO R002 remains aborted in the sample log after a stop; no success is fabricated.


Real decisions require the identity/date/scope/evidence records in [gate template](../../templates/approval-record.md). The sequences above are narrative examples, not completed sign-offs. [Modular plan](../../templates/test-plan.md) and [readiness](../../templates/readiness-checklist.md) must be completed with real evidence before authorized execution.
