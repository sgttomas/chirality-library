---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-01
package_id: PKG-02
decomposition_basis: execution/_Decomposition/PROJECT_DECOMP.md
project_scope_refs: [SOW-0004, SOW-0005, SOW-0008, SOW-0010, SOW-0017, SOW-0018, SOW-0021]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-003, OBJ-004, OBJ-005]
---

# DEL-02-01 — Carry and recover an authorized holding change

## Purpose and Objective Traceability

A maintainer holding a bounded, authorised undertaking can carry a change to a
Library holding from preparation through proportionate verification, review
and integration, and can pick up work that was left unfinished or interrupted,
using guidance found in the Library and not in a conversation. The holding may
be one of the maintenance instructions themselves.

This deliverable contributes three things to that result. The first is the
guidance for five of the eight operations in PRD R04 (add or revise; organise,
relocate or retire; review and integrate; recover or continue; change the
maintenance means), with the rule for how much verification a change needs and
the rule for exceptional custody. For the other three operations it
contributes the connection to the deliverable that owns them. The second is
the guidance shown to work on an actual change, including a change to the
maintenance means. The third is recovery and custody shown to work on retained
work or a labelled case.

Its allocation is the DEL-02-01 card of the
[accepted decomposition](../../_Decomposition/PROJECT_DECOMP.md), with its
interfaces in §9. It serves [PRD](../../../docs/PRD.md) objectives O1 to O5 and
is the accountable contribution for acceptance criteria A2 (with DEL-03-01),
A5 and A8.

| Scope item | What this deliverable contributes | Objectives | PRD |
|---|---|---|---|
| SOW-0004 | Instructions for adding or revising a holding: purpose, scope, destination, relevant existing material, source identity and checks | OBJ-002 (O2) | R04 "Add or revise a holding", A2 |
| SOW-0005 | Instructions for organising, relocating or retiring a holding: actual references and consumers, replacement or historical standing, recovery and deletion authority | OBJ-002, OBJ-003, OBJ-005 (O2, O3, O5) | R04 "Organize, relocate or retire", §5 |
| SOW-0008 | Review and integration with proportionate scrutiny, the actual checked revision, findings, updates to owning text and the repository change procedure | OBJ-002, OBJ-003 (O2, O3) | R04 "Review and integrate", R12, R14, A2 |
| SOW-0010 | The entry, roles, methods, tools and execution maintained under the text already in force: a replacement reviewed under it, the preceding text kept usable, adoption only after verification | OBJ-001, OBJ-002, OBJ-003 (O1, O2, O3) | R06, R04 "Change the maintenance means", A5 |
| SOW-0017 | Verification of the actual candidate in proportion to the change, with content, behaviour and consumer-interface claims kept apart and missing evidence stated | OBJ-002, OBJ-003, OBJ-004 (O2, O3, O4) | R12, A2, A4 to A6 |
| SOW-0018 | Unfinished work recoverable from its locality and review record | OBJ-002, OBJ-004, OBJ-005 (O2, O4, O5) | R12, R04 "Recover or continue", A8 |
| SOW-0021 | Exceptional exclusive custody through an existing mechanism, with holder, item, reserved operation, release and recovery condition and honest enforcement limits | OBJ-002, OBJ-005 (O2, O5) | R14, A8 |

## Deliverable Definition — Ontology

A **holding** is anything the Library maintains: an instruction, a tool, a
publication, reference material or an execution text such as a scope. The
**maintenance means** are the holdings used to maintain the others: the entry,
the roles, the methods, the tools and the execution texts.

The **selected basis** is the identified text or revision that actually
governs a use or a review. A proposed replacement is not the selected basis
until it is verified and adopted.

The **guidance** is a connected set of instructions held where a maintainer
already reads them. It is not one workflow per operation.

A **maintenance case** is an actual authorised change with its review record.
A **recovery case** is real retained work or a case constructed for the
purpose and labelled as such.

**Custody** is an exceptional reservation of one identified item for one
operation by one holder. It is not a general lock, and readers keep the last
checked-in material while it lasts.

Integration, publication, examination and adoption are different acts; the
guidance covers integration.

