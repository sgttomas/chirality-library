# Chirality Library — Group 2 decomposition candidate

**Status:** Working reconciliation of the owner's approved Group 2 directions;
reviewed by Agent 0 for fidelity and ready for decision/snapshot binding.
No Group 3 audit or final decomposition acceptance is claimed.
**Revision:** G2-candidate-6, 2026-10-31. Agent 0 review annotations on the
approved PKG-04 reframing and DEL-05-02 removal; scope allocations unchanged.
**Method origin:** `chirality-root:bundled:workflow:project-decomp`.

Five flat Packages and seven Deliverables express the approved structural
direction: library access, maintenance practice/shared meaning, executable
support, self-monitoring and reflective improvement, and independent reuse and
publication. PKG-01/02/03/05 concern holdings and their maintenance; PKG-04
contributes their reconciliation and examination of the practice. The three accepted output forms guide concrete artifact kinds;
they do not determine the partition. A checked revision of an existing holding
can supply the result. No new companion, universal tool or global graph is proposed.

## 1. Accepted basis and current authority

The owner said: **“I approve this normalized scope, vocabulary and objective
basis.”** Agent 0 recorded that decision in the immutable Group 1 snapshot.
This author resolved [_LATEST_GROUP1.md](_LATEST_GROUP1.md), read the
[decision](checkpoint_snapshots/GROUP1-20261031T231127Z/DECISION.md),
[manifest](checkpoint_snapshots/GROUP1-20261031T231127Z/ACCEPTED_MANIFEST.csv)
and [handoff](checkpoint_snapshots/GROUP1-20261031T231127Z/HANDOFF_STATE.md), and
verified all three manifest entries before using the
[accepted payload](checkpoint_snapshots/GROUP1-20261031T231127Z/PROJECT_DECOMP.md).

