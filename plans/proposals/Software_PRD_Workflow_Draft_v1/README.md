# Software PRD workflow: draft version 1

This is a portable review export, not an installed or registered Chirality workflow.

## Read and discuss

Start with `software-prd/WORKFLOW.md`. Its two linked resources provide optional product-development questions and guidance on records and review. Those three files are the complete reusable package. Read `review/DESIGN_AND_REVIEW.md` for the design choices and source distinctions and `review/WALKTHROUGH.md` for the fifteen analytical cases. `review/PACKAGE_VALIDATION.json` records local structural checks, not a live runtime validation. `review/DELIVERY_STATUS.json` records the exact delivered state and source identities.

The main proposed choices are two grouped human checkpoints, proportionate intake and records, and separate examination of the completed candidate before human acceptance. Existing explicit alignment can satisfy the first checkpoint without repeating the same decision. Maintenance remains outside scope. The method ends with an accepted PRD and handoff, not with execution of FEED.

## Registration remains a later action

Creation of this package does not authorise registration. Inspect the exact files and resolve changes in discussion first. Before any later registration, resolve the actual intended project or personal root, inspect the effective catalog for collisions, and retain the source-qualified identity. Do not invent a sourceRootId from this export path.

In Chirality App, the reviewed draft route is `<project>/.chirality/workflow-drafts/software-prd/` or `~/.chirality/workflow-drafts/software-prd/`, after the real destination is resolved. Use the host's review and registration controls and verify the resulting catalog entry. Do not copy this draft directly into `.chirality/workflows` as a substitute for review. A bundled-library contribution needs separate library-maintenance authority. Registration must not automatically execute the workflow.

After accepted registration and observed discovery, select `Workflow: software-prd` or its verified source-qualified identity. The present export has not performed those steps.

No execution.json is included. The package has no unverified tool or role restriction metadata; actual host permissions and instructions still govern. No live PRD run, independent review, accepted PRD, or empirical reuse is claimed.

SHA256SUMS.json identifies the bytes in this export, excluding itself. Earlier supplied sources remain unchanged.

## Registration note (2026-09-26)

On the owner's direction, this draft was revised to current conventions and registered in the Root bundled library at `workflows/software-prd/` (tranche `ROOT-SOFTWARE-PRD-REGISTRATION-20260926`). The registered package is in core navigation and adds an `execution.json` limiting compatible roles to HELP_HUMAN, HELPS_HUMANS and WORKING_ITEMS. This folder remains unchanged as history apart from this note. `SHA256SUMS.json` identifies the export as delivered; its `README.md` entry matches this file as it stood before the note was added (repository revision `8f9bd314c5f2499e6faf5bf4bdce917927e8185e`).
