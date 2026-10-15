# GitHub setup — proposed Stage 4, not deployed

No repository/Project/label/issue/permission/Drive writes were performed. Organization access is unconfirmed: the connected GitHub repository listing returned no accessible McGill-Baja-Racing repositories. Local pilot files are complete; GitHub rendering, permissions and views require an explicitly authorized sandbox exercise. Confirm visibility and owner before creation.

## Authorization boundary

Obtain explicit authorization for creating the target repository/Project and uploading files/demo issues. Proposed production targets are `McGill-Baja-Racing/Testing` and a separate `Testing Management` Project; do not reuse or change ProjectBoard or ESP32DataLogger. Review and separately approve any permission change, invitation, organization automation or Drive change. These instructions do not grant approval. No Actions workflows are included.

## Exact setup sequence after authorization

1. With an authorized account, confirm access to the organization and permission to create the intended private sandbox repository and Project. Confirm which account/organization owns them. Do not infer rights from this local package or request broader scopes automatically.
2. In GitHub choose **New repository**, select approved owner/name, choose **Private**, enable Issues and create the empty repository. Upload this package on a feature branch and open a draft PR; do not merge or publish without the required approval. Use a distinct DEMO repository if production `Testing` has not been approved.
3. Create labels from [labels.json](../config/labels.json) through repository **Issues → Labels → New label** (name, six-digit color, description). Existing labels need not be removed. Pre-create `test-request` and `preparation` so form labels apply.
4. Review/approve the sandbox branch merge to its default branch to test form discovery. GitHub discovers issue templates there. Open **Issues → New issue** and check both forms. Do not treat unmerged feature-branch form rendering as verified. Blank issue creation is disabled in [config](../.github/ISSUE_TEMPLATE/config.yml); this is convenience, not access control.
5. Open approved owner's **Projects → New project → Table**, choose blank and name it **Testing Management** (or explicitly approved DEMO name). Set private visibility in Project settings. Review current access and report needed changes for separate approval; do not grant new permissions by default. Disable or leave off optional auto-add, auto-close and status workflows for the pilot; inspect existing defaults, particularly close/reopen status syncing.
6. Open Project menu **Settings → Fields** (or table **+ → New field**). Customize built-in **Status** with exactly: Submitted, Screening, Awaiting Approval, Awaiting Capacity, Preparing, Ready, Scheduled, Executed, Analyzing, Closed. Remove unused default status options only in this new sandbox. Configure additional fields using the exact specification in [project.json](../config/project.json). Built-in Title/Assignees/Labels remain available. A default status, if used, is Submitted; always set Disposition=Active and Work type explicitly at intake.
7. Create the five views below with **New view**, choose layout, set filter in filter bar, choose group/sort in view menu and **Save changes**. If UI tokens differ, select field values from the filter picker; verify visible issues against the acceptance scenarios. No view is an authorization gate. Add new items through an unfiltered intake view: adding items inside a filtered view may populate filtered fields automatically; review Status and gate evidence before using those values.
8. After approval to create DEMO issues, submit [A/B/C examples](../examples/README.md) with `demo` label. Add them to the Project through issue sidebar **Projects** or Project **Add item**. Populate fields, link parent tests/requirements, copy gate record template and run the acceptance scenarios. Preparation tasks use native sub-issues where available; otherwise use a parent task-list/full issue link and backlink. Never move existing issues.
9. Check archive access with the intended reader only when authorized Drive links exist. Run local validation and record the manual sandbox results in [PILOT_TEST_PLAN](../PILOT_TEST_PLAN.md). Leadership reviews the complete pilot before any rollout or permission changes.

## Fields and responsibilities

[project.json](../config/project.json) is the exact reproducible specification, not a deployed Project export. Built-in Assignees identify current work owners, not approvers. Text owner fields are searchable names/handles without granting access.

