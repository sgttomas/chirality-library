---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-02
package_id: PKG-02
decomposition_basis: execution/_Decomposition/PROJECT_DECOMP.md
project_scope_refs: [SOW-0016]
package_objective_refs: [OBJ-002, OBJ-003]
---

# Make library and adopted-product meanings explicit

## Purpose and Objective Traceability

A maintainer or a consumer who relies on a statement in a shared reference,
the thesis or the manual can tell which of five things it is: a reusable
Library definition, current Library practice, a contract a consuming product
adopted, historical runtime policy, or an explanatory edition's account. They
can then act on it without taking on an obligation that is not theirs:
ownership by the retired Runtime, approval procedures that applied only to an
earlier deployment, or an edition's earlier convention for where work lives.

This deliverable contributes that distinction for one bounded case, finding
F-02 of the decomposition: the passages of three shared references whose
wording allows the wrong reading, and the thesis and manual passages that
describe the same matters. Resolving it is the Library's scoped-inconsistency
case for PRD acceptance criterion A4.

Its allocation is the DEL-02-02 card of the
[accepted decomposition](../../_Decomposition/PROJECT_DECOMP.md), with its
interfaces in §9. It serves [PRD](../../../docs/PRD.md) objectives O2 and O3.

| Scope item | What this deliverable contributes | Objectives | PRD |
|---|---|---|---|
| SOW-0016 | The affected definitions and relationships, warranted claims, described actions and governing values reconciled together; the guidance and publications that describe them reconciled, or the earlier basis of a retained edition named; historical identities and scoped adopted contracts preserved; the reasoning for each consequential reading recorded in the owning work | OBJ-002 (O2): the clarification is usable in authorised maintenance through the Library's existing methods. OBJ-003 (O3): the affected meanings are coherent for their uses, or a consequential conflict is exposed for the owner | R11, §2.3, A4; A5 where a maintenance instruction is itself revised |

## Deliverable Definition — Ontology

An **applicability statement** identifies a claim's subject, its audience or
adopter, the standing of its source, the condition under which it applies and
the authority behind it.

A **shared definition** is a reusable Library meaning. It imposes no runtime
policy on a product by itself.

An **adopted contract** is the identified basis a project selected. Consulting
the Library, or a later publication, does not amend it.

**Current Library practice** is what `AGENTS.md`, the active undertaking and
the accepted PRD require of work in this repository. The references and the
decomposition call it Root practice, the Library's name when they were
written.

A **historical source** keeps a recoverable meaning and creates no active
obligation.

**Explanation**, **instruction**, **example** and **proposal** keep their
distinct standing.

These terms specialise the decomposition's vocabulary for this case. They do
not replace a consumer's own definitions.

- **OUT-001** — The applicability reference set: the affected sections of the runtime-interface reference (`sgttomas/chirality:docs/AGENT_WORKFLOW_RUNTIME.md`), the product-boundary reference (`sgttomas/chirality:docs/PRODUCT_BOUNDARIES.md`) and the compatibility-format reference (`sgttomas/chirality:docs/COMPATIBILITY_FORMATS.md`). Warranted changes or explicit qualifications there distinguish reusable concepts, current Library practice and adopted or historical product rules, and keep retained identities and their original meanings. A passage that already reads correctly is kept. Serves SOW-0016.
- **OUT-002** — A consistent account of the same meanings in the affected thesis and manual passages at their maintained homes: `docs/thesis/04_architecture.md`, and the Consolidated v9 manual's Markdown source with its generated HTML under `docs/alignment-manual/`. Where an edition keeps an earlier account, it says which earlier basis it keeps. Serves SOW-0016.

The three references in OUT-001 are no longer Library holdings. They are kept
in the Git history of the private `sgttomas/chirality` repository, and Library
methods and the thesis cite them there. Whether OUT-001 keeps a home, and
where, is the owner's to decide.

### The case and its passages

The case asks whether a reader can use the Library's current localities, and
adopt Library material independently, without importing retired Runtime
ownership, approval procedures that belonged to the earlier deployment, or a
publication's earlier locality convention.

