# Pilot acceptance plan

Local checks are executable now; GitHub/manual scenarios below are pending an explicitly authorized sandbox. Every exercise item must be DEMO. No actual hardware operation is part of software acceptance.

Run `python3 scripts/validate.py` from root. It parses every YAML/JSON file, checks form structure/required fields and example completeness, label references, project specification, CSV schema/unique run IDs/timestamps, Markdown paths/anchors, required deliverables and unverified DEMO DVP&R states. Local file checks do not prove live permissions or GitHub UI rendering.

| Scenario | Action | Expected evidence/result | State |
| --- | --- | --- | --- |
| YAML/JSON/CSV/links | Run validator | All checks pass; exit 0; report actual counts | See validation report |
| Regression guards | Run validator self-test | Corrupted YAML, forms, CSV, relative paths/anchors and missing deliverables are rejected in temporary copies | See validation report |
| Forms discovered | Authorized sandbox default branch → New issue | Both forms render; intended labels exist; blank chooser disabled; check required-field behavior on private repo | Pending manual |
| Completeness/roles | Attempt missing question and non-lead submission | Required fields behave per GitHub; responsible lead still confirms completeness; no authority inferred | Pending manual |
| A low-effort path | Submit engine RPM DEMO, screen, record staged decisions | No separate preparation issue required; no Ready before evidence; joint final decision stays separate | Pending manual |
| B capacity blocker | Submit pressure DEMO and prep task; withhold one manager's commitment | Parent Awaiting Capacity; blocked work visible in workload; no inferred assignment commitment | Pending manual |
| C feasibility boundary | Submit strain DEMO; authorize only capped investigation | Stops at cap/review; full preparation remains unauthorized; no Ready/scheduling | Pending manual |
| Readiness vs schedule | Attempt schedule before installed evidence; then add hypothetical evidence | Governance review rejects early scheduling; fields alone cannot enforce or prove approval | Pending manual |
| Change and safety stop | Change configuration / simulate stop | Reassessment scope documented; anyone may stop; proper clearance + renewed joint go/no-go before resume | Pending manual |
| Invalid/inconclusive closure | Use DEMO R001 + follow-up; also exercise inconclusive outcome | Raw retained; validity separate from design result; unresolved requirement unverified; linked follow-up | Pending manual |
| Valid failure | Simulate applicable valid evidence outside owner criteria | Attempt valid, design FAIL; requirement not verified-failed only with applicable evidence | Pending manual |
| Overdue analysis | Set DEMO past due date; simulate reminder/check-in escalation | Named owner; reminder then documented escalation; no automation claimed | Pending manual |
| Requirement coverage | Inspect subsystem/vehicle tables with no test issue | Unplanned requirements visible in Markdown even if absent from Project | Pending manual |
| Reuse/N/A | Simulate prior evidence applicability and N/A decision | Configuration/conditions rationale or explicit N/A reason/owner; no automatic verification | Pending manual |
| Disposition | Clarify, defer, decline/cancel fictional items | Canonical decisions preserved; fields/views reflect them; no fabricated execution | Pending manual |
| Access/archive | Use authorized real link as reader when available | Intended access confirmed without unapproved sharing change; raw immutability conventions followed | Pending authorization/manual |

Manual exercise record template: scenario, sandbox URL, actor/date, action, observed behavior, evidence link, pass/fail/blocker, follow-up owner. Never mark these passed from a local validator. Production rollout requires separate approval after review.