- **OUT-001** — The maintenance guidance at its existing homes. In `AGENTS.md`: preparing a change to a holding and receiving a contributed one ("Maintain holdings and receive contributions"); relocating or retiring a holding ("Holding changes and recovery"); how much verification a change needs, who integrates it and under which Git conventions ("Verification and authority" with its standing Git grant); and the pointer that sends a workflow change to create-workflow. In `workflows/create-workflow/WORKFLOW.md`: creating or revising a reusable workflow. For an execution holding: `workflows/scope-of-work/WORKFLOW.md` for a deliverable's scope, and `workflows/scope-change/WORKFLOW.md` for the accepted decomposition and the commitments that follow from it. In `docs/document-metadata.md`: the header of a maintained Markdown document. For diagnosis, reconciliation and connected change the guidance sends the maintainer to `workflows/bounded-reconciliation/WORKFLOW.md`; for publication preparation and update inspection, to the consumer route in `README.md`. It restates neither. Serves SOW-0004, SOW-0005, SOW-0008, SOW-0010, SOW-0017.
- **OUT-002** — The guidance applied: an actual authorised change to an instruction or a tool carried through preparation, verification, review and integration by the guidance in OUT-001; and a revision of a maintenance instruction, the entry or a supporting tool made under the text that preceded it. One change can be both. Serves SOW-0004, SOW-0008, SOW-0010, SOW-0017.
- **OUT-003** — Recovery and exceptional-custody guidance in the "Holding changes and recovery" section of `AGENTS.md`, and its use: real retained work or a labelled recovery case continued from its locality and review record; and, where custody applies, a real or labelled interrupted-custody case that exercises release or recovery and shows what the mechanism does not enforce. Serves SOW-0018, SOW-0021.

An existing checked holding can supply part or all of an output. A shown gap
is repaired at the home that owns it.

The decomposition names the roles among the maintenance means (SOW-0010) and
allocates what the role instructions under `agents/` say to no deliverable,
apart from the passages of `agents/AGENT_HELP_HUMAN.md` that are DEL-04-02's.
This scope sets a criterion on how a role is changed (REQ-005) and none on
what a role says. Whether the role instructions and the role registry are this
deliverable's product is the owner's to decide.

Boundary:

- **CLM-001** — The reconciliation method, and the diagnosis and connected-change assessment it carries, belong to `DEL-04-01`; this deliverable's guidance invokes that method. The method that questions goals and framing belongs to `DEL-04-02`.
- **CLM-002** — Tools and their usage instructions belong to `DEL-03-01`. The content of the shared-reference clarification belongs to `DEL-02-02`. Obtaining, version selection, update inspection, named-consumer compatibility and publication preparation belong to `DEL-05-01`. The entry and navigation belong to `DEL-01-01`. In shared files the split is this. In `AGENTS.md` this deliverable's parts are the passages OUT-001 names; the entry, the route to a scope and the rule that consumed indexes are regenerated from their sources are `DEL-01-01`'s, and the working cycle's reconciliation rule and the pointer to the reconciliation method are `DEL-04-01`'s. In `workflows/scope-of-work/` this deliverable's part is the method; the tool policy and the statements of what each tool does are `DEL-03-01`'s. The workflow index builder and the workflow metadata validator that create-workflow directs are tools and are not this deliverable's.
- **CLM-003** — Changes to commitments or acceptance criteria, explicit holds, risk acceptance, acceptance of a result, release, a protected baseline, reactivation of frozen App v3 or Runtime work, and any further archival removal belong to the owner. A consuming product's development, policy, data, adoption and release belong to that consumer. Interrupted custody is resolved by the authorised maintainer of the reserved operation. The frozen campaign brief `tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md` keeps its bytes unchanged, and a successor brief is made only with the owner's authorisation.

