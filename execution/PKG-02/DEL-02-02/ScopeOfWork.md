---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-02
package_id: PKG-02
decomposition_basis: execution/_Decomposition/checkpoint_snapshots/GROUP3-20261101T011431Z/PROJECT_DECOMP.md@fd847ac9ac68250b2f35d2e9c0087c16e86b510a
project_scope_refs: [SOW-0016]
package_objective_refs: [OBJ-002, OBJ-003]
---

# Make library and adopted-product meanings explicit

## Purpose and Objective Traceability

A maintainer or consumer must be able to distinguish reusable library definitions,
current Root practice, scoped adopted contracts, historical runtime policy and
explanatory editions, and use the affected claims coherently. This is the bounded
F-02 applicability contribution, not a new ontology or runtime design.

| Accepted reference | Contribution here | Product warrant |
|---|---|---|
| SOW-0016 | Reconcile affected definitions and relationships, warrant, actions and values together; reconcile affected guidance/publications or identify their earlier basis; preserve historical identities and adopted contracts. | docs/PRD.md R11, §2.3, A4 and A5 |
| OBJ-002 | Make the selected reference clarification usable in authorized maintenance through the library's existing methods. | PRD O2; A4, with A5 only to the extent a maintenance instruction is actually revised and checked under its preceding basis |
| OBJ-003 | Make the affected meanings coherent for their uses, or expose a consequential conflict for owner disposition. | PRD O3; A4 |

The accepted basis is the Group 3 snapshot named above, specifically its vocabulary,
objectives, SOW-0016 ledger row, DEL-02-02 card, §8.1 formation obligations, §9
interfaces/evidence and §10 qualifications. Its payload SHA-256 is
`313bdb78d1a000d8a903aa12197603ac45bcb7a601df1ee12447eaaf29031261`.
`execution/_Decomposition/_LATEST_ACCEPTED.md` resolves the snapshot;
`DECISION.md` in that snapshot supplies acceptance and setup authority, despite
historical submission wording in the payload. All four manifest entries were
verified for this authoring. Snapshot-relative links resolve from the original
`execution/_Decomposition/PROJECT_DECOMP.md`. The preceding accepted `docs/PRD.md`
at `4214db1c0ed04ce5466e65979c215fe018bd19d7` has SHA-256
`95c3c25ee36d4d4ddadf54d266a47a2ee58c6b37fbbdef75ad20a97986a718ca`.
The current PRD applies the owner's “There is no PEC” correction to §2.3 and
identifies that clarification; this historical hash is not the corrected file's hash.
Accepted snapshot bytes and the original acceptance/source identity are preserved.

- **CLM-001** — Maturity: bounded F-02 production drafting and examination is authorized against AC-001 through AC-004. The owner approved the connected reference/manual content and selected-row findings at `4ac85ca97caa716a31bf68b726ffac931cb7ca08` for integration, after independent examination and Agent 0 verification of the bounded repair. Work/Applicability.md and the actual PR retain the evidence and decision. The locality and its needs do not establish input suitability, an accomplished repair, accepted product or release. Existing qualifications and checked holdings may satisfy part or all of an output; new files are not inherently required. Setup basis: Group 3 DECISION.md/HANDOFF_STATE.md and decomposition §8.1; current production authority: the bounded F-02 undertaking supplied through Agent 0.

The initial source assessment and continuation conditions are in [Work/Applicability.md](Work/Applicability.md). Consumer-local needs are now declared in `deliverable.yaml`; their presence establishes no satisfaction claim.

## Deliverable Definition — Ontology

- **OUT-001** — A coherent, scoped applicability reference set in the affected sections of docs/AGENT_WORKFLOW_RUNTIME.md, docs/PRODUCT_BOUNDARIES.md and docs/COMPATIBILITY_FORMATS.md. Warranted changes or explicit qualifications distinguish reusable concepts, current Root practice and adopted/historical product rules while preserving invariant identities and their original meanings. Existing adequate passages may be retained with an evidenced no-edit finding. Scope: SOW-0016. Objectives: OBJ-002, OBJ-003.
- **OUT-002** — A consistent account of the selected meanings in affected thesis/manual passages at their maintained source homes, or an explicit qualification of an edition's earlier basis. Its consequential comparison reasoning and candidate-bound evidence belong in execution/PKG-02/DEL-02-02/Work/ and the actual review record, linked to the source passages; they need not be separate reports. Scope: SOW-0016. Objectives: OBJ-002, OBJ-003.

