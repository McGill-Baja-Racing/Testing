# Repository acceptance scenarios

This filename is retained for existing links. The scenarios apply to the production revision. Run local validation with Python 3.9+ and Ruby's standard YAML library; no packages/network needed:

```sh
python3 scripts/validate.py
python3 scripts/validate.py --self-test
```

Local automation checks file/form syntax, example field coverage and record references, links, CSV integrity, configured views and fictional DVP&R states. It does not execute GitHub approval gates or certify an engineering method. [Actual results](VALIDATION_REPORT.md).

## Review the example flows locally

| Scenario | Check | Required conclusion |
| --- | --- | --- |
| New Subsystem Lead | From README find request form and lead guide in two minutes | Role restriction, measurement need, timing and no implied approval are clear |
| Manager review | Open Manager guide and decision index | Individual value decision; capacity first, then preparation authorization; five separate gates |
| Simple RPM | Follow request → compact plan → logs → exploratory interpretation | Checklist suffices; no forced design threshold; readiness/go-no-go and closure are separate |
| Medium pressure | Follow adaptation task, both resource owners and installed checks | Missing commitment blocks preparation; standalone calibration is insufficient |
| Complex strain | Follow capped feasibility and conditional full-preparation task | Stop/review at cap; full development needs fresh commitments and separate Manager authorization |
| Invalid attempt | Follow pressure mismatch → retained sample log → linked follow-up → DVP&R gap | Process violation identified; no design FAIL or verified requirement inferred |
| Electronics navigation | From README locate availability, calibration and pending work | Available differs from ready for this installation/test |

## Manual checks after separately authorized deployment

All are **pending** for this revision. Previous DEMO issue creation does not pass revised-form checks. Record scenario/date/actor/URL, observed result and evidence; use only authorized DEMO records and never actual vehicle operation for software acceptance.

| Scenario | Action and expected behavior |
| --- | --- |
| Forms | On approved default branch, open New issue and both forms. Verify visible labels/descriptions, multiline fields, dropdown choices, required-field behavior including timing, and labels on submission. Check non-lead submission still requires governance review; no identity enforcement is claimed. |
| Simple path | Exercise low-effort checklist without separate prep issue. Explicit gate comments precede corresponding stage changes. |
| Capacity | Withhold one medium-task manager commitment; keep Awaiting Capacity. Do not infer commitment from assignment. Managers authorize defined preparation only after commitments. |
| Feasibility | Authorize only a bounded DEMO investigation with capacity/cap. Review at cap; no automatic development/Ready promotion. |
| Project views | Configure per specification. Confirm only Scheduled tests appear in Confirmed testing, Ready remains backlog, DEMO excluded operationally, workload includes blockers, analysis sorted by due date. Verify actual filter-picker syntax. |
| Change/stop | Simulate post-readiness configuration change: reassessment/repeated affected checks before readiness restored. Anyone can stop; proper clearance and renewed joint go/no-go before resume. |
| Valid failure | Simulate applicable valid data failing justified criteria: attempt valid, design FAIL, requirement not verified-failed only with applicable evidence. |
| Inconclusive/invalid | Preserve originals, record limitations and linked unresolved-objective follow-up, leave requirements unverified. Lead approves interpretation and Testing Manager checks closure records. |
| Deadline | Simulate overdue analysis: named owner receives reminder, then unresolved work escalates to Subsystem Lead/Managers. No automation claimed. |
| Evidence reuse/coverage | Show unplanned requirement with no issue in DVP&R; require configuration/conditions justification for reused evidence and owner/reason for N/A. |
| Disposition | Clarify/defer/decline/cancel DEMO work: reasons preserved, appropriate earlier status, no fabricated execution. |
| Archive/access | Only with separate Drive consent: verify actual links and intended reader access, manifest/original retention, and backup/custodian without unapproved sharing changes. |

Managers review practical results before adoption. [Deployment boundary](HANDOFF.md).
