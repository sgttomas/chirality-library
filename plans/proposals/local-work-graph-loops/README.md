# Local work graphs and bounded reconciliation — revised review draft

Prepared for owner review against repository revision
`00115c71931bcae79909602d653740d3bb72dfa1`. The active workflows, loop files,
project instructions and records have not been changed. Nothing here registers
or executes a new workflow, resumes an undertaking, or records an owner ruling.

## Read the proposed artifacts

| Artifact | What to review |
|---|---|
| [Construct a local work graph](../../../.chirality/workflow-drafts/construct-local-work-graph/WORKFLOW.md) | Infer and clarify user intent, choose the relevant route through the DAG, develop scope from deliverables and code, then construct the graph. |
| [Graph template](../../../.chirality/workflow-drafts/construct-local-work-graph/resources/work-graph-template.md) | Compact coverage, work, results and recovery fields. The format is optional; existing JSON graphs can continue. |
| [Bounded reconciliation](../../../.chirality/workflow-drafts/bounded-reconciliation/WORKFLOW.md) | Reconcile a stable code slice with the actual contents of its deliverable folders and make the warranted document changes. |
| [Proposed App LOOP_INIT](proposed/projects/chirality-app-dev/loop/LOOP_INIT.md) | Current graph pointer and the common six-step loop, with App-specific project pointers. |
| [Proposed Piping LOOP_INIT](proposed/projects/chirality-piping/loop/LOOP_INIT.md) | The same loop structure, with Piping-specific project pointers and its existing graph selected. |
| [Companion changes](COMPANION_CHANGES.patch) | Exact proposed edits to Root/project instructions and current coordination pointers needed to make the loop changes coherent. |
| [Review and walkthrough](REVIEW.md) | Sources, validation, interruption cases and outstanding adoption checks. |

The workflow packages are ordinary local draft files under
`.chirality/workflow-drafts/`, outside registered workflow discovery. This
directory is Git-ignored by repository policy; they are not committed or
automatically backed up by Git. Preserve their reviewed bytes as part of the
eventual adoption. The proposed loop files and companion patch are also local
review material. Relative paths inside a proposed loop resolve at its intended
project location, not at this review directory.

## What changed after feedback

The first draft assumed a sufficiently defined objective and concentrated on
representing and maintaining a graph. It also described reconciliation as a
generic claim comparison. That obscured the two methods' practical purposes.

Graph construction now starts with interpreting the user's init steering and
subsequent chat: desired result, priorities, approach, scope and completion.
The user selected **infer and clarify material gaps**; the method makes its
reading visible and asks where different answers would change the work. It then
selects a route through the DAG, reads the relevant deliverables and code, and
develops enough detail to construct executable nodes. Ongoing traversal and
recovery stay primarily in LOOP_INIT, avoiding a second loop manual.

Bounded reconciliation now targets named deliverable folders and their contents.
It explicitly covers ScopeOfWork.md and the active legacy equivalents, Remaining,
dependency records, memory and references. It compares docs to code and code to
docs, then makes the warranted edits. Future requirements remain visible when
implementation falls short; established details should replace obsolete setup
wording or resolved TBDs where appropriate. A separate generic report is not a
substitute for the authorized document changes.

The loop drafts keep the structure the user preferred. Only their graph-construction
and reconciliation steps have been aligned with these clearer methods. The
companion patch's reconciliation wording is aligned too; its other proposals
remain for review. The earlier reviewed draft is preserved outside discovery in
`.archive/draft-1.tar.gz`; the earlier review verdict does not cover this revision.

## The proposed behavior

`LOOP_INIT.md` identifies the current graph. The session verifies its saved basis
against actual work and follows ready nodes. With no graph, construction develops
intent and scope from the conversation and project evidence, saves the graph,
updates the pointer and returns to the loop. A broken pointer calls for recovery;
missing intent or an existing pause is not permission to start a new undertaking.

The graph lasts across sessions and records the work, its consequences and next
steps. Stable results can stay in the undertaking folder while planned bounded
reconciliation updates the deliverables. Those nodes name the affected documents
and the code/evidence to consume; they can run alongside independent implementation.
Implementation and reconciliation completion remain distinguishable. Required
operational evidence stays available without becoming the subject of the graph.

