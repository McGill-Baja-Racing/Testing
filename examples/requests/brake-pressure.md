# EXAMPLE — installed brake-pressure adaptation

**DEMO / Hypothetical training material only.** All people, dates, specifications, decisions and outcomes below are fabricated; none approve real work. Stable historical example test ID: **TST-DEMO-002**.

## Filled request

### Requesting subsystem and Subsystem Lead
Brakes — EXAMPLE Brakes Subsystem Lead.

### Test purpose
Characterization

### Engineering question
Can an installed pressure trace explain pressure-rise behavior during the fictional controlled bench actuation?

### Physical measurements and expected outputs
Pressure versus time at the example master-cylinder port, actuation notes and configuration; output pressure-rise trace with measurement limitations. All conditions describe a fabricated fixture, not real brake procedures.

### Intended engineering decision and sufficient evidence
Decide whether to request a comparison of brake-system configurations. Evidence must cover the defined actuation, installed scaling, timestamps and uncertainty; the Subsystem Lead owns any later comparison criteria. This characterization has no fabricated vehicle stopping-performance threshold.

### Consequences of not testing
A design comparison could rely on unknown pressure behavior or invalid scaling, hiding a measurement problem.

### Requirement IDs and references
[DEMO-VEH-05](../vehicle-validation.md), fictional evidence need only.

### Requested and last useful timing
Preferred EXAMPLE session 2099-01-01; latest useful 2099-01-10 before fictional brake review.

### Known hazards, constraints and context
Pressure/fluid compatibility and stored energy require competent mechanical/technical safety review. No vehicle operation is included in this example; complexity and operational risk are assessed separately.


## Screening and decisions

Category **Existing needs adaptation**, medium preparation effort and medium technical complexity. Tasks: interface compatibility, installation, reference verification, scaling/timebase and installed end-to-end check. Example estimate: 3 Electronics hours plus 2 mechanical hours across two fictional days; dependent on compatible fittings/reference availability. Screening does not commit either team.

Correct sequence: individual Manager value decision → both resource managers commit defined scope/owners/time → Managers authorize preparation → [linked adaptation task](../preparation/brake-adaptation.md) → successful technical readiness → confirmed day → joint on-site go/no-go. If either team cannot commit, stay Awaiting Capacity. A known adapter method makes separate feasibility investigation N/A only with the technical rationale recorded.

## Working plan

- **Identity/people:** TST-DEMO-002, EXAMPLE-config-B/v1, fictional author EXAMPLE Test Lead on 2098-12-28; EXAMPLE Brakes Subsystem Lead, Testing Manager, Instrumentation Owner and Brakes Analysis Owner, due 2099-01-04.
- **Scope/configuration:** EXAMPLE-DEV-P-01 / EXAMPLE-INST-P-01/v1 / EXAMPLE-CAL-P-01/v1; example stationary fixture in 0–4 MPa, with actuation/ambient conditions recorded. This is not an approved operating range for the real car. Controlled valve/fixture configuration is recorded per run.
- **Measurement/procedure:** specialist-owned example 100 Hz logging for behavior below 10 Hz, ±0.03 MPa uncertainty over the demonstrated range. After competent clearance and joint go/no-go, check reference zero/scaling/timebase, collect an actuation trace, inspect it and preserve originals. Repeat only for a justified comparison or data-quality need within scope. Required controls: compatibility/leak check, safe stored-energy release and stop on unsafe behavior or invalid signals.
- **Readiness:** adapter/mounting/wiring, traceable reference, channel scaling/units/timebase and installed reference-to-recording verification; Instrumentation Owner signs actual config. Any setting/installation change needs Testing Manager reassessment and affected checks before continuing.
- **Records/analysis:** [sample run log](../run-log.csv) and [archive explanation](../data/README.md); assess scaling/dropout, pressure-rise metric and uncertainty before interpreting. Real raw links and calibration evidence must be supplied in a real attempt.

## Invalid-attempt case study

The fictional R001 illustrates a **process violation**: a post-readiness scaling change was not reassessed; the per-run check finds a factor-of-two mismatch. This is not an acceptable route through readiness. Stop, preserve raw/configuration and classify the attempt **invalid / design outcome not assessed**, never design FAIL. R002 is an illustrative aborted run after a stop; no resume or successful retest is implied.

The example results summary states: question unresolved; invalid evidence due to scaling; raw/log/version links retained; uncertainty unsuitable for interpretation; EXAMPLE Analysis Owner reports by 2099-01-04; linked [follow-up TST-DEMO-004](../follow-up.md) owns correction/retest. Subsystem Lead interpretation approval and Testing Manager record check would be required for closure. DEMO-VEH-05 remains **insufficient evidence**, not verified. Substantial changes return to screening and revised authorization.

[Decision record](../../templates/approval-record.md) · [Readiness](../../templates/readiness-checklist.md) · [Results format](../../templates/results-summary.md)