| Fields | Type | Maintainer |
| --- | --- | --- |
| Status, Disposition, Work type | Single select | Testing Manager from issue records |
| Subsystem | Single select | Requesting lead; confirm roster on rollout |
| Priority | Single select | Leadership; qualitative rationale, no aggregate score |
| Preparation effort, Instrumentation category | Single select | Relevant resource/instrumentation owner |
| Resource team, Parent test | Text | Resource manager/work owner; linked prep per team where useful |
| Test ID, Test day, Gate record | Text | Testing Manager; Gate record links canonical parent comment |
| Requirement IDs | Text | Subsystem lead; Markdown DVP&R is canonical |
| Test Lead, Instrumentation owner, Analysis owner | Text | Named during planning with responsible managers/leads |
| Prep due, Target test date, Analysis due | Date | Committed work owner, Testing Manager, analysis owner/lead respectively |

Disposition options: Active, Clarification, Deferred, Declined, Cancelled. Keep last meaningful stage for clarification/deferred work and record resolution/re-screening needs. Declined/cancelled attempts can use Closed after documented disposition; do not fabricate readiness or execution. Reopening records reason and returns to the appropriate stage. Preparation issues use Submitted/Awaiting Capacity/Preparing/Ready/Closed as applicable, never pretend they were vehicle runs. Ready means deliverable ready for parent integration; Closed means accepted by its owner. Parent readiness still needs integrated evidence.

Instrumentation categories: Ready; Existing needs adaptation; New development; Unknown feasibility; No instrumentation support. Last category must distinguish no DAQ needed from support unavailable; it never waives evidence. Effort is Low/Medium/High, independent of operational safety risk and technical complexity assessed in the plan.

## Views

| View | Layout / filter | Group / sort / visible columns |
| --- | --- | --- |
| Pipeline | Board; `"Work type":Test Disposition:Active` | Status; show priority, subsystem, target date |
| Preparation workload | Table; `"Work type":Preparation Disposition:Active` | Resource team / Prep due; show owner, Parent test, effort, Status and Gate record |
| Next testing day | Table; `"Work type":Test Disposition:Active status:Ready,Scheduled` | Test day / Target test date; show Test Lead, instrumentation owner, Gate record; narrow to selected day |
| Analysis & closure | Table; `"Work type":Test Disposition:Active status:Executed,Analyzing` | Analysis owner / Analysis due; show requirement IDs and parent evidence |
| Subsystem/DVP&R overview | Table; `"Work type":Test` | Subsystem; show Requirement IDs, Status, Disposition, Gate record; link Markdown coverage tables |

Always inspect Markdown DVP&R for requirements without test issues; the Project cannot show missing coverage automatically. Active preparation workload intentionally includes blocked/uncommitted tasks; read parent commitments for actual capacity/WIP. Use Disposition field filters for deferred/declined/cancelled review rather than hiding them permanently. Labels only aid search; field/label divergence is resolved by documented issue decisions.

## What can be automated, and what remains manual

Repository file upload/PRs, labels and issue creation can use GitHub REST/CLI after authorization. Projects use GraphQL: create project (`createProjectV2`), add supported custom fields (`createProjectV2Field`), add issues (`addProjectV2ItemById`) and update supported item fields (`updateProjectV2ItemFieldValue`) with actual node/field/option IDs. This pilot includes no mutation script; JSON files are specifications, not executable API payloads. API availability/authentication must be checked for the selected account. Do not put credentials in repository files.

Manually configure and verify views, layout/filter/sort, default Status options, visibility/access, workflows and any organization-specific rules in the UI. Project/field/view capabilities evolve; use current API schema if later scripting them. UI names can vary. Filter references: [GitHub filtering documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects). Authoritative sources: [Projects API](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects) and [issue form syntax](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema), checked 2026-10-15.

Human actions cannot be automated into authority: confirm requester role, assess test value, commit resources/WIP, sign configuration-specific readiness, give joint on-site go/no-go and approve conclusions. GitHub required fields help completeness but do not prove roles or approval; verify actual private-repository enforcement during sandbox testing and retain lead completeness review. Do not broaden write access to enforce this process.
