---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-01
package_id: PKG-03
decomposition_basis: execution/_Decomposition/checkpoint_snapshots/GROUP3-20261101T011431Z/PROJECT_DECOMP.md@fd847ac9ac68250b2f35d2e9c0087c16e86b510a
project_scope_refs: [SOW-0009, SOW-0015, SOW-0024]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-004, OBJ-005]
---

# Support current localities with actual reusable tools

## Purpose and Objective Traceability

DEL-03-01_maintenance-toolkit is PKG-03's executable maintenance utility set
with its direct usage contract. Existing repeatable setup, validation and query
operations must support adopted Root localities and meaningful local conditions.
A maintainer needs commands whose inputs, dependencies, effects, failures and
limits are accurate, so authorized work can proceed from evidence.

This is a newly authored setup contract, not a declaration of fulfillment. The
assignment authorizes this contract and its checks, not product implementation,
acceptance or release. Existing checked holdings can supply part or all of an
output; an output does not require a new file. Production contributor assignment
remains open and this authoring assignment is not permanent staffing.

All paths below are repository-relative unless explicitly described otherwise.
The accepted basis is the frontmatter snapshot, resolved through
`execution/_Decomposition/_LATEST_ACCEPTED.md`. Its `DECISION.md` and
`HANDOFF_STATE.md` establish acceptance and setup authority; the payload's
submitted status is historical. `ACCEPTED_MANIFEST.csv` binds all four snapshot
files. The payload hash is
`313bdb78d1a000d8a903aa12197603ac45bcb7a601df1ee12447eaaf29031261`.
`docs/PRD.md`, hash
`95c3c25ee36d4d4ddadf54d266a47a2ee58c6b37fbbdef75ad20a97986a718ca`,
supplies the product warrant. Snapshot relative references resolve from the
original `execution/_Decomposition/PROJECT_DECOMP.md` location.

| Accepted scope | Contribution here | Objective meaning retained |
|---|---|---|
| SOW-0009; PRD R05, R17, A2 | Executable commands and direct instructions agree on dependencies, effects, failure handling and permitted fallbacks. | OBJ-002: carry authorized maintenance through usable library methods and tools. |
| SOW-0015; PRD R03, R10 | Derive bounded relationships from owning declarations with source basis, unknowns and partial coverage visible. | OBJ-001: find the relevant basis and conditions; OBJ-004: support local action and coordination without a complete graph. |
| SOW-0024; PRD §1, §2.2, R17 | Reuse standalone repository foundations; repair only demonstrated, authorized gaps. | OBJ-001, OBJ-002, OBJ-005: accessible maintenance and dependable reuse/continuity. |

The initial source assessment and continuation conditions are in [Work/ToolBasis.md](Work/ToolBasis.md). Consumer-local needs are now declared in `deliverable.yaml`; their presence establishes no satisfaction claim.

The post-60 usage-contract examination and owner-approved structured-brief dependency
clarification are recorded in [Work/ToolBasis.md](Work/ToolBasis.md). The linked
complete-source candidate provides bounded standalone-use evidence; its content
and exact source-delivery candidate were approved in PR #1787; release remains separate.

## Deliverable Definition — Ontology

A utility is executable repeatable behavior, distinct from instructions describing
it. A locality contains `ScopeOfWork.md`, `deliverable.yaml` and `Work/`; source
code and reusable instructions retain their maintained homes. A need is the
consumer's input/use condition, case and source or unresolved binding, not a
supplier appointment. A query is a derived observation, not acceptance or an
execution decision. These meanings follow accepted decomposition §2 and PRD R08–R10.

- **OUT-001** — Supported current-locality setup and contract-validation utilities, including their applicable maintained regression cases: `tools/scaffolding/current_locality.py`, `tools/scaffolding/scaffold_package.sh`, `tools/scaffolding/scaffold_deliverable.sh`, `tools/validation/check_min_viable_fileset.sh` and the existing `tools/scope_of_work/` validators/checklist tools. Reuse the repaired implementation; make changes only for an actual connected defect or unfulfilled claim. Maps to SOW-0009, SOW-0024 and OBJ-001, OBJ-002, OBJ-005.
- **OUT-002** — Supported declaration-based queries and relevant maintained regression cases at `tools/deliverables/`, preserving live metadata selection, project-root references and truthful limits for undertaking-specific views. Maps to SOW-0015, SOW-0024 and OBJ-001, OBJ-004, OBJ-005.
- **OUT-003** — Accurate direct usage contracts at the affected existing tool guides and caller instructions: `tools/deliverables/README.md`, `tools/workflow_runtime/README.md`, `workflows/project-setup/resources/current-project.md`, `.agents/skills/preparation/` and `workflows/scope-of-work/`. Reuse `tools/workflow_runtime/` utilities where selected; do not infer a resolver change or host-enforcement product. Keep claim-specific applicability and unresolved gaps in this locality's `Work/` or the actual review, with maturity explicit. Maps to SOW-0009, SOW-0015, SOW-0024 and OBJ-001, OBJ-002, OBJ-004, OBJ-005.