## Concrete choices proposed for approval

1. **Workflow home.** Adopt both methods into Root's bundled `chirality-root`
   library after review so both projects can select the same source-qualified
   methods. Their provisional names are `construct-local-work-graph` and
   `bounded-reconciliation`. Draft authoring does not register them there.
2. **New graph home.** Prefer
   `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` in the owning
   project. Keep associated evidence there when it has no better existing home.
   Continue serviceable historical graphs in place; there is no bulk migration
   of AgentRuns or requirement to change an existing JSON graph's format.
3. **Initial pointers.** App is `none`: the inspected direction records a
   development pause pending owner-steered reconciliation, and the last loop
   amendment is not an active product undertaking. Piping points to its existing
   UI implementation graph. Main and surviving worktree copies have different
   continuation state, so adoption must verify the owning branch and current
   owner steering before relying on it. This proposal resumes neither project.
4. **Record placement.** Current state and recovery live in the graph; concise
   claim/results records and supporting evidence are linked. Routine development
   sessions no longer need an additional handoff, run narrative or loop receipt.
   Existing records remain intact. Other expressly selected workflows retain
   their own output contracts.
5. **Navigation upkeep.** Updating the explicitly designated current-graph
   pointer within an authorized undertaking is state maintenance. Changing the
   loop procedure or its constraints remains an instruction amendment. The
   companion patch makes this distinction explicit in Root `AGENTS.md`.

These choices are proposed, not prior owner decisions. The user has directed
drafting and specified that bounded reconciliation is a separate method, the
loop points to or constructs its graph, and interruption/transfer must be
recoverable from that graph. Earlier discussion remains design input unless
explicitly adopted.

## Changes to existing surfaces

| Surface | Proposed change |
|---|---|
| App/Piping `loop/LOOP_INIT.md` | Replace the long procedure with project pointers and the common orient, construct/revise, organize, execute/check, reconcile, continue/close sequence. |
| Root `AGENTS.md` | Distinguish a navigation-pointer update from a behavioral instruction change. No other role or governance amendment. |
| App `AGENTS.md` | Keep App fences, dependency selection, evidence contract, checks and substantive decision rules in their owning project instructions; point historical LOOP_INIT evidence citations there. Replace receipt-specific attribution placement with available execution evidence. |
| Piping `AGENTS.md` | Retain independent review, protected checks, DEC-025, empirical evidence, native behavior and integration constraints that would otherwise disappear when LOOP_INIT is shortened. |
| Both project `AGENTS.md` | Establish persistent graph continuity, bounded factual reconciliation and concise records; supersede routine development receipt append requirements without erasing operational provenance. |
| App `_Coordination/_LATEST.md` | Route entry through the graph pointer and label the old loop-amendment run as historical context. |
| Both `_Coordination/_COORDINATION.md` | Add a current navigation note while retaining historical ruled records. |

The development launch prompts already enter HELP_HUMAN through `LOOP_INIT.md`
and need no change. Existing receipt files, their frozen prefixes, validators
and self-check integration remain unchanged: the validators protect retained
history and do not demand a new entry on every invocation. No product code,
deliverable, accepted DAG, standing hold or release authorization is changed.

Task-management has separate launch prompts and record requirements. It is not
activated or redesigned by this development-loop proposal. The inspected
prompts also reference a retired role; that existing issue is outside this
draft and must be addressed before using those entrypoints.

## Adoption after review

Apply the reviewed workflow packages, loop replacements and companion edits
together in an authorized instruction tranche, register the methods in the
intended library, and verify their source-qualified discovery. Revalidate current
graph selection and owner holds on the actual adoption revision. Run the checks
required for that candidate and obtain the required independent review. Route
notices to the App and Piping development loops; because Root `AGENTS.md` also
changes, discover and notify any other loop whose accepted corpus pins it.
Each receiving loop owns its adoption. Do not re-pin or migrate unrelated
consumers as part of this draft.

The authoring method is the existing bundled
[`create-workflow`](../../../workflows/create-workflow/WORKFLOW.md), identity
`(bundled, chirality-root, workflow, create-workflow)`. No same-name collision
was found for the two drafts in inspected project, user or bundled libraries.
The proposed methods are not yet selectable through a registered catalog.
