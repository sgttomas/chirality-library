---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-01
package_id: PKG-04
decomposition_basis: execution/_Decomposition/checkpoint_snapshots/GROUP3-20261101T011431Z/PROJECT_DECOMP.md@fd847ac9ac68250b2f35d2e9c0087c16e86b510a
project_scope_refs: [SOW-0006, SOW-0007, SOW-0012, SOW-0013, SOW-0014]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-003, OBJ-004]
---

# DEL-04-01 — Library reconciliation

## Purpose and Objective Traceability

Make the affected holdings, actual result, evidence and local declarations agree
before integration, or expose a consequential unresolved condition to its actual
decision owner. This contribution supplies the reconciliation procedure and its
bounded applications, including the actual initial setup and local needs required
by the accepted decomposition. It does not centralize other contributors' work.

The governing basis is `docs/PRD.md` (accepted 2026-10-31), the accepted snapshot
named above, and its `DECISION.md` and `ACCEPTED_MANIFEST.csv`, reached through
`execution/_Decomposition/_LATEST_ACCEPTED.md`. The snapshot's submitted labels
are historical: the decision records final acceptance and setup authority.
Snapshot-relative references resolve from the original
`execution/_Decomposition/PROJECT_DECOMP.md`. The PRD SHA-256 is
`95c3c25ee36d4d4ddadf54d266a47a2ee58c6b37fbbdef75ad20a97986a718ca`;
the accepted decomposition payload SHA-256 is
`313bdb78d1a000d8a903aa12197603ac45bcb7a601df1ee12447eaaf29031261`.

| Accepted scope | Local contribution | Objectives and source warrant |
|---|---|---|
| SOW-0006 | Diagnose conflicting claims, source meaning and observed behavior; identify owning material, evidence and bounded repair | OBJ-002, OBJ-003; PRD R04, R11, A4 |
| SOW-0007 | Follow relevant inputs, uses and consequences across affected instructions, tools, publications and execution | OBJ-002, OBJ-003; PRD R04, R11, §2.2 |
| SOW-0012 | Materialize selected accepted localities with real contracts, Work and useful metadata pointers | OBJ-001, OBJ-002, OBJ-004; PRD R08, §6.2–6.3, A3, A8 |
| SOW-0013 | Author actual consumer-local input/use conditions after scope exists | OBJ-004; PRD R09, §6.1–6.2, A3 |
| SOW-0014 | Demonstrate authorized local action, evidence-directed revision of the route and examination of affected uses | OBJ-002, OBJ-003, OBJ-004; PRD R10, A3 |

OBJ-001 concerns locating the applicable basis and work; OBJ-002 concerns usable
maintenance means; OBJ-003 concerns coherence with warranted meaning and values;
OBJ-004 concerns meaningful local progress within the wider product. The accepted
vocabulary and objective statements remain in decomposition §§2–3. The local
allocation follows its ledger, DEL-04-01 card, §8.1 and §9.

**Maturity:** integrated setup and owner-approved case assessment; broader
product fulfillment remains unestablished. The
formation undertaking is authorized; this authoring assignment does not authorize
product implementation, acceptance or release. Existing maintained guidance and
checked evidence may satisfy parts or all of an output where the claim matches.
Structural preparation, empty Work and an empty needs list do not establish the
formation outputs or suitability. No lifecycle state is introduced.

The initial source assessment and continuation conditions are in [Work/FormationAndReconciliation.md](Work/FormationAndReconciliation.md). Consumer-local needs are now declared in `deliverable.yaml`; their presence establishes no satisfaction claim.

## Deliverable Definition — Ontology

A reconciliation application is a bounded comparison and warranted correction
within the implementation PR. A locality is the owning contract, consumer needs
and working material, not a new central record. A need is an input plus its
intended use/condition, case or trigger, and source or unresolved binding. Evidence
establishes a particular claim at a stated basis; an inferred relationship is not
a supplier commitment. Instructions and explanatory material are the principal
output forms here; executable tools remain maintained at their existing homes.