Here an **applicability statement** identifies the subject, audience/adopter, source
standing, condition of use and authority of a claim. A **shared definition** does
not itself impose product runtime policy. An **adopted contract** is a project's
identified selected basis; consultation or a later publication does not amend it.
**Current Root practice** is bounded by AGENTS.md, the active undertaking and the
accepted PRD. **Historical source** preserves recoverable meaning without creating
an active obligation. **Explanation**, **instruction**, **example** and **proposal**
must retain their distinct standing. These terms specialize the accepted vocabulary
for this case; they do not replace consumer definitions.

### Selected F-02 case and passage boundaries

The case asks whether a reader can use current Root localities and independently
adopt library material without mistakenly importing retired Runtime ownership,
old Root-only approval procedures or a publication's earlier locality convention.
The initial inspected source basis is `fd847ac9ac68250b2f35d2e9c0087c16e86b510a`.
Rebind the actual candidate and changed source passages during implementation.

| Source and actual section | Passage to examine | Evaluative question and retained boundary |
|---|---|---|
| docs/AGENT_WORKFLOW_RUNTIME.md, introduction and Method libraries and catalogs | The introduction limits historical App v3/Runtime contracts to explicit reactivation and says adoption is project-specific, yet states “The Runtime project owns production discovery”; the catalog section says project methods “cannot weaken Root governance”. | Does each statement identify its adopted/historical audience without implying that Root governs every independent consumer or that retired Runtime is the current library provider? Preserve source-qualified discovery/selection meanings and any scoped adopted restriction. |
| docs/AGENT_WORKFLOW_RUNTIME.md, Context selection and execution; Retained Runtime process interface | Method selection grants no permissions; actual execution requires host capability and authority. The retained process interface describes a Runtime-owned service. | Can a reader distinguish instructions and reference utilities from actual host enforcement and the historical service? No service behavior or current App architecture is established by this text review. |
| docs/PRODUCT_BOUNDARIES.md, opening; Professional accountability; Retained invariant identifiers; Domain integration; Frozen Runtime reference | Adopted commitments persist; old header records and dependency procedures are not reinstated; Runtime contracts apply only upon explicit reactivation and do not describe App v4. Professional approval and protected domain writes have their own actors. | Use these existing qualifications to test the runtime-reference reading. Retain original invariant identities, professional accountability and domain control; do not broaden or erase adopted safeguards. |
| docs/COMPATIBILITY_FORMATS.md, opening; Paths and containment §§0.2.1–0.2.4 | The opening selects ScopeOfWork, Work and native needs for new/adopting projects. The retained deployment dialect describes retired Root working roots, a separate instruction root and M2/G4 authority for instruction changes. | Identify which deployment/adoption makes the retained path and authority clauses applicable. Compare current Root authority with AGENTS.md and PRD §2.3; do not treat historical M2/G4 language as universal or remove adopted containment protections. |
| docs/COMPATIBILITY_FORMATS.md, Scope-of-work format; Identifier grammar; Output and evaluation matrix; Legacy production-format resolution; Legacy dependency CSV | Current SOW_V1 and native dependencies coexist with legacy source formats and explicitly selected conversion routes. | Can the reader select the current numeric locality without inventing legacy lifecycle/phase files, a conversion, or a CSV authoring route? Preserve old identifiers and recoverability; no consumer migration follows from clarification. |
| docs/thesis/04_architecture.md §§4.2.1–4.2.3 | ScopeOfWork/Work/native needs and derived views; historical Design references retain source-revision meaning; files, application state and domain stores serve distinct purposes. | Check the explanation against the affected references and current locality practice. Retain the distinction between a recorded relationship, its suitability and an actual work result. No whole-thesis rewrite. |
| docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v9.md, Authorship and use; §§1.3–1.4, 3.2–3.4, 6.3–6.6; Working vocabulary | Project commitments remain authoritative; capability differs from authorization; §3.2 describes the new locality convention and an owner-led Design-to-Work reconciliation; recovery does not reactivate frozen products; edition discovery differs from reliance. | Examine whether the locality-transition explanation needs current clarification or an earlier-basis qualification alongside the thesis's explicit adopted Work statement. Preserve the manual's wider audience and avoid imposing repository paths on all undertakings. |
| docs/alignment-manual/README.md, Discovery and reliance; Read and render; Earlier editions | Consolidated v9 is the discovered current edition; the pointer is mutable, exact reliance needs a resolved edition/source, and earlier adopted editions keep their identities. | Bind the v9 source at the inspected revision for this comparison. Retain earlier editions and consumer pins. If a maintained rendered edition is affected, use its declared source/render route and inspect that actual form. |

