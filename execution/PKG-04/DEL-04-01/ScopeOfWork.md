---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-01
package_id: PKG-04
decomposition_basis: execution/_Decomposition/PROJECT_DECOMP.md
project_scope_refs: [SOW-0006, SOW-0007, SOW-0012, SOW-0013, SOW-0014]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-003, OBJ-004]
---

# DEL-04-01 — Library reconciliation

## Purpose and Objective Traceability

A change to the Library leaves the affected holdings (the instructions, tools
and publications that describe the change), scopes, needs and pointers in
agreement with what was actually made, checked and integrated, or it names the
disagreement it could not settle and who decides it. This deliverable
contributes five things to that result: the reconciliation method a
contributor applies in the pull request that carries the change; the places in
the Library's instructions from which a contributor reaches that method; the
reconciliation carried out in actual changes; the Library's own deliverable
localities with their needs, which are what the method compares a result
against; and one actual authorised action that shows local progress under PRD
A3.

Its allocation is the DEL-04-01 card of the
[accepted decomposition](../../_Decomposition/PROJECT_DECOMP.md), with the
formation allocation in that document's §8.1 and the interfaces in §9. It
serves [PRD](../../../docs/PRD.md) objectives O1 to O4.

| Scope item | What this deliverable contributes | Objectives | PRD |
|---|---|---|---|
| SOW-0006 | Diagnosis of conflicting claims, source meaning and observed behaviour, naming the owning material, the evidence and the repair scope | OBJ-002, OBJ-003 (O2, O3) | R04 "Diagnose and reconcile", R11, A4 |
| SOW-0007 | Following the inputs, uses and consequences a change touches across instructions, tools, publications and execution, within the authorised undertaking | OBJ-002, OBJ-003 (O2, O3) | R04 "Assess connected change", R11 |
| SOW-0012 | The Library's own deliverable localities, each holding its scope and its needs and pointers | OBJ-001, OBJ-002, OBJ-004 (O1, O2, O4) | R08, §6.2–6.3, A3, A8 |
| SOW-0013 | Needs authored by each consumer after its scope exists | OBJ-004 (O4) | R09, A3 |
| SOW-0014 | Local action chosen from the goal, the evidence and actual input conditions; the route, the understanding and the understood neighbourhood revised when a finding warrants it; unaffected work continued; affected uses checked with one integration owner. This deliverable holds the action and source-reconciliation side; DEL-04-02 holds the examination of goals and framing | OBJ-002, OBJ-003, OBJ-004 (O2, O3, O4) | R10, A3 |

## Deliverable Definition — Ontology

**Reconciliation** is a bounded comparison of a concrete result and its
verification with the holdings, scopes, needs and pointers that result
affects, followed by the warranted edits, made in the pull request that
carries the change. It is the same pre-merge work, not a stage after it.

A **holding** is an instruction, tool or publication the Library maintains. A
holding, scope, need or pointer is **affected** when the change makes what it
says untrue, incomplete or newly relevant. Affected items are found from the
assignment and the diff, following only the sources needed to establish what
the commitment or interface means.

The comparison separates three findings. **Missing behaviour**: the commitment
stands and the work is unfinished. **Stale description**: the text is corrected
where intended behaviour and boundary are unchanged. **Missing evidence**: the
claim is reported as unverified.

A **locality** is `execution/PKG-nn/DEL-nn-nn/`: the deliverable's scope in
`ScopeOfWork.md` and its needs and code and check pointers in
`deliverable.yaml`. A **need** is declared by its consumer and states the
input, its intended use or condition, the case or trigger, and the source or
unresolved binding. A need is not a supplier commitment and not a
finish-to-start constraint on a whole deliverable.

The **implementation owner** carries reconciliation into its assignments and
through repairs. The **integration owner** checks the combined result before
merge.