- **CON-001** — The inconsistency to resolve: the runtime reference's wording on production ownership and Root governance, and the compatibility reference's M2/G4 and retired working-root clauses, permit a reading that conflicts with independent adoption and with current Library practice under `AGENTS.md` and PRD §2.3 and §6.1.

Each row names a passage and what a reader of it must be able to tell. A row
is a bound on the examination. It is not a finding that the passage is wrong.

| Passage | What a reader must be able to tell, and what is kept |
|---|---|
| Runtime reference: introduction; Method libraries and catalogs. The introduction limits App v3 and Runtime contracts to explicit reactivation and makes adoption project-specific, yet says "The Runtime project owns production discovery"; the catalog section says project methods "cannot weaken Root governance". | That each statement has an adopted or historical audience, and that neither makes the Library govern every independent consumer or the retired Runtime the current provider. Kept: the meanings of discovery and selection with their source qualification, and any restriction a deployment adopted. |
| Runtime reference: Context selection and execution; Retained Runtime process interface. Selecting a method grants no permissions; execution needs host capability and authority; the process interface describes a service the Runtime owned. | Instructions and reference utilities apart from actual host enforcement and from the historical service. The text establishes no service behaviour and no current App architecture. |
| Product-boundary reference: opening; Professional accountability; Retained invariant identifiers; Domain integration; Frozen Runtime reference. Adopted commitments persist; old header records and dependency procedures are not reinstated; Runtime contracts apply only on explicit reactivation and do not describe App v4; professional approval and protected domain writes have their own actors. | These qualifications are the test for the reading of the runtime reference. Kept unchanged: the invariant identities, professional accountability and domain control. An adopted safeguard is neither widened nor erased. |
| Compatibility reference: opening; Paths and containment §§0.2.1 to 0.2.4. The opening selects ScopeOfWork, Work and native needs for new and adopting projects; the retained deployment dialect describes retired working roots, a separate instruction root and M2/G4 authority for instruction changes. | Which deployment or adoption makes the retained path and authority clauses apply. Current Library authority comes from `AGENTS.md` and PRD §2.3, and the M2/G4 language is not universal. Kept: the containment protections where adopted. |
| Compatibility reference: Scope-of-work format; Identifier grammar; Output and evaluation matrix; Legacy production-format resolution; Legacy dependency CSV. The current scope format and native needs coexist with legacy source formats and explicitly selected conversion routes. | How to select the current numeric locality without inventing legacy lifecycle or phase files, a conversion or a CSV authoring route. The format-resolution rule applies to current projects: a valid sole contract is the current format, missing, partial or invalid input is invalid, and unauthorised dual content is ambiguous. Only the legacy conversion and retirement duties depend on adoption. Kept: old identifiers and recoverability. No consumer migration follows from a clarification. |
| `docs/thesis/04_architecture.md` §§4.2.1 to 4.2.3: deliverable localities, needs and derived views; historical references keep their source-revision meaning; files, application state and domain stores serve distinct purposes. | That the explanation agrees with the reference meaning and with the current locality convention. Kept: the difference between a recorded relationship, its suitability and an actual work result. No rewrite of the thesis. |
| Consolidated v9 manual: Authorship and use; §§1.3 to 1.4, 3.2 to 3.4, 6.3 to 6.6; Working vocabulary. Project commitments stay authoritative; capability differs from authorisation; §3.2 describes the locality convention; recovery reactivates no frozen product; discovering an edition differs from relying on it. | Whether the locality account needs a current statement or a statement of the earlier basis it keeps. Kept: the manual's wider audience. No repository path is imposed on other undertakings. |
| `docs/alignment-manual/README.md`: Discovery and reliance; Read and render; Historical manuals. The index pointer is mutable; exact reliance needs a resolved edition and source; earlier editions keep their identities. | That the comparison rests on an identified edition and source revision. Kept: earlier editions and consumer pins. A change this row warrants is made with DEL-01-01 and DEL-05-01, whose text the index is. |

A consequential reference outside these rows is followed only as far as
judging this case needs. No other publication or course is included by
association.

