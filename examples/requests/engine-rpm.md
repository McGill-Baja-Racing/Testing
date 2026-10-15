# DEMO request — engine rpm

**Hypothetical exercise only; no real approval, date, device capability or result.** Stable test ID: TST-DEMO-001.

## Requester fields

### Requesting subsystem and lead
Drivetrain — DEMO lead

### Test purpose
Diagnostics

### Engineering question
Does the engine-speed trace show repeatable speed instability under the owner-defined controlled condition?

### Physical measurements and expected outputs
Engine speed versus time, operating condition and configuration; output trace and instability description.

### Intended engineering decision and sufficient evidence
Decide whether further drivetrain investigation is warranted. Evidence must distinguish physical behavior from dropout/timebase artifacts; no forced numeric threshold for this diagnostic.

### Consequences of not testing
The team may change tuning based on an untested explanation.

### Requirement IDs and references
DEMO-DT-01; [DVP&R index](../../verification/vehicle.md) and [drivetrain](../../verification/subsystems/drivetrain.md).

### Requested and last useful timing
Requested: DEMO future session; last useful: before the DEMO tuning decision; no real date.

### Known hazards, constraints and context
Technical complexity low; operational safety risk assessed independently by competent owners. DEMO role holders: drivetrain lead, Testing Manager, Test Lead, electronics instrumentation owner; analysis owner is DEMO drivetrain analyst, due DEMO execution + 2 days (to be replaced by an agreed date in a real plan).

## Illustrative subsequent issue records — DEMO only

Quick screening: Ready (assumed existing validated configuration only in this fictional exercise); low effort; installation/reference verification + logging check; lead time depends on availability; actual inventory remains unverified.


1. DEMO lead confirms completeness; electronics screen assumes unchanged, previously validated installation/configuration, with current evidence checked before Ready.
2. DEMO leadership representative records individual value approval. Feasibility investigation is N/A with reason: known configuration, no development uncertainty.
3. Separate DEMO full-preparation authorization; DEMO electronics manager commits a short verification slot and names owner/date. Low effort stays a checklist: mount/reference verification, logging/timebase, installed dry run, storage.
4. DEMO instrumentation owner signs actual-context readiness evidence; Testing Manager may then schedule. Joint on-site go/no-go remains pending until execution.
5. Hypothetical valid trace yields an exploratory finding, design outcome not assessed. Post results on the parent, lead approves conclusions and Testing Manager checks records. Only applicable evidence can change DEMO-DT-01 later; this file does not verify it.


Real decisions require the identity/date/scope/evidence records in [gate template](../../templates/approval-record.md). The sequences above are narrative examples, not completed sign-offs. [Modular plan](../../templates/test-plan.md) and [readiness](../../templates/readiness-checklist.md) must be completed with real evidence before authorized execution.