- **OUT-001** — The reconciliation method, `workflows/bounded-reconciliation/WORKFLOW.md`, and its invocation points: the working cycle and the method pointer in `AGENTS.md`; the project-setup workflow with its current-project, package-activation and project-entry resources; and the step before integration in `workflows/coordinated-knowledge-work/WORKFLOW.md`. One method, reached from where a contributor already is; no parallel manual. Serves SOW-0006 and SOW-0007.
- **OUT-002** — In each change carried under the method, the warranted corrections to the affected holdings (the instructions, tools and publications that describe the change), scopes, needs and code and check pointers, made in the same pull request by the implementation owner, with any unresolved condition stated to its decision owner. A comparison that warrants no edit produces one sentence in the return or pull request and nothing else. Serves SOW-0006 and SOW-0007.
- **OUT-003** — The seven localities `execution/PKG-01/DEL-01-01/`, `execution/PKG-02/DEL-02-01/`, `execution/PKG-02/DEL-02-02/`, `execution/PKG-03/DEL-03-01/`, `execution/PKG-04/DEL-04-01/`, `execution/PKG-04/DEL-04-02/` and `execution/PKG-05/DEL-05-01/`, formed through the Library's own setup route. Each `ScopeOfWork.md` states the local goal, accepted scope and objective references, outputs, boundaries, acceptance criteria and verification; each `deliverable.yaml` carries the id, name, needs and code and check pointers. Serves SOW-0012.
- **OUT-004** — The needs declared in those localities, authored after their scopes. Serves SOW-0013.
- **OUT-005** — An actual authorised action on accepted and set-up scope that shows local progress as PRD A3 describes it: chosen from the local goal, the evidence and a real input or use condition; a finding that changed the route or the understanding; the neighbouring uses examined. This is the action side of A3. Serves SOW-0014.

The decomposition also allocates DEL-03-02, whose locality
`execution/PKG-03/DEL-03-02/` exists. Whether it belongs to OUT-003 and
OUT-004 is undecided.

Boundary:

- **CLM-002** — Each deliverable's contributor owns the content of its own locality through implementation and repairs. This deliverable owns that the set of localities exists, is formed by the Library's route and is checked together. It holds no second copy of any locality and has no authority to edit one centrally.
- **CLM-003** — Navigation belongs to DEL-01-01. The wider maintenance route, which invokes this method, and recovery and custody belong to DEL-02-01. The content of the shared-reference repair belongs to DEL-02-02. Scaffolding, validators, queries and their usage contracts belong to DEL-03-01. The accepted decomposition and the method that questions goals and framing belong to DEL-04-02. Obtaining, named compatibility and publication belong to DEL-05-01. In shared files this deliverable's part is the passage that tells a contributor to reconcile before integration: in `AGENTS.md`, the working cycle's reconciliation rule and the pointer to the method; in the project-setup files, their reconciliation steps; in coordinated-knowledge-work, the step before integration at which the combined result is checked.
- **CLM-004** — Changes to commitments or acceptance criteria, risk acceptance, explicit holds, protected baselines, acceptance and release belong to the owner. Adoption, policy and release of a consuming product belong to that consumer.

Outside the product: a global audit, a central graph or register of
relationships, a routine reconciliation report, an approval step after
ordinary repair, and any monitoring service or automatic loop.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The method compares the affected definitions and relationships, warranted claims, described actions and governing values with the actual result and the uses it touches. It separates missing behaviour, stale description and missing evidence, keeps the repair within the assignment, and exposes a consequential uncertainty instead of widening the commitment. Operating guidance and publications that describe a changed holding are reconciled with it, or name the earlier basis of the edition they retain. Source: PRD R04, R11, R12.
- **REQ-002** — Reconciliation is carried in the pull request doing the work, before integration. The implementation owner returns the changed locations, checks, findings and open decisions; the integration owner checks that result and declarations agree. A scope is edited only where the thing being made, or its description within the six parts, materially changed; a commitment the result has not met stays as written; unchanged declarations stay unchanged. Historical identities, scoped adopted contracts, accepted evidence and accepted snapshots keep their original meaning; a new result does not rewrite them. The pull request is the change record: no separate assessment stage, receipt or report. Source: PRD R08, R11, A4; decomposition card and §8.1.
- **REQ-003** — Each locality in OUT-003 is formed through project-setup, scope-of-work and dependency-extract with their tools. A scope is authored from the accepted decomposition and PRD; a scaffold or blank contract is not a scope. Source: SOW-0012; PRD R08, §6.2–6.3; decomposition §8.1.
- **REQ-004** — Needs are authored by the consumer after its scope exists, from that scope and its sources. Distinct conditions between the same endpoints, preliminary and final uses, reciprocal relationships and technical holds stay distinct. Suitability is judged from evidence; file presence, merge status and a structural pass do not establish it, and no supplier commitment is inferred from a need. Source: SOW-0013; PRD R09.
- **REQ-005** — The A3 contribution is an actual authorised action on accepted and set-up scope. A synthetic or labelled case, a discussion, or the formed structure alone does not count. Needs and the understood neighbourhood are revised when a finding warrants it; unaffected work continues while a condition is unresolved; one integration owner checks the related contributions. Source: SOW-0014; PRD R10, A3; decomposition §8.1.
- **REQ-006** — A claim about the method or an application of it is checked against the actual candidate, and missing evidence is reported as unverified. A revision of the method or of an invocation point is made through `workflows/create-workflow/WORKFLOW.md` and reviewed under the text that preceded it. That text stays recoverable until the replacement is verified and adopted; proposed text does not authorise itself. Source: PRD R06, R12, A5.
- **REQ-007** — The method and its invocation points contain nothing that CLM-003 allocates to another deliverable, and direct no edit of another contributor's locality outside the assignment.
- **REQ-008** — Neither the method nor an application of it changes a commitment, acceptance criterion, explicit hold, protected baseline or risk disposition, weakens one so that it appears satisfied, or declares or implies acceptance, adoption or release. Such a choice goes to its owner as a concrete choice with its consequence, and unaffected work continues. Source: CLM-004; decomposition card; PRD R10, §5.
- **REQ-009** — The method text, the changes an application makes and anything published with them hold no credentials, private consumer data or machine-specific private information. Source: PRD R17.