Outside the product: a workflow for every operation, a separate change
workflow or Git checklist, a case register, a routine receipt or recovery log,
a central inventory, and a lock service.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The guidance covers adding or revising a holding with its purpose, scope, destination, relevant existing material, source identity and checks; organising, relocating or retiring one with its actual references and consumers, its replacement or historical standing, its recovery and the authority to delete it; and review and integration with findings, proportionate scrutiny, the actual checked revision, updates to the owning text and the repository change procedure. It connects applicable methods and does not require one method per operation. Source: SOW-0004, SOW-0005, SOW-0008; PRD R04, R14.
- **REQ-002** — For diagnosis, reconciliation and connected-change assessment the guidance sends the maintainer to DEL-04-01's method, and for publication preparation and update inspection to DEL-05-01's route, so that all eight R04 operations can be reached. It adds no duplicate procedure and no assessment stage of its own. Source: PRD R04; decomposition card and §9; CLM-001, CLM-002.
- **REQ-003** — Where the guidance directs a command, the command exists and the guidance agrees with that tool's usage instructions on inputs, dependencies, outputs, write effects, failure behaviour and limits. It states an unavailable capability and the permitted fallback. It assumes no file-only query interface, namespace adapter, enforced lock, scheduling or external delivery. A reusable repair found while carrying a change is made in the material that owns the procedure. Source: SOW-0004, SOW-0010, SOW-0017; PRD R05, R06, R17.
- **REQ-004** — The guidance requires verification bound to the actual candidate and keeps content, executable behaviour and consumer-interface claims apart. A routine, reversible change is inspected or exercised. Ordinary implementation has a focused check. A change to numerical meaning, persistence, permissions or a destructive operation has focused regression checks and independent scrutiny by a separate agent. Applicable passing evidence is reused, missing evidence is reported as unverified, and neither a test count nor a merge stands for completion. An expected result is never changed merely to silence a failure. Source: SOW-0017; PRD R12.
- **REQ-005** — A change to the entry, a role, a method, a tool or an execution instruction is reviewed under the text that preceded it. Both the changed holding and the means used to change it are verified. The preceding text stays usable and recoverable until the replacement is verified and adopted by someone with authority to adopt it. Proposed text does not authorise itself and does not redefine the basis of its own review. Source: SOW-0010; PRD R06, A5.
- **REQ-006** — Recovery establishes the source basis, the usable result, the checks, the open conditions, the next needed action and the current authority from the owning locality and the actual review record. At most one replaceable recovery note is kept, and only where those sources are insufficient. A past record gives no authority to restart work and creates no standing backlog. Source: SOW-0018; PRD R12, A8.
- **REQ-007** — Custody names the holder, the affected item, the reserved operation, the existing mechanism in use, the release and recovery conditions and what the mechanism does not enforce. Readers keep the last checked-in material. Interrupted custody is resolved by the authorised maintainer of the reserved operation; elapsed time or silence gives no right to discard work. A mechanism is described as enforcing exclusion only after that enforcement has been exercised, and an operation that needs enforced exclusion is held until it has. Source: SOW-0021; PRD R14, A8.
- **REQ-008** — This deliverable shall perform no act owned by another deliverable: stating the reconciliation method or the diagnosis and connected-change assessment it carries (`DEL-04-01`, CLM-001); stating the method that questions goals and framing (`DEL-04-02`, CLM-001); implementing a tool or stating its usage instructions (`DEL-03-01`, CLM-002); settling the content of the shared-reference clarification (`DEL-02-02`, CLM-002); stating obtaining, version, update-inspection or publication guidance, or claiming compatibility with a named consumer (`DEL-05-01`, CLM-002); and stating the entry or navigation (`DEL-01-01`, CLM-002). Invoking another deliverable's method, relying on its evidence for a claim that is its own, and returning a concrete gap to it keep the boundary.
- **REQ-009** — The guidance sends each choice in CLM-003 to the party CLM-003 names and grants none of them. It directs no archival removal and no new tool or companion without the owner's specific decision. Its text and anything published with a case hold no credentials, private knowledge or consumer operational data. Source: PRD §2.3, §5, R17.