- **OUT-001** — Applicable maintained reconciliation instructions and connected invocation points, serving SOW-0006 and SOW-0007 / OBJ-002 and OBJ-003. The principal home is `workflows/bounded-reconciliation/WORKFLOW.md`; existing invocation points are `AGENTS.md`, `workflows/project-setup/resources/current-project.md`, `workflows/project-setup/resources/package-activation.md` and `workflows/coordinated-knowledge-work/WORKFLOW.md`. Reuse the implemented practice; edit only a demonstrated gap, under the selected maintenance authority. A parallel manual is not required.
- **OUT-002** — A selected actual maintenance application's warranted source corrections and evidence, serving SOW-0006 and SOW-0007 / OBJ-002 and OBJ-003. Corrections stay in the affected holdings and local ScopeOfWork, Work and needs/pointers, alongside the actual implementation change. Consequential reasoning stays in the owning Work; the PR identifies the candidate, checks and unresolved conditions. A no-edit result needs only a brief return or PR statement. Existing checked applications can supply evidence within their demonstrated limits.
- **OUT-003** — The initial selected accepted localities with substantive ScopeOfWork contracts, Work content of explicit maturity and useful source/code/check pointers in deliverable.yaml, serving SOW-0012 / OBJ-001, OBJ-002 and OBJ-004. The actual homes are `execution/PKG-01/DEL-01-01/`, `execution/PKG-02/DEL-02-01/`, `execution/PKG-02/DEL-02-02/`, `execution/PKG-03/DEL-03-01/`, `execution/PKG-04/DEL-04-01/`, `execution/PKG-04/DEL-04-02/` and `execution/PKG-05/DEL-05-01/`. Each contributor retains its local contract, reasoning, evidence, alternatives, consequential attempts, unresolved conditions and local outputs as applicable to actual work. Maintained code, publications and reusable instructions retain their source homes, referenced locally. This formation obligation is not satisfied by reusable setup instructions alone.
- **OUT-004** — Actual consumer-local needs and conditions in the selected localities' `deliverable.yaml`, authored after their scopes, serving SOW-0013 / OBJ-004. Each need preserves input identity, intended use/condition, relevant case/trigger, source or unresolved binding, and applicable technical holds. Distinct uses between the same endpoints, preliminary/final use and reciprocal relationships remain distinct. No duplicate dependency register is produced.
- **OUT-005** — Evidence of an actual authorized local action on accepted and set-up scope, serving SOW-0014 / OBJ-002, OBJ-003 and OBJ-004. The owning locality and actual review retain the goal, evidence and input/use condition that selected the action, the finding that changed its route or understanding, and examination of affected neighboring uses. This is the local action/source-reconciliation contribution to PRD A3; DEL-04-02 contributes examination of goals and framing. The same actual case may serve multiple criteria without a second report.

- **CLM-001** — Decomposition §6.1 records PR #1779 as an implemented current setup/reconciliation repair and reusable evidence, at checked head `a0bb0dc77a53b041262571f658f9fd9590d44269` and equal-tree merge `a052783460f60c76e6fa229500f59a51f67c5265`. This is the accepted source's evidence account, not tests rerun during scope authoring. It supports the repaired means; it does not establish live formation, need suitability, complete maintenance coverage, named compatibility or product acceptance.
- **CLM-002** — Decomposition §8.1 and §9 assign actual contracts, Work, needs and repairs to the contributor responsible for each local goal. Implementation owners carry same-PR reconciliation through repairs; Agent 0 checks the combined result before integration. The local goal owns its sources; DEL-04-01 accounts for formation coverage and the practice, not a second copy or central edit authority.
- **CLM-003** — Decomposition cards and §9 assign navigation to `DEL-01-01`, the broader maintenance route and recovery/custody case to `DEL-02-01`, the specific shared-reference/publication clarification and F-02 repair to `DEL-02-02`, executable maintenance tools and direct usage contracts to `DEL-03-01`, accepted decomposition formation and reflective guidance on goals/framing to `DEL-04-02`, and obtaining/use, named compatibility and publication/update-inspection applications to `DEL-05-01`. These are bounded contributions; source-file relevance is not exclusive ownership of every edit to a shared file.
- **CLM-004** — Root `AGENTS.md`, PRD §§2.3, 3–5 and the Group 3 decision reserve changed commitments and acceptance criteria, risk acceptance, protected-baseline changes and releases to their actual owner. Product acceptance and Root release are owner acts; consumer adoption, product operation, local policy and release belong to each independent consumer. App v3 and Runtime remain frozen absent explicit reactivation. Additional archival disposition, including `plans/` and `_DomainEngines/`, requires the owner's specific direction; the owning project's authority governs domain changes.