- **CLM-001** — Accepted decomposition §6.1 records PR #1779's repaired current setup path at checked head `a0bb0dc77a53b041262571f658f9fd9590d44269`, merged as `a052783460f60c76e6fa229500f59a51f67c5265`. Its reported selected-tool checks and independent collision review are reusable evidence for the claims they actually covered. This author inspected the relevant helper, wrapper/check and current setup/ScopeOfWork instruction sources and found no differences from that checked head. The historical test suite was not rerun for this contract.
- **CLM-002** — The current setup route uses explicit `--current` selection and Python 3/PyYAML. It creates numeric package/deliverable folders, `Work/` and accepted identity/name YAML with initially empty needs, preserving existing work. It leaves substantive ScopeOfWork authoring separate. Prepared structural checks omit the missing-contract requirement; authored structural checks require matching contract identity, and the ScopeOfWork validator checks full contract format. These are separate claims, not interchangeable passes. Sources: current helper, wrappers/checker and current-project guide.
- **CLM-003** — `tools/deliverables/README.md` and `tools/deliverables/cli.py` describe a read-only JSON query interface requiring Python 3, PyYAML, Git and resolvable HEAD. The live loader discovers working `deliverable.yaml` files, including uncommitted declarations; historical comparisons use the selected Git basis. References are project-relative. Unknown suppliers and cycles are observations; malformed input reports errors with any usable partial result. Structural success does not assess suitability, execute referenced checks, lift holds or infer readiness. The workflow resolver describes selection/policy composition and explicitly does not enforce a process/filesystem sandbox.
- **CLM-004** — Accepted decomposition §8 cards, §8.1 and §9 allocate the broader maintenance route to `DEL-02-01`, the bounded shared-meaning repair to `DEL-02-02`, reconciliation practice and setup/need formation coverage to `DEL-04-01`, reflective review and decomposition formation coverage to `DEL-04-02`, entry/navigation to `DEL-01-01`, and acquisition, named compatibility and publication-preparation/change-inspection guidance to `DEL-05-01`. Actual formation is performed by its authorized undertaking and local contributors; each contributor retains their own contract, Work and needs. Agent 0 coordinates and retains integration responsibility. This toolkit supplies executable behavior and direct usage contracts to those contributions, not duplicate ownership.
- **CLM-005** — The accepted decision, PRD §§2.3/5, R10/R13/R15/R17 and `AGENTS.md` reserve changed commitments/acceptance criteria, risk acceptance, protected-baseline decisions, additional archival disposition, frozen-project reactivation and release to their actual owner. Root's owner controls Root decisions; independent consumers control their product work, adaptations, operational data, adoption and release. No actor is authorized by this contract to publish credentials or private data. Source authors and maintainers keep historical identities; reading a newer source or merging a change does not replace an adopted or published basis.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — Current setup shall preserve the CLM-002 numeric-locality contract and existing content, separate preparation from real contract authoring, and retain the unflagged legacy behavior as a compatibility interface. The current setup shall not create legacy phase directories, lifecycle/control files, blank contracts or routine setup receipts. F-01 is repaired: no unperformed-build gate is imposed for that repair.
- **REQ-002** — Queries shall derive views from owning declarations with live selection and project-root reference semantics preserved. They shall retain distinct conditions between endpoints, preliminary/final uses, reciprocity, gating distinctions and technical holds, and report basis, scope, unknowns and partial/cyclic coverage. No second manually maintained progress graph or complete DAG is required; query results are facts and unknowns for judgment, not supplier commitments or completion claims.
- **REQ-003** — Direct usage guidance shall state actual invocation, input contract, dependencies, outputs, write effects, failure behavior and limitations of each selected operation. It shall distinguish structural checks, substantive contract validation, executable evidence and human suitability decisions. When queries cannot run without their declared dependencies, direct source/declaration inspection with the query limit stated is the documented fallback; no Git-free adapter is assumed.
- **REQ-004** — For each affected operation, classify existing support as usable, needing connection/repair or absent, using bounded source and evidence inspection. Reuse applicable PR #1779 evidence; exercise changed behavior and unresolved claims only as needed. Keep meaningful regressions in maintained tests when code changes warrant them. Persistence, containment, permissions, numerical meaning or destructive changes require targeted regressions and independent scrutiny. A test cannot create acceptance criteria or justify weakening an expected result merely to pass.
- **REQ-005** — The supported utility set and instructions shall preserve standalone repository use and ordinary Git/search/review/release/validation/scheduling foundations. Ordinary use shall not depend on undisclosed sibling checkouts, dated scratch/run directories, private inputs or credentials. Public changes and retained public evidence require maintained credential/private-term screening; private consumer evidence stays local and only cleared fixtures or summaries may be public.
- **REQ-006** — This deliverable shall perform no act owned by another deliverable: general maintenance/custody/recovery procedure ownership belongs to `DEL-02-01`; shared-meaning repair belongs to `DEL-02-02`; setup/need formation accounting and reconciliation practice belong to `DEL-04-01`; decomposition formation accounting and reflective review belong to `DEL-04-02`; entry/navigation belongs to `DEL-01-01`; acquisition, named compatibility qualification and publication-preparation/change-inspection guidance belong to `DEL-05-01`, as supported by CLM-004. Authorized local contributors perform actual setup, author their local needs and reconcile their work, with Agent 0 retaining combined integration; utility support does not take those acts over.
- **REQ-007** — Excluded authority acts shall remain with the owners named in CLM-005: the Root owner decides changed commitments/acceptance criteria, risk, Root protected baselines, additional archival removal, frozen-project reactivation and Root release; each independent consumer decides its own product work, operational data use, adaptation, adoption and release. No new application, runtime, companion, graph service, automated management or host enforcement is commissioned; expanding the accepted scope would require the actual owner's decision. No archival deletion, frozen development/verification or consumer operation follows from this contract. Publication of private data or credentials remains prohibited, not reassigned.

