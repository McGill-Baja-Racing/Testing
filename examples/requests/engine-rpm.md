# EXAMPLE — simple engine RPM diagnostic

**DEMO / Hypothetical training material only.** All people, dates, specifications, decisions and outcomes below are fabricated; none approve real work. Stable historical example test ID: **TST-DEMO-001**.

## Filled request

### Requesting subsystem and Subsystem Lead
Drivetrain — EXAMPLE Drivetrain Subsystem Lead.

### Test purpose
Diagnostics

### Engineering question
Does engine speed fluctuate during two stationary operating conditions in a way that warrants a separate tuning investigation? RPM means revolutions per minute.

### Physical measurements and expected outputs
Engine speed versus time, operating-point/configuration notes and logger health; two 30 s traces plus an independent speed-reference comparison. These are fictional conditions, not operating instructions for the real vehicle.

### Intended engineering decision and sufficient evidence
Decide whether to request further tuning diagnostics. Sufficient evidence is continuous time-aligned traces at both example points with reference/logging checks that distinguish physical fluctuations from acquisition faults. No engineering pass/fail threshold is forced on this exploratory question.

### Consequences of not testing
Tuning changes may be based on an untested explanation of apparent speed variation.

### Requirement IDs and references
[DEMO-DT-01](../../verification/subsystems/drivetrain.md); fictional diagnostic evidence requirement.

### Requested and last useful timing
Preferred EXAMPLE session: 2099-01-01; latest useful 2099-01-08 before the fictional tuning review. No real booking.

### Known hazards, constraints and context
Stationary guarded configuration; rotating/hot parts and exhaust require competent site-specific controls and technical/safety clearance. Simple instrumentation does not imply low operational risk.


## Screening and decisions

EXAMPLE Instrumentation Owner screens **Ready**, low preparation effort, low technical complexity: use the unchanged [EXAMPLE RPM installation/calibration](../instrumentation.md). Estimated work: 30 minutes for inspection, reference and installed logging checks; available only if Electronics Manager commits that slot. Operational safety is assessed separately.

The correct path is: Subsystem Lead completeness → screen → individual Manager value decision → Electronics Manager's defined 30-minute capacity commitment → Managers' preparation authorization → installed technical sign-off → confirmed day → joint on-site go/no-go. Bounded feasibility is N/A with reason: existing known method. These are teaching steps, not actual completed approvals. Low effort stays this checklist; no separate preparation issue.

## Working plan

1. **Identity/objective:** TST-DEMO-001, plan `EXAMPLE-config-A/v1`; author EXAMPLE Test Lead, fictional 2098-12-28. Question/decision above; DEMO-DT-01 defines diagnostic evidence, not a design limit.
2. **People/timing:** EXAMPLE Drivetrain Subsystem Lead, Testing Manager, Test Lead and Instrumentation Owner; EXAMPLE Drivetrain Analysis Owner due 2099-01-03. Session 2099-01-01 is illustrative until all gates are satisfied.
3. **Configuration/conditions:** EXAMPLE-config-A, example firmware revision A; EXAMPLE-DEV-RPM-01 / EXAMPLE-INST-RPM-01/v1 / EXAMPLE-CAL-RPM-01/v1. Hold the fictional 1500 and 3000 rpm operating points; record ambient conditions, actual speed/reference and configuration. These values do not authorize actual engine operation.
4. **Risk/procedure:** competent technical/safety owners review guarded stationary setup, exhaust/hot surfaces and emergency stop. Stop for unsafe conditions or corrupted logging. After joint clearance: verify references/settings; log a 30 s run at each point; inspect data before changing point; secure setup and preserve originals. Two runs cover two conditions, not a universal repeat rule. Further repeatability questions need adequate added evidence within authorized scope or a new request.
5. **Measurement:** example derived speed at 100 Hz for behavior below 10 Hz, with pulse metadata retained; example uncertainty ±10 rpm over reference points. Specialist justifies these fabricated choices for the question; no generic rate/accuracy applies. Compare independent reference, units and timestamps, and verify the installed pulse-to-file chain.
6. **Preparation/readiness:** inspect mounting/wiring; reference check; verify scaling/timebase/logging; installed dry run; data access. Instrumentation Owner links successful evidence and signs the actual configuration before Ready. Managers resolve any day conflict. On-site go/no-go remains distinct.
7. **Data/analysis:** [sample runs](../run-log.csv), [archive example](../data/README.md); real use would link actual originals and manifest. Analyze each trace with documented settings; review missing samples/reference deviation and report limitations. Analysis Owner posts the parent results summary.

## Illustrative handoff and outcome

The fabricated narrative yields continuous traces with 12 and 18 rpm standard deviations; those numbers have no real measurement source. The example interpretation is **valid exploratory finding / design outcome not assessed**, not design PASS. Those summary numbers alone do not establish a tuning cause; uncertainty/reference limits must be reviewed. The Subsystem Lead would review that interpretation and the Testing Manager would check records before closure. DVP&R remains a fictional plan; no team requirement is verified. A new tuning investigation uses a linked request.

[Five-gate record](../../templates/approval-record.md) · [Common plan](../../templates/test-plan.md) · [Readiness template](../../templates/readiness-checklist.md)