- **AC-001** — A maintainer starting from a bounded brief can find and follow guidance for each of the eight R04 operations. For the five this deliverable owns, the guidance states what REQ-001, REQ-004, REQ-005, REQ-006 and REQ-007 require. For the other three, it leads to the owning deliverable's method without restating it. Every command the guidance directs exists and is described as that tool's usage instructions describe it, and each unavailable capability has a stated fallback. Verify with VER-001.
- **AC-002** — For one actual authorised change to an instruction or a tool, the pull request and its sources show the preparation, the checks, the review and the integration at an identified checked revision, each using the guidance in OUT-001. Any reusable procedure the change needed is present in the Library material that owns it. A claim the record does not support is stated as unverified. Verify with VER-002.
- **AC-003** — For one revision of a maintenance instruction, the entry or a supporting tool, the review was made under the identified text that preceded it; both the resulting holding and the means used to change it were checked; the preceding text is recoverable; and the adoption names who adopted it and under what authority. Verify with VER-003.
- **AC-004** — In the selected change, the checks match the consequence class REQ-004 assigns it. Content, behaviour and interface claims each rest on evidence of their own kind. Where numerical meaning, persistence, permissions or a destructive operation changed, focused regression checks and scrutiny by a separate agent are present. No claim rests on a passing structural check or on the merge. Verify with VER-004.
- **AC-005** — Real retained work or a labelled recovery case is continued from its locality and review record alone. The continuation establishes the source basis, the usable result, the checks, the open conditions, the next action and the current authority. It revives no frozen work and no historical backlog, and it needs no routine receipt. Verify with VER-005.
- **AC-006** — Where custody applies, a real or labelled interrupted-custody case identifies the holder, item, reserved operation and mechanism. Release or recovery by the authorised maintainer is exercised. What the mechanism does not enforce is shown by observation. Readers' access to the checked-in material is unchanged throughout. Nothing is discarded because time passed. Verify with VER-006.
- **AC-007** — The guidance and the cases contain none of the acts REQ-008 excludes, make no named-compatibility or publication claim of their own, send every choice in CLM-003 to its owner, direct no removal or new tooling the owner has not decided, and pass the credential scan. Verify with VER-007.

## Production and Verification Method — Praxeology

Choices that define the product:

- Guidance lives where a maintainer already reads it. An operation gets a
  method of its own only where a gap is shown.
- Ordinary Git work is carried by the authorised brief and the conventions in
  `AGENTS.md`. There is no separate change workflow.
- The guidance invokes the reconciliation method and the consumer route. It
  does not copy them.
- A reusable workflow is created or revised through create-workflow.
- Custody uses a coordination or locking mechanism the repository or host
  already has, and states what that mechanism does not enforce. No lock service
  is built.
- Recovery reads the actual state of the work, its locality and its review
  record.
- A change already integrated counts as a maintenance case for the claims its
  record supports. A further case is selected only for a claim no record
  supports.

