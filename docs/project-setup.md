# Testing Project setup and operation

## Current state and fallback

The private `McGill-Baja-Racing/Testing` repository and three DEMO issues were deployed previously. **This production revision is local and unpublished. No testing Project is configured or connected to Drive.** Previous Project API access was blocked by missing `read:project` and `read:org`; write configuration also needs Project write authority. Access has not been broadened or rechecked in this revision.

Until a Project is authorized, the Testing Manager uses parent issue decision comments and ordinary issue search. [Requests excluding DEMO](https://github.com/McGill-Baja-Racing/Testing/issues?q=is%3Aissue+is%3Aopen+label%3Atest-request+-label%3Ademo) · [Preparation excluding DEMO](https://github.com/McGill-Baja-Racing/Testing/issues?q=is%3Aissue+is%3Aopen+label%3Apreparation+-label%3Ademo). Do not maintain a second tracking spreadsheet. Read committed scope and due dates in parent/task records; label/status never proves authorization.

## Configure only after authorization

1. Confirm the selected account's existing organization/Project access and private visibility. Obtain approval before publishing this revision, creating a Project, changing permissions or enabling organization automation. Do not create another repository or touch existing Baja projects.
2. Publish the reviewed files through an authorized feature branch/PR to the **existing** Testing repository. After the separately approved default-branch update, check **Issues → New issue**: Test request and Preparation task render, warnings/fields appear, and required-field behavior is tested. Schema checks are not a substitute for this browser check. Safari settings were previously left unchanged when automation was blocked.
3. Under **Issues → Labels**, compare the seven [configured labels](../config/labels.json) with existing labels. The seven were previously created; retain unrelated labels and add/update only as explicitly authorized. Form labels must already exist. Do not add auto-assignees or automatic Project membership to the forms.
4. In approved organization's **Projects → New project → Table**, create a blank **Testing Management** Project only if that creation is authorized and no intended existing Project needs adoption. Set **Private** visibility and inspect current access; do not invite people/change team permissions. In **Settings → Workflows**, inspect default close/reopen/status behavior. Leave automation off unless separately reviewed/authorized; automatic status changes must never imply sign-off.
5. Customize built-in **Status** using the list below. In table **+ → New field** (or **Settings → Fields**), add [the remaining fields](../config/project.json). Keep built-in Title, Assignees and Labels. Set new test intake explicitly to Submitted, Active, Work type=Test; preparation tasks use Work type=Preparation. Assignees are work owners, not approvers.
6. Create the five views below with **New view**, set table/board layout, filters, grouping, sorting and visible columns, then **Save changes**. Use the UI field picker for fields containing spaces; copied filter text is an aid, not a tested live configuration. Add items from an unfiltered intake view; filtered views can populate fields when adding items.
7. Add existing test/preparation issues manually through their **Projects** sidebar or **Add item**. Link the parent gate index, owner fields and requirements. Native sub-issues are optional; full parent/task links work without feature-dependent behavior. Never move existing Baja issues.
8. Run the [manual acceptance scenarios](../PILOT_TEST_PLAN.md) using clearly labeled DEMO records only after authorization. DEMO items are excluded from operational views; use a temporary authorized review view or remove that filter during the exercise. Record actual UI results. Managers approve adoption; repository permissions and any Drive setup remain separate authorization decisions.

## Fields and statuses

[project.json](../config/project.json) lists exact names, types, options, ownership and views; it is a specification, not an API export or a live Project. Keep detailed decisions and evidence on the parent issue rather than duplicate every sign-off as a Project field.

| Field group | Fields | Maintainer |
| --- | --- | --- |
| Workflow | Status; Disposition; Work type | Testing Manager from issue records |
| Prioritization | Subsystem; Priority | Subsystem Lead; Managers |
| Preparation | Preparation effort; Instrumentation category; Resource team; Parent test; Prep due | Resource manager / Instrumentation Owner |
| Identity and responsibility | Test ID; Requirement IDs; Test Lead; Instrumentation Owner; Analysis Owner; Gate record | Testing Manager with responsible owners |
| Dates | Target test date; Test day; Analysis due | Testing Manager / Analysis Owner and Subsystem Lead |

Status: **Submitted → Screening → Awaiting Approval → Awaiting Capacity → Preparing → Ready → Scheduled → Executed → Analyzing → Closed**. The phase may revisit earlier states. Ready requires installed technical evidence; Scheduled is a confirmed day after readiness. Target test date can be tentative; leave Test day empty until confirmed. Neither Ready nor Scheduled authorizes operation. Managers resolve time conflicts.

Disposition: Active, Clarification, Deferred, Declined, Cancelled. Keep the last meaningful phase during clarification/deferment, with reasons/review triggers in the issue. Declined/cancelled work may close with documented disposition, never fabricated execution. Preparation issues use relevant Submitted/Awaiting Capacity/Preparing/Ready/Closed states: their Ready means a deliverable is ready for integration, not the parent test ready for operation.

Instrumentation category: Ready, Existing needs adaptation, New development, Unknown feasibility, No instrumentation support. Clarify whether the last means no instrumentation needed or no support available. Effort low/medium/high is not a capacity plan or a safety-risk rating. Resource managers acknowledge actual capacity before Managers authorize preparation. [Decision handling](guides/approvals.md).

## Views

All operational views exclude `demo` to avoid treating examples as team work.

| View | Layout and filter | Group / sort / useful columns |
| --- | --- | --- |
| Pipeline | Board; `"Work type":Test Disposition:Active -label:demo` | Status; Subsystem, Priority, Target test date |
| Preparation workload | Table; `"Work type":Preparation Disposition:Active -label:demo` | Resource team / Prep due; Assignees, Parent test, effort, Status, Gate record |
| Confirmed testing | Table; `"Work type":Test Disposition:Active status:Scheduled -label:demo` | Test day / Target test date; Test Lead, Instrumentation Owner, Gate record |
| Analysis backlog | Table; `"Work type":Test Disposition:Active status:Executed,Analyzing -label:demo` | Analysis Owner / Analysis due; Requirement IDs, Gate record |
| Subsystem/DVP&R overview | Table; `"Work type":Test -label:demo` | Subsystem; Requirement IDs, Status, Disposition, Gate record |

Confirmed testing intentionally excludes Ready backlog. Select a specific Test day for a single confirmed day. Preparation workload includes blocked/uncommitted tasks; consult parent commitments for actual allocation. Review deferred/declined/cancelled work through Disposition filters. DVP&R Markdown also shows requirements with no issue; a Project cannot expose missing coverage automatically.

## API boundaries and implementation defaults

Repository files/PRs, labels and issues can be managed through REST/CLI after authorization. Projects use GraphQL for supported project/field/item mutations with actual node/option IDs; these JSON files cannot be posted as API payloads. Creation normally needs Project write authority (for classic tokens, `project`; organization queries may also need `read:org`); a read scope is not write permission. Stop on missing permissions, never refresh/broaden credentials without approval.

Configure and verify visibility/access, built-in status options, views/filter/layout/sort and workflow defaults manually. Capabilities may change. References checked 2026-10-15: [Issue Forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms), [form schema](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema), [Project filters](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects) and [Projects API](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects).

The approved process is in [standards](standards/testing-lifecycle.md). Proposed implementation defaults are these fields/views/labels, issue-derived IDs, record locations, reminder cadence and raw-retention duration. Managers confirm them at adoption. There is no approval automation or role-verification bot; broad write access is not a substitute for governance.
