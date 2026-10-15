# Repository audit and design decisions

## Starting point

Inspected the existing 41-file repository snapshot, forms, examples, templates, configuration and validator. The baseline is preserved in local Git history. This revision applies the Production Repository Brief; the attached document supplies process requirements, not authorization to publish.

| Reuse | Improve |
| --- | --- |
| Existing paths, two native Issue Forms, common plan and results-on-parent pattern | Replace deployment-heavy README with role navigation and a short request path |
| Distinct approvals, contextual readiness and raw-data retention | Enforce capacity confirmation before Managers authorize preparation; distinguish five gates |
| Markdown verification and device/calibration structure | Separate fictional examples from empty operational registers; provide complete fabricated examples |
| Offline YAML/CSV/link checks | Validate form attributes, example answers, cross-record IDs, Project/view consistency and negative cases |
| Published private demonstration context | Keep deployment history in handoff; no new GitHub/Drive writes or browser settings changes |

Missing role guides are added at stable paths. Existing guides link to authoritative standards rather than repeat them. Real names, inventory, requirements, dates and engineering limits must come from responsible owners; none are inferred. Blank reusable templates are intentional; working examples use concrete, explicitly fictional values. Stage labels and internal implementation history are removed from onboarding.

Proposed implementation defaults (not engineering policy): Project fields/views/labels, issue-derived IDs, record locations, reminder cadence and raw-data retention duration. [Setup](project-setup.md) lists decisions and authorization-dependent steps. No approval bot, Actions workflow or custom tracking application is introduced.