Input and use conditions for later consumer-local binding:

| Trigger/use | Required input and source | Condition and current limit |
|---|---|---|
| Initial formation | Final accepted decomposition, manifest and owner setup decision at the bound snapshot | Acceptance and setup authority are established; author actual scopes before needs. Agent 0 integrates the selected seven localities. This author edits only this contract. |
| Reuse or exercise formation means | Maintained project-setup/current-project, preparation, scope-of-work, dependency-extract and registered tools; decomposition §6.1 evidence | Assess the selected command and source revision against the actual use. Reuse the current route; no outstanding F-01 build prerequisite is assumed. |
| Concrete holding change | Authorized brief, actual candidate/diff and checks, affected ScopeOfWork/Work/needs and relevant consumer sources at real revisions | Bind the bounded case and revision in its execution brief; distinguish a source's availability from suitability. Unknown dependent conditions remain held; unaffected work continues. |
| A3 action and affected-use examination | Accepted/set-up local goal, actual need/use condition, action evidence, finding and affected-use sources | Formation structure or a synthetic fixture alone is insufficient. Bind the actual case and warranted source evidence when selected. |
| Changed goal, framing or burden | Current purpose, local experience and consequential reconciliation findings | Human–Agent 0 dialogue, supported by DEL-04-02, decides whether to retain the route or return a reserved choice; no extra assessment gate. |
| Named compatibility or publication consequence | DEL-05-01's maintained consumer contract/fixtures and revision, or actual candidate/version and prior basis | Q-04 and Q-05 remain claim-specific unknowns. Do not infer qualification, adoption or publication from guidance or merge status. |

## Completion and Reliance Basis — Epistemology

The criteria below express accepted commitments, not results already achieved.
Tool passes establish the checked structure or behavior; they do not confer
human acceptance. Evidence may be reused only for its actual source basis and
claim. Each criterion names its verification method explicitly.

- **REQ-001** — Reconciliation shall compare affected definitions/relationships, warranted claims/evidence, described actions and governing values with the actual result and relevant uses. It shall distinguish missing behavior, stale description and missing evidence, bound repair scope, and expose consequential uncertainty without silently expanding commitments. Source: PRD R04, R11–R12; SOW-0006 and SOW-0007.
- **REQ-002** — The implementation owner shall carry reconciliation in the implementation PR before integration, retain responsibility through repairs and return affected locations, evidence and unresolved conditions for Agent 0's integration check. Correct changed current meaning, connect genuinely new work from the next contributor's reading path and preserve unchanged declarations and historical evidence. No separate assessment stage or routine receipt is required. Sources: CLM-002; decomposition DEL-04-01 card and §8.1; `AGENTS.md` working cycle.
- **REQ-003** — Initial setup shall produce the actual selected accepted localities in OUT-003 using the current route, with substantive contracts, applicable Work content and useful metadata pointers. Scope/objective links, goal, outputs, boundaries, acceptance and verification shall remain grounded in the accepted source. Work shall state maturity, limitations and unresolved conditions and preserve what is needed to use or recover actual work. Empty folders and blank declarations are not fulfillment. Sources: SOW-0012; PRD R08; decomposition §8.1.
- **REQ-004** — After scope exists, each consumer shall author its actual needs under OUT-004 from that scope, relevant work and sources. Assess suitability for the stated use from evidence; preserve distinct conditions, preliminary/final uses, reciprocal relations, technical holds and unresolved bindings. File presence, merge status and structural checks shall not be treated as suitability, supplier appointments or whole-deliverable finish-to-start constraints. Sources: SOW-0013; PRD R09; decomposition §8.1.
- **REQ-005** — The A3 contribution shall use an actual authorized action on accepted/set-up scope, selected from the goal, evidence and a meaningful input/use condition; show a finding that revises route or understanding and examine affected neighboring uses. Revise the local neighborhood as knowledge changes, continue unaffected work and retain one integration owner for combined contributions. Sources: SOW-0014; PRD R10, A3; decomposition §8.1 and §9.
- **REQ-006** — Verification shall establish the claim actually made against the actual candidate and selected basis, with focused checks and independent scrutiny for numerical meaning, persistence, permissions or destructive operations. Proposed replacement instructions shall not authorize themselves; evaluate instruction revisions under the preceding basis. Preserve historical qualifications and report missing evidence as unverified. Sources: PRD R06, R11–R12, A4–A5; CLM-001.
- **REQ-007** — This deliverable shall perform no act owned by another deliverable: navigation design by `DEL-01-01`; broader maintenance-operation coverage and custody/recovery demonstration by `DEL-02-01`; specific F-02 shared-reference/publication content repair by `DEL-02-02`; executable-tool implementation and direct usage contracts by `DEL-03-01`; accepted decomposition formation and guidance examining changed goals/framing by `DEL-04-02`; and obtaining/use, named compatibility, publication-candidate and update-inspection applications by `DEL-05-01`, as assigned in CLM-003. This exclusion preserves those owners while allowing their authorized implementation owners to apply reconciliation and share applicable evidence. OUT-003 and OUT-004 retain local ownership under CLM-002.
- **REQ-008** — Reconciliation shall not change commitments, acceptance criteria, protected baselines, explicit holds or risk disposition without the actual owner's decision, nor declare product acceptance or release for the owner. It shall not adopt material, change policy, operate or release a consumer product for that consumer. It shall not reactivate frozen work or dispose of additional archival/domain material without the authority identified in CLM-004. Global audit services, central graphs, mandatory companions, automatic model loops and central management of local Work are outside the accepted undertaking, not unassigned deliverables to implement. Sources: CLM-002, CLM-004; PRD §2.3, R17; decomposition §7–§10.
- **REQ-009** — Public contract, guidance and retained evidence shall preserve source identity and exclude credentials, private consumer data and machine-specific private information. Use maintained credential/private-term checks with their available inputs, reporting the actual screening limit. Public summaries or fixtures cannot substitute for an unavailable named consumer contract. Sources: PRD R13, R17; Q-04 and CLM-004.