- **AC-001** — Selected current preparation behavior creates the accepted numeric locality and initial YAML/Work structure while preserving existing content and rejecting relevant identity/collision cases; unflagged legacy interfaces remain compatible. Applicable PR #1779 evidence may establish unchanged behavior, with selected-use applicability explicit. Verify by VER-001.
- **AC-002** — The preparation, authored-locality and full ScopeOfWork checks are usable for their separate purposes: an absent contract is allowed only by the prepared structural check, authored structure requires matching identity, and full validation assesses SOW_V1 content. Current INIT leaves lifecycle sources untouched and does not require absent legacy material. Verify by VER-002.
- **AC-003** — For each supported affected query claim, evidence establishes live metadata selection, distinct conditions, project-root references and truthful partial/unknown/cyclic results with source basis retained; the result does not assert suitability, readiness or completion. Verify by VER-003.
- **AC-004** — Selected commands and direct instructions agree on inputs, dependencies, outputs, effects and failure limits, including query Git/HEAD/PyYAML requirements, the direct-inspection fallback and any selected workflow resolver's enforcement limits. Verify by VER-004.
- **AC-005** — The utility contribution uses existing foundations, records a concrete gap before additional implementation, and binds checked behavior and reused evidence to the actual affected source/caller basis; repairs carry proportionate regressions and independent scrutiny where required by REQ-004. Verify by VER-005.
- **AC-006** — Selected utility use and its required resources are available from the repository without a mandatory companion or undisclosed private/sibling inputs; public changes and retained evidence pass applicable local credential/private-term checks with unavailable screening explicitly distinguished. Verify by VER-006.
- **AC-007** — The combined toolkit result respects REQ-006 and REQ-007, preserves unresolved authority/input conditions, and reconciles changed usage meaning with affected callers and local material without treating a setup check, merge or this contract as acceptance. Verify by VER-007.

Inputs below inform later consumer-local `deliverable.yaml` authoring. They are
use conditions, not a complete dependency graph, new supplier commitments or
whole-deliverable finish-to-start gates.