These are source-grounded examination bounds, not a prior verdict that every named
passage is wrong or must change. Follow a consequential reference only as needed
to judge this case. No other publication or course is commissioned by association.

- **CON-001** — Root-facing qualification approved; historical adoption remains unresolved: the preceding runtime-reference production-ownership/Root-governance wording and compatibility-reference M2/G4/retired-Root clauses permitted a reading inconsistent with current independent adoption and Root library execution under AGENTS.md and PRD §§2.3/6.1. The approved content makes their adopted/historical subjects explicit and aligns the selected manual locality explanation. Work/Applicability.md examines all selected passages and real source uses. Exact transitive historical adoption remains unverified; this source comparison does not adjudicate all adopted meanings. Consequence: preserve existing scoped contracts and hold any incompatible alteration until its warrant and affected adoption are established; continue supported Root-facing clarification. Escalate a genuine commitment conflict with both passages and its consequence to the actual owner.

### Allocation and actors

- **CLM-002** — Decomposition §9 allocates general reconciliation practice to `DEL-04-01`, broader maintenance procedures to `DEL-02-01`, executable utilities/direct usage contracts to `DEL-03-01`, navigation to `DEL-01-01`, and named-consumer qualification plus publication preparation/change inspection to `DEL-05-01`. Reflection on the practice/framing belongs to `DEL-04-02` with the human and Agent 0. This deliverable owns its specific reference/publication content comparison. Shared-file relevance creates no exclusive file ownership; the implementation coordinator selects one editor/integrator for a combined change.
- **CLM-003** — Under AGENTS.md and PRD §2.3/R13/R15, App v4 and SWBPIPE each own their product implementation, local policy, adaptation, adoption and product release through their own authority. Root's integration grant is Root-only. Historical Runtime implementation remains frozen with App v3; reactivation requires explicit owner authority, not a library edit. A named adopter's contract is not supplied by this setup assignment.
- **CLM-004** — Under AGENTS.md, PRD §§4–5/R15 and docs/PRODUCT_BOUNDARIES.md Professional accountability/Domain integration, the Root owner retains changed commitments/acceptance criteria, risk acceptance, explicit holds, product acceptance, library release and further archival disposition. The competent licensed professional retains engineering approval, certification, signing/sealing and issuance for reliance. Protected domain baselines remain with the owning domain engine; application uses declared domain-controlled tools with the required human acceptance. Neither source clarification nor a structural PASS transfers these acts to this author.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The reference set shall resolve the selected F-02 applicability case through source-grounded qualifications or warranted revisions, distinguishing definitions, actual claims, described actions and governing values together. It shall preserve adopted/historical identities and expose remaining substantive conflict with sources and consequence. The examination must address every selected table row; a justified no-edit disposition is valid, omission is not. Basis: SOW-0016, PRD R11 and A4.
- **REQ-002** — Affected publication passages shall agree with the scoped reference meaning for their stated use or identify their earlier edition/source basis explicitly. Exact reliance shall use an identified edition and revision, not only a mutable discovery pointer. Unaffected passages/editions remain unchanged. Basis: PRD R11–R12, decomposition DEL-02-02 card.
- **REQ-003** — Evidence shall bind the actual candidate and source passages, distinguish content examination, executable observation and named-consumer qualification, and state missing evidence as unverified. Documentation and reference-tool passes shall not establish production enforcement. Changes to numerical meaning, persistence, permissions or destructive behavior require focused regression checks and independent scrutiny under the repository rules. Basis: PRD R12 and AGENTS.md.
- **REQ-004** — Before an incompatible change to an adopted clause, establish the named consumer's maintained contract/fixtures and exact revision and the supported path or coordinated adapter required by PRD R13. While that binding is unknown, preserve the scoped contract and hold that dependent change; proceed with unaffected work. Preserve Q-04 and Q-05 as distinct conditions, rather than treating integration as qualification, publication or adoption.
- **REQ-005** — The implementation shall reconcile its actual result/evidence with this contract, owning Work and actual needs before integration using the selected maintained procedure, leaving unchanged declarations alone. Consequential reasoning shall explain the source reading, decision and use limitation sufficiently for the next specialist; avoid routine receipts or a second progress register. Basis: PRD R08–R12 and decomposition §8.1/§9.
- **REQ-006** — This deliverable shall perform no act owned by another deliverable: general reconciliation-method authoring (`DEL-04-01`), broader maintenance-procedure authoring (`DEL-02-01`), executable-tool implementation (`DEL-03-01`), entry/navigation authoring (`DEL-01-01`), named-consumer qualification and publication-candidate/update-inspection production (`DEL-05-01`), or reflective-practice/framing guidance authoring (`DEL-04-02`); each excluded act resolves to CLM-002. Applying their available means to the specific content case does not duplicate those contributions.
- **REQ-007** — Excluded acts are independent consumer implementation/policy/adaptation/adoption/product release and frozen-product development/verification or reactivation (CLM-003); changed commitments/acceptance criteria, risk acceptance, lifting holds, product acceptance, library release and additional archival removal (Root owner, CLM-004); engineering approval/certification/signing/sealing/issuance (licensed professional, CLM-004); and direct protected-domain baseline writes (owning domain engine and required human acceptance, CLM-004). This content contribution shall not perform those acts. Q-01 retains plans/ and _DomainEngines/ pending owner disposition. Q-02 adds no tooling or companion without a demonstrated gap and authorized scope. Public outputs shall contain no private operational data or credentials; source clarification supplies no authority to export them.

