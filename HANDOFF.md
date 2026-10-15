# Review and deployment handoff

## Ready for review, not published

This revision improves the existing repository files on a local `production-review` branch. The original 41-file snapshot is preserved in local history. No new GitHub, organization, permission or Drive changes were made. [README](README.md) is the preview entry point; [audit](docs/repository-audit.md) explains the design changes; [validation](VALIDATION_REPORT.md) records actual checks.

Known prior state, not rechecked during this revision: the private [Testing repository](https://github.com/McGill-Baja-Racing/Testing) contains the earlier 41-file snapshot, seven configured labels and three DEMO issues. No Project was created. Project API access previously lacked `read:project` and `read:org`; browser form inspection was blocked by Safari's disabled Apple Events JavaScript setting, which was left unchanged. No current live rendering or permissions claim is made.

## Before deployment

1. **User authorizes publishing these changes.** Then compare against the current remote, use an isolated feature branch and draft PR in the existing Testing repository, and resolve any newer work without overwriting it. Review/merge requires the appropriate separate approval. Keep the repository private; do not create another prototype repository.
2. An authorized reader tests the revised forms after the approved default-branch update: chooser entries, warnings, controls, required fields, labels and a clearly DEMO exercise. No new live issues are authorized by this handoff. [Acceptance scenarios](PILOT_TEST_PLAN.md).
3. **Project creation/configuration requires explicit authorization and existing adequate access.** Follow [setup](docs/project-setup.md); stop on missing scopes. Configure fields/views manually where necessary, exclude DEMO from operational views and check workflow defaults. Do not broaden permissions or enable automation without approval.
4. Managers confirm role responsibility/coverage, designated test-approval Manager/substitution, review cadence, resource capacity handling and proposed implementation defaults. Subsystem Leads enter actual priority requirements/criteria; Instrumentation Owners enter actual equipment/calibration records. Empty operational tables intentionally contain no invented team data.
5. **Drive changes require separate consent.** An authorized archive owner confirms the existing location, stable links, intended reader access, retention and backup. No folder creation/sharing change is implied.
6. Walk through simple, adaptation, feasibility and invalid-follow-up scenarios. Managers authorize adoption only after practical checks pass; do not treat the local validator as rollout approval.

The package contains repository files, a review diff and preserved baseline/history for review. A rendered README preview is optional review material, not a deployed website or Project. [Implementation coverage](IMPLEMENTATION_CHECKLIST.md).
