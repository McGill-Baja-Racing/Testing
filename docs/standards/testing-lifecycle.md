# Testing lifecycle

This is the approved testing process. Project statuses are an implementation aid; documented decisions authorize work.

## Request and screen

Only a **Subsystem Lead** formally requests a test in GitHub. Other members and Managers raise needs through the appropriate Subsystem Lead. The request states question, physical measurements, outputs, intended decision, sufficient evidence, why the test matters, consequences of not testing and preferred/latest useful timing. The Subsystem Lead confirms completeness; the Testing Manager reviews clarity/testability without changing the objective unilaterally.

Relevant specialists, including Electronics, quickly screen feasibility before prioritization: instrumentation category, low/medium/high preparation effort, tasks, dependencies, uncertainty and rough lead time. They may return precise clarification questions. Screening is not a resource commitment. [Request guide](../guides/subsystem-lead.md).

## Five distinct gates

| Gate | Who decides | Required record before advancing |
| --- | --- | --- |
| 1. Test-value approval | Managers; designated test-approval Manager or any substituting Manager records it | Individual approve/defer/decline decision with rationale, scope, identity and date after screening |
| 2. Bounded feasibility authorization, when needed | Managers, after relevant resource managers confirm capacity for that investigation | Question, cap, defined work/deliverable and stop/review point; no implied full-development approval |
| 3. Preparation authorization | Managers, **after resource managers confirm capacity and commit defined work** | Team, owner, work scope, allocated availability/effort, due dates, dependencies and manageable simultaneous-work limit |
| 4. Technical readiness | Relevant technical owners, including the Instrumentation Owner; Testing Manager coordinates | Procedure/equipment/installation/calibration, units/timebase/logging and successful installed integrated verification where applicable |
| 5. Final execution go/no-go | Subsystem Lead **and** Testing Manager jointly, subject to mandatory technical/safety clearance | On-site configuration/conditions, clearance and both decision-makers' identity/date |

An earlier gate never implies a later gate. Keep [decision records](../../templates/approval-record.md) on the parent test issue. A known method may mark gate 2 N/A with a reason. Investigation capacity and authorization do not commit full development. At the cap stop and review; any expanded work needs renewed capacity and authorization.

## Prepare and schedule

The Testing Manager coordinates; named technical owners prepare. Low-effort work may stay a checklist. Medium/high work needs linked preparation issues. Name the **Test Lead**, **Instrumentation Owner**, **Analysis Owner** and analysis due date during planning. Resource managers decide how much simultaneous work their teams can manage.

Only fully technically prepared tests enter the confirmed day. Integrated verification must succeed where applicable; if unsafe/inapplicable, record the reason, alternative evidence and required technical/safety clearance. A possible test may remain in a backlog/planning view, never labeled confirmed/ready. Managers resolve time conflicts. Three to four weeks is a normal expectation for significant tests, not a ban on small or urgent requests.

Configuration changes after readiness require the Testing Manager's reassessment with relevant technical/safety owners; repeat affected checks. Significant scope changes return to screening and revised authorization as needed. Alternative methods must answer the original question; new investigations from unexpected observations require new linked requests.

## Execute, analyze and close

The Test Lead follows the plan and records every run, including deviations and raw references. Check data after each run when feasible, at minimum before leaving where practicable. Preserve originals, metadata and evidence links. [Day operations](../guides/testing-day.md).

The subsystem owns analysis and conclusions; Electronics/Instrumentation Owner supports measurement quality. The Testing Manager tracks deadlines with reminder then escalation and checks documentation; the Subsystem Lead approves engineering interpretation. Close attempts as valid, inconclusive, invalid or aborted. A valid result may show design PASS or FAIL, or an exploratory finding. Invalid/inconclusive attempts need linked follow-ups for unresolved objectives; relevant requirements remain unverified. [Closure](../guides/closure.md).

Urgent new tests still need individual Manager approval. The Testing Manager and affected leads may rearrange already approved work. Anyone can stop unsafe work; resume only after proper clearance and renewed joint go/no-go. Stopping, inspecting and making safe never wait for paperwork.
