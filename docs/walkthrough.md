# Walk through one test

Start with [the README](../README.md). This is a file-based walkthrough, not a live Project simulation. All linked example decisions/data are fictional; no sign-offs are implied.

## A. A simple RPM question

Open [the filled request](../examples/requests/engine-rpm.md). A Subsystem Lead can answer the intake fields without choosing a sensor. The screen assumes an existing known installation; a 30-minute checklist is enough preparation, subject to Electronics Manager capacity and Managers' authorization. The compact [working plan](../examples/requests/engine-rpm.md#working-plan) links calibration/configuration instead of repeating it.

Follow the five separate decisions in the [parent index](../templates/approval-record.md). A known method can justify no feasibility investigation; it cannot skip technical readiness or final joint go/no-go. After fictional runs, the exploratory finding has no forced design PASS/FAIL. Subsystem Lead interpretation and Testing Manager record check would precede closure.

## B. Adapt an installed brake sensor

[Pressure request](../examples/requests/brake-pressure.md) needs [medium preparation](../examples/preparation/brake-adaptation.md). Both resource managers commit defined work before Managers authorize it. Awaiting Capacity is the honest state while either commitment is missing. Readiness needs installed scaling/timebase/reference evidence, not merely a calibrated standalone unit.

The [invalid case study](../examples/requests/brake-pressure.md#invalid-attempt-case-study) deliberately shows a missed configuration reassessment: per-run checks expose scaling mismatch. It demonstrates a process violation, not a permitted shortcut. Preserve originals, stop and document invalid evidence. The [follow-up](../examples/follow-up.md) leaves the requirement unverified and returns correction/retest through appropriate screening and authorization.

## C. Investigate strain feasibility before development

[Strain request](../examples/requests/half-shaft-strain.md) starts with unknown feasibility. A [90-minute bounded task](../examples/preparation/strain-feasibility.md) produces a blocker/method note, not readiness. Stop/review at the cap. Only after a feasible method and fresh resource commitments can Managers authorize [full preparation](../examples/preparation/strain-integration.md). Calibration and installed integration are still required before scheduling.

## Inspect the records

Compare [model/unit/calibration/installation examples](../examples/instrumentation.md) with the [operational inventory](../instrumentation/inventory.md): available is not ready for this test. Compare [DVP&R rows](../verification/subsystems/drivetrain.md) with [attempt validity](guides/closure.md): closed is not verified. No fictional record supplies actual evidence.

Run `python3 scripts/validate.py` and `python3 scripts/validate.py --self-test` from the repository root. [Validation report](../VALIDATION_REPORT.md) states what was checked; [acceptance scenarios](../PILOT_TEST_PLAN.md) separate local checks from browser/Project/manual checks requiring authorized deployment.