- **AC-001** — For the selected F-02 case, every reference row has a supported applicability disposition tied to its source passage and actual candidate: what is reusable, current Root, adopted, historical or unverified is intelligible, and retained invariant/contract meanings are preserved. Verify by VER-001.
- **AC-002** — The affected thesis/manual explanation is consistent for its stated audience/use, or explicitly identifies an earlier basis; each selected publication row has a reasoned change or no-edit disposition, with exact source/edition identity and verification of an affected maintained derivative. Verify by VER-002.
- **AC-003** — The substantive case examination connects a changed distinction or resolved applicability reading to its warranted claim, permitted action and governing value, showing why the result is usable and how affected references/publications agree. Remaining conflict is explicit with consequence and actual owner disposition where required; cosmetic edits or an unresolved conflict alone do not establish A4 completion. Verify by VER-003.
- **AC-004** — Candidate evidence and local reconciliation distinguish established content, behavior and compatibility claims; unmet input conditions remain visible, no incompatible adopted change proceeds without its condition, and each excluded act remains with its identified actor. The result claims neither product acceptance nor release. Verify by VER-004.

### Inputs and use conditions

| Input / source | Intended use and trigger | Condition / unresolved binding |
|---|---|---|
| Accepted Group 3 decision/payload and docs/PRD.md; current AGENTS.md | Select scope and authority before authoring or changing meaning. | Verified identities above retain the accepted setup basis. The current bounded F-02 assignment authorizes production drafting and examination, with owner content approval before integration; proposed text cannot authorize itself. |
| Named shared references and selected thesis/manual passages above | Compare actual definitions/applicability before editing; retain the preceding basis for review. | Inspect source and revision actually used. No archived execution backlog, private planning or frozen implementation is an input to this setup. |
| workflows/bounded-reconciliation/WORKFLOW.md and applicable current maintenance route | Use the existing same-PR practice for this content change, with DEL-04-01 supplying practice and DEL-02-01 broader method coverage. | Select maintained instructions at the execution basis; no whole-deliverable completion gate. The current F-02 application and its remaining evidence are described in Work/Applicability.md. |
| Selected executable operation/source and observed check evidence, accounted for by DEL-03-01 | Required if the clarification makes a behavior or enforcement claim. | Exact operation/candidate/check is not selected here. Until observed, such behavior is unverified; a documentation walkthrough is insufficient. |
| Named maintained adopter contract/fixtures, coordinated through DEL-05-01 | Required before named compatibility claims or an incompatible adopted-clause change. | Q-04: named consumer, location and exact revision remain unresolved. Preserve the contract in the meantime; Root content inspection can proceed. |
| Explicit manual/thesis source edition and candidate revision | Needed when comparing or changing the selected explanatory passages. | Initial v9/thesis sources are bound above; implementation must identify actual candidate and any affected rendered form. A mutable index does not rebind reliance. |
| Verified publication candidate/version, prior comparison basis and affected-holdings account, under DEL-05-01 | Required only for the distinct A7 preparation/inspection claim or when consuming its change account. | Q-05 remains unresolved. This comparison may supply meaning/use consequences, but does not create that candidate, release or A7 evidence. |