- **AC-001** — The maintained reconciliation route and its invocation points let a bounded contributor identify affected owning material, compare meaning, evidence, method and values, distinguish missing behavior from stale description or missing evidence, make authorized same-PR corrections and return reserved choices to the actual owner without a new assessment gate. Verify with VER-001.
- **AC-002** — A selected actual maintenance change identifies its authorized scope, candidate/revision and evidence; compares affected declarations and relevant uses before integration; and leaves warranted corrections or explicit unresolved conditions in owning sources, with history and unchanged declarations preserved. A no-edit conclusion has an evidence-grounded explanation in the return or PR. Verify with VER-002.
- **AC-003** — The seven selected accepted localities in OUT-003 contain substantive source-grounded contracts, Work content sufficient for their actual current work and recovery with maturity/limitations explicit, and useful source/code/check pointers in metadata. Current authored-locality and substantive contract checks pass, and human content review finds the required formation meaning present. Setup instructions, empty Work or structure-only evidence do not satisfy this criterion. Verify with VER-003.
- **AC-004** — Actual consumer-local needs are authored after scope and preserve input, intended use/condition, trigger/case, source or unresolved binding, distinct preliminary/final and reciprocal uses and technical holds where applicable. Bounded structural/query checks and source review support the declarations without inferring suitability, supplier commitments or finish-to-start constraints from presence or merge status. Verify with VER-004.
- **AC-005** — An actual authorized action on accepted/set-up scope is traced to a local goal and product objectives, evidence and an actual input/use condition; a finding changes the route or understanding; affected neighboring uses are examined and unresolved dependent conditions are distinguished from work that can continue. A synthetic case or the accepted structure alone is insufficient. Verify with VER-005.
- **AC-006** — The bounded application and its retained evidence respect the specific local, sibling, human and consumer authority boundaries, preserve protected and historical bases, and state unverified claims and Q-01/Q-02/Q-04/Q-05 limits where applicable. Required credential/private-term screening is clean for its stated inputs, and evidence does not imply product acceptance, consumer adoption or owner release. Verify with VER-006.

## Production and Verification Method — Praxeology