- **TBD-001** — Whether App v4 or SWBPIPE adopted a containment, governance or instruction-root clause of the references, and at which revision, is not established. Until it is, those clauses keep their text and an incompatible change to one is held (REQ-004).

Boundary:

- **CLM-002** — The reconciliation method belongs to `DEL-04-01`, the wider maintenance procedures to `DEL-02-01`, tools and their usage instructions to `DEL-03-01`, navigation and the standing of each publication to `DEL-01-01`, named-consumer qualification, the render route and publication preparation and inspection to `DEL-05-01`, and reflection on the practice and its framing to `DEL-04-02`. This deliverable owns the content of this one reference and publication comparison. A shared file has one editor for a combined change.
- **CLM-003** — App v4 and SWBPIPE each own their product, local policy, adaptations, adoption and release. App v3 and Runtime are frozen, and a Library edit does not reactivate them. There is no PEC product; a PEC-labelled identifier in retained invariant text is a historical name.
- **CLM-004** — The references assign engineering approval, certification, signing, sealing and issuance for reliance to a competent licensed professional, and writes to a protected domain baseline to the owning domain engine with the human acceptance it requires. Changes to commitments or acceptance criteria, explicit holds, risk acceptance, acceptance and release belong to the owner.

Outside the product: a new ontology, a universal manual, a set of four
perspective reports, a standing coherence audit, a graph or register, a new
tool or companion, the removal of any holding, and any change to a product's
behaviour or a consumer's adoption made so that the references read
consistently.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The reference set resolves the case by qualifications or warranted revisions grounded in the sources, treating the affected definitions, claims, described actions and governing values together. It keeps adopted and historical identities, and states a conflict that remains with its sources and consequence. Every row of the case table is addressed; keeping a passage unedited for a stated reason is valid, and leaving a row out is not. Where a revised passage is a maintenance instruction, or one a Library method cites as governing, the revision is examined under the text that preceded it, that text stays recoverable, and the revision does not authorise itself. Source: SOW-0016; PRD R06, R11, A4, A5.
- **REQ-002** — Each affected publication passage agrees with the reference meaning for its stated use, or says which earlier edition or source basis it keeps. Where a claim depends on exact content, the edition and source revision are identified and a mutable pointer is not relied on. A generated HTML edition is the renderer's output for its Markdown source. Unaffected passages and editions are unchanged. Source: PRD R11, R12; decomposition card.
- **REQ-003** — A statement in the reference set or the publication passages that a tool or a host behaves in a given way, or enforces a rule, rests on observation of that behaviour. Where there is none, the statement is worded as a requirement or a description and not as a fact. A statement about a named consumer's compatibility rests on that consumer's contract (REQ-004). Source: PRD R11, R12.
- **REQ-004** — A clause a consumer adopted is changed incompatibly only after that consumer's maintained contract or fixtures are established at an exact revision, with the supported path or coordinated adapter PRD R13 requires. While that is not established, the clause keeps its text and work it does not affect continues. Integrating a clarification is not qualification, publication or adoption. Source: PRD R13.
- **REQ-005** — Each consequential reading that is changed or deliberately kept has its reasoning recorded in the owning work: the source reading, the decision and the limit on its use, sufficient for the next specialist. No routine receipt and no second register is kept. Source: SOW-0016; PRD R11.
- **REQ-006** — This deliverable shall perform no act owned by another deliverable: stating the reconciliation method (`DEL-04-01`), stating wider maintenance procedures (`DEL-02-01`), implementing a tool or stating its usage instructions (`DEL-03-01`), stating navigation or the standing of a publication (`DEL-01-01`), qualifying a named consumer, changing the render route or preparing or inspecting a publication (`DEL-05-01`), and stating reflective guidance (`DEL-04-02`), as CLM-002 allocates. Applying another deliverable's method or tool to this case keeps the boundary.
- **REQ-007** — The clarification keeps the meaning of the safeguards and the names of the identities CLM-003 and CLM-004 name, changes an adopted safeguard incompatibly only as REQ-004 allows, sends each choice CLM-004 reserves to the owner, and implies no acceptance, release, adoption or reactivation. Its public text holds no private operational data or credentials. Source: PRD §2.3, §5, R17.