| Input and source | Intended use / trigger | Condition and present limit |
|---|---|---|
| Accepted snapshot §2/§8.1/card, decision; PRD R08 | Selecting the locality and output target | Accepted identities and selected activation authority plus actual target contents are required before live creation. This authoring assignment supplies no new creation authority. |
| Repaired helper/caller sources; snapshot §6.1 and PR #1779 | Reusing current setup and its verification | Bind the relevant source revision and actual checked claim. Repaired F-01 is available; absent future localities do not block reuse of source/evidence. |
| Current `deliverable.yaml` declarations, selected project root and Git/HEAD | Querying actual input/use conditions | Scope precedes need authoring. Empty needs mean none declared yet, not no inputs; parent authors bindings after scope. Selected evidence must address the actual condition. |
| Affected caller contract and maintained fixtures | Before changing a utility or exported interface | Inspect the actual caller and required use; unknown callers stay unknown. Relevant existing evidence may suffice for unchanged behavior. |
| `DEL-05-01` qualification input, Q-04 | Before claiming named compatibility or making an incompatible exported change | Bind the named maintained contract/fixtures and exact revision; provide a supported path or coordinated adapter before incompatible change. Concrete selection is unresolved. |
| Existing maintenance and reconciliation methods; affected local Work and needs | Before integrating an authorized toolkit change | Check the candidate under the preceding selected method and reconcile current descriptions/evidence in the same PR; preserve unchanged declarations. |

- **TBD-001** — Q-02 remains conditional: no demonstrated gap or implementation is selected for bespoke tooling, a file-only query interface, namespace adapter or companion. SOW-0033 has no production allocation. Continue supported utility work; return a demonstrated gap and consequence before any expanded commitment.
- **TBD-002** — Q-04's named external contract/fixtures and exact revision are unbound. Root component checks and PR #1779's reported absence of a blocking consumer constraint do not establish A6. This limits named compatibility and incompatible-interface work, not independent instruction/utility assessment.
- **TBD-003** — Q-05's verified publication candidate/version and prior comparison basis remain unbound in `DEL-05-01`. Any later claim about toolkit delivery or update inspection must bind those inputs; this setup contract supplies neither A7 evidence nor release authority.
- **TBD-004** — Q-01 additional disposition remains reserved: retain `plans/`, `_DomainEngines/` and other unselected paths. Q-03 future production assignment remains open. Neither condition creates toolkit work or a permanent supplier appointment.

## Production and Verification Method — Praxeology

Select the bounded operation and its actual use condition. Inspect its current
source and caller, reuse applicable checked holdings, and identify any real gap.
Under a later authorized implementation assignment, repair only that gap at the
maintained home, retaining useful regression evidence. Keep consequential reasoning
and remaining conditions in `Work/` and the actual review; there is no routine
receipt, new capability census or parallel framework requirement. This INIT performs
contract checks only. No code change or product behavioral verification is claimed.

- **VER-001** — Compare the selected current helpers/wrappers and caller contract with the checked PR #1779 basis and its creation/preservation/collision evidence. Inspect maintained compatibility coverage for unflagged calls. Exercise only changed or uncovered setup behavior in an authorized isolated case, including affected preservation/identity/collision behavior, and retain candidate-bound results. Do not recreate live localities merely to retest.
- **VER-002** — Inspect the selected current INIT path and reuse relevant repair evidence for stage distinctions. For an actually authored locality run `zsh tools/validation/check_min_viable_fileset.sh --current <DEL-path> <accepted-DEL-ID>` without `--prepared`, then `python3 tools/scope_of_work/validate_scope_of_work.py <DEL-path>/ScopeOfWork.md --json`. Use the deterministic checklist and boundary-owner checker for contract QA. Verify status preservation/absence by inspection; assess uncovered stage/failure claims through applicable focused evidence, not the authored structural pass alone.
- **VER-003** — Inspect the live loader and project-root resolution against selected declarations and applicable maintained query evidence. Where a claim lacks applicable evidence, run a focused authorized case addressing distinct/reciprocal needs, unknown or partial inputs, cycles and live-versus-historical selection as relevant. Use `python3 -m tools.deliverables --project . check` and a bounded `neighborhood`, `impact`, `touches` or `dag-diff` inquiry for actual use. Compare output to owning declarations, noting coverage, source basis, error behavior and suitability limits. A synthetic case is behavioral evidence, not the actual A3 formation case.
- **VER-004** — Review each selected invocation and guide against executable argument/failure paths, dependency declarations and observed or reused focused evidence. Confirm effects and fallback wording, including resolver policy-composition versus host enforcement where that interface is selected. Report missing invocation/failure evidence as unverified rather than inferring it from a walkthrough.
- **VER-005** — Review the bounded capability assessment, prior method basis, actual source/caller revision and evidence applicability. For a repair, inspect its focused regressions and required independent scrutiny; for unchanged reusable holdings, state why existing evidence applies. Confirm necessity and authority before added tooling and distinguish supported portions of PRD A2/A5 from unevaluated operations.
- **VER-006** — Inspect the selected use path and resources for standalone availability, declared dependencies and public suitability. Screen changed content and retained review artifacts using `tools/validation/validate_run_record_leaks.py` and `tools/validation/validate_private_terms.py` maintained APIs with available local terms, without exposing them. State that local screening does not establish the hosted secret-set or named-consumer qualification. Product-use evidence is distinct from this contract's content screening.
- **VER-007** — Compare the actual toolkit contribution, authority boundaries, changed direct guidance and affected uses to the accepted card/§8.1/§9 and PRD. Review the one-for-one act/owner mapping, outstanding Q-01/Q-02/Q-04/Q-05 conditions and local evidence/needs reconciliation with the implementation owner and Agent 0 before integration. Human acceptance and any changed commitments remain separate owner acts; report a substantive ambiguity as CONFLICT and continue unaffected work.