- **AC-001** — A contributor holding an assignment and a diff, starting from any invocation point in OUT-001, reaches the method and from its text can: identify the affected deliverables and holdings; compare their scopes, needs, pointers and descriptions with the result and its verification; tell missing behaviour from stale description from missing evidence; make the warranted edits in the same pull request; and bring a changed commitment or unresolved intent to its owner. Nothing on the route adds a stage, approval or record after ordinary repair. Verify with VER-001.
- **AC-002** — In an actual change carried under the method, the pull request identifies its candidate and checks. Each affected holding, scope, need and code and check pointer agrees with the integrated result or states an unresolved condition and who decides it; guidance or a publication that describes the changed holding agrees with it or names its earlier basis. Commitments, criteria and holds are unchanged unless their owner decided otherwise, and no commitment is weakened to appear satisfied. Unchanged declarations are untouched, and historical identities and accepted evidence are unaltered. The change passes the credential scan and implies no acceptance, adoption or release. A no-edit conclusion gives its reason. Verify with VER-002.
- **AC-003** — Each of the seven localities in OUT-003 exists. Each scope passes the scope validator and the authored-locality check and, read against its decomposition card, states the goal, scope and objective references, outputs, boundaries, acceptance criteria and verification the card allocates. Each `deliverable.yaml` carries its id, name, needs, `code_paths` that name the code that is that deliverable's own, with any path shared with another deliverable split or reported, and check pointers that resolve. Verify with VER-003.
- **AC-004** — Each need declared in those localities states its input, use condition, trigger and source or unresolved binding in its provider's terms; distinct uses between the same endpoints are separate entries; no need makes a whole deliverable's completion its condition; the deliverables check reports no error. Verify with VER-004.
- **AC-005** — One actual authorised change on accepted and set-up scope shows, in its pull request and changed sources: the local goal traced to product objectives; the action chosen from evidence and a stated input or use condition; a finding that changed the route or understanding; the neighbouring uses that were examined; and what stayed held while other work continued. Verify with VER-005.
- **AC-006** — The method and its invocation points send every changed commitment, criterion, hold or risk choice to its owner, contain nothing allocated to a sibling deliverable, and pass the credential scan. Verify with VER-006.

## Production and Verification Method — Praxeology

Choices that define the product:

- Reconciliation is done by the implementation owner in the implementation
  pull request. It is not handed to a later reviewer or a separate stage.
- Its extent is set by the assignment and the diff. It is not a corpus audit.
- A decision edits the text it governs, and the pull request records the
  change. Nothing is appended to a register.
- Localities are formed by the Library's own route, in order: project-setup,
  then scope-of-work for the contract, then dependency-extract for needs.
  Scope precedes needs.
- A question about whether the goal or framing still serves goes to the human
  and Agent 0 through DEL-04-02's reflective method. Reconciliation works
  under the commitments as they stand.