A locality holds only its scope and its needs. Where the reasoning REQ-005
requires is kept is the owner's to decide. The reasoning recorded before the
`Work/` folders were removed is in the
[applicability comparison](https://github.com/sgttomas/chirality-library/blob/1d536c58b787db14d544783667e0fbe4d8c44cbd/execution/PKG-02/DEL-02-02/Work/Applicability.md)
at revision `1d536c58b787db14d544783667e0fbe4d8c44cbd`; that link locates it and
decides nothing about where later reasoning is kept.

- **AC-001** — For each reference row of the case table, a reader of the passage can say which standing each consequential statement has (reusable definition, current Library practice, adopted contract, historical policy, or not established) and which adopter or condition makes a retained rule apply. Retained identifiers keep their names and adopted safeguards keep their meaning. A passage left unedited has a stated reason. A revised passage that is a maintenance instruction, or that a Library method cites as governing, was examined under its preceding text, and that text is recoverable. Verify with VER-001.
- **AC-002** — Each thesis and manual row either agrees with the reference meaning for its stated audience and use or states the earlier basis it keeps. Each has a reasoned change or a stated reason for none. The edition and source revision compared are identified, and an HTML edition whose source changed equals the renderer's output for that source. Verify with VER-002.
- **AC-003** — For at least one consequential distinction in the case, the changed or qualified reading can be followed from its source warrant to the action a reader may now take and the value it protects, and the neighbouring claims that reading touches agree with it. A conflict that remains is stated with both passages, its consequence and who decides it. Edits that change no reading do not meet this criterion. Verify with VER-003.
- **AC-004** — No adopted clause is changed incompatibly without what REQ-004 requires. No statement of tool or host behaviour or of consumer compatibility exceeds REQ-003. The outputs contain none of the acts REQ-006 excludes, keep what REQ-007 protects, and pass the credential scan. Verify with VER-004.

## Production and Verification Method — Praxeology

Choices that define the product:

- A precise applicability qualification, or a checked decision to keep a
  passage, is preferred to a rewrite. A qualification can be the whole repair.
- A change is made at the passage's maintained source. Markdown is edited and
  its HTML regenerated; the two are never edited separately.
- The comparison is carried with DEL-04-01's reconciliation method, in the
  pull request that makes the change.
- Inquiry widens only for a concrete consequence. A wider commitment goes to
  the owner.

- **VER-001** — Judgment by a reader who did not write the text (reads each reference row's passage against PRD §2.3, §6.1 and R11 and `AGENTS.md`), with a comparison with a named reference for the format row (the behaviour of the scope format resolver, observed by running it) and for a revised governing passage (its preceding text, recovered from Git): For each reference row, read the candidate or retained passage for its source standing, its adopter or trigger, the original meaning of each retained identifier and the reason for any passage left unedited. Check that current Library use can be told from retained Runtime and deployment rules without inferring what a host implements. Where a revised passage is a maintenance instruction or one a Library method cites as governing, recover its preceding text, confirm from the review record that the revision was judged under it, and check that the method citing it still resolves to a recoverable basis. Record a contradictory reading that remains, with its sources.
- **VER-002** — Judgment by a reader who did not write the text (reads each publication row against the reference dispositions) and an executable check (`python3 docs/alignment-manual/render_manual.py` with `--check`, which observes only that the HTML equals the renderer's output for the named source): Compare the meaning of locality, condition, authority and recovery in the thesis and manual passages with the reference dispositions, keeping each passage's audience and edition standing. Identify the edition and source revision compared. If a Markdown source changed, run the renderer check on its HTML and read the changed passage in the rendered page; otherwise say why no derivative changed.
- **VER-003** — Judgment by a reviewer who did not make the change (follows one distinction end to end in the pull request and its sources): Trace at least one consequential distinction from its source warrant through the permitted action to the value it protects, then read the neighbouring claims it touches. Compare the reading before and after, or the reason a reading was kept. Say what remains unresolved and whether it prevents A4. This examines content and use; it is not a runtime test and does not stand in for the owner's acceptance.
- **VER-004** — Judgment by a reviewer who did not make the change (reads the diff against REQ-003, REQ-004, REQ-006 and REQ-007, one protected item at a time), with an executable check (the credential scan, which observes only the patterns it holds): For any adopted clause the diff changes, find the named consumer's contract at an exact revision or record that the change is held. For any behaviour or compatibility statement, find its observation. Run `python3 tools/validation/validate_run_record_leaks.py --base <base> --head <head>` on the change and state what the scan does not cover.

## Governing Values and Decisions — Axiology

- **AX-001** — Warrant sets the strength of a claim. Better is fewer statements a reader can take as stronger than their grounds: a definition read as policy, a requirement read as enforced behaviour, history read as a current duty. That may never be gained by deleting or weakening a clause a consumer adopted, or by wording that hides a real conflict.
- **AX-002** — Consumers stay independent and accountable acts stay with their actors. Better is fewer passages from which a reader could infer that the Library governs an independent consumer or that a retired product provides a current service. That may never be gained at the cost of an adopted safeguard: containment, professional accountability or a protected domain write.
- **AX-003** — Keep what is sound. Better is a smaller change for the same resolved reading: fewer passages edited and less text added. That economy may never leave a row of the case unaddressed or rename a historical identity.
- **AX-004** — Reasoning sits with the change it explains. Better is less that a later specialist must reconstruct to trust a disposition. That may never be bought with a second register, a routine receipt or a report per perspective.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | OBJ-002, OBJ-003 | REQ-001, REQ-003, CON-001 | AC-001 | VER-001 | What each standing means comes from PRD §2.3, R11 and R13 and from `AGENTS.md`. What a retained clause meant comes from the reference text before the change, which this deliverable did not write. That a revised governing passage is examined under its preceding text comes from PRD R06 and A5, and that text is read from Git, which the revision did not write. For the format row the reading is compared with the behaviour of the scope format resolver, DEL-03-01's tool. Whether a reader can tell the standings apart is judged by a reader who did not write the text. |
| OUT-002 | OBJ-002, OBJ-003 | REQ-002, REQ-003 | AC-002 | VER-002 | The meaning to agree with is the reference meaning, which AC-001 grounds in the PRD and `AGENTS.md`; an edition's standing comes from the manual index, which is not this deliverable's text. The HTML is compared with the renderer's output for the committed Markdown; the renderer is not this deliverable's code, and the comparison shows only that the derivative matches its source. |
| OUT-001 | OBJ-002, OBJ-003 | REQ-001, REQ-002, REQ-005, CON-001 | AC-003 | VER-003 | What the case must show comes from PRD A4. The warrant traced is a PRD clause, `AGENTS.md` or an adopted contract, none of them written by the change, and the tracing is judged by a reviewer who did not make the change. |
| OUT-002 | OBJ-002, OBJ-003 | REQ-001, REQ-002, REQ-005, CON-001 | AC-003 | VER-003 | What the case must show comes from PRD A4. The warrant traced is a PRD clause, `AGENTS.md` or an adopted contract, none of them written by the change, and the tracing is judged by a reviewer who did not make the change. |
| OUT-001 | OBJ-002, OBJ-003 | REQ-003, REQ-004, REQ-006, REQ-007, CLM-002, CLM-003, CLM-004, TBD-001 | AC-004 | VER-004 | The condition for changing an adopted clause comes from PRD R13, and the contract compared is the named consumer's own at an exact revision, an outside source. The sibling allocation comes from decomposition §9. The credential scan is the Library's own tool and covers only the patterns it holds. |
| OUT-002 | OBJ-002, OBJ-003 | REQ-003, REQ-004, REQ-006, REQ-007, CLM-002, CLM-003, CLM-004, TBD-001 | AC-004 | VER-004 | The condition for changing an adopted clause comes from PRD R13, and the contract compared is the named consumer's own at an exact revision, an outside source. The sibling allocation comes from decomposition §9. The credential scan is the Library's own tool and covers only the patterns it holds. |
