# Revised draft review and evidence

Status: draft 2 for review; no registration, adoption or workflow execution.
Repository basis: `00115c71931bcae79909602d653740d3bb72dfa1`.

## Design correction

The first draft treated intent as supplied and reconciliation as a generic claim
comparison. The user's feedback made the missing purposes explicit: develop an
understanding of how they want to proceed through the DAG, and reconcile the
actual contents of deliverable folders with code and evidence. The user selected
"Infer and clarify material gaps" for intent gathering; a mandatory discussion
checkpoint for every new graph was not selected.

The revised graph method now directs intent gathering, DAG route selection,
scope development from documents and code, graph construction, and return to
the loop. Its template records the intended outcome, steering and selected route.
The revised reconciliation method names the target deliverable files and calls
for warranted document edits. Ongoing traversal and recovery remain primarily
in the LOOP_INIT drafts, with their structure retained.

## Sources used to make the methods concrete

Historical examples inform useful distinctions; their process details are not
prescribed merely because they occurred:

- [App shell grammar reconciliation](../../../projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/pkg07/MANAGER_RETURN_v1.md):
  one bounded obligation checked against a particular implementation and evidence,
  with local document corrections separated from wider completion.
- [App UI refinement graph](../../../projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_UI_REFINEMENT_20260912/WORK_GRAPH.md):
  coherent outputs, independent work and review/integration dependencies.
- [Piping picking-stability graph](../../../projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-PICKING-STABILITY/WORK_GRAPH.json):
  implementation and subsequent verification remained distinct obligations.

Current deliverable contents were inspected to ground the new file-level method:

- [Piping viewport ScopeOfWork](<../../../projects/chirality-piping/execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-01_3D viewport and centerline editor/ScopeOfWork.md>)
  contains definition, completion/reliance, production/verification, values/decisions
  and output/evaluation sections, including older setup wording and controlling
  current declarations. Reconciliation must distinguish those statements.
- [App document-kit ScopeOfWork](../../../projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts/ScopeOfWork.md)
  has a controlling amendment as well as consolidated semantic sections.
- A bounded Terra/high inspection additionally checked App DEL-02-04 and Piping
  DEL-09-04. Both consolidate the old four-document kit in ScopeOfWork.md. This
  supports inspecting the current carrier instead of manufacturing legacy files.

No sampled deliverable was changed or reconciled during this draft revision.
Historical test passes were read, not rerun.

## Walkthroughs

| Case | Required result under draft 2 |
|---|---|
| Steering gives a desired outcome but no deliverable IDs | Infer the result and priorities; locate candidate deliverables, follow prerequisites and explain the selected route. Ask only where an unresolved interpretation would materially alter the work. |
| Chat changes the priority or intended stopping point | Revise the graph's intent and selected route, preserve completed results and explicitly account for displaced obligations. A tentative proposal is not an adopted scope change. |
| Other DAG nodes are ready but unrelated to the objective | Exclude them from the undertaking rather than treating graph readiness as a work-selection mandate. |
| Design uncertainty prevents a useful implementation brief | Create a bounded investigation/design node with the question it must answer; do not fabricate implementation detail. |
| Code establishes a formerly unresolved detail | Inspect the affected ScopeOfWork section and relevant decisions; update the current detail and supporting records where authorized, preserving genuine future requirements. |
| Code violates a documented requirement | Retain the requirement and identify the specific implementation gap in Remaining and the graph. Do not make the defect the new specification. |
| Bounded change exposes an interface/dependency consequence | Compare the affected local dependency statements and evidence, update both representations within scope, or return the precise amendment needed. Do not silently change the project DAG. |
| Authorized documentation edits are required | Make and check those edits. A standalone findings report cannot claim the edit assignment complete. |
| Document edits require authority outside the assignment | Return exact proposed edits and leave their application outstanding in the graph. |
| Evidence shows no document change is warranted | Return the checked basis and supported no-change result; avoid a ceremonial edit. |
| Missing graph target or historical recovery cursor | Recover the named work and apply the cursor's validation rules. Do not quietly start a duplicate undertaking. |
| Interrupted work has unrecorded edits or live workers | Inspect files and active operations before repeating work; confirm workers/checks stopped or explicitly transfer ownership before reassignment. |
| Source or document target changes during reconciliation | Recheck affected comparisons against current bytes or report stale evidence; preserve concurrent edits. |

These are document walkthroughs, not executed product tests or evidence of
model-specific performance on reconciliation.

## Independent review and validation

A Terra/high TASK reviewed the revised methods, template, loop candidates and
aligned companion patch. It found that the moved recovery guidance omitted an
explicit live-worker/ownership check. Both LOOP_INIT drafts now carry that check
in Step 0. The reviewer backchecked the saved correction and returned PASS,
with no other material findings. This review concerns draft quality; adoption
still requires review and checks on the actual applied candidate.

Validation uses the existing workflow metadata validator, package containment
and link checks, and `git apply --check` for the companion patch. Saved output
identities are in [BASIS.json](BASIS.json). Active tracked files and the registered
catalog remain unchanged. No full product test or catalog-registration result
is claimed for these unapplied drafts.

## Revision and supplied context

The earlier reviewed draft, its review and basis are retained outside workflow
discovery in `.archive/draft-1.tar.gz`. Its review verdict remains historical.
Current files replace that draft for the next owner review.

HELP_HUMAN revised and integrated the methods in response to the user, using the
already consulted HELPS_HUMANS role guidance and bundled create-workflow method.
A Terra/high TASK supplied bounded deliverable-file discovery and another
performed review/backcheck. Launches and returns remain in the task conversation;
source identities and actual delegation configuration are recorded in BASIS.json.
Role/write limits were instruction-asserted in the shared checkout. These files
remain local review drafts and have not been committed or registered.