- **VER-001** — A reader who did not write the method starts from each invocation point with a bounded assignment and diff, follows the route, and records whether each step in AC-001 can be taken from the text. Read the route for any added stage, approval or record. For a revision, compare with the preceding text and confirm create-workflow was followed.
- **VER-002** — Judgment by the integration owner, who did not make the edits (reads the pull request, its diff and its checks against the affected text), with an executable check (the credential scan, which observes only the patterns it holds): For the selected change, list the scopes, needs and pointers the diff affects, using `python3 -m tools.deliverables --project . touches <ref>` and `impact <DEL-ID>` where they run, and the instructions, tools and publications that describe what changed, and compare each with the integrated result. Confirm that commitments, criteria and holds are unchanged unless their owner decided otherwise and none was weakened to match the result, that historical identities and accepted evidence are unaltered, that nothing in the pull request implies acceptance, adoption or release, and that source inspection, observed behaviour and unverified claims are told apart. Run `python3 tools/validation/validate_run_record_leaks.py --base <base> --head <head>` on the change and state what the scan does not cover.
- **VER-003** — Executable checks (the locality check and the scope validator, which observe structure and format only) and judgment by the integration owner (reads each scope against its decomposition card and each pointer against the code): For each locality in OUT-003 run `zsh tools/validation/check_min_viable_fileset.sh --current <locality> <DEL-ID>` and `python3 tools/scope_of_work/validate_scope_of_work.py <locality>/ScopeOfWork.md`. Then read each scope against its decomposition card for the content AC-003 names; read each `code_paths` entry against the code for whether it names that deliverable's own code, and for any path another locality also lists whether a scope states the split; and confirm each check pointer resolves. The structural pass and the content reading are separate findings.
- **VER-004** — Run `python3 -m tools.deliverables --project . check` and a `neighborhood <DEL-ID>` query for each locality. Read each need against its consumer's scope and against the provider's scope: which criterion there makes the condition true. State the Git, HEAD and PyYAML basis and what the query did not cover.
- **VER-005** — Read the selected case end to end in its pull request and changed sources: goal and objective, condition, the evidence that selected the action, the finding, the changed route or understanding, the affected uses, what was held. The reading is done by someone other than the case's implementation owner. A labelled or synthetic case is rejected.
- **VER-006** — Read the method and each invocation point for where a reserved choice is sent and for content CLM-003 allocates elsewhere. Run `python3 tools/validation/validate_run_record_leaks.py --base <base> --head <head>` on the change and state what the scan does not cover.

## Governing Values and Decisions — Axiology

- **AX-001** — Agreement serves the intended result. Better is fewer scope statements and needs found stale or contradicted by integrated work the next time they are read. That count may never be improved by weakening a commitment or criterion so that it matches what was built.
- **AX-002** — Reuse what is sound. Better is less reading and editing per change beyond what the change affects, and no new file where an existing one already carries the meaning. That economy may never leave an affected use unexamined or a known disagreement unstated.
- **AX-004** — Authority is specific to the claim. Better is fewer statements in a reconciliation return that claim more than the check behind them examined. That may never be gained by leaving a disagreement unstated, and a passing check never stands in for the owner's acceptance.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | OBJ-002, OBJ-003 | REQ-001, REQ-002, REQ-006 | AC-001 | VER-001 | What the route must cover comes from PRD R04's "Diagnose and reconcile" and "Assess connected change" rows and R11, an owner ruling. Whether the text delivers it is judged by a reader who did not write it. |
| OUT-002 | OBJ-002, OBJ-003 | REQ-001, REQ-002, REQ-008, REQ-009, CLM-002, CLM-004 | AC-002 | VER-002 | What must not change comes from the commitments as accepted, and what must stay unaltered from PRD R11 and A4, owner rulings. What the descriptions must match comes from the change's own candidate and checks. Agreement is judged by the integration owner, who did not make the edits. The credential scan is the Library's own tool and covers only the patterns it holds. |
| OUT-003 | OBJ-001, OBJ-002, OBJ-004 | REQ-003, CLM-002 | AC-003 | VER-003 | What a locality must contain comes from PRD R08 and each deliverable's decomposition card, owner rulings. Whether a `code_paths` entry names a deliverable's own code is read against the code and the neighbouring scopes. The validator and locality check are the Library's own tools: a pass shows conformance to the format they encode and guards against change. |
| OUT-004 | OBJ-004 | REQ-004, CLM-002 | AC-004 | VER-004 | The form of a need comes from PRD R09, an owner ruling. Whether a condition holds is read from the provider's scope. The deliverables check is the Library's own tool and shows only that declarations are well formed. |
| OUT-005 | OBJ-002, OBJ-003, OBJ-004 | REQ-005 | AC-005 | VER-005 | What the case must show comes from PRD A3, an owner ruling. The case is an actual pull request, read by someone other than its implementation owner. |
| OUT-001 | OBJ-002, OBJ-003 | REQ-007, REQ-008, REQ-009, CLM-003, CLM-004 | AC-006 | VER-006 | Reserved choices come from PRD §5 and R10 and the sibling allocation from decomposition §9, owner rulings. The credential scan is the Library's own tool and covers only the patterns it holds. |
