# Decision index — parent test issue

Required: test ID/issue link; current plan/configuration reference; each applicable decision's author/role, date/time, scope, rationale and evidence/comment link. Start pending; leave no implied sign-offs. Link records already held elsewhere instead of retyping them.

## Intake and screening

Subsystem Lead completeness confirmation: __.
Specialist screen: category (Ready / Existing needs adaptation / New development / Unknown feasibility / No instrumentation support); preparation effort low/medium/high; tasks; lead time/estimate; dependencies/uncertainty; author/date: __.
Technical complexity and operational safety risk are assessed separately in the plan. State whether “No instrumentation support” means no instrumentation needed or unavailable support.

## Five gates

| Gate | Decision / scope / rationale | Decision-maker and date | Evidence/comment |
| --- | --- | --- | --- |
| 1. Test value | Pending: approve / defer / decline | Designated test-approval Manager or substituting Manager | __ |
| 2. Bounded investigation, if needed | Pending, or N/A with reason; cap, deliverable, stop/review point | Managers, after resource commitment below | __ |
| 3. Full preparation | Pending; defined work authorized only after resource commitment below | Managers | __ |
| 4. Technical readiness | Pending; installed configuration, intended use, successful applicable checks and limits | Relevant technical owners / Instrumentation Owner | __ |
| 5. Final execution | Pending: joint go/no-go for actual conditions subject to mandatory clearance | Subsystem Lead AND Testing Manager | __ |

## Resource commitment — required before gates 2 and 3

Per team and phase: resource manager; defined work/deliverable; owner; effort estimate; allocated availability; due date; dependencies; current commitments and manageable simultaneous-work limit; dated acknowledgment/comment. Investigation commitment covers only its cap. Full preparation requires a fresh/explicitly extended commitment and Manager authorization. Uncommitted work stays Awaiting Capacity.

## Scheduling, changes and closure

- Confirmed test day: Testing Manager record only after readiness; Managers resolve time conflicts.
- Change: old/new configuration or scope; Testing Manager reassessment with technical/safety owners; checks repeated; revised approvals where needed. Major scope change returns to screening.
- Stop/resume: reason/run/time; clearance by relevant owners; renewed joint go/no-go before resume.
- Closure: Subsystem Lead conclusion approval; Testing Manager record check; links to results, DVP&R updates and unresolved-objective follow-ups.

For simple tests this index and a few dated comments suffice. Separate linked preparation tasks are required only for medium/high effort. [Authority](../docs/standards/testing-lifecycle.md#five-distinct-gates).