- **TBD-001** — Q-04's named adopter and maintained contract/fixture revision are unknown. No new supplier appointment or unconditional producer edge follows from the table. Consumer-local need authoring follows this contract under Agent 0's setup coordination.
- **TBD-002** — Q-05's verified publication candidate/version and prior comparison basis are unknown. This does not prevent passage comparison at the inspected source basis, but it prevents claiming publication preparation/inspection completed.
- **TBD-003** — The current bounded F-02 assignment appoints one WORKING_ITEMS editor through ordinary repairs; Agent 0 retains owner continuity, consumer coordination and final integration. This appointment does not resolve other Q-03 staffing. The actual diff and Work/Applicability.md identify the candidate scope, affected uses and remaining evidence.

## Production and Verification Method — Praxeology

Use the selected library basis and the available reconciliation/maintenance method.
Establish the affected passage set and intended readings, compare each with its
accepted authority and actual use conditions, and record consequential reasoning
in owning Work. Prefer a precise applicability qualification or checked retention
when sufficient. Carry warranted changes to actual source homes and examine
connected publication meaning. Expand inquiry only for a concrete consequence;
return any expanded commitment to its owner. Do not implement product behavior
or migrate an adopter merely to make the references read consistently.

- **VER-001** — Passage-level content review of OUT-001 against the table, PRD §§2.3/6.1/R11 and current AGENTS.md at identified revisions. For each row inspect the actual candidate or retained bytes, source standing, adopter/trigger, original invariant meaning and no-edit warrant. Check whether current Root use is distinguishable from retained Runtime/deployment rules without inferring host implementation. Record unresolved contradictory readings with sources.
- **VER-002** — Review OUT-002 against the reference dispositions, thesis §4.2, the named v9 manual passages and its README edition/reliance rules at explicit revisions. Compare the meaning of locality, condition, authority and recovery; retain the audience and edition qualifications. If a maintained HTML edition changes, use the declared source renderer/check route and inspect links/readability of that actual output; otherwise state why no derivative changed. No broad publication render or rewrite is required.
- **VER-003** — Evaluate the bounded real applicability case using the maintained reconciliation practice: trace at least one consequential distinction through its source warrant, authorized action and human/consumer value, then inspect affected neighboring claims. Compare before/after or justified retained readings and demonstrate resolution/qualification, rather than just changed wording. Identify what remains unresolved and whether it prevents A4; any required owner disposition must be real and scoped. This is content/use examination, not a runtime test or a substitute for human acceptance.
- **VER-004** — Inspect the actual candidate diff, cited evidence, input conditions, Work/needs reconciliation and per-act owner mapping in REQ-006/REQ-007 against CLM-002–CLM-004. Check exact named-contract evidence before any incompatible change; check focused behavior evidence and independent scrutiny when required by REQ-003. Run applicable maintained structural/credential/private-term checks on changed public material, state their coverage and limits, and report missing evidence without redefining acceptance. Reuse applicable passing evidence with its actual source/candidate identity.