| Basis | Identity / use |
|---|---|
| Accepted Group 1 | `GROUP1-20261031T231127Z`; payload SHA-256 `dd80227079e29e65a73da4c1650295aeb6e65f45940427bf0b698b6a5e1edddd`. DECISION.md supplies acceptance; submitted proposal wording in the snapshot is historical. |
| Accepted product intent | [docs/PRD.md](../../docs/PRD.md), revision 2026-10-31, SHA-256 `95c3c25ee36d4d4ddadf54d266a47a2ee58c6b37fbbdef75ad20a97986a718ca`, originally fixed at `d5ca6594ce6010c94c7981fe35cc540a822e9aa8`. |
| Current inspection basis | `6865c6eaeed2bbf6b87f96ec45da18d837c6eb7b`, branch `codex/library-decomposition-20261031`, incorporating the merged repair. Affected §6 observations are refreshed against this basis; unchanged observations reuse the earlier inspection at `cd81b47b6ba1a29a606caec3d1be691f4691c4e7`. No global census. |
| Reused repair basis | [PR #1779](https://github.com/sgttomas/chirality/pull/1779), merge `a052783460f60c76e6fa229500f59a51f67c5265`; final checked head `a0bb0dc77a53b041262571f658f9fd9590d44269`. Source inspection and reused verification are distinguished in §6.1. |
| Selected method | [Workflow](../../workflows/project-decomp/WORKFLOW.md), [contract](../../workflows/project-decomp/resources/contract.md), [Group 2 method](../../workflows/project-decomp/resources/method.md). Same bytes as the original Group 1 method basis. |
| Authority and entry | [AGENTS.md](../../AGENTS.md), [TASK](../../agents/AGENT_TASK.md), [Root entry](../_Coordination/LOOP_INIT.md), and this assignment. Owner steering retains Agent 0 coordination/review and this directly managed Type 2 author; no Type 1 layer is introduced. |
| Historical transition | PR #1778; [recovery route](../../projects/FROZEN.md#pre-library-root-execution); tag `archive/pre-library-execution-2026-10-31` at `f80f1510fb50799764720303b86c36da64b75d19`. Reset already executed; retention only, no repeated removal job. |

The accepted snapshot's relative links resolve from its original source path,
`execution/_Decomposition/PROJECT_DECOMP.md`, at its recorded basis. Group 1's
33 scope statements/classifications, five objective meanings and qualifications
remain unchanged. The latest direction changes Group 2 allocation and clarifies
organization; it does not amend the PRD or rewrite snapshot history.

### 1.1 Owner direction applied in this revision

The owner discussed PKG-04 as Chirality's self-monitoring contribution, with
reflective judgment exercised through human–Agent 0 dialogue. They approved
“Self-monitoring and reflective improvement”, with “Library reconciliation” and
“Reflective review of the practice”, and removal of the separate edition/change
information Deliverable. The discussion concluded: **“Approved. Proceed
accordingly.”** These decisions are supplied by the conversation/assignment,
not inferred from a merge or authored as an approval by this preparer.

Agent 0 has reviewed this translation of the approved direction and found no
material discrepancy. The decision record will bind the resulting representation
without claiming the owner inspected its hash before approving the structure.
Agent 0 records the decision and then commissions the separate Group 3 audit.
No snapshot, pointer, live locality, contract, need declaration, release or final
acceptance is created by this authoring continuation.

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
| Scope item / SSOW | Normalized atomic scope / structured scope | One independently classifiable commitment or boundary, with stable SOW identity and source warrant. This SSOW was accepted at Group 1. Selected contract, PRD §6.2. |
| Objective | Success condition, product outcome | Testable intended improvement. Accepted OBJ identifiers map to accepted O references; they do not replace or amend them. PRD §2.1, §6.2. |
| Deliverable / local goal | Bounded contribution | A meaningful intended improvement, scope, outputs and evaluative evidence connected to product objectives. A directory, activity or requirement alone is not a deliverable. R07. No deliverables were defined at Group 1; §8 now proposes them. |
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

### 2.1 Accepted output forms

The owner-confirmed distinction guides what the proposed deliverables produce:

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

Group 2 defines concrete artifact kinds and bounded deliverables from scope,
objectives and semantic coupling. It may identify a closely connected set of
outputs where the result requires one, such as a tool and its necessary usage
instructions. This does not prescribe three packages, one deliverable per form,
or an output of every form for each goal. A revised existing holding can be the
complete output; no new document, program or companion is required merely to
populate the structure. Conditional tooling remains subject to SOW-0033.

### 2.2 Owner clarification of organization and reflection

| Term | Meaning in this structural direction |
|---|---|
| Package | Enduring project organization/accountable scope home; not an episode or a required management tier. |
| Deliverable | Bounded production commitment with maintained outputs and evaluative evidence; subsequent maintenance uses that basis without making one task or meeting an everlasting Deliverable. |
| Undertaking | A purposeful authorized episode that realizes or revises contributions; decomposition and setup are formation undertakings. |
| Task | A bounded Type 2 assignment within an undertaking; it does not delegate or replace a local goal. |
| Workflow | A reusable method used by an undertaking. Coordinated knowledge work supplies realization/integration practice across contributions; it is not itself an execution undertaking. |
| Self-monitoring and reflection | Bounded comparison of work with purpose, evidence and commitments, and human–Agent 0 examination of whether that comparison, its goals and framing remain useful. Human judgment bounds this examination; no further monitoring hierarchy is required. |
| Repository-maintained execution | Descriptions and commitments of Root's actual work, maintained using library methods and inspectable as self-monitoring sources. They are not automatically reusable content that consumers inherit; no export of all local records or transfer of Root authority follows. |

These distinctions clarify the accepted vocabulary; no accepted normalized scope
statement is changed. Initial formation still supplies the actual decomposition
and localities required by R07–R10 (§8.1). Instructions and descriptive/explanatory
material support reflection; dialogue is an activity, not a required report stream.
Other projects may later adopt matured practice under their own authority; this
structure commissions no rollout.

## 3. Accepted objectives

The five OBJ identities retain the five accepted O outcomes and their evaluative
meaning. Their statements and PRD mappings below are unchanged from Group 1.
Proposed `MappedDeliverables` are derived from §4 and shown in §9. Evaluation
remains future work; structural mapping is not evidence of satisfaction.

| ObjectiveID | Statement / testable outcome | PRD mapping | Evaluative basis (future evidence, not a present pass) |
|---|---|---|---|
| OBJ-001 | A maintainer entering with a bounded undertaking can locate the applicable holdings, instructions, source basis, execution work and unresolved conditions. | O1 | A1; A5's maintenance of the entry. Test purposeful discovery and source distinctions without a global graph. |
| OBJ-002 | A maintainer can carry authorized changes, including changes to maintenance means, through preparation, verification, review, integration and recovery using usable library instructions and tools. | O2 | A2, A4, A5. An actual instruction/tool change and its reusable procedure must both be demonstrated; a walkthrough alone proves no executable behavior. |
| OBJ-003 | A scoped change leaves affected definitions, warranted claims, actions, values, publications and work coherent for their uses, or exposes a consequential unresolved conflict for owner disposition. | O3 | A4, A5, A7. Preserve earlier editions and scoped adopted contracts; a repair alone does not establish maintenance-method availability. |
| OBJ-004 | Accepted local goals support evidence-directed action, meaningful input/use conditions, evolving reasoning and coordinated integration within the wider product without a complete graph. | O4 | A3, A8. Demonstrate an actual condition and a finding that revises the route; continue unaffected work and inspect affected uses. |
| OBJ-005 | Independent consumers can obtain identified material, inspect consequential changes and choose adoption, while maintainers preserve history, prepare publication and recover retained work. | O5 | A6, A7, A8. Named-contract compatibility, publication preparation and recovery establish different claims; consumer adoption and owner release remain separate. |

## 4. Scope ledger reconciled to the owner direction

`IN`, `OUT` and `TBD` retain their accepted Group 1 meanings. Every scope item
has exactly one accountable Package home in this working translation. Only IN items receive
production Deliverable allocation. A Package home for an exclusion/reservation
makes its boundary accountable; it does not activate that scope. SOW-0026 maps
only to preservation of the completed transition's source/recovery conditions.

The first four columns, objective mapping and substantive qualifications are
unchanged from the accepted basis. SourceRef refers to the PRD unless another
source is named. The SOW-0011 note is refreshed solely for checkpoint standing.
This table is the canonical scope-to-Package/Deliverable mapping. Deliverable
cards and §9 summarize it for review and must agree with it.

| ScopeItemID | InOutStatus | ScopeItemStatement and qualifications | SourceRef | PackageID | DeliverableID(s) | ObjectiveID(s) | OpenIssue / notes |
|---|---|---|---|---|---|---|---|
| SOW-0001 | IN | Maintain a locatable starting route from a bounded undertaking to the selected basis, applicable role/repository instructions, relevant holdings and execution. Initialization selects no undertaking; the entry is itself maintainable. | R01; O1; A1, A5; §6.1 | PKG-01 | DEL-01-01_library-discovery-guide | OBJ-001, OBJ-002 | FALSE. Current entry is an input, not evidence of full A1 satisfaction. |
| SOW-0002 | IN | Make holdings locally intelligible and searchable through purpose, applicability, standing, resources, outputs and limits; distinguish explanation, instruction, example, proposal and history, preserving resources/notices when copied. Principles and publications retain maintained source homes. | R02; §1; §2.3; A1, A6 | PKG-01 | DEL-01-01_library-discovery-guide | OBJ-001, OBJ-003, OBJ-005 | FALSE. Categories remain with the material; no new central registry. |
| SOW-0003 | IN | Support purposeful search, reference following and structured queries with source identity, declared/inferred/unknown relationships and search limits visible. Retain or deliberately migrate consumed indexes, checking/regenerating from owning sources; read selected material. | R03; §5; A1 | PKG-01 | DEL-01-01_library-discovery-guide | OBJ-001, OBJ-003, OBJ-005 | FALSE. Views may be incomplete, cyclic and revised. |
| SOW-0004 | IN | Provide usable maintenance instructions for adding or revising holdings with purpose, scope, destination, relevant material, source identity and checks. Reuse/connect applicable methods rather than prescribe a new method per operation. | R04, “Add or revise a holding”; §2.2; A2 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002 | FALSE. Classify affected existing means as usable, needing connection/repair or absent during bounded work. |
| SOW-0005 | IN | Support organization, relocation or retirement using actual references/consumers, replacement or historical standing, recovery and deletion authority. | R04, “Organize, relocate or retire”; §5 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-003, OBJ-005 | FALSE. Specific archival removals beyond the completed reset remain SOW-0032. |
| SOW-0006 | IN | Support diagnosis and reconciliation of conflicting claims, source meaning and observed behavior, identifying the owning material, evidence and repair scope. | R04, “Diagnose and reconcile”; R11; A4 | PKG-04 | DEL-04-01_library-reconciliation | OBJ-002, OBJ-003 | FALSE. Reusable procedure and its result are distinct obligations. |
| SOW-0007 | IN | Support assessment of connected changes across relevant inputs, uses and consequences in instructions, tools, publications and execution, bounded by the authorized undertaking. | R04, “Assess connected change”; R11; §2.2 | PKG-04 | DEL-04-01_library-reconciliation | OBJ-002, OBJ-003 | FALSE. Discovery of further consequences does not silently expand commitments. |
| SOW-0008 | IN | Support review and integration with proportionate scrutiny, the actual checked revision, findings, updates to owning text and the repository change procedure. | R04, “Review and integrate”; R12; R14; A2 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-003 | FALSE. Root's grant does not transfer through library consumption. |
| SOW-0009 | IN | Align tool-use instructions with actual commands/interfaces, dependencies, outputs, write effects, failure behavior and limits. Use available selected-library tools for repeatable operations; state unavailable capabilities and permitted fallbacks, repairing necessary reusable procedure at its source. | R05; R17; §6.1; A2 | PKG-03 | DEL-03-01_maintenance-toolkit | OBJ-002 | FALSE. Existing deliverables CLI requires Git, HEAD and declared dependencies; file-only/namespace adapters are not assumed. |
| SOW-0010 | IN | Maintain entry, roles, methods, tools and execution under the existing authorized basis; review replacement means, preserve the usable preceding basis and adopt only after verification with actual authority. | R06; R04, “Change the maintenance means”; A5 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-001, OBJ-002, OBJ-003 | FALSE. Proposed instructions do not authorize themselves or alter their own review basis. |
| SOW-0011 | IN | Establish an accepted decomposition of bounded contributions with meaningful intended improvements, scope, outputs and evaluative evidence mapped to product objectives, without directory/requirement-driven partitioning or conflicting change ownership. | R07; §2.2; §6.2–6.3; A3 | PKG-04 | DEL-04-02_reflective-review | OBJ-001, OBJ-002, OBJ-004 | FALSE. Group 1 basis accepted; approved Group 2 direction is translated here, awaiting Agent 0 fidelity review and snapshot binding; independent final audit and decomposition acceptance remain outstanding. |
| SOW-0012 | IN | Set up accepted localities using the library's applicable tools: ScopeOfWork.md for goal, accepted scope/objective references, outputs, boundaries, acceptance criteria and verification; deliverable.yaml for actual needs/conditions and useful source/code/check pointers; Work/ for reasoning, evidence, alternatives, consequential attempts, unresolved conditions and local outputs with maturity explicit. | R08; §6.2–6.3; A3, A8 | PKG-04 | DEL-04-01_library-reconciliation | OBJ-001, OBJ-002, OBJ-004 | FALSE. Future execution/PKG-nn/DEL-nn-nn/ only after accepted scope; maintained outputs retain source homes and unchanged declarations stay unchanged. |
| SOW-0013 | IN | Author consumer-local needs after scope exists, identifying input, intended use/condition, trigger/case and source or unresolved binding. Preserve distinct conditions, preliminary/final use, reciprocal relations and technical holds; judge suitability from evidence. | R09; §6.1–6.2; A3 | PKG-04 | DEL-04-01_library-reconciliation | OBJ-004 | FALSE. No inferred supplier commitments or whole-deliverable finish-to-start constraints; presence, merge and structural checks do not establish suitability. |
| SOW-0014 | IN | Support authorized local action from goals, evidence and actual input conditions, revising understanding/routes and neighborhoods as findings emerge, continuing unaffected work and checking affected uses with one integration owner. | R10; A3; §4 closing paragraphs | PKG-04 | DEL-04-01_library-reconciliation, DEL-04-02_reflective-review | OBJ-002, OBJ-003, OBJ-004 | FALSE. Commitment/acceptance changes and reserved decisions return to the owner; local completion must serve the product. |
| SOW-0015 | IN | Derive relationship queries and undertaking-specific views from owning declarations, reporting basis, scope, unknowns and partial coverage while preserving actual live-metadata selection and project-root reference semantics. | R03; R10; §6.1–6.2 | PKG-03 | DEL-03-01_maintenance-toolkit | OBJ-001, OBJ-004 | FALSE. No second manual progress graph or required global DAG. |
| SOW-0016 | IN | Reconcile affected definitions/relationships, warranted claims, actions and values together, recording consequential reasoning in owning work and reconciling affected guidance/publications or identifying an edition's earlier basis. Preserve historical identities and scoped adopted contracts. | R11; §2.3; A4, A5 | PKG-02 | DEL-02-02_shared-meaning-reference | OBJ-002, OBJ-003 | FALSE. Four perspectives do not require four reports/approvals; library definitions remain distinct from product runtime enforcement. |
| SOW-0017 | IN | Verify the actual candidate proportionately and distinguish content, behavior and consumer-interface claims. Numerical meaning, persistence, permissions and destructive changes require focused regression checks and independent scrutiny; reuse applicable evidence and expose missing evidence as unverified. | R12; §4; A2, A4–A6 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-003, OBJ-004 | FALSE. Applicable checks attach to actual future changes, not a blanket product-verification run in this stage. |
| SOW-0018 | IN | Make unfinished work recoverable from its locality and review record: source basis, usable result, checks, unresolved conditions and next needed action. Add at most one replaceable recovery note only if needed. | R12; R04, “Recover or continue”; A8 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-004, OBJ-005 | FALSE. A labelled recovery case is allowed by A8; past records create no new authority or standing backlog. |
| SOW-0019 | IN | Provide independent paths to consult, invoke or copy identified material through ordinary files, Git, archives and documented interfaces, retaining resources/licenses/source basis and distinguishing local adaptations. | R13; R17; A6 | PKG-05 | DEL-05-01_consumer-use-guide | OBJ-005 | FALSE. Reading the library does not require Git; executable tools declare their own dependencies. |
| SOW-0020 | IN | Check affected named consumer interfaces at an explicit maintained-contract/fixture revision and supply a supported path or coordinated adapter before incompatible change. | R13; §2.2–2.3; §6.1; A6 | PKG-05 | DEL-05-01_consumer-use-guide | OBJ-003, OBJ-005 | FALSE. Needed input: affected named contract/fixtures at a specified basis, used when an interface change is selected; concrete selection unresolved until that scope is defined. Private evidence stays local; adoption/release are independent. |
| SOW-0021 | IN | Support exceptional exclusive custody through an existing lock/coordination mechanism stating holder, item, reserved operation and release/recovery condition with honest enforcement limits; resolve interruption through the authorized maintainer. | R14; A8 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-005 | FALSE. Readers normally retain checked-in material; elapsed time never authorizes disposal. No new lock service is prescribed. |
| SOW-0022 | IN | Prepare named publication candidates from verified revisions with source identity, notices, dependencies, limitations and recoverable commit/edition routes; preserve owner publication authority and independent consumer adoption. | R15; R04, “Prepare publication and inspect updates”; A7 | PKG-05 | DEL-05-01_consumer-use-guide | OBJ-003, OBJ-005 | FALSE. Named publications are downstream default; explicitly following main is development. A merge is not release. Actual release is not this task's work. |
| SOW-0023 | IN | Explain consequential old/new basis, reason, meaning/use and migration effects in existing review/publication notes, and exercise polling/inspection via existing release/diff facilities. | R16; R04, “Prepare publication and inspect updates”; A7 | PKG-05 | DEL-05-01_consumer-use-guide | OBJ-003, OBJ-005 | FALSE. Interests stay local; examined is not adopted; partial/failed checks do not prove no change. Scheduling, delivery and unattended operation require actual configuration/authority; no new notice register. |
| SOW-0024 | IN | Preserve standalone repository use and existing Git/search/review/release/validation/scheduling foundations, classifying affected capabilities as usable, needing connection/repair or absent and implementing only necessary changes. | §1; §2.2; R17 | PKG-03 | DEL-03-01_maintenance-toolkit | OBJ-001, OBJ-002, OBJ-005 | FALSE. Optional bespoke tooling remains conditional under SOW-0033; no permanent capability census. |
| SOW-0025 | IN | Keep ordinary library use independent of undisclosed sibling checkouts, dated run directories, private inputs and credentials; use cleared public fixtures/summaries and required credential/private-term checks for public changes. | R17; §2.3; §6.3; A6, A7 | PKG-05 | DEL-05-01_consumer-use-guide | OBJ-002, OBJ-005 | FALSE. Private consumer inventory need not be read for this stage. |
| SOW-0026 | IN | Preserve traceability and recoverability of the authorized pre-library execution transition and original consumer-pinned history, including the App's historical SWBPIPE source bytes, without reinstating prior structure, commitments or lifecycle state. | §2.2; §5; §6.1, §6.3 step 2; R12, R15 | PKG-05 | DEL-05-01_consumer-use-guide | OBJ-003, OBJ-005 | FALSE. Transition already executed in PR #1778; archive identity verified here. Retention is the ongoing constraint; no repeat removal or migrated backlog. Selected archive bytes must be verified before future reliance. |
| SOW-0027 | OUT | Require a new App, agent runtime, hosted service or compulsory companion as the library product or a prerequisite for repository use. | §1; §2.3; R17 | PKG-03 |  | OBJ-001, OBJ-002, OBJ-005 | FALSE. Optional, justified thin support is distinct; see SOW-0033. |
| SOW-0028 | OUT | Establish a standing global audit, central relationship graph, subscriber/notice registry, automated project management or a complete DAG/global census requirement. | §2.3; R03, R10, R16 | PKG-01 |  | OBJ-001, OBJ-004, OBJ-005 | FALSE. Existing consumed indexes and bounded derived views remain in scope. |
| SOW-0029 | OUT | Transfer Root grants, execution authority or runtime policy to consumers, perform independent consumer product work, or require their production adoption/release to accept a verified library interface. | §2.3; R11, R13, R15 | PKG-05 |  | OBJ-003, OBJ-005 | FALSE. App v4 and SWBPIPE remain independent; coordination conveys no owner authority. |
| SOW-0030 | OUT | Reactivate, develop or verify frozen App v3, Runtime or PEC through decomposition, recovery or library maintenance. | §2.3; §6.3; AGENTS.md | PKG-02 |  | OBJ-003, OBJ-005 | FALSE. Explicit reactivation would be a separate authorized change. |
| SOW-0031 | OUT | Publish private knowledge, consumer operational data or credentials in library artifacts, examples or fixtures. | §2.3; R17; §6.3 | PKG-05 |  | OBJ-005 | FALSE. Cleared public evidence may support compatibility claims; generic evidence cannot establish named-consumer compatibility. |
| SOW-0032 | TBD | Further archival disposition of plans/, _DomainEngines/ and additional removals, if specifically authorized. | §2.3; §5 | PKG-02 |  | OBJ-003, OBJ-005 | TRUE — Q-01. Retain pending specific owner disposition; historical classification alone authorizes no deletion. No writes there in this undertaking. |
| SOW-0033 | TBD | Add bespoke tooling or a thin companion, including a file-only query interface or namespace adapter, only where a selected consumer/maintenance need demonstrates a gap in existing means. | §1; R17; §6.1 | PKG-03 |  | OBJ-002, OBJ-004, OBJ-005 | TRUE — Q-02. No gap or implementation selected here; neither availability nor a new product commitment is assumed. |

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
SOW-0025 and SOW-0027–0032. Section 5 is preserved in the Group 2 decision binding
still to be recorded, SOW-0003/0026/0032 and the absence of new platform/schema decisions.
Section 6's source conditions, method order and future locality convention are
preserved in §§1/4/8 here and SOW-0009–0015/0020/0026/0033. The already executed
§6.3 step 2 is retained as history, not reassigned future transition work.

## 6. Representative holdings and bounded findings

These source inspections distinguish available means, bounded completed repair
and remaining connection or evaluation needs. No whole Deliverable is declared
complete. Existing good material and applicable repair evidence are reused;
“not established” below is not a claim that nothing exists elsewhere. No private
consumer repository, historical execution backlog or frozen product was opened.

| Observed source at current basis | What exists / what needs connecting or repairing | Proposed contribution |
|---|---|---|
| [README](../../README.md), Root entry, [workflow guide](../../workflows/README.md) | Entry links already distinguish the library, independent projects and frozen recovery. Workflow source identity, selected-resource loading and generated indexes are documented. Connect these routes to the accepted local execution and a bounded worked discovery route; no new universal catalog. | DEL-01-01_library-discovery-guide |
| [create-workflow](../../workflows/create-workflow/WORKFLOW.md), [change](../../workflows/change/WORKFLOW.md), [Root change skill](../../.agents/skills/chirality-change/SKILL.md), [bounded-reconciliation](../../workflows/bounded-reconciliation/WORKFLOW.md), [coordinated-knowledge-work](../../workflows/coordinated-knowledge-work/WORKFLOW.md) | Reusable authoring, review/integration and recovery practices exist. PR #1779 aligns AGENTS, bounded-reconciliation and package activation: the implementation owner reconciles concrete results/evidence with affected ScopeOfWork, Work and needs in the same PR; Agent 0 checks agreement. Revise changed meaning and connect genuinely new work; preserve unchanged declarations/history. DEL-04-01_library-reconciliation owns that practice; DEL-02-01_maintenance-procedures invokes it while establishing the remaining maintenance-operation coverage and R14 custody case. The inspected route does not yet demonstrate a complete custody or library update-inspection procedure. | DEL-02-01_maintenance-procedures; consumer update inspection belongs to DEL-05-01_consumer-use-guide |
| [runtime reference](../../docs/AGENT_WORKFLOW_RUNTIME.md), [boundaries](../../docs/PRODUCT_BOUNDARIES.md), [compatibility reference](../../docs/COMPATIBILITY_FORMATS.md) | Existing scoped/historical contracts coexist with statements such as “The Runtime project owns production discovery” and project methods “cannot weaken Root governance.” Their intended applicability needs explicit comparison with independent adoption and frozen Runtime standing; do not erase adopted contracts. | DEL-02-02_shared-meaning-reference; scoped applicability reconciliation, not a runtime redesign |
| [thesis architecture §4.2](../../docs/thesis/04_architecture.md), [manual entry](../../docs/alignment-manual/README.md) and its current v9 source's vocabulary/recovery/edition passages | Explanations already describe local conditions, derived views, current source homes, recoverability and edition identity. Reuse these as explanatory basis; reconcile only claims affected by the selected boundary/setup changes. A whole thesis/manual/course rewrite is not evidenced. | DEL-02-02_shared-meaning-reference; DEL-01-01_library-discovery-guide links the current editions |
| [setup](../../workflows/project-setup/WORKFLOW.md) and [current route](../../workflows/project-setup/resources/current-project.md), [preparation](../../.agents/skills/preparation/SKILL.md) and [scaffold contract](../../.agents/skills/preparation/references/scaffold-contract.md), [current helper](../../tools/scaffolding/current_locality.py) and shell entrypoints | F-01's current-route mismatch is repaired. Explicit `--current` calls create numeric PKG/DEL paths, Work/ and YAML with accepted id/name and empty needs; no blank ScopeOfWork or legacy control files. [Fileset check](../../tools/validation/check_min_viable_fileset.sh) with `--current --prepared` checks pre-authoring structure; without `--prepared`, it also requires matching ScopeOfWork frontmatter. Full contract validity uses the existing ScopeOfWork validator. Unflagged historical calls and explicitly selected legacy/domain contracts remain separate. No routine current setup log/receipt/handoff is required. | DEL-03-01_maintenance-toolkit and DEL-02-01_maintenance-procedures reuse the implemented means and §6.1 evidence; initial formation (§8.1) still requires accepted scope, authorized live setup and authored content; this does not hold unaffected reconciliation work |
| [scope-of-work](../../workflows/scope-of-work/WORKFLOW.md) and [tool policy](../../workflows/scope-of-work/resources/tools.md) | Current INIT/VERIFY now explicitly work without `_STATUS.md` or a legacy kit; absent status remains absent and present status is preserved. Ordinary authorized factual reconciliation uses bounded-reconciliation before integration. Formal REVISE/CONVERT retain their selected amendment/lifecycle/source rules; no status act belongs to this workflow. Routine current INIT/VERIFY receipts are removed. | Reuse the applicable authoring/validation route in DEL-04-01_library-reconciliation; broader procedure and tool evaluation remain with DEL-02-01_maintenance-procedures and DEL-03-01_maintenance-toolkit |
| [deliverables guide](../../tools/deliverables/README.md) and [loader](../../tools/deliverables/cli.py) `load`, [local graph method](../../workflows/construct-local-work-graph/WORKFLOW.md), [need authoring](../../workflows/dependency-extract/WORKFLOW.md) | Consumer-local conditions, Git/HEAD/PyYAML requirements, working-file discovery and project-root path semantics already exist. Loader walks live deliverable.yaml files and verifies local identity; views remain derived and do not judge suitability. Reuse and verify on adopted localities before proposing repairs. | DEL-03-01_maintenance-toolkit; DEL-04-01_library-reconciliation |
| [workflow utility guide](../../tools/workflow_runtime/README.md), [manual rendering route](../../docs/alignment-manual/README.md#read-and-render), [LICENSE](../../LICENSE.md), recovery reference | Identified method resources, explicit host enforcement limits, source-derived publication rendering, notices and recovery routes exist. General library acquisition, selected-consumer qualification and polling need a joined usable path; their end-to-end sufficiency was not exercised here. | DEL-05-01_consumer-use-guide |

[HELP_HUMAN](../../agents/AGENT_HELP_HUMAN.md) already requires attention to
purpose, changed questions, current commitments and continuity through the
conversation and authoritative artifacts. [Coordinated knowledge work](../../workflows/coordinated-knowledge-work/WORKFLOW.md)
examines premises and combined results, diagnoses waiting before adding mechanisms,
and returns consequential framing choices to the human. These are the existing
homes to reuse for DEL-04-02_reflective-review; the direction does not evidence a
need for another manual, monitoring service or routine review ceremony.

### 6.1 Repair evidence available for reuse

[PR #1779](https://github.com/sgttomas/chirality/pull/1779) supplies an actual
maintenance change, not an unperformed build requirement. The author inspected
the affected current instructions, current_locality.py, wrapper selection and
ScopeOfWork changes, verified their identity against the repair, and confirmed
that merge `a052783460f60c76e6fa229500f59a51f67c5265` has the same tree as final
checked head `a0bb0dc77a53b041262571f658f9fd9590d44269`.

Agent 0 supplied the verification account: 1382 selected-tool tests passed, five
historical-source skips and one pre-existing pytest warning; required hosted
harness/Repository checks passed on the final head. Independent Type 2 review of
`64ebc86b5e961128ea00e8ac11491e9ea04c4eaa` found no blockers and independently
exercised filesystem collision cases; the final head adds two nonblocking wording
repairs in the ScopeOfWork brief. These are reused reports, not tests rerun by
this author. Agent 0 also reported no blocking compatibility constraint from
SWBPIPE; that is not named-consumer qualification or adoption evidence for A6.

The material interpretation change is narrow: F-01 no longer requires building a
current setup path. Use the implemented path and its applicable evidence, assess
any remaining claim-specific gaps, and repair only a newly demonstrated mismatch.
The repair supports relevant portions of A2/A5; it does not establish all R04
operations, custody/recovery, live setup, actual local need suitability, complete
Deliverables or product acceptance. Final accepted decomposition and activation
scope are still required before live setup. The repair itself required no structural change; the later owner decisions in
§1.1 supply the reframing in this revision.

## 7. Packages under the approved direction

Five flat Packages remain. Each design Package declares one discipline; these
are contribution disciplines, not staffing tiers. The enduring organization is
separate from the bounded outputs below and from episodes that realize them.

| PackageID | Name / purpose | Discipline | Inclusion criteria and boundaries |
|---|---|---|---|
| PKG-01 | Library access — find and interpret the selected basis from a bounded undertaking | Information architecture | Entry/navigation, local intelligibility and purposeful discovery. Owns SOW-0028's no-central-census boundary. Does not implement query algorithms or rewrite every holding. |
| PKG-02 | Maintenance practice and shared meaning — make changes operable, coherent and recoverable | Knowledge engineering | Maintenance route and shared concept/applicability reference set. Invoke PKG-04's reconciliation practice as part of carrying a change through; do not duplicate ownership of it. Retain frozen-work and extra-removal boundaries. No tool implementation or global content audit. |
| PKG-03 | Executable maintenance support — make selected repeatable operations fit the current library contract | Software engineering | Existing selected scaffolding, validation, resolution/query utilities and direct usage instructions. Standalone-use and conditional-tooling boundaries remain. No new App/service, compulsory companion, consumer runtime or global query system. |
| PKG-04 | Self-monitoring and reflective improvement — reconcile holdings and examine whether the practice, goals and framing serve the work | Knowledge engineering | The actual same-PR reconciliation practice and its human-grounded examination/improvement. Account for initial decomposition/setup obligations in §8.1 while preserving each local owner's commitments and Work. No central control of other localities, global audit/graph, monitoring service, model loop, report stream or extra ceremony. |
| PKG-05 | Independent reuse and publication — make identified material usable, inspectable and recoverable by consumers | Technical publishing | Consumer/version/update guidance, named compatibility evidence, ordinary publication preparation and historical recovery. Git, PRs and release mechanisms carry version/change information; no separate edition/history product. Source publications remain maintained holdings. No imposed adoption, owner release act, consumer development or additional removals. |

PKG-01 concerns discovery within a selected basis; PKG-05 concerns obtaining and
inspecting identified material. PKG-02's maintenance route invokes PKG-04's
practice; it does not also own it. PKG-03 implements actual tool behavior.
PKG-04 serves the holdings and their local owners, with human judgment directing
and bounding reflection on the practice. This is not a three-form partition or a new hierarchy.

## 8. Deliverables and formation obligations

Seven bounded production commitments remain. Future contributor assignments are
**TBD**, made through Agent 0's actual briefs; Agent 0 retains integration and
human continuity. The reflective activity includes the human and Agent 0, but
that does not assign every future guidance edit to this Type 2 author.

Canonical suffix-bearing IDs retain their numeric identity. Future paths and
native bindings use numeric `execution/PKG-nn/DEL-nn-nn/` and DEL prefixes. No
localities or production files are created here. Concrete artifact sets may mix
instructions and descriptions, or tools with needed usage information; they do
not require all three output forms. Files, cases and repeated instances remain
artifacts within a coherent commitment.

### 8.1 Initial establishment remains required

SOW-0011–0014 / R07–R10 are still accountable to PKG-04. Their initial production
obligations are allocated with the practices they establish: SOW-0011 to
DEL-04-02_reflective-review; SOW-0012/0013 to DEL-04-01_library-reconciliation;
SOW-0014 to both, distinguishing local source reconciliation from examination of
goals/framing. This allocation does not replace the concrete formation outputs
with generic guidance or create a central owner of all execution material.

Agent 0 coordinates the current **decomposition undertaking** using project-decomp.
It must finish the actual normalized/structured design, applicable Group 2 decision
binding, separate Group 3 audit and final acceptance before downstream setup.
This working document and required accepted snapshots are real outputs of that
episode, retained at execution/_Decomposition/. They are not a permanent
“decomposition product” or a recursively commissioned project.

After final acceptance and selected activation authority, the **setup undertaking**
uses current project-setup, preparation, scope-of-work and dependency-extract.
It must materialize the selected accepted localities with real ScopeOfWork.md
contracts, deliverable.yaml needs/conditions and Work/ content with maturity
explicit. Accepted scope/objective links, outputs, boundaries, acceptance methods,
actual input/use conditions, unknown bindings and useful code/check pointers
remain required. Scope precedes needs. Use the repaired `--current`/`--prepared`
and authored structural checks, substantive contract validation and bounded query
checks; structural passes do not determine suitability. PR #1779 is reusable
supporting evidence, not proof that these localities exist or meet their goals.

The contributor responsible for each local goal owns its contract, Work and needs
through implementation and repairs. Coordinated-knowledge-work supplies the
realization/integration method where contributions combine; implementation owners
reconcile their actual results and verification in the same PR. PKG-04 accounts
for the practice and formation coverage, not a second copy of everyone's records.
Unchanged declarations remain unchanged. For A3, use accepted/set-up scope and an
actual authorized action with a meaningful condition, a finding that changes the
route or understanding, and examination of affected uses. Neither this structure
nor a synthetic fixture establishes that evidence.

### DEL-01-01_library-discovery-guide — A usable route into the selected library

- **ParentPackageID:** PKG-01. **Type:** Library navigation and discovery guide.
  **ResponsibleParty:** TBD — information architecture contributor.
- **Local goal:** Given a bounded maintenance brief, a maintainer can find the
  applicable holding, method, source standing, execution locality and unresolved
  conditions without treating an index or inferred relationship as authority.
- **CoversScopeItems:** SOW-0001, SOW-0002, SOW-0003.
  **SupportsObjectives:** OBJ-001, OBJ-002, OBJ-003, OBJ-005.
- **Anticipated artifacts:** A connected/revised entry and local navigation set
  in README.md, execution/_Coordination/LOOP_INIT.md and selected owning indexes;
  concise directed-search instructions and a bounded discovery example attached
  to that route. Include purpose/applicability/standing/resources/outputs/limits
  for the holdings actually traversed. Existing workflow and publication indexes
  stay at their homes and are regenerated only when their owning sources change.
  These are guide components, principally instructions and explanations.
- **Evaluation:** A1 walkthrough from an actual selected brief, checking source
  distinctions, search limits and required resources/notices. Establish separately
  whether any invoked command behaved as claimed; no complete-inventory claim.
- **Needed inputs / use conditions:** Before wiring a current-work link, consume
  the final accepted decomposition identities and actual usable localities from
  the formation undertakings (§8.1), at their recorded source basis; a proposed
  path alone cannot claim active work. For method discovery, consume
  workflows/README.md, catalog/index and selected package metadata/resources at
  the inspected revision (R01–R03). For publication links, resolve the edition at
  docs/alignment-manual/README.md or docs/thesis/README.md; pin it when a claim
  relies on exact content. Existing-entry work can proceed before new locality
  links become available.
- **Boundary:** This guide supplies navigation and provenance. The meaning of a
  disputed shared claim is reconciled by DEL-02-02_shared-meaning-reference;
  query behavior by DEL-03-01_maintenance-toolkit. It claims no consumer adoption.

### DEL-02-01_maintenance-procedures — Carry and recover an authorized holding change

- **ParentPackageID:** PKG-02. **Type:** Library maintenance procedure set.
  **ResponsibleParty:** TBD — maintenance-method contributor.
- **Local goal:** A maintainer can add/revise, organize/retire, diagnose, assess
  connected change, review/integrate and recover a holding, including its own
  maintenance means, using an available method with actual authority and evidence.
- **CoversScopeItems:** SOW-0004, SOW-0005, SOW-0008, SOW-0010, SOW-0017, SOW-0018, SOW-0021.
  **SupportsObjectives:** OBJ-001, OBJ-002, OBJ-003, OBJ-004, OBJ-005.
- **Anticipated artifacts:** Connected/revised applicable maintenance guidance at
  its existing homes, beginning with create-workflow, change and the Root change
  skill, including proportionate verification, unavailable-capability limits and
  exceptional custody/recovery using an existing mechanism with explicit holder,
  item, reserved operation, release/recovery conditions and enforcement limits.
  Invoke the reconciliation practice owned by DEL-04-01_library-reconciliation
  within carrying changes through; do not clone or separately own that procedure.
  Reuse coordinated-knowledge-work for realization across contributions and
  DEL-05-01_consumer-use-guide for version/publication/update guidance. PR #1779's
  repaired setup/ScopeOfWork instructions are available inputs, not new required
  builds. Further instruction changes need a demonstrated gap; no workflow per
  operation or separate reconciliation assessment stage.
- **Evaluation:** Reuse PR #1779's actual instruction/tool change and
  review/check evidence (§6.1) for the relevant A2/A5 claims under the preceding
  basis. Assess that evidence against each claim, including the available reusable
  procedure; do not declare all operational coverage or either criterion complete
  from the test count or merge. A8 still needs retained work or a labelled
  interrupted-custody case that tests recovery and the mechanism's limits. Keep
  adequate source/review evidence; do not create a routine case register.
- **Needed inputs / use conditions:** When a method directs a command, consume
  its verified command/dependency/write/failure contract from the selected existing
  tool source (R05–R06), with DEL-03-01_maintenance-toolkit accounting for remaining
  tool claims. For reconciliation during that change, use the actual maintained
  bounded-reconciliation basis owned by DEL-04-01_library-reconciliation; do not
  wait for a whole-Deliverable completion label or re-author the procedure here.
  The current setup/authoring path and actual maintenance case are
  now bound to PR #1779's final checked head and current instructions (§6.1), not
  an unknown future repair. Select additional cases only for claims the available
  evidence does not establish. For custody, use the actual repository/host
  coordination mechanism for the operation; specific holder/mechanism remain TBD,
  and no enforcement claim is permitted until examined (R14). For semantic repair
  use the scoped applicability basis of DEL-02-02_shared-meaning-reference;
  content disagreement cannot be resolved by replacing a check or applying
  proposed instructions to their own review.
- **Boundary:** The maintenance route invokes reconciliation; PKG-04 owns
  its practice and examination/improvement. PKG-03 supplies executable support.
  Implementation owners perform the actual same-PR source reconciliation; a
  shared-file change has one editor/integrator. This Deliverable does not duplicate
  bounded-reconciliation or HELP_HUMAN guidance, grant new permissions, reactivate
  frozen work or authorize extra removals.

### DEL-02-02_shared-meaning-reference — Make library and adopted-product meanings explicit

- **ParentPackageID:** PKG-02. **Type:** Shared concept and applicability reference set.
  **ResponsibleParty:** TBD — knowledge/reference contributor.
- **Local goal:** A maintainer or consumer can distinguish reusable library
  definitions and current Root practice from scoped adopted contracts, historical
  runtime policy and explanatory editions, and use the affected claims coherently.
- **CoversScopeItems:** SOW-0016.
  **SupportsObjectives:** OBJ-002, OBJ-003.
- **Anticipated artifacts:** Warranted revisions/qualifications in the affected
  sections of docs/AGENT_WORKFLOW_RUNTIME.md, docs/PRODUCT_BOUNDARIES.md and
  docs/COMPATIBILITY_FORMATS.md; consequential updates or explicit earlier-basis
  qualifications in affected thesis/manual passages at their maintained homes.
  The initial comparison is the §6 reusable-versus-Root/frozen-runtime wording
  and current execution representation. Preserve original invariant identities,
  consumer-adopted meanings and retained editions. A scoped reference clarification
  can be the whole output; no new ontology, universal manual or four-report set.
- **Evaluation:** A4's scoped inconsistency/applicability case with definitions,
  warranted claims, described actions and governing values examined together;
  affected guidance and publication claims agree or expose a genuine retained
  conflict. The raw wording in §6 identifies the comparison, not a prior ruling
  that all historical statements should be rewritten. ScopeOfWork must bind the
  selected case and evidentiary test; mere cosmetic edits do not establish A4.
- **Needed inputs / use conditions:** Use accepted PRD §§2.3/6.1, current AGENTS,
  the relevant cited reference passages and their original adopted source meaning
  before changing applicability. For a claim about executable behavior, require
  observed evidence from the selected operation/DEL-03-01_maintenance-toolkit;
  documentation alone cannot establish it. If a named consumer adopted a disputed
  clause, its exact maintained contract/basis is needed before incompatible change;
  that external source is TBD, carried by DEL-05-01_consumer-use-guide. Preserve
  the existing scoped contract while the binding is unresolved. Publications use
  their explicit edition/source, not just a mutable “current” link.
- **Boundary:** Use DEL-04-01_library-reconciliation for the comparison; this
  Deliverable owns the specific reference-content repair. It is not a global coherence
  audit or a rewrite of every publication. Runtime implementation, professional
  acceptance and consumer policy stay outside Root's change authority.

### DEL-03-01_maintenance-toolkit — Support current localities with actual reusable tools

- **ParentPackageID:** PKG-03. **Type:** Executable maintenance utility set with usage contract.
  **ResponsibleParty:** TBD — software contributor.
- **Local goal:** Existing repeatable setup, validation and query operations
  support the adopted Root locality and meaningful local conditions, with commands
  whose inputs, dependencies, effects, failure handling and limits are accurate.
- **CoversScopeItems:** SOW-0009, SOW-0015, SOW-0024.
  **SupportsObjectives:** OBJ-001, OBJ-002, OBJ-004, OBJ-005.
- **Anticipated artifacts:** The supported existing utility set and accurate direct
  usage instructions at their maintained homes. PR #1779 already supplies
  tools/scaffolding/current_locality.py, `--current` wrapper/check routes and
  the preparation/setup/ScopeOfWork instruction alignment; reuse these outputs
  rather than commission them again. Current structural creation supplies numeric
  paths, Work/ and accepted id/name/empty needs, leaving the real ScopeOfWork to
  authoring. Preserve the separate unflagged legacy interfaces. Reuse existing
  ScopeOfWork validators, tools/deliverables and workflow-runtime utilities;
  amend code/README/checks only for an actual connected defect or unfulfilled
  claim. Retain meaningful regression cases in maintained tests. No new unified
  framework or helper is required to populate this Deliverable; further tooling
  remains conditional on an evidenced need, and SOW-0033 has no production
  allocation.
- **Evaluation:** Reuse the applicable passing repair evidence in §6.1,
  including current-locality creation/preservation and collision checks, instead
  of repeating the tool suite because work moved into decomposition. Establish
  applicability to the selected operation and exercise only changed behavior or
  unresolved claims. Live-metadata selection, distinct conditions, partial/unknown/
  cyclic views and project-root references still require evidence for any actual
  affected query claim. Check invocation/failure limits against declared
  Python/PyYAML and, for queries, Git/HEAD dependencies. The `--prepared` check
  does not require a newly authored ScopeOfWork; the authored structural check
  requires its matching header, while full contract validity uses the existing
  validator. New persistence/containment changes require targeted regression and
  independent scrutiny. No expected-result weakening or frozen verification.
- **Needed inputs / use conditions:** Accepted R08 locality and Group 1 output
  definitions supply the target contract. Consume the repaired sources at the
  current basis and applicable PR #1779 evidence (§6.1) when selecting the current
  path; no unperformed build condition remains for F-01. Before changing a helper
  again, inspect the actual affected caller contract and relevant fixtures;
  undiscovered callers remain uncertain, not assumed absent. Final accepted DEL
  identities, selected activation scope and actual target contents are still
  required before live creation in the authorized formation undertaking (§8.1).
  An absent future locality does not prevent reuse of checked sources or their
  evidence. Named external compatibility evidence remains required before any
  incompatible exported-interface change (DEL-05-01_consumer-use-guide).
- **Boundary:** Executable behavior/direct usage contracts belong here.
  PKG-02 invokes the maintained methods; PKG-04 owns reconciliation practice and
  its examination, not the utilities. Formation undertakings and local owners
  perform actual setup/use (§8.1). No file-only query adapter, companion, graph
  service or new host enforcement is presumed.

### DEL-04-01_library-reconciliation — Library reconciliation

- **ParentPackageID:** PKG-04. **Type:** Reconciliation procedure and application set.
  **ResponsibleParty:** TBD — reconciliation-practice contributor; implementation
  owners carry their own same-PR applications, with Agent 0 integration review.
- **Local goal:** The reconciliation performed by workers makes the affected
  holdings, actual result, evidence and local declarations agree before integration,
  or exposes a consequential unresolved condition to its actual decision owner.
- **CoversScopeItems:** SOW-0006, SOW-0007, SOW-0012, SOW-0013, SOW-0014.
  **SupportsObjectives:** OBJ-001, OBJ-002, OBJ-003, OBJ-004.
- **Anticipated artifacts:** An applicable maintained reconciliation procedure
  at workflows/bounded-reconciliation/WORKFLOW.md and its existing invocation
  points in AGENTS, project-setup/package activation and coordinated-knowledge-work;
  reuse PR #1779's implemented guidance and change only demonstrated gaps. A
  bounded application produces warranted edits to the affected ScopeOfWork,
  Work and needs/pointers alongside the actual change, with consequential reasoning
  in the owning work. Add new working material only for a real subject and link
  it from the next contributor's reading path; a no-edit finding needs only a
  brief return/PR statement. Initial local contracts and needs under §8.1 remain
  concrete formation outputs at each owning locality. No parallel reconciliation
  manual, central register or separate routine assessment report is produced.
- **Evaluation:** In a selected actual maintenance change, compare implementation
  and evidence with affected declarations before integration, follow relevant
  uses, and verify that warranted corrections or explicit unresolved conditions
  remain in the owning sources. Distinguish missing behavior from stale description
  or missing evidence; do not weaken a commitment to make it appear satisfied.
  Reuse checked PR #1779 evidence where applicable. A3 additionally requires the
  formation and actual action/use-condition evidence in §8.1. A4's specific shared
  reference repair remains DEL-02-02_shared-meaning-reference's content work;
  this Deliverable supplies and examines the practice used to reconcile it.
- **Needed inputs / use conditions:** When a concrete change affects a holding,
  consume its authorized scope, actual candidate/diff and verification, the owning
  ScopeOfWork/Work/needs, and relevant consumer sources at their real revisions.
  Select the bounded case and source revision in its execution brief; these are
  not supplied by a global census. Formation requires the final accepted
  decomposition and selected activation before live setup (§8.1); existing
  checked tooling comes from maintained PKG-03 sources. An unknown input/use
  condition stays explicit and dependent work stays held while unaffected work
  continues. Goal/framing concerns go to human–Agent 0 reflection supported by
  DEL-04-02_reflective-review; no automatic escalation loop is established.
- **Boundary:** This is the SAME pre-merge reconciliation in the implementation
  PR, not an extra assessment stage. PKG-02 invokes it, PKG-03 supplies tools,
  and local owners make and retain their source edits. PKG-04 does not manage
  everyone's Work centrally or require a separate approval after ordinary repairs.
  Commitments, acceptance criteria, risk and release retain their actual owners.

### DEL-04-02_reflective-review — Reflective review of the practice

- **ParentPackageID:** PKG-04. **Type:** Reflective-practice guidance and criteria set.
  **ResponsibleParty:** TBD — practice-guidance contributor; the human and Agent 0
  conduct the actual dialogue and retain their decision responsibilities.
- **Local goal:** Human–Agent 0 reflection can examine whether reconciliation,
  the chosen local goals and the framing of work still help the intended result,
  and produce a warranted revision or an explicit reason to retain the practice.
- **CoversScopeItems:** SOW-0011, SOW-0014.
  **SupportsObjectives:** OBJ-001, OBJ-002, OBJ-003, OBJ-004.
- **Anticipated artifacts:** Reuse and, where warranted, clarify guidance/criteria
  in agents/AGENT_HELP_HUMAN.md and the relevant existing
  workflows/coordinated-knowledge-work/WORKFLOW.md passages. Make it usable to
  notice a changed question, compare local completion with intended use, examine
  the cost and warrant of monitoring, and decide whether to retain the route,
  revise a method or return a commitment/framing choice to the owner. Keep needed
  explanatory rationale with that guidance or affected owning Work. Initial
  objective-grounded decomposition and acceptance outputs in §8.1 remain actual
  formation obligations, not a new enduring product of this Deliverable. A revised
  existing passage and a bounded warranted application may be sufficient; do not
  clone these roles/workflows into another manual or require a new program.
- **Evaluation:** Examine a bounded real framing/practice question with the human
  and Agent 0 against intended use, evidence, uncertainty and consequences. Assess
  whether the guidance helped identify a warranted retain/change decision and
  whether any authorized consequence reached the governing text/local work.
  The owner's present reframing is available context, not proof that all future
  guidance or A3 is complete. A3 still requires accepted/set-up scope and the
  actual local action/use-condition case in §8.1. Check an instruction revision
  under its preceding basis (R06); proposed guidance cannot authorize itself.
- **Needed inputs / use conditions:** Use the person's current purpose/steering,
  accepted objectives and affected local goals, concrete experience from the
  bounded work/reconciliation, and the actual HELP_HUMAN/coordinated-knowledge-work
  basis before proposing changes. A burden, repeated mismatch or changed purpose
  can occasion reflection; no calendar/check-in or exhaustive audit is required.
  During formation, consume the verified Group 1 basis and actual later decisions
  for the decomposition; identify gaps rather than fabricate acceptance. Unknown
  warrants remain unknown, and reserved choices go to the human.
- **Boundary:** Human judgment directs and bounds reflective review. Dialogue/meetings are
  activities, not a stream of mandatory reports or successive monitoring levels.
  Preserve only consequential reasoning and warranted changes in existing owning
  material; no routine reflection receipts. PKG-04 examines/improves the practice
  without taking local owners' authority. Other projects may later adopt matured
  practice; no rollout, consumer policy change or automatic model loop is in scope.

### DEL-05-01_consumer-use-guide — Obtain, qualify and inspect identified library material

- **ParentPackageID:** PKG-05. **Type:** Consumer-use and compatibility guide.
  **ResponsibleParty:** TBD — technical publishing contributor.
- **Local goal:** Consumers can obtain/use identified material, assess named
  compatibility, inspect versions and consequential changes, and choose adoption
  while maintainers preserve source/recovery and prepare publication through
  ordinary mechanisms with owner release authority intact.
- **CoversScopeItems:** SOW-0019, SOW-0020, SOW-0022, SOW-0023, SOW-0025, SOW-0026.
  **SupportsObjectives:** OBJ-002, OBJ-003, OBJ-005.
- **Anticipated artifacts:** Obtaining/copying/version-selection and update-
  inspection guidance in the existing README and selected tool/workflow/reference
  guides, with resources, notices, dependencies, limitations, source/adaptation
  distinctions and named compatibility evidence. Git history, actual PR descriptions
  and ordinary release notes carry the old/new basis, reason, changed meaning/use
  and migration consequences; no parallel edition/history deliverable or notice
  register. Retain documented routes to commit-pinned history and editions,
  including the completed archive transition and original consumer pins. A
  concrete identifiable publication candidate and meaningful change account are
  still required for A7: prepare them from verified maintained sources through
  the ordinary review/publication route as a bounded application of this guide,
  not a new source home or a release act. Existing publications remain holdings
  maintained by their responsible contributors.
- **Evaluation:** A6 obtains/uses identified material with resources/notices and
  checks the actual named maintained contract/fixtures at a specified revision;
  generic examples or Root component tests do not substitute. A7 prepares the
  identifiable candidate and meaningful account, checks its actual delivery form,
  and exercises the documented release/diff inspection against an identified prior
  basis. A Git log alone is insufficient. Distinguish proposed, integrated,
  published, examined and adopted; partial/failed inspection cannot claim no change.
  Verify historical bytes actually relied on and reuse preservation evidence;
  do not re-audit all history. Public credential/private-term checks apply.
- **Needed inputs / use conditions:** Before qualification, require the selected
  use surface, its resources/licenses and candidate revision. The named consumer,
  maintained contract/fixture location and exact revision remain TBD (Q-04).
  Before A7, bind a verified candidate/version label, prior comparison revision
  and actual affected-holdings account (Q-05); use existing repository/release
  facilities and publication sources at their maintained homes. For a claimed
  incompatible interface change, require a supported path or coordinated adapter
  before that change; PKG-03 owns any separately justified implementation. Historical
  pins and editions must identify the content used. Scheduling/external delivery
  applies only if separately selected with actual configuration/authority.
- **Boundary:** Consumers retain data, authority, adaptation, adoption and product
  release; the owner publishes named versions, downstream default, while explicitly
  following main remains development. A merge is not publication. No new adapter
  mandate, consumer work/contact, private-input export or archival removal is
  authorized. Source publications and local Root work are not automatically bundled
  for all consumers. Removing the separate DEL-05-02 does not remove R15/R16/A7.

## 9. Interfaces, allocation reasons and evidence coverage

The work uses bounded input/use conditions, not a complete dependency DAG or
supplier appointments. Preliminary and final uses can differ. Source-file
relevance does not grant exclusive ownership or create a finish-to-start gate.

| Interface | Ownership / use condition |
|---|---|
| PKG-02 maintenance route and PKG-04 reconciliation | DEL-02-01_maintenance-procedures invokes the same-PR practice; DEL-04-01_library-reconciliation owns that practice; DEL-04-02_reflective-review supports its examination. SOW-0006/0007 move to PKG-04 to avoid duplicate procedure ownership. Actual content/code corrections remain with the implementation owner, using one shared-file editor. |
| PKG-04 and coordinated knowledge work | The workflow supplies realization and pre-integration coordination. Its reusable method is not an execution undertaking. PKG-04's practice contribution is carried out through concrete undertakings, bounded briefs and local owners, not a parallel coordinator or assessment stage. |
| Formation and ongoing self-monitoring | SOW-0011–0014 remain mandatory, accountable to PKG-04, with concrete formation outputs/authority in §8.1. The accepted decomposition and local contracts are inputs to work and reflection; PKG-04 does not centralize or automatically export them. No recursive setup or extra decomposition product. |
| PKG-04 and PKG-03 | Actual tools and direct usage contracts belong to PKG-03; monitoring uses their truthful, bounded results and human judgment. Reuse the PR #1779 current path/evidence. No self-monitoring application, universal graph or extra helper is implied. |
| Specific content and general reconciliation | DEL-02-02_shared-meaning-reference owns its bounded reference/publication clarification and F-02; DEL-04-01_library-reconciliation supplies the practice. The same PR carries necessary source edits and evidence; it does not create duplicate reference ownership. |
| Entry and consumer guidance | PKG-01 owns navigation meaning, PKG-05 supplies obtaining/version/use conditions. Shared README/index edits have one editor and are checked together. Publication sources remain at their homes. |
| Version information and publication | SOW-0022/0023/0026 now map to DEL-05-01_consumer-use-guide. Ordinary Git/PR/release mechanisms carry the actual change account and candidate identity. A7 still requires a real candidate and exercised inspection. No separate version-history product; actual release remains the owner act. |
| Historical retention and consumer independence | PKG-05 preserves documented historical routes/pins; PKG-02 retains frozen/additional-removal boundaries. Neither creates removal or consumer-adoption scope. Named compatibility still needs Q-04 evidence; no private inventory or consumer rollout is commissioned. |

PKG-04's two artifact kinds are a usable reconciliation procedure/application set
and reflective guidance/criteria for judging that practice and framing. Neither is
an instance-per-task/report split. PKG-02's procedure set remains the broader
maintenance route, and its reference set remains content clarification. The other
Packages retain their concrete kinds. All contributions remain subject to the
accepted evidence, authority and public-boundary constraints regardless of the
scope item's accountable home.

### Objective-to-Deliverable view

Derived from the canonical ledger; shared objectives indicate purpose, not edges.

| ObjectiveID | MappedDeliverables |
|---|---|
| OBJ-001 | DEL-01-01_library-discovery-guide, DEL-02-01_maintenance-procedures, DEL-03-01_maintenance-toolkit, DEL-04-01_library-reconciliation, DEL-04-02_reflective-review |
| OBJ-002 | DEL-01-01_library-discovery-guide, DEL-02-01_maintenance-procedures, DEL-02-02_shared-meaning-reference, DEL-03-01_maintenance-toolkit, DEL-04-01_library-reconciliation, DEL-04-02_reflective-review, DEL-05-01_consumer-use-guide |
| OBJ-003 | DEL-01-01_library-discovery-guide, DEL-02-01_maintenance-procedures, DEL-02-02_shared-meaning-reference, DEL-04-01_library-reconciliation, DEL-04-02_reflective-review, DEL-05-01_consumer-use-guide |
| OBJ-004 | DEL-02-01_maintenance-procedures, DEL-03-01_maintenance-toolkit, DEL-04-01_library-reconciliation, DEL-04-02_reflective-review |
| OBJ-005 | DEL-01-01_library-discovery-guide, DEL-02-01_maintenance-procedures, DEL-03-01_maintenance-toolkit, DEL-05-01_consumer-use-guide |

### Accepted criteria and remaining evidence

| Criterion | Accountable contribution and claim boundary |
|---|---|
| A1 | DEL-01-01_library-discovery-guide uses the actual formation outputs/localities (§8.1) and PKG-03's truthful query limits; no complete graph required. |
| A2 | DEL-02-01_maintenance-procedures and DEL-03-01_maintenance-toolkit reuse the actual PR #1779 case for supported claims; PKG-04 owns the reconciliation practice it invokes. Full operational coverage is not established by its test count. |
| A3 | PKG-04 accounts for actual accepted decomposition, setup and local conditions through §8.1. DEL-04-01_library-reconciliation examines actual action/evidence and affected uses; DEL-04-02_reflective-review examines changed understanding/framing with human judgment. Neither guidance alone nor a discussion substitutes for the required accepted/set-up case. |
| A4 | DEL-02-02_shared-meaning-reference's scoped inconsistency/qualification case, using DEL-04-01_library-reconciliation and appropriate verification; preserve historical bases and values. |
| A5 | DEL-02-01_maintenance-procedures and the affected holding's owner retain preceding-basis verification/adoption authority. PKG-04's practice/guidance revisions use those methods; reuse applicable PR #1779 evidence, with remaining claims explicit. |
| A6 | DEL-05-01_consumer-use-guide's identified obtaining/use case, resources/notices and named-contract qualification at an explicit revision; Q-04 remains unresolved. |
| A7 | DEL-05-01_consumer-use-guide's ordinary publication-preparation/update-inspection application produces the identifiable candidate and meaningful account and exercises comparison with a prior basis (Q-05). Actual delivery-form checks, limitations and independent adoption remain; deleting the standalone Deliverable does not waive this criterion. |
| A8 | DEL-02-01_maintenance-procedures's recovery/custody case, using real retained local work or a labelled case. Formation supplies the local contracts/work; reconciliation preserves current meaning and evidence. Custody release/recovery and actual enforcement limits remain to be demonstrated where applicable. |

## 10. Owner decisions translated, correspondence and open matters

The owner approved the discussed structural direction with “Approved. Proceed
accordingly.” This section records the author's translation, not an invented
exact-byte approval or a completed checkpoint snapshot. Agent 0 checks fidelity
and records the actual decision. No accepted Group 1 statement needs revision;
allocation and vocabulary clarification suffice. Any contrary substantive finding
must be returned explicitly, not silently amended into the accepted history.

| Previous proposal identity | Current treatment under owner direction |
|---|---|
| PKG-04, Root local execution | PKG-04, Self-monitoring and reflective improvement; initial formation remains explicit in §8.1. |
| DEL-04-01_execution-decomposition | Numeric identity DEL-04-01 retained; now DEL-04-01_library-reconciliation. Prior decomposition obligation SOW-0011 moves to the formation allocation under DEL-04-02_reflective-review. |
| DEL-04-02_local-execution-contracts | Numeric identity DEL-04-02 retained; now DEL-04-02_reflective-review. Prior setup/needs obligations SOW-0012/0013 move to DEL-04-01_library-reconciliation's formation allocation; SOW-0014 supports both bounded contributions. |
| DEL-05-02_publication-candidate (discussed as library editions/change information) | Removed from active structure; ID is not reused. SOW-0022/0023/0026 move to DEL-05-01_consumer-use-guide and ordinary maintenance/publication mechanisms; R15/R16/A7 remain intact. |

SOW-0006/0007 move from PKG-02 to PKG-04 to give reconciliation/connected-change
practice one accountable home. PKG-02 still invokes it and owns the broader
maintenance route. SOW-0016/F-02 remains PKG-02's specific content contribution,
not a competing owner of the general practice. All other Package homes remain
unchanged. DEL-04-01 and DEL-04-02's shared SOW-0014 mapping separates source
reconciliation from reflection on goals/framing; it creates no duplicate authority.

| Ref | Current condition | Consequence |
|---|---|---|
| F-01 | Repaired for the current route by PR #1779; sources/evidence in §6.1 remain applicable. | Reuse the tools and instructions in formation and maintenance. No unperformed build hold; final accepted scope, activation, authored localities and actual suitability remain necessary. No whole-Deliverable completion claimed. |
| F-02 | Shared reference applicability still needs bounded reconciliation with independent consumer authority and frozen Runtime standing. | DEL-02-02_shared-meaning-reference owns the particular content repair, using PKG-04's practice. No global publication/reference rewrite. |
| Q-01 | SOW-0032 / PKG-02: further archival disposition remains reserved. | Retain plans/, _DomainEngines/ and other unselected paths; no production allocation or removal authority. |
| Q-02 | SOW-0033 / PKG-03: additional bespoke tooling remains conditional on a demonstrated gap. | No production allocation or monitoring-service mandate. Reuse PR #1779; further changes need evidence and actual authority. |
| Q-03 | Seven future contributor assignments remain TBD. | Agent 0 assigns bounded work under actual authority. Local owners retain their own commitments/Work/needs; human–Agent 0 dialogue supplies reflection, not another staffing tier. |
| Q-04 | DEL-05-01_consumer-use-guide / SOW-0020: named maintained consumer contract/fixtures and exact revision unresolved. | Required before named compatibility/A6 or an incompatible change; independent guide work can proceed. No rollout or unauthorized external access. |
| Q-05 | DEL-05-01_consumer-use-guide / SOW-0022/0023: actual verified candidate/version label and prior comparison basis unresolved. | Bind real sources for A7 within ordinary publication preparation/inspection; a history log alone does not establish the criterion. Owner release remains separate. |

No substantive conflict with the approved direction was identified by the author.
The unresolved matters above retain their meanings; this translation creates no
new reserved structural choice. Agent 0's fidelity review found no material
discrepancy. Decision/snapshot binding and the separate final audit remain the
next steps, not a repeated owner question on the approved structural direction.

## 11. Coverage telemetry and checks

| Field | Current working value |
|---|---|
| Revision | G2-candidate-6, 2026-10-31 |
| ScopeItemCount | 33: 26 IN, 5 OUT, 2 TBD; accepted statements/classifications unchanged |
| PackageCount | 5 flat Packages with one declared design discipline each |
| DeliverableCount | 7 active, numeric identities preserved; DEL-05-02 removed and not reused |
| ObjectiveCount | 5 accepted identities/meanings; all have production support |
| UnassignedScopeItems / multiple Package homes | 0 / 0 |
| IN items without production mapping | 0; all seven OUT/TBD items have no production mapping |
| Production coverage | All 26 IN items covered; SOW-0014 has two distinct contributions within PKG-04 |
| Responsibility / artifact fields | 7 explicit contributor TBDs; 7 concrete artifact sets, input/use conditions and evaluations |
| OpenIssuesByType | Reserved disposition Q-01; conditional scope Q-02; staffing Q-03 (7 assignments); named-consumer input Q-04; publication candidate basis Q-05 |
| Findings | F-01 repaired for current route; F-02 remains bounded content work |
| Source coverage | O1–O5, R01–R17 (all eight R04 operations), A1–A8 and §§2/5/6 retained |

Preparation checks passed on the saved candidate: immutable manifest and PRD
identity; all 33 accepted scope statements/classifications/source and objective
mappings (apart from refreshed checkpoint-standing wording); five objective
meanings; five single-discipline Package declarations; seven coupled active DEL
IDs; one Package home per scope item; IN-only production coverage; agreement of
cards, ledger and objective view; local link targets; sole authorized modification.
Former suffix-bearing IDs occur only in the historical correspondence table; the
removed ID has no active allocation. Credential and available local host-term
screening found no issues, without printing private terms.

Author semantic inspection retained the concrete formation outputs, R07–R10/A3,
R15/R16/A7's actual candidate and inspection, local ownership and human-grounded
reflection. No accepted statement required amendment and no true conflict was
identified. Agent 0 subsequently reviewed the changed allocation, formation
coverage, reconciliation ownership, reflective guidance and removal of the
standalone edition/history product against the owner's directions and the PRD.
Checks confirmed the accepted statements/objective meanings, five packages,
seven deliverables and complete IN-only production mapping. This is not the
independent Group 3 audit, implementation evidence or owner product acceptance.

The existing XRG checker expects CSV cross-register data and would skip this
inline representation; DOMAIN checks are inapplicable. In-memory table checks
supply the applicable structural evidence without fabricating registers or changing
validators. PR #1779's passing evidence is reused, not rerun for this document edit.
Hosted secret-set/commit-range checks remain distinct from available local screening.

## 12. Working package and next boundary

Only execution/_Decomposition/PROJECT_DECOMP.md is the mutable working surface.
No companion tables or dependency/review/receipt register is needed. The accepted
Group 1 snapshot and pointer remain immutable. The owner's structural decisions
have been translated here and reviewed by Agent 0 for snapshot binding; no final
decomposition acceptance is manufactured. Agent 0 then commissions
the separate Group 3 auditor. No live setup or release is performed in this turn.
