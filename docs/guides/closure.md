# Analysis, results and closure

**Analysis Owner:** complete analysis by the date agreed during planning. The subsystem owns conclusions; Electronics/Instrumentation Owner supports processing and data-quality judgments. Preserve raw originals and link run/configuration/calibration versions and reproducible code/settings.

1. Post the [results summary](../../templates/results-summary.md) on the original test issue. Complex tests link a [detailed report](../../templates/test-report.md). Describe actual method, deviations, metrics, uncertainty/limitations and sufficient evidence.
2. Separate attempt validity from engineering outcome:

| Attempt | What follows |
| --- | --- |
| valid | Applicable criteria can yield PASS or FAIL; exploratory work can yield a finding without pass/fail |
| inconclusive | Question unresolved; linked follow-up for unresolved objectives; relevant requirements remain unverified |
| invalid | Evidence unsuitable; preserve reasons/raw; linked follow-up; relevant requirements remain unverified |
| aborted | Record stop/clearance history, unresolved objectives and follow-up or explicit disposition |

3. The Subsystem Lead approves engineering interpretation and updates [DVP&R](../standards/verification-strategy.md) with evidence applicability/status. A closed attempt never automatically verifies a requirement. Significant follow-up scope changes return to screening and revised authorization.
4. The Testing Manager checks logs, raw access, metadata, plan/configuration, analysis, sign-offs and linked follow-ups before closing the attempt. If analysis cannot be completed, record why, limitations, unresolved objectives and acknowledged disposition; do not claim evidence validity from missing analysis.

## Overdue analysis

The Testing Manager reminds the Analysis Owner, then escalates unresolved work to the Subsystem Lead and Managers. **Proposed cadence:** reminder when overdue, escalation at the next agreed check-in (default seven calendar days); shorten by agreement for urgent decisions. This is a coordination default, not an installed automation.

[Invalid-attempt example](../../examples/follow-up.md) · [Subsystem Lead](subsystem-lead.md) · [Testing Manager](testing-manager.md).