The initial setup verified the production contract with validate_scope_of_work.py,
derived the deterministic review checklist twice and compared bytes, checked
boundary-owner resolution with semantic QA for acts the tool cannot decide, and
ran the authored-locality check without --prepared. Those checks establish
setup structure and reviewability only. No conversion/parity/finalization, lifecycle
file, HTML contract derivative, production case execution or acceptance is implied.

## Governing Values and Decisions — Axiology

- **AX-001** — Warrant governs the strength of a claim. A reusable definition, recorded approval, structural validation, observed behavior and independent adoption are different grounds. Preserve uncertainty and genuine conflict rather than erase it through a universal wording change. Basis: PRD R11–R12 and docs/PRODUCT_BOUNDARIES.md Professional accountability/Retained invariant identifiers.
- **AX-002** — Preserve human accountability, consumer independence and protected baselines. The owner accepted the decomposition “as the basis for project setup”; that setup decision did not authorize production by itself. The current bounded F-02 assignment authorizes reference drafting and examination, with owner content approval before integration; it does not authorize consumer implementation, expanded commitments, product acceptance or release. Reserved actors/acts remain those in CLM-003/CLM-004. Current instruction changes must be assessed under their preceding selected basis. Basis: Group 3 DECISION.md, PRD R06/R13/R15 and AGENTS.md.
- **AX-003** — Keep useful existing material and historical identity. A source qualification can be the entire required repair; no new ontology, universal manual, four-report set, standing coherence audit, new graph/register, archival removal or compulsory companion is required. Q-01/Q-02 remain qualified; no source is deleted because it is historical. Basis: decomposition DEL-02-02 card and §10; PRD §§2.3/5 and R17.
- **AX-004** — Integrate a usable result with minimum sufficient reasoning at its actual home. The specific content owner retains ordinary repairs; Agent 0 retains integration and owner continuity. Shared edits have one coordinator/editor, and unchanged declarations stay unchanged. Public evidence must be cleared; unavailable private or hosted screening sources cannot be claimed checked. Basis: AGENTS.md, decomposition §8.1/§9 and PRD R08/R12/R17.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | OBJ-002, OBJ-003 | REQ-001, REQ-003, CLM-001 | AC-001 | VER-001 | Candidate/source-bound reference dispositions for each selected row; preserved identities, scoped qualifications and reasoned no-edit results. |
| OUT-002 | OBJ-002, OBJ-003 | REQ-002, REQ-003, CLM-001 | AC-002 | VER-002 | Passage comparison with exact thesis/manual source and edition basis; affected derivative check or warranted no-derivative finding. |
| OUT-001 | OBJ-002, OBJ-003 | REQ-001, REQ-002, CON-001 | AC-003 | VER-003 | Substantive F-02 examination connecting definition, warrant, action and value; actual resolution/qualification and any remaining owner decision, with A4 limits. |
| OUT-002 | OBJ-002, OBJ-003 | REQ-001, REQ-002, CON-001 | AC-003 | VER-003 | Substantive F-02 examination connecting definition, warrant, action and value; actual resolution/qualification and any remaining owner decision, with A4 limits. |
| OUT-001 | OBJ-002, OBJ-003 | REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, CLM-002, CLM-003, CLM-004 | AC-004 | VER-004 | Actual checked candidate and claim-specific evidence; local reconciliation, preserved unmet conditions, one-for-one boundary actors and public-screening scope. |
| OUT-002 | OBJ-002, OBJ-003 | REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, CLM-002, CLM-003, CLM-004 | AC-004 | VER-004 | Actual checked candidate and claim-specific evidence; local reconciliation, preserved unmet conditions, one-for-one boundary actors and public-screening scope. |
