# Chirality Library — Group 1 decomposition candidate

**Status:** PROPOSAL — Group 1 basis reviewed by Agent 0; awaiting owner decision.
The owner accepted the PRD, not this normalized basis.
**Revision:** G1-candidate-3, 2026-10-31. Owner-confirmed output-form distinction
added to vocabulary and structural guidance; scope and objective proposals
unchanged from the Type 2 return.
**Method origin:** `chirality-root:bundled:workflow:project-decomp`.

This candidate supplies the basis, normalized scope, vocabulary, objectives and
open interpretations for the first grouped checkpoint. It proposes no Packages,
Deliverables, specific production artifacts or dependency bindings. Combined review has
not been selected. Group 2 may begin only after the owner's Group 1 decision and
the applicable accepted snapshot/pointer have been established by the coordinator.
No acceptance record, snapshot or pointer exists in this candidate.

## 1. Source basis and authority

All repository references below resolve at clean base commit
`d5ca6594ce6010c94c7981fe35cc540a822e9aa8` (PR #1778), unless expressly qualified.
The working branch is `codex/library-decomposition-20261031`.

| Source | Standing and use |
|---|---|
| [Library PRD](../../docs/PRD.md), revision 2026-10-31 | Accepted product intent: O1–O5, R01–R17, A1–A8 and §§2, 5, 6. Current file SHA-256: `95c3c25ee36d4d4ddadf54d266a47a2ee58c6b37fbbdef75ad20a97986a718ca`. The PRD separately preserves the pre-annotation approved-source hash; these are different byte identities, not competing product bases. |
| Owner's output-form clarification, 2026-10-31 | The owner agreed to distinguish instructions, descriptive/explanatory material and executable tools, then requested the corresponding candidate revision. This refines the vocabulary for anticipated outputs; it does not accept the whole Group 1 basis or assign deliverables. |
| [Root entry](../_Coordination/LOOP_INIT.md) | Current library entry and reset standing. SHA-256: `28673a218654273757c1af2fcb043a6a53c47e1dea7599cb1244bcc090a61c7b`. Initialization starts no undertaking. |
| [AGENTS.md](../../AGENTS.md), [TASK role](../../agents/AGENT_TASK.md) and the assignment | Root authority and bounded preparation. Owner steering explicitly assigns Agent 0 coordination and a directly managed Type 2 preparation; the workflow's usual WORKING_ITEMS coordinator does not introduce a Type 1 layer here. No delegation or Git integration by this preparer. |
| [Selected workflow](../../workflows/project-decomp/WORKFLOW.md), [contract](../../workflows/project-decomp/resources/contract.md), [method](../../workflows/project-decomp/resources/method.md) | Root bundled PROJECT method, Group 1 only. Source commit fixes the package identity. The method's stage sequencing governs when later validity requirements become applicable. |
| [Recovery reference](../../projects/FROZEN.md#pre-library-root-execution) | Historical traceability only. Archive tag `archive/pre-library-execution-2026-10-31` resolves to `f80f1510fb50799764720303b86c36da64b75d19`. No old execution content was used to reconstruct scope. |

The accepted product is a maintained library of information, instructions, tools,
publications and execution material, usable to maintain and develop itself.
Principles, thesis, manuals and courses are holdings. Root execution is also a
holding. Maintained outputs keep their source homes. Neither repository layout
nor requirement numbering predetermines future deliverables.

Only this working document is authored. Its scope is a proposed normalization of
accepted intent, not authority to execute its IN items now. Agent 0 owns review,
integration and presentation of the human checkpoint. Product acceptance,
commitment changes, releases and reserved dispositions remain owner acts.

## 2. Vocabulary map

| CanonicalTerm | Synonyms / nearby terms | Practical meaning and source |
|---|---|---|
| Library holding | Material, library content | Principles, publications, roles, workflows, tool-use instructions, executable tools, formats, reference information and execution; not only code or instructions. PRD §1, §2.3. |
| Instructions | Guidance for action | Roles, workflows, maintenance procedures and tool-use guidance describing how a contribution can proceed and within what conditions. PRD R02, R04–R06; owner output-form clarification. |
| Descriptive and explanatory material | Account, definition, reference information | Information about what exists, what is known, its relationships, reasons and warrant, including state descriptions, evidence and accounts of commitments. PRD R02, R08–R12; owner output-form clarification. |
| Executable tools | Program, query, validator, transformation | Repeatable operations supplied as executable behavior, with declared inputs, outputs, dependencies, effects and limits. Tool-use instructions are a related information output. PRD R05, R13, R17; owner output-form clarification. |
| Artifact / output form | Maintained result, anticipated output | A tangible new or revised result of a later deliverable. The three forms in §2.1 guide its meaning and evaluation; concrete artifact kinds and their allocation belong to Group 2. Selected decomposition contract; PRD R07–R08. |
| Selected basis | Source revision, edition in use | Identified material actually governing a use or review. A proposed replacement or a newer examined publication does not silently replace it. R06, R15–R16. |
| Maintenance | Add, revise, reconcile, integrate, recover | Authorized changes to holdings and their maintenance means using applicable methods, actual capabilities and proportionate checks. R04–R06. No standing audit/backlog is implied. |
| Consumption | Consult, invoke, copy, embed | Independent use through files, Git, archives or documented interfaces. Local authority, operational data, adaptations, adoption and release remain with the consumer. R13, §2.3. |
| Scope item / SSOW | Normalized atomic scope / structured scope | One independently classifiable commitment or boundary, with stable SOW identity and source warrant. This SSOW is proposed until Group 1 acceptance. Selected contract, PRD §6.2. |
| Objective | Success condition, product outcome | Testable intended improvement. Proposed OBJ identifiers map to accepted O references; they do not replace or amend them. PRD §2.1, §6.2. |
| Deliverable / local goal | Bounded contribution | A meaningful intended improvement, scope, outputs and evaluative evidence connected to product objectives. A directory, activity or requirement alone is not a deliverable. R07. No deliverables defined at this stage. |
| Work locality | Execution locality, local work | Future accepted locality containing ScopeOfWork.md, deliverable.yaml and Work/. It references maintained outputs at their actual homes. Older Design/ references in adopting products mean Work/. R08; AGENTS.md. |
| Dependency condition | Need, input/use condition | Consumer-owned input plus intended use/condition, case/trigger and source or unresolved binding. Distinct uses, preliminary/final use, reciprocity and holds remain distinct. Not a supplier commitment or inferred whole-deliverable finish-to-start relation. R09. |
| Execution | Maintenance work and its retained material | Local goals, reasoning, evidence, conditions and authorized action within the library. Does not mean a new agent runtime or automated project manager. R07–R10, §1. |
| Publication (holding) | Manuscript, manual, course, edition | Material prepared for an audience, which can contain instructions and descriptive/explanatory content. Its audience, edition and maintained home do not make it a separate fundamental output form. PRD §1, §2.3, R11; owner output-form clarification. |
| Publishing (act) | Release, making a version available | Owner publication of identified material from a verified revision; named versions are the downstream default. Proposed, integrated, published, examined and adopted retain distinct standing. R15–R16, A7. |
| Check-in | Review and integration | Integration within the actual repository grant at the checked revision; it neither publishes a release nor accepts the product for the owner. R14–R15. |
| Custody | Exclusive maintenance holding, lock | Exceptional reservation of an item and operation, with holder and release/recovery condition and honest enforcement limits. Readers normally retain checked-in material; timeout alone grants no disposal authority. R14. |
| Source declaration | Stated relationship, owning declaration | What the source or consumer actually declares, with provenance and use limits. Queries derive views from these declarations. R03, R09–R10. |
| Inferred relationship | Hypothesis, discovered connection | An interpretive result labelled separately from a declaration, unknown or search limit. It creates no binding or supplier obligation. Local views can be partial, cyclic and revised. R03, R10. |
| Historical source | Archive, earlier basis | Recoverable identified evidence with its original meaning. It is neither current instruction nor a standing backlog and does not reactivate frozen work. R02, R12, §§5–6. |

### 2.1 Output forms for later structural proposals

The owner-confirmed distinction guides what the later deliverables produce:

| Form | Typical expression in this library | Evaluation emphasis |
|---|---|---|
| Instructions | Role descriptions, workflows, maintenance procedures, tool-use guidance | Whether the intended reader or agent can use the guidance under its stated conditions, with adequate decisions, resources and limits |
| Descriptive and explanatory material | Definitions, reference models, publication content, scope and dependency descriptions, state information and evidence | Whether meaning is clear, claims are warranted, relationships and qualifications are preserved, and the account fits its intended use |
| Executable tools | Queries, validators, transformations and other repeatable operations | Whether the documented behavior, outputs, dependencies, effects and failure handling hold when exercised |

The first two are information outputs. These forms describe the function of the
material, not a file extension, directory or fixed package partition. A file or
cohesive artifact can contain more than one form; evaluate its claims accordingly.
The four perspectives remain applicable across all forms rather than assigning
one perspective to each type.

Publications express instructions and explanations for their readers. Execution
contains particular descriptions, commitments, evidence and applicable working
guidance about maintaining the library. Neither its location nor a publication's
delivery format creates an additional fundamental output type.

Group 2 will define concrete artifact kinds and bounded deliverables from scope,
objectives and semantic coupling. It may identify a closely connected set of
outputs where the result requires one, such as a tool and its necessary usage
instructions. This does not prescribe three packages, one deliverable per form,
or an output of every form for each goal. A revised existing holding can be the
complete output; no new document, program or companion is required merely to
populate the structure. Conditional tooling remains subject to SOW-0033.

## 3. Proposed objective set

Five objectives retain the five distinct accepted outcomes. Combining them would
hide useful acceptance distinctions; splitting them by operation would prematurely
parcel the work. Formal OBJ identifiers are proposed aliases, not new product
vision or changed acceptance criteria. Each objective has scope coverage below.
`MappedDeliverables` is **not yet applicable — Group 2** for every objective.

| ObjectiveID | Statement / testable outcome | PRD mapping | Evaluative basis (future evidence, not a present pass) |
|---|---|---|---|
| OBJ-001 | A maintainer entering with a bounded undertaking can locate the applicable holdings, instructions, source basis, execution work and unresolved conditions. | O1 | A1; A5's maintenance of the entry. Test purposeful discovery and source distinctions without a global graph. |
| OBJ-002 | A maintainer can carry authorized changes, including changes to maintenance means, through preparation, verification, review, integration and recovery using usable library instructions and tools. | O2 | A2, A4, A5. An actual instruction/tool change and its reusable procedure must both be demonstrated; a walkthrough alone proves no executable behavior. |
| OBJ-003 | A scoped change leaves affected definitions, warranted claims, actions, values, publications and work coherent for their uses, or exposes a consequential unresolved conflict for owner disposition. | O3 | A4, A5, A7. Preserve earlier editions and scoped adopted contracts; a repair alone does not establish maintenance-method availability. |
| OBJ-004 | Accepted local goals support evidence-directed action, meaningful input/use conditions, evolving reasoning and coordinated integration within the wider product without a complete graph. | O4 | A3, A8. Demonstrate an actual condition and a finding that revises the route; continue unaffected work and inspect affected uses. |
| OBJ-005 | Independent consumers can obtain identified material, inspect consequential changes and choose adoption, while maintainers preserve history, prepare publication and recover retained work. | O5 | A6, A7, A8. Named-contract compatibility, publication preparation and recovery establish different claims; consumer adoption and owner release remain separate. |

## 4. Normalized scope ledger

`IN` means accepted product intent retained in this proposed normalization;
`OUT` preserves an explicit boundary; `TBD` marks a contingent scope/disposition
whose inclusion is not established. These are scope classifications, not maturity
or completion states. Statements and qualifications must be read together.

Each `SourceRef` below refers to [the PRD at the source basis](../../docs/PRD.md).
OBJ mappings express contribution or boundary relevance, not package assignment.
For **every row**, `PackageID` is **not yet applicable — Group 2**. For IN rows,
`DeliverableID(s)` is **not yet applicable — Group 2**; for OUT/TBD rows it is
empty by contract. These uniform later fields are stated here to avoid repeating
placeholders in every row. No accountable package home is asserted yet.

| ScopeItemID | InOutStatus | ScopeItemStatement and qualifications | SourceRef | ObjectiveID(s) | OpenIssue / notes |
|---|---|---|---|---|---|
| SOW-0001 | IN | Maintain a locatable starting route from a bounded undertaking to the selected basis, applicable role/repository instructions, relevant holdings and execution. Initialization selects no undertaking; the entry is itself maintainable. | R01; O1; A1, A5; §6.1 | OBJ-001, OBJ-002 | FALSE. Current entry is an input, not evidence of full A1 satisfaction. |
| SOW-0002 | IN | Make holdings locally intelligible and searchable through purpose, applicability, standing, resources, outputs and limits; distinguish explanation, instruction, example, proposal and history, preserving resources/notices when copied. Principles and publications retain maintained source homes. | R02; §1; §2.3; A1, A6 | OBJ-001, OBJ-003, OBJ-005 | FALSE. Categories remain with the material; no new central registry. |
| SOW-0003 | IN | Support purposeful search, reference following and structured queries with source identity, declared/inferred/unknown relationships and search limits visible. Retain or deliberately migrate consumed indexes, checking/regenerating from owning sources; read selected material. | R03; §5; A1 | OBJ-001, OBJ-003, OBJ-005 | FALSE. Views may be incomplete, cyclic and revised. |
| SOW-0004 | IN | Provide usable maintenance instructions for adding or revising holdings with purpose, scope, destination, relevant material, source identity and checks. Reuse/connect applicable methods rather than prescribe a new method per operation. | R04, “Add or revise a holding”; §2.2; A2 | OBJ-002 | FALSE. Classify affected existing means as usable, needing connection/repair or absent during bounded work. |
| SOW-0005 | IN | Support organization, relocation or retirement using actual references/consumers, replacement or historical standing, recovery and deletion authority. | R04, “Organize, relocate or retire”; §5 | OBJ-002, OBJ-003, OBJ-005 | FALSE. Specific archival removals beyond the completed reset remain SOW-0032. |
| SOW-0006 | IN | Support diagnosis and reconciliation of conflicting claims, source meaning and observed behavior, identifying the owning material, evidence and repair scope. | R04, “Diagnose and reconcile”; R11; A4 | OBJ-002, OBJ-003 | FALSE. Reusable procedure and its result are distinct obligations. |
| SOW-0007 | IN | Support assessment of connected changes across relevant inputs, uses and consequences in instructions, tools, publications and execution, bounded by the authorized undertaking. | R04, “Assess connected change”; R11; §2.2 | OBJ-002, OBJ-003 | FALSE. Discovery of further consequences does not silently expand commitments. |
| SOW-0008 | IN | Support review and integration with proportionate scrutiny, the actual checked revision, findings, updates to owning text and the repository change procedure. | R04, “Review and integrate”; R12; R14; A2 | OBJ-002, OBJ-003 | FALSE. Root's grant does not transfer through library consumption. |
| SOW-0009 | IN | Align tool-use instructions with actual commands/interfaces, dependencies, outputs, write effects, failure behavior and limits. Use available selected-library tools for repeatable operations; state unavailable capabilities and permitted fallbacks, repairing necessary reusable procedure at its source. | R05; R17; §6.1; A2 | OBJ-002 | FALSE. Existing deliverables CLI requires Git, HEAD and declared dependencies; file-only/namespace adapters are not assumed. |
| SOW-0010 | IN | Maintain entry, roles, methods, tools and execution under the existing authorized basis; review replacement means, preserve the usable preceding basis and adopt only after verification with actual authority. | R06; R04, “Change the maintenance means”; A5 | OBJ-001, OBJ-002, OBJ-003 | FALSE. Proposed instructions do not authorize themselves or alter their own review basis. |
| SOW-0011 | IN | Establish an accepted decomposition of bounded contributions with meaningful intended improvements, scope, outputs and evaluative evidence mapped to product objectives, without directory/requirement-driven partitioning or conflicting change ownership. | R07; §2.2; §6.2–6.3; A3 | OBJ-001, OBJ-002, OBJ-004 | FALSE. This candidate contributes Group 1 only; acceptance, later structure and independent final audit remain outstanding. |
| SOW-0012 | IN | Set up accepted localities using the library's applicable tools: ScopeOfWork.md for goal, accepted scope/objective references, outputs, boundaries, acceptance criteria and verification; deliverable.yaml for actual needs/conditions and useful source/code/check pointers; Work/ for reasoning, evidence, alternatives, consequential attempts, unresolved conditions and local outputs with maturity explicit. | R08; §6.2–6.3; A3, A8 | OBJ-001, OBJ-002, OBJ-004 | FALSE. Future execution/PKG-nn/DEL-nn-nn/ only after accepted scope; maintained outputs retain source homes and unchanged declarations stay unchanged. |
| SOW-0013 | IN | Author consumer-local needs after scope exists, identifying input, intended use/condition, trigger/case and source or unresolved binding. Preserve distinct conditions, preliminary/final use, reciprocal relations and technical holds; judge suitability from evidence. | R09; §6.1–6.2; A3 | OBJ-004 | FALSE. No inferred supplier commitments or whole-deliverable finish-to-start constraints; presence, merge and structural checks do not establish suitability. |
| SOW-0014 | IN | Support authorized local action from goals, evidence and actual input conditions, revising understanding/routes and neighborhoods as findings emerge, continuing unaffected work and checking affected uses with one integration owner. | R10; A3; §4 closing paragraphs | OBJ-002, OBJ-003, OBJ-004 | FALSE. Commitment/acceptance changes and reserved decisions return to the owner; local completion must serve the product. |
| SOW-0015 | IN | Derive relationship queries and undertaking-specific views from owning declarations, reporting basis, scope, unknowns and partial coverage while preserving actual live-metadata selection and project-root reference semantics. | R03; R10; §6.1–6.2 | OBJ-001, OBJ-004 | FALSE. No second manual progress graph or required global DAG. |
| SOW-0016 | IN | Reconcile affected definitions/relationships, warranted claims, actions and values together, recording consequential reasoning in owning work and reconciling affected guidance/publications or identifying an edition's earlier basis. Preserve historical identities and scoped adopted contracts. | R11; §2.3; A4, A5 | OBJ-002, OBJ-003 | FALSE. Four perspectives do not require four reports/approvals; library definitions remain distinct from product runtime enforcement. |
| SOW-0017 | IN | Verify the actual candidate proportionately and distinguish content, behavior and consumer-interface claims. Numerical meaning, persistence, permissions and destructive changes require focused regression checks and independent scrutiny; reuse applicable evidence and expose missing evidence as unverified. | R12; §4; A2, A4–A6 | OBJ-002, OBJ-003, OBJ-004 | FALSE. Applicable checks attach to actual future changes, not a blanket product-verification run in this stage. |
| SOW-0018 | IN | Make unfinished work recoverable from its locality and review record: source basis, usable result, checks, unresolved conditions and next needed action. Add at most one replaceable recovery note only if needed. | R12; R04, “Recover or continue”; A8 | OBJ-002, OBJ-004, OBJ-005 | FALSE. A labelled recovery case is allowed by A8; past records create no new authority or standing backlog. |
| SOW-0019 | IN | Provide independent paths to consult, invoke or copy identified material through ordinary files, Git, archives and documented interfaces, retaining resources/licenses/source basis and distinguishing local adaptations. | R13; R17; A6 | OBJ-005 | FALSE. Reading the library does not require Git; executable tools declare their own dependencies. |
| SOW-0020 | IN | Check affected named consumer interfaces at an explicit maintained-contract/fixture revision and supply a supported path or coordinated adapter before incompatible change. | R13; §2.2–2.3; §6.1; A6 | OBJ-003, OBJ-005 | FALSE. Needed input: affected named contract/fixtures at a specified basis, used when an interface change is selected; concrete selection unresolved until that scope is defined. Private evidence stays local; adoption/release are independent. |
| SOW-0021 | IN | Support exceptional exclusive custody through an existing lock/coordination mechanism stating holder, item, reserved operation and release/recovery condition with honest enforcement limits; resolve interruption through the authorized maintainer. | R14; A8 | OBJ-002, OBJ-005 | FALSE. Readers normally retain checked-in material; elapsed time never authorizes disposal. No new lock service is prescribed. |
| SOW-0022 | IN | Prepare named publication candidates from verified revisions with source identity, notices, dependencies, limitations and recoverable commit/edition routes; preserve owner publication authority and independent consumer adoption. | R15; R04, “Prepare publication and inspect updates”; A7 | OBJ-003, OBJ-005 | FALSE. Named publications are downstream default; explicitly following main is development. A merge is not release. Actual release is not this task's work. |
| SOW-0023 | IN | Explain consequential old/new basis, reason, meaning/use and migration effects in existing review/publication notes, and exercise polling/inspection via existing release/diff facilities. | R16; R04, “Prepare publication and inspect updates”; A7 | OBJ-003, OBJ-005 | FALSE. Interests stay local; examined is not adopted; partial/failed checks do not prove no change. Scheduling, delivery and unattended operation require actual configuration/authority; no new notice register. |
| SOW-0024 | IN | Preserve standalone repository use and existing Git/search/review/release/validation/scheduling foundations, classifying affected capabilities as usable, needing connection/repair or absent and implementing only necessary changes. | §1; §2.2; R17 | OBJ-001, OBJ-002, OBJ-005 | FALSE. Optional bespoke tooling remains conditional under SOW-0033; no permanent capability census. |
| SOW-0025 | IN | Keep ordinary library use independent of undisclosed sibling checkouts, dated run directories, private inputs and credentials; use cleared public fixtures/summaries and required credential/private-term checks for public changes. | R17; §2.3; §6.3; A6, A7 | OBJ-002, OBJ-005 | FALSE. Private consumer inventory need not be read for this stage. |
| SOW-0026 | IN | Preserve traceability and recoverability of the authorized pre-library execution transition and original consumer-pinned history, including the App's historical SWBPIPE source bytes, without reinstating prior structure, commitments or lifecycle state. | §2.2; §5; §6.1, §6.3 step 2; R12, R15 | OBJ-003, OBJ-005 | FALSE. Transition already executed in PR #1778; archive identity verified here. Retention is the ongoing constraint; no repeat removal or migrated backlog. Selected archive bytes must be verified before future reliance. |
| SOW-0027 | OUT | Require a new App, agent runtime, hosted service or compulsory companion as the library product or a prerequisite for repository use. | §1; §2.3; R17 | OBJ-001, OBJ-002, OBJ-005 | FALSE. Optional, justified thin support is distinct; see SOW-0033. |
| SOW-0028 | OUT | Establish a standing global audit, central relationship graph, subscriber/notice registry, automated project management or a complete DAG/global census requirement. | §2.3; R03, R10, R16 | OBJ-001, OBJ-004, OBJ-005 | FALSE. Existing consumed indexes and bounded derived views remain in scope. |
| SOW-0029 | OUT | Transfer Root grants, execution authority or runtime policy to consumers, perform independent consumer product work, or require their production adoption/release to accept a verified library interface. | §2.3; R11, R13, R15 | OBJ-003, OBJ-005 | FALSE. App v4 and SWBPIPE remain independent; coordination conveys no owner authority. |
| SOW-0030 | OUT | Reactivate, develop or verify frozen App v3, Runtime or PEC through decomposition, recovery or library maintenance. | §2.3; §6.3; AGENTS.md | OBJ-003, OBJ-005 | FALSE. Explicit reactivation would be a separate authorized change. |
| SOW-0031 | OUT | Publish private knowledge, consumer operational data or credentials in library artifacts, examples or fixtures. | §2.3; R17; §6.3 | OBJ-005 | FALSE. Cleared public evidence may support compatibility claims; generic evidence cannot establish named-consumer compatibility. |
| SOW-0032 | TBD | Further archival disposition of plans/, _DomainEngines/ and additional removals, if specifically authorized. | §2.3; §5 | OBJ-003, OBJ-005 | TRUE — Q-01. Retain pending specific owner disposition; historical classification alone authorizes no deletion. No writes there in this undertaking. |
| SOW-0033 | TBD | Add bespoke tooling or a thin companion, including a file-only query interface or namespace adapter, only where a selected consumer/maintenance need demonstrates a gap in existing means. | §1; R17; §6.1 | OBJ-002, OBJ-004, OBJ-005 | TRUE — Q-02. No gap or implementation selected here; neither availability nor a new product commitment is assumed. |

### Source inputs carried at scope, without producer bindings

Owner steering and accepted PRD govern all scope. The current entry, roles and
repository instructions supply authority and route for SOW-0001/0008/0010.
Existing selected methods/tools are inputs to SOW-0004–0015 and SOW-0021–0024;
their actual applicability, dependencies and write effects must be checked when
used. Maintained holdings and references supply the meanings, editions and uses
for SOW-0002/0003/0005–0007/0016. Relevant execution/review evidence supplies
reusable checks and recovery conditions for SOW-0017/0018, without renewed scope.

PRD §6.1 identifies docs/AGENT_WORKFLOW_RUNTIME.md,
docs/PRODUCT_BOUNDARIES.md and docs/COMPATIBILITY_FORMATS.md as possible inputs
for scoped reusable-versus-Root interpretation; publication sources/editions and
consumer contracts/fixtures are needed when those uses are actually selected.
Their existence is not a defect finding, adoption instruction or proof of fit.
The generic consumer needs in the PRD suffice for Group 1; no private inventory
or consumer repository has been opened. SOW-0020 carries the eventual contract
selection and SOW-0026 carries archive identity/byte-reliance conditions. Until
consuming deliverables exist, there are no producer IDs, supplier commitments,
dependency rows or authoritative dependency graph.

## 5. Accepted-intent coverage

This table checks representation of accepted requirements and acceptance criteria.
It claims **no implementation completion or product acceptance**. The ledger's
qualifications and the PRD remain governing; compact mapping does not replace them.

| PRD requirement | Scope representation |
|---|---|
| R01 | SOW-0001 |
| R02 | SOW-0002, SOW-0019 |
| R03 | SOW-0003, SOW-0015, SOW-0028 |
| R04 | Add/revise: SOW-0004; organize/relocate/retire: SOW-0005; diagnose/reconcile: SOW-0006; connected change: SOW-0007; review/integrate: SOW-0008; publication/update inspection: SOW-0022/0023; recover/continue: SOW-0018; change maintenance means: SOW-0010 |
| R05 | SOW-0009 |
| R06 | SOW-0010 |
| R07 | SOW-0011 |
| R08 | SOW-0012 |
| R09 | SOW-0013 |
| R10 | SOW-0014, SOW-0015 |
| R11 | SOW-0006, SOW-0007, SOW-0016, SOW-0029 |
| R12 | SOW-0017, SOW-0018, SOW-0026 |
| R13 | SOW-0019, SOW-0020, SOW-0029 |
| R14 | SOW-0008, SOW-0021 |
| R15 | SOW-0022, SOW-0026 |
| R16 | SOW-0023, SOW-0028 |
| R17 | SOW-0009, SOW-0024, SOW-0025, SOW-0027, SOW-0031, SOW-0033 |

| Criterion | Scope representation | Claim/evidence boundary retained for later evaluation |
|---|---|---|
| A1 | SOW-0001–0003, SOW-0015 | Bounded entry/discovery case with provenance and unresolved conditions; no central graph prerequisite. |
| A2 | SOW-0004, SOW-0008–0010, SOW-0017 | Actual instruction/tool change through integration and available reusable maintenance procedure. |
| A3 | SOW-0011–0015 | Requires accepted/set-up local scope, actual use condition, changed route/understanding and examined neighboring uses. Group 1 alone cannot establish it. |
| A4 | SOW-0006, SOW-0007, SOW-0016, SOW-0017 | Scoped inconsistency resolved, including publication where affected; warrant, use and values checked with historical qualifications. |
| A5 | SOW-0001, SOW-0010, SOW-0016, SOW-0017 | Maintain entry/instructions/tools under existing basis; verify both changed holding and maintenance means with preceding basis/authority preserved. |
| A6 | SOW-0002, SOW-0017, SOW-0019, SOW-0020, SOW-0025 | Obtain/use identified material and check a named consumer contract/fixtures at a specified revision, including resources/notices. Generic walkthrough is insufficient. |
| A7 | SOW-0022–0025 | Identifiable publication candidate, meaningful change account and exercised inspection against prior basis; release/adoption not implied. |
| A8 | SOW-0012, SOW-0018, SOW-0021 | Recover real retained work or a labelled case; verify custody release/recovery and actual enforcement where applicable. |

PRD §2.2 is covered by SOW-0001–0026; §2.3 boundaries by SOW-0002/0012/0016,
SOW-0025 and SOW-0027–0032. Section 5 is preserved in this candidate's pending
acceptance, SOW-0003/0026/0032 and the absence of new platform/schema decisions.
Section 6's source conditions, method order and future locality convention are
preserved in §§1/4/6 here and SOW-0009–0015/0020/0026/0033. The already executed
§6.3 step 2 is retained as history, not reassigned future transition work.

## 6. Interpretation choices, open matters and stage boundary

These distinguish preparation interpretations from the owner's output-form
clarification. They are not acceptance of the complete normalized basis.

| Ref | Treatment and warrant | Consequence / next authority |
|---|---|---|
| I-01 | PROPOSAL: retain one OBJ alias for each O outcome and let scope items support several objectives. PRD §2.1 explicitly permits many-to-many contribution. | Owner confirms/corrects with the Group 1 basis. No package geometry implied. |
| I-02 | PROPOSAL: scope units describe separately assessable capabilities/constraints; their related steps and necessary qualifications stay together. R04 operations are explicitly covered without requiring one workflow or deliverable per row. | Agent 0 reviewed atomicity/coverage; Group 2 later decides cohesive contributions. |
| I-03 | FACT: source reset is already integrated in the declared base; current tracked execution contains only LOOP_INIT.md. SOW-0026 preserves the constraint/history, not a second removal assignment. PRD §6.3 and current entry/recovery reference. | Keep original source identities; no imported historical tasks or lifecycle state. Archive file contents were not re-audited here. |
| I-04 | Stage interpretation: package accountability and deliverable coverage apply when Group 2 structure exists. The method places normalized scope/objectives at Group 1 and package assignment at Group 2. | Later fields are explicitly not applicable here. This candidate is not a fully valid final decomposition; no fabricated IDs or “zero gaps” verdict. |
| I-05 | Authority resolved by explicit steering: Agent 0 coordinates and reviews the Type 2 contribution despite usual WORKING_ITEMS metadata. Current PRD/AGENTS and assignment require ScopeOfWork.md, deliverable.yaml and Work/. | No new authority conflict needs owner ruling; no role/instruction edits or legacy scaffold adoption. |
| I-06 | OWNER-CONFIRMED: anticipated outputs are instructions, descriptive/explanatory material and executable tools (§2.1). Publications and execution can contain these forms; a maintained revision is a valid output. | Group 2 uses this distinction when defining concrete artifact kinds. It adds no scope item, package, deliverable or mandatory tooling. |
| Q-01 | RESERVED DISPOSITION — SOW-0032. PRD §5 retains plans/, _DomainEngines/ and other removals pending specific disposition. No such removal is needed for this basis. | Owner decision needed only before including additional archival changes. Default for this candidate: retain; Group 1 can proceed with the reservation explicit. |
| Q-02 | CONDITIONAL SCOPE — SOW-0033. Whether a selected need demonstrates a gap justifying bespoke tooling remains unknown. PRD R17, §6.1. | Do not promise a companion/adapter or its availability. Later bounded investigation may resolve fit within accepted scope; a new commitment or expanded scope returns to the owner. No platform decision is needed now. |

No conflicting accepted product claims were identified in this bounded reading.
No additional product assumption is needed to draft the basis. Existing holdings
are not presumed complete, broken or absent: classify each affected area during
authorized work using evidence. The absence of a consumer contract selection at
Group 1 is an input-selection limit, not evidence that a contract is unavailable.

The pending owner matter now is confirmation/correction of **this entire Group 1
basis**. Agent 0's review found no substantive correction needed. Q-01 remains
reserved; Q-02 can remain contingent. Later Package/Deliverable
design, setup, ScopeOfWork/dependency authoring, independent final decomposition
audit and implementation/product acceptance are outside this preparation.

## 7. Coverage telemetry and candidate checks

| Field | Group 1 value |
|---|---|
| Revision | G1-candidate-3, 2026-10-31 |
| ScopeItemCount | 33: 26 IN, 5 OUT, 2 TBD |
| ObjectiveCount | 5 proposed, each with accepted O mapping and IN scope support |
| PackageCount / DeliverableCount | 0 / 0 proposed; structure not yet applicable |
| UnassignedScopeItems | 33; assignment deferred to Group 2, not a final-stage pass |
| ScopeItemsWithoutDeliverableMapping | 26 IN items; mapping deferred to Group 2 |
| UnmappedObjectives | 5 without deliverables (Group 2); 0 without source O mapping or supporting IN scope |
| OpenIssuesByType | Reserved disposition: 1 (Q-01, SOW-0032); conditional implementation scope: 1 (Q-02, SOW-0033). No identified source conflict. |
| Source coverage | O1–O5, R01–R17 including all eight R04 operations, A1–A8 and PRD §§2/5/6 represented; not implementation evidence |

Candidate checks are scoped to the authored document and declared source basis:

- Source identity: HEAD and the PRD, entry, AGENTS, TASK role and selected workflow
  package bytes match the declared base. PRD SHA-256 matches the supplied hash.
  Archive tag resolves to the recovery reference's stated commit. Historical
  archive contents and original consumer pins were not reverified in this stage.
- In-memory structural checks: 33 unique scope IDs, valid classifications and
  counts, five unique objective IDs with one-to-one O1–O5 mappings and supporting
  IN scope; all referenced SOW/OBJ IDs resolve; source references are present;
  all 17 R and eight A coverage rows exist. Local Markdown link targets resolve;
  no conflict markers or concrete Package/Deliverable IDs occur.
- Content review against the PRD: all eight R04 operations, §2 boundaries,
  §5 reservations and §6 input/order conditions are represented. Optional tooling,
  named-consumer evidence, independent authority, local use conditions and the
  executed reset retain their qualifications. Agent 0 independently compared
  the scope, vocabulary, objectives and coverage against the PRD and selected
  method, checked the source identities and structural mappings, and found no
  blocking findings. This does not substitute for the Group 3 independent final
  audit or the owner's Group 1 decision.
- Output-form refinement: Agent 0 checked the added vocabulary and §2.1 against
  the owner's clarification and PRD R02/R04–R13/R17. Scope ledger and objective
  proposals are unchanged; no specific artifact or structural allocation is
  asserted by the three forms.
- Public-content checks: the maintained credential scanner screened the
  candidate bytes with no findings. Agent 0 also used the maintained private-term
  scanner with its local host-term source: three patterns, no findings, with no
  private terms printed. The configured hosted `PRIVATE_TERMS` set is unavailable
  locally and remains a required integration check. No Git-range/commit-metadata
  pass is claimed for this uncommitted candidate.

Checks run without changing validators, staging files or creating test artifacts.

The existing validate_decomposition_registers.py XRG checker expects later
Deliverables.csv/ScopeLedger.csv cross-register mappings; with this inline Group 1
candidate it would skip its checks. The DOMAIN checker addresses a different
variant. Neither is used to claim a Group 1 pass. Package coverage, ID coupling,
discipline/type/artifact structure, responsibility and deliverable-objective
mapping checks are Group 2 work; independent final audit is Group 3 work.
The deliverables CLI's structural check applies after setup and cannot establish
input suitability or acceptance. No validator was weakened or given fabricated
registers/values; no product behavior or consumer interface was exercised here.

## 8. Working-package inventory

`execution/_Decomposition/PROJECT_DECOMP.md` is the sole canonical **candidate**
working surface. Its inline ledger, objective mapping, vocabulary, coverage and
open matters are maintained here without duplicate companion tables. There are no
companion registers, derivative publication bundles, dependency registers,
accepted amendments, snapshots or pointers in this Group 1 output. It is retained
for the owner's Group 1 checkpoint, not downstream setup use.