For an authorized implementation undertaking, begin from its goal, actual diff,
affected sources and input conditions. Read only the relevant holdings and uses.
Reuse `workflows/bounded-reconciliation/WORKFLOW.md` and the current invocation
points. Repair a demonstrated procedural gap at its maintained home using the
applicable authoring/change method; creating or revising a reusable workflow uses
`workflows/create-workflow/WORKFLOW.md`. Keep its preceding basis available.

Formation uses current project-setup, preparation, scope-of-work INIT and then
dependency-extract. The preparation helpers use the explicit current route;
ScopeOfWork and needs are authored, not inferred from scaffolding. Each local
owner retains its contract, Work and needs. Agent 0 checks their combined result
against §8.1 before integration, including the actual Work content and unresolved
bindings. This contract accounts for that coverage without granting its author
writes across localities or making sibling completion a blanket prerequisite.

For a concrete change, compare the actual result and checks with affected
ScopeOfWork, Work and needs. Correct ordinary descriptions within authority;
retain unsatisfied requirements when behavior falls short. Add an artifact only
for a real subject, link it locally and retain consequential reasoning. Apply
already-authorized decisions; return a genuine substantive ambiguity as CONFLICT
with its consequence, continuing unaffected work. Human–Agent 0 reflection about
the goal or framing uses DEL-04-02's contribution. Evidence and review remain in
the owning work and actual PR; no routine reconciliation report is required.

- **VER-001** — Inspect the maintained route and invocation points against the accepted card, REQ-001 and REQ-002, and trace their use in a bounded application. Check scope, inputs, prescribed comparison, outputs, authority and absence of a duplicate gate. Reuse CLM-001 for matching implemented guidance; verify any revision under its preceding basis and applicable workflow/package checks. Retain only claim-relevant source references and findings.
- **VER-002** — Inspect the actual case's authorized brief, candidate/diff, verification and affected ScopeOfWork/Work/needs plus relevant uses at their identified revisions. Compare before/after meaning, warrant, actions and values. Confirm warranted changes in the same implementation PR, unresolved conditions in owning sources, unchanged/historical material preserved, and no-edit explanations where applicable. Distinguish source inspection, observed behavior and unverified claims; reuse matching evidence rather than rerun unrelated checks.
- **VER-003** — Inspect each selected locality against its accepted card and §8.1 for real goal/scope/output/boundary/evaluation content, useful metadata pointers and recoverable Work with maturity, evidence and open conditions. Run `zsh tools/validation/check_min_viable_fileset.sh --current <locality> <DEL-ID>` without the preparation-only flag and `python3 tools/scope_of_work/validate_scope_of_work.py <locality>/ScopeOfWork.md --json`; use the deterministic checklist and boundary-owner QA for authored contracts. Review substantive content separately from structure. Record gaps in the actual review; do not create routine receipts or count an empty Work directory as content.
- **VER-004** — Review actual consumer declarations against scope, work and cited input sources, assessing the condition for the actual intended use. Run `python3 -m tools.deliverables --project . check` and a bounded `neighborhood <DEL-ID>` or `impact <DEL-ID>` query relevant to the selected case. Check distinct conditions, cases, source identity, unresolved bindings and holds against evidence. State Git/HEAD/PyYAML and coverage limits; a structural or query pass proves no suitability or acceptance.
- **VER-005** — Examine the actual A3 case in its owning locality/review: trace accepted goal and objective, meaningful condition, evidence used to choose the authorized action, observed finding, changed route/understanding and affected-use examination. Confirm what remained held and what could proceed, and check the combined consequence with the integration owner. Distinguish this local action evidence from DEL-04-02's human judgment about goals/framing. Do not replace the actual case with a synthetic fixture.
- **VER-006** — Review the selected application against REQ-006 through REQ-009 and CLM-002 through CLM-004, enumerating excluded acts and their actual owners. Check candidate-bound proportionate verification and independent scrutiny where required, preserved historical/protected bases, source/claim limits and unresolved Q qualifications. Use the maintained credential scanner `tools/validation/validate_run_record_leaks.py` and private-term scanner `tools/validation/validate_private_terms.py` (or their maintained APIs for uncommitted files) on public changes and retained evidence. Keep terms and credentials out of diagnostics; disclose local-versus-hosted screening limits. Human acceptance remains separate.

## Governing Values and Decisions — Axiology