- **VER-001** — Judgment by a reader who did not write the guidance (follows the text from a bounded brief), with an executable check (invokes each command the guidance directs as the guidance gives it and observes that it runs, which does not show that the tool's results are correct): Walk the brief through all eight R04 operations: add or revise; organise, relocate or retire; diagnose and reconcile; assess connected change; review and integrate; prepare publication and inspect updates; recover or continue; change the maintenance means. At each, record whether the inputs, destination, method and limits can be taken from the text and whether a hand-off reaches the owning method. Report the walkthrough and the command observations as separate findings; the walkthrough alone shows no executable behaviour.
- **VER-002** — Judgment by a reviewer other than the change's implementation owner (reads the pull request, its diff and its checks): For the selected change, identify the changed holding, the preceding, reviewed and final revisions and the checks, and match each to the claim it supports. Read the reusable procedure at the home that owns it. Name any step the record does not show and any evidence that no longer applies.
- **VER-003** — Comparison with a named reference (the preceding text, recovered from Git) and judgment by a reviewer other than the reviser: Recover the preceding text. Confirm from the review record that the replacement was judged under it, that both the holding and the means were checked, and who adopted the replacement under what authority.
- **VER-004** — Judgment by a reviewer other than the change's implementation owner (reads the candidate's consequence class against its checks): Classify the change under REQ-004. Check that each content, behaviour and interface claim has evidence of its own kind bound to the candidate, and that scrutiny was separate where REQ-004 requires it. For reused evidence, check that it still applies. Where behaviour changed or is uncertain, run the focused check.
- **VER-005** — Comparison with a named reference (the source the work was recovered from, read from Git) and judgment by a reviewer other than the recoverer: Continue the retained work or labelled case using only its locality and review record. Compare the recovered result with its source. Record each item AC-005 lists and each step not performed, and say whether the case is real or labelled.
- **VER-006** — Executable check (observes whether a write by a process other than the holder's is prevented, and whether the checked-in material is unchanged before and after) and judgment by the authorised maintainer (decides release or recovery): Exercise the custody case, real or labelled as a safe simulation. Record the holder, item, operation and mechanism, the release or recovery, and the observed limit. Say which parts were simulated and which were live.
- **VER-007** — Judgment by a reviewer who did not write the guidance (reads it against REQ-008 and CLM-003, one excluded act and one reserved choice at a time), with an executable check (the credential scan, which observes only the patterns it holds): Read the guidance and the cases for content allocated elsewhere and for where each reserved choice is sent. Run `python3 tools/validation/validate_run_record_leaks.py --base <base> --head <head>` on the change and state what the scan does not cover.

## Governing Values and Decisions — Axiology

- **AX-001** — Reuse what is sound. Better is less text and fewer steps between a bounded brief and the guidance that applies to it, with no new method where an existing one carries the operation. That economy may never leave one of the eight operations without usable guidance or drop a consideration REQ-001 names.
- **AX-004** — Continuity. Better is less work lost or redone when an undertaking is interrupted, and less that a successor must reconstruct to continue. That may never be gained by discarding work because time passed, or by treating a past record as authority to restart.
- **AX-005** — Claims match their evidence. Better is fewer statements in a change record that claim more than the checks behind them examined. That may never be gained by lowering the verification REQ-004 requires for a consequence class, and a passing check never stands in for the owner's acceptance.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | OBJ-001, OBJ-002, OBJ-003, OBJ-004, OBJ-005 | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, CLM-001, CLM-002 | AC-001 | VER-001 | What the guidance must cover comes from PRD R04's table and R05, R06, R12 and R14. Whether the text delivers it is judged by a reader who did not write it. That a directed command runs as described is observed from the tool itself, which this deliverable did not write. |
| OUT-003 | OBJ-002, OBJ-004, OBJ-005 | REQ-006, REQ-007 | AC-001 | VER-001 | What the recovery and custody guidance must state comes from PRD R04's table and R12 and R14. Whether the text delivers it is judged by a reader who did not write it. |
| OUT-002 | OBJ-001, OBJ-002, OBJ-003, OBJ-004 | REQ-001, REQ-004 | AC-002 | VER-002 | What the case must show comes from PRD A2. The case is an actual pull request with its checked revision, read by someone other than its implementation owner. |
| OUT-002 | OBJ-001, OBJ-002, OBJ-003 | REQ-005, CLM-003 | AC-003 | VER-003 | What must hold comes from PRD R06 and A5. The preceding text is read from Git, which the revision did not write, and the review record is read by someone other than the reviser. |
| OUT-002 | OBJ-002, OBJ-003, OBJ-004 | REQ-003, REQ-004 | AC-004 | VER-004 | The consequence classes and what each requires come from PRD R12. The change's checks are compared with them by a reviewer who did not make the change. |
| OUT-003 | OBJ-002, OBJ-004, OBJ-005 | REQ-006 | AC-005 | VER-005 | What recovery must establish comes from PRD R12 and A8. The recovered result is compared with the source it came from, read from Git. |
| OUT-003 | OBJ-002, OBJ-005 | REQ-007, CLM-003 | AC-006 | VER-006 | What custody must state and show comes from PRD R14 and A8. The enforcement limit is observed from a write the holder did not make, and reader access from the checked-in bytes. |
| OUT-001 | OBJ-002, OBJ-003, OBJ-005 | REQ-002, REQ-008, REQ-009, CLM-001, CLM-002, CLM-003 | AC-007 | VER-007 | The sibling allocation comes from decomposition §9 and the reserved choices from PRD §2.3 and §5. The credential scan is the Library's own tool and covers only the patterns it holds. |