## Governing Values and Decisions — Axiology

- **AX-001** — Preserve the accepted purpose and actual authority. The owner's Group 3 instruction, “I accept this decomposition as the basis for project setup,” authorizes setup with Agent 0's direct management and Type 2 scope authoring; it does not accept product implementation or waive later decisions. Proposed replacement instructions cannot authorize or retrospectively validate themselves.
- **AX-002** — Prefer accurate, reusable existing means and proportionate evidence over new artifacts for their own sake. PR #1779 repairs F-01 and supports relevant A2/A5 claims; it does not establish all maintenance operations, live setup, local need suitability, custody/recovery, complete toolkit capability or product acceptance. The current live setup likewise cannot establish those wider claims.
- **AX-003** — Preserve source identity, compatibility and independent use. Retain legacy interfaces without selecting their legacy folders for this setup; preserve historical bases and private boundaries. Match judgments to evidence and return consequential uncertainty without inventing a global census or holding unrelated work.
- **AX-004** — Keep utility/direct-usage ownership here and the sibling contributions in CLM-004 with their actual owners. Shared-file changes require one coordinated editor; a code-path relevance match grants no exclusive ownership. Parent reconciliation must connect the authored scopes, useful code/check pointers, actual need bindings and maturity of Work under §8.1. This contract alone closes none of that combined formation evidence.

## Output and Evaluation Matrix

Each row binds one criterion to its actual verification method. Evidence may be
reused when its basis and claim remain applicable; expectations below do not
assert that future execution has occurred.

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-0009, SOW-0024, OBJ-001, OBJ-002, OBJ-005 | REQ-001, CLM-001, CLM-002 | AC-001 | VER-001 | Applicable repair and compatibility evidence; focused results for any changed or uncovered creation/preservation/collision claim. |
| OUT-001 | SOW-0009, SOW-0024, OBJ-002 | REQ-001, REQ-003, CLM-002 | AC-002 | VER-002 | Stage-specific evidence plus authored locality identity, SOW validation, deterministic checklist and boundary QA where applicable. |
| OUT-002 | SOW-0015, SOW-0024, OBJ-001, OBJ-004, OBJ-005 | REQ-002, CLM-003 | AC-003 | VER-003 | Selected declaration/source basis, relevant query cases/results, truthful unknowns and coverage limits. |
| OUT-003 | SOW-0009, SOW-0015, OBJ-001, OBJ-002, OBJ-004 | REQ-003, CLM-002, CLM-003 | AC-004 | VER-004 | Invocation/guide agreement and actual or applicable reused failure/dependency evidence. |
| OUT-001 | SOW-0009, SOW-0024, OBJ-002, OBJ-005 | REQ-004, CLM-001 | AC-005 | VER-005 | Bounded necessity/evidence applicability account; any repair's regressions and required independent scrutiny. |
| OUT-002 | SOW-0015, SOW-0024, OBJ-001, OBJ-004, OBJ-005 | REQ-004, CLM-003 | AC-005 | VER-005 | Query-specific necessity, source/caller bindings and applicable evidence or explicit gaps. |
| OUT-003 | SOW-0009, SOW-0024, OBJ-002, OBJ-005 | REQ-005 | AC-006 | VER-006 | Usable selected resources and declared dependencies; public-screening evidence with its actual limits. |
| OUT-003 | SOW-0009, SOW-0015, SOW-0024, OBJ-001, OBJ-002, OBJ-004, OBJ-005 | REQ-006, REQ-007, CLM-004, CLM-005 | AC-007 | VER-007 | One-for-one boundary review, relevant caller/local reconciliation and remaining decisions or unverified claims. |