- **AX-001** — Useful coherence serves the intended result, not a report stream or local completion claim. Bound inquiry by the authorized undertaking; follow consequential uses without silently committing to repair everything connected. PRD R10–R11 and decomposition §9 supply this value.
- **AX-002** — Reuse sound holdings and applicable checked evidence. A new file is not intrinsically a better output; unchanged declarations stay unchanged. Current meaning is corrected where owned, while history keeps its original standing. CLM-001 and CLM-002 govern this economy and continuity.
- **AX-003** — The owner's Group 3 words, “I accept this decomposition as the basis for project setup,” authorize formation under Agent 0's direct management and bounded Type 2 scope authoring. They do not constitute product acceptance or appoint permanent production staff/suppliers. Agent 0 retains integration and dependency-authoring arrangements; each local contributor retains its own work. Q-03 future production assignments remain unappointed by this authoring act.
- **AX-004** — Authority and reliance are claim-specific. Commitments, acceptance criteria, protected baselines, explicit holds, risk, adoption and release retain the owners in CLM-004. Proposed methods cannot approve themselves; tests implement verification and cannot redefine acceptance.

- **TBD-001** — The selected actual F-02 application is now bound in the linked Work and native need, including source revisions, the current-validator counterexample, repair and affected uses. DEL-04-02 additionally examines the actual owner feedback and changed undertaking boundary. Agent 0’s assessment was approved for integration in PR #1785; other cases and broader fulfillment remain unestablished.
- **TBD-002** — Initial consumer-local bindings for the seven accepted localities are authored after scope under Agent 0's arrangement. Their presence supplies no input completeness or suitability claim. For this deliverable, bind the formation authority, selected maintained means, affected candidate/local declarations and actual use-case evidence only for their intended conditions; do not invent supplier promises or edges from shared objective labels.
- **TBD-003** — Q-01 retains further archival disposition for the owner; Q-02 retains additional bespoke tooling as contingent on a demonstrated selected need and actual authority. Neither creates an unperformed removal or build prerequisite for current reconciliation. Do not modify `plans/`, `_DomainEngines/` or unselected frozen material under this setup contract.
- **TBD-004** — Q-04's named maintained consumer contract/fixtures and exact revision, and Q-05's actual verified publication candidate/version and prior comparison basis, remain unresolved under DEL-05-01. They are required before affected named compatibility or publication-inspection claims, respectively; independent reconciliation and setup can continue. No consumer contact, rollout or owner release is commissioned here.

No substantive source conflict is identified in this initial contract. Unknown
bindings above remain unknown. The formation outputs and future evaluations are
commitments to establish, not accomplished facts; overall acceptance remains
with the owner.

## Output and Evaluation Matrix

Each row carries one criterion and exactly its stated verification method.
Evidence expectations describe what will warrant evaluation; this matrix records
no acceptance verdict.

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | OBJ-002, OBJ-003 | REQ-001, REQ-002, REQ-006, CLM-001 | AC-001 | VER-001 | Maintained route/invocation basis and bounded-use review; matching prior evidence or checked authorized corrections |
| OUT-002 | OBJ-002, OBJ-003 | REQ-001, REQ-002, REQ-006, CLM-002 | AC-002 | VER-002 | Actual candidate/diff, meaningful checks, affected-use comparison and owning corrections or explicit unresolved/no-edit result in the implementation PR |
| OUT-003 | OBJ-001, OBJ-002, OBJ-004 | REQ-003, CLM-002 | AC-003 | VER-003 | Seven actual localities with substantive contracts, useful metadata and Work content; authored structural/schema checks plus separate content/recovery review |
| OUT-004 | OBJ-004 | REQ-004, CLM-002 | AC-004 | VER-004 | Actual consumer-local declarations, source/use-condition review and bounded query/check evidence with limitations |
| OUT-005 | OBJ-002, OBJ-003, OBJ-004 | REQ-005, CLM-002 | AC-005 | VER-005 | Actual accepted/set-up A3 case linking goal, condition, action, finding, changed route and affected uses |
| OUT-002 | OBJ-002, OBJ-003 | REQ-006, REQ-007, REQ-008, REQ-009, CLM-002, CLM-003, CLM-004 | AC-006 | VER-006 | Claim-specific authority/boundary review, proportionate candidate checks, public screening and explicit unresolved limits; no inferred acceptance or release |
