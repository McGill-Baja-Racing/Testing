# Implementation checklist

## Delivered locally

- [x] Separate preparation sandbox; subsequently deployed only to the explicitly authorized new private Testing repository. No existing Baja repository changes.
- [x] Native test-request and medium/high preparation forms; blank issue config; no duplicate report form.
- [x] README onboarding and explicit approved-methodology/proposed-implementation distinction.
- [x] Lifecycle, technical and V&V standards plus approval/day/closure guides.
- [x] Modular plan, gate records, readiness, run CSV, issue results, technical report, DVP&R and sensor record templates.
- [x] DEMO vehicle, drivetrain and suspension DVP&Rs; no fabricated verification/limits.
- [x] Model/device/install/calibration/contextual readiness inventory.
- [x] Three DEMO requests, linked medium/high preparation, invalid-run follow-up and sample run log.
- [x] Proposed field/view/label configuration and exact authorized deployment steps.
- [x] Data layout, IDs, raw immutability, metadata, access and retention proposal.
- [x] Local walkthrough and repeatable validation script with acceptance scenarios.

## Pending explicit authorization / manual checks

- [x] Confirm repository owner/access and create the authorized new private McGill-Baja-Racing/Testing target; Project API access is blocked.
- [x] Publish all 41 pilot files to the new repository default branch and create seven configured labels.
- [ ] Verify rendered forms manually; local syntax passes but Safari automation is disabled and was left unchanged.
- [ ] Create private Project, configure views/fields, inspect workflow defaults and current access.
- [x] Create three DEMO issues from published form fields through the API; verify bodies/labels.
- [ ] Run remaining manual acceptance exercise; record actual results.
- [ ] Leadership approves production rollout; separately approve permission or Drive changes if needed.

Validation results are recorded in [validation report](VALIDATION_REPORT.md). Local schema checks are not GitHub's server-side validator. [Pilot acceptance plan](PILOT_TEST_PLAN.md).

See [current deployment status](README.md). No Project was created because existing authentication lacks the required Project/organization read scopes; no access was broadened.
