---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-01
package_id: PKG-05
decomposition_basis: execution/_Decomposition/PROJECT_DECOMP.md
project_scope_refs: [SOW-0019, SOW-0020, SOW-0022, SOW-0023, SOW-0025, SOW-0026]
package_objective_refs: [OBJ-002, OBJ-003, OBJ-005]
---

# Obtain, qualify and inspect identified library material

## Purpose and Objective Traceability

Someone outside the Library can take an identified edition of it, or a single
role, workflow or tool from it, use it in their own project with everything it
needs, know exactly which source they hold, see what a later edition changes,
and decide for themselves whether to adopt it. The owner can publish an edition
whose source, contents and limits are known, and whatever a consumer pinned
earlier stays recoverable.

This deliverable contributes five things to that result: the guidance a
consumer follows to choose, obtain, copy and update Library material; the
qualification of one named consumer interface against that consumer's own
contract; a publication candidate prepared for the owner's release decision;
the account of what an edition changes, with the inspection procedure exercised
against the prior basis; and the routes by which commit-pinned history and
earlier editions are recovered.

Its allocation is the DEL-05-01 card of the
[accepted decomposition](../../_Decomposition/PROJECT_DECOMP.md), with the
interfaces in that document's §9. It serves [PRD](../../../docs/PRD.md)
objective O5, with O2 and O3, and carries the PRD's acceptance criteria A6 and
A7.

| Scope item | What this deliverable contributes | Objectives | PRD |
|---|---|---|---|
| SOW-0019 | Independent routes to consult, invoke or copy identified material through ordinary files, Git, archives and documented interfaces, keeping its resources, licence notices and source basis, with local adaptations distinguishable | OBJ-005 (O5) | R13, R17, A6 |
| SOW-0020 | A named consumer interface checked against that consumer's maintained contract or fixtures at an explicit revision; a supported path or coordinated adapter in place before an incompatible change | OBJ-003, OBJ-005 (O3, O5) | R13, A6 |
| SOW-0022 | A named publication candidate prepared from a verified revision, with source identity, notices, dependencies, limitations and recoverable commit and edition routes; publication stays with the owner and adoption with the consumer | OBJ-003, OBJ-005 (O3, O5) | R15, R04 "Prepare publication and inspect updates", A7 |
| SOW-0023 | The old and new basis, the reason, the change in meaning or use and the migration effects explained in review descriptions and publication notes; change inspection through existing release and diff facilities, exercised | OBJ-003, OBJ-005 (O3, O5) | R16, R04 "Prepare publication and inspect updates", A7 |
| SOW-0025 | Ordinary use that needs no undisclosed sibling checkout, dated run directory, private input or credential; public fixtures and summaries cleared; public changes credential-checked | OBJ-002, OBJ-005 (O2, O5) | R17, A6, A7 |
| SOW-0026 | The pre-library execution transition and original consumer-pinned history traceable and recoverable, without reinstating earlier structure, commitments or lifecycle state | OBJ-003, OBJ-005 (O3, O5) | R12, R15, §6.3 step 2 |

## Deliverable Definition — Ontology

An **edition** is a named publication of the Library: `Chirality library
<version>`, tagged `library-v<version>`, published by the owner from one exact
integrated source revision through the repository's release facility. Its
release carries the complete tracked-source archive of that revision, the
archive's SHA-256 checksum, the change account and the known limitations. It
is a source edition: its files are read and its tools run in place. It is not
an installed product, a Python package or an application runtime, and the
edition name of a book or manual is not a Library version.

A **publication candidate** is the concrete material proposed as an edition:
an identified source revision in its delivery form, with a proposed name. A
version proposal, a merge or a Git log is not a candidate.

Five words describe different acts, and none implies the next. A change or
candidate is **proposed**. A change is **integrated** when it is merged to
`main`. An edition is **published** when the owner releases it. Material is
**examined** when someone compares it with a basis. It is **adopted** when a
consumer changes its selected basis to it.

A consumer's **selected basis** is the edition or full source revision that
actually governs its use. Published editions are the consumer default;
following `main` is an explicit choice to use development.

A **local adaptation** is a consumer's changed copy of Library material,
marked so that it stays distinguishable from its source. A **derivation** is a
project document adapted from a Library source file. It may record that source
and the published edition it was last reconciled against in the optional
`metadata.upstream` field that `docs/document-metadata.md` defines.

A **named compatibility claim** says that a stated interface of a named
consumer works with stated Library material. It holds only for that consumer,
interface and use, the consumer's maintained contract or fixtures, and the two
revisions examined.

A **change account** explains, for an edition or an integrated change, the
holdings affected, the old and new basis, the reason, the difference in
meaning or use, and the known migration consequences. An edition's account is
in its release notes; an integrated change's account is its pull request
description.

A **recovery route** is a documented way to reach commit-pinned history, an
earlier edition or a removed holding. It names the repository, the tag or
revision, and whether that repository is public.

**Public material** is whatever this repository or a release carries.
Evidence drawn from a consumer's private operation is **cleared** when its
custodian has released it for publication.

- **OUT-001** — The consumer guidance: choosing a version, choosing and obtaining material, copying it with its resources and notices, marking adaptations, hearing of a new edition, and what a copy does not carry with it. Its homes are those in CLM-001. Serves SOW-0019 and SOW-0025.
- **OUT-002** — The qualification of the named compatibility claim selected in CLM-005: the probe `tools/workflow_runtime/fixtures/app_workflow_reader.rs` and its observed result for a stated consumer revision and stated Library package bytes. Serves SOW-0020 and SOW-0025. The one observed result recorded, for the consumer revision in CLM-005, is in the [consumer basis](https://github.com/sgttomas/chirality-library/blob/1d536c58b787db14d544783667e0fbe4d8c44cbd/execution/PKG-05/DEL-05-01/Work/ConsumerBasis.md#named-reader-examination-and-reproduction) under "Named-reader examination and reproduction", at revision `1d536c58b787db14d544783667e0fbe4d8c44cbd`; the file is no longer in the tree. That result is for the package bytes it examined. The package's files have changed since, and no result is recorded for their current bytes.
- **OUT-003** — For each edition proposed to the owner, a publication candidate: the proposed name and tag, the exact source revision, the complete tracked-source archive and its checksum, the notices, dependencies and known limitations, and, where the candidate changes a rendered reading edition, that edition regenerated from its committed source by `docs/alignment-manual/render_manual.py`. Serves SOW-0022 and SOW-0025.
- **OUT-004** — The change account of each candidate against the prior edition; the update-inspection procedure in `README.md`; the comparison method for derivations, `workflows/compare-library-derivations/WORKFLOW.md`; and the inspection procedure exercised on the candidate against its prior basis. Serves SOW-0023 and SOW-0025.
- **OUT-005** — The recovery routes of CLM-004, each documented in the guide that refers to what it recovers or, for the pre-library transition, in the private repository's recovery note. Serves SOW-0026.

Homes and boundary:

- **CLM-001** — The guidance lives in existing guides, and in a shared file this deliverable's part is the passage named here. In `README.md`: within "Use the library", choosing a version, obtaining and copying, staying informed and deciding whether to update, with the optional command-line details, and the licence statement; which holding to start from, and the rest of the file, are navigation. `LICENSE.md` is the repository notice. In `workflows/README.md`: the passage on copying a complete package and the passage on reading private-archive citations. In `docs/alignment-manual/README.md`: "Read and render" and the statements of where retired and earlier editions are recovered; how each book is presented, what standing it has, and the difference between a discovery link and the edition a claim relies on are navigation. `workflows/compare-library-derivations/WORKFLOW.md`, the renderer `docs/alignment-manual/render_manual.py` with its pinned requirements, and the probe in OUT-002 are wholly this deliverable's; the rest of `tools/workflow_runtime/` is not.
- **CLM-002** — Navigation and the standing of each holding belong to `DEL-01-01`. The maintenance route, including review, integration, custody, the retirement of a holding and the definition of document metadata, belongs to `DEL-02-01`. The shared-reference repair belongs to `DEL-02-02`. Tool behaviour, tool usage guides and the implementation of any adapter belong to `DEL-03-01`. The retained historical source of the former repository-change evaluator belongs to `DEL-03-02`. The reconciliation method, the deliverable localities and the project-entry template belong to `DEL-04-01`. Reflective guidance, the decomposition and the content of *Chirality in Practice* belong to `DEL-04-02`. This deliverable supplies the conditions for obtaining, versioning, qualifying, publishing and inspecting; it does not supply those contributions.
- **CLM-003** — Publishing an edition is the owner's act. A consumer's data, adaptations, adoption and product release are that consumer's. Private evidence stays with its custodian until cleared. Scheduling, external delivery and unattended operation belong to the operator who configures them. The shared Library checkout that App v4's and SWBPIPE's standing instructions name is moved only on an explicit coordinator request or the owner's direction; a Library development checkout and other consumers are not so restricted.
- **CLM-004** — The recovery routes are these. The pre-library execution transition is the tag `archive/pre-library-execution-2026-10-31` at commit `f80f1510fb50799764720303b86c36da64b75d19` in the private `sgttomas/chirality` repository, whose `projects/FROZEN.md` describes that transition and the recovery of the frozen products. Holdings removed from this repository in its migration are in that repository's Git history at or before `05d96f3e11`. Original consumer pins, including the App's historical SWBPIPE source identity and the manual editions the App's original project definition named, resolve in that history, and the manual index says where each retired or earlier edition is. Editions from `library-v2.0.0` are tags and releases of this repository; earlier editions were released from the private repository.
- **CLM-005** — The named compatibility claim selected is that chirality-app's workflow-package reader, its `Snapshot` capture and declaration reading governed by that project's workflow-declaration and workspace-and-registration contracts, captures the Library's `coordinated-knowledge-work` package with each file's bytes and the package's content identity preserved and reads its declaration standing. Capture is read-only; registering or executing a package in that product is a separate act outside the claim. The consumer basis selected is chirality-app revision `366e7a6656d807142e7bdeda0ccf99c37d7227b1`; a claim against another consumer revision, interface or consumer is a new claim with its own contract and examination. No other consumer interface is selected.

Outside the product: a packaging system, a notice register, a subscriber
registry, a separate edition or history record, a companion or service, any
consumer's adoption work, and the release act itself.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The guidance gives independent routes to consult, invoke or copy selected material through ordinary files, Git, archives and documented interfaces. Reading needs no Git installation, and each tool's real dependencies are stated in that tool's guide. For the material selected, the guidance identifies the edition or full source revision, the resources the material needs, the applicable licence notices and the known limitations, and tells the consumer to keep original relative paths, record the selected basis and mark local adaptations. The guidance directs a consumer to a published edition by default and presents following `main` as an explicit choice to use development. Ordinary use depends on no undisclosed sibling checkout, dated run directory, private input or credential. The guidance says that a copy carries no authority: the Library's `AGENTS.md`, grants and execution rules govern work on the Library only. Source: PRD R13, R15, R17, §2.3; SOW-0019, SOW-0022, SOW-0025.
- **REQ-002** — A named compatibility claim is tested by exercising the consumer's own maintained reader or fixtures at an exact stated consumer revision against stated Library bytes. A generic demonstration or a Library component test does not establish it. The claim stands only for the bytes examined, and is examined again when a change affects the material that interface consumes. The probe runs in a disposable complete export of the consumer, changes nothing in the consumer's reader, resources, pins or repository, and is not part of ordinary Library use or the Library's CI. Before an incompatible change to an interface a named consumer uses, a supported path or coordinated adapter exists under the relevant authority; while it does not, that change is held and other work continues. Source: PRD R13, A6; SOW-0020.
- **REQ-003** — A candidate identifies its proposed edition name and tag, its exact source revision and its delivery form. The archive is built from the integrated Git objects of that revision, not from working files; every archived file's bytes and mode match that revision, and the checksum offered is the archive's. The candidate keeps the resources its material needs, the licence notices, the stated dependencies and the known limitations. A rendered reading edition it carries is the render route's output for an identified committed Markdown source and shows the source revision it was rendered from. Earlier editions and commit-pinned history stay reachable by their recovery routes. A merge is not a publication, and preparing a candidate publishes nothing. Source: PRD R15, A7; SOW-0022; decomposition card.
- **REQ-004** — The change account names the affected holdings, the old and new basis, the reason, the difference in meaning or use and the known migration consequences; a list of commits is not an account. The inspection procedure uses existing release and diff facilities, leaves the consumer's interests and last examined basis with the consumer, and distinguishes the basis in use from the editions examined. A failed or partial inspection states its limit: a failed query is not absence, a failed comparison is not "no change", and a path-limited comparison says nothing about other material. Inspecting adopts nothing. Hearing of a new edition uses the hosting service's own watch and feed facilities. Source: PRD R16, A7; SOW-0023.
- **REQ-005** — Each recovery route names its repository, its tag or revision and whether that repository is public. Historical bytes are verified at their identified source before they are relied on, and what was not examined or cannot be reached is said. Original consumer pins keep their meaning; no route rewrites history. Recovery reinstates no earlier commitment, lifecycle state, structure or frozen development. Source: PRD R12, R15, §6.3 step 2; SOW-0026.
- **REQ-006** — Guidance, candidate material, release notes and any evidence published with them pass the maintained credential check at the basis examined. A fixture or summary drawn from a consumer's private operation is public only when cleared; private operational data stays with its custodian. Source: PRD R17; SOW-0025.
- **REQ-007** — The outputs shall perform no act owned by another deliverable, as allocated in CLM-002: navigation and holding standing (`DEL-01-01`); the maintenance route and document metadata (`DEL-02-01`); the shared-reference repair (`DEL-02-02`); tool behaviour, tool guides and adapter implementation (`DEL-03-01`); the former evaluator's retained source (`DEL-03-02`); the reconciliation method, localities and project-entry template (`DEL-04-01`); reflective guidance, the decomposition and the book's content (`DEL-04-02`). Linking to a sibling's product, or applying it, takes nothing over.
- **REQ-008** — No output declares or implies an owner release, a consumer's adoption or product acceptance. None configures scheduling, external delivery or unattended operation. None creates a notice register, subscriber registry or separate edition history. Source: CLM-003; PRD R15, R16, §2.3.
- **REQ-009** — The comparison method for derivations is used when a consumer adopts an edition or explicitly selects a comparison, by that project's Agent 0 or a coordinator under that project's authority; the project's Agent 0 makes and integrates the edits. It compares the prior Library source, the project's adaptation and the target Library source together; without a prior baseline it compares adaptation with target and says that the history of each difference is unavailable. Deliberate local adaptations may remain. `metadata.upstream` is added or advanced only for a document wholly reconciled against the published edition recorded; a partial comparison leaves it unchanged. An improvement worth sharing goes to the Library's Agent 0 as a proposal. The method gives no authority to write in another project and requires no report, new checker or comparison at session start. Source: PRD R13, R16.

- **AC-001** — Following only the guidance, from an identified edition, a reader who did not write it obtains the edition and one selected holding without Git, finds the holding's required resources and its licence notice, and can state the source basis of what they hold. The obtained bytes equal the stated revision's, and a copied workflow package keeps its relative paths and resources. Each tool the guidance points to states its dependencies in its own guide. The guidance sends the reader to a published edition by default and names following `main` as an explicit development choice. No step needs a sibling checkout, dated run directory, private input or credential. Verified by VER-001. This is the obtaining part of PRD A6.
- **AC-002** — For the claim in CLM-005, the consumer's own reader at the stated consumer revision captures the stated Library package: every captured file's bytes equal the package's; the content identity the consumer's contract defines is unchanged when the package is relocated and changes when one resource's bytes change; the declaration standing is read as that contract defines it for a package carrying no declaration, with no declaration or hygiene finding; and the original package and the consumer's reader source are unchanged afterwards. The result names both revisions. No change that is incompatible with that reader's use of the material the claim covers is integrated until a supported path or coordinated adapter exists for that consumer; while none exists the change is held, and a probe result that shows the incompatibility is reported as a failure. Verified by VER-002. This is the named-compatibility part of PRD A6.
- **AC-003** — For the candidate: it has a proposed edition name and tag; its archive identifies the stated revision, and the archive's paths, bytes and modes equal that revision's tracked tree with nothing added; the checksum offered equals the archive's SHA-256; the licence notice and the required resources of the holdings the guidance offers are in the archive; dependencies and known limitations are stated; each rendered reading edition the candidate changes equals the render route's output for its stated source; and no text calls the candidate published before the owner publishes it. Verified by VER-003. Contributes to PRD A7.
- **AC-004** — The candidate's change account, read against the actual difference between the prior edition and the candidate, names each affected holding a consumer may have selected, its old and new basis, the reason, what changes in meaning or use and what a consumer must do or will lose, and separates known consequences from unknown ones. Verified by VER-004. Contributes to PRD A7.
- **AC-005** — The update-inspection procedure, followed on the candidate against the identified prior basis with the release and diff facilities it names, yields the comparison. The exercise distinguishes the basis in use from the material examined and leaves the selected basis unchanged. A comparison against an unavailable revision is reported as failed, not as no change. Verified by VER-005. Required for PRD A7.
- **AC-006** — Each route in CLM-004 is documented where OUT-005 places it, names its repository, tag or revision and whether it is public, and resolves when followed by someone with access. Historical bytes relied on equal the object at that source. What cannot be reached or was not examined is said, and no route restores earlier work. Verified by VER-006.
- **AC-007** — The public material of OUT-001 to OUT-005 at the examined basis passes the credential check, any published fixture or summary drawn from a consumer's operation is cleared, and the stated coverage of the screening is accurate. Verified by VER-007.
- **AC-008** — The outputs contain nothing CLM-002 allocates to a sibling as this deliverable's own, leave each act in CLM-003 with its owner, declare or imply no release, adoption or product acceptance, and add no notice register, subscriber registry or separate edition history. Verified by VER-008.
- **AC-009** — From the comparison method's text, a project's Agent 0 holding an adapted document, its Library source and a target edition can map the document to its source, compare the three or, lacking a prior baseline, the two while saying what is then unknown, settle each consequential difference as kept, changed locally, proposed upstream or unresolved, and tell whether `metadata.upstream` may be added or advanced. Nothing in the method writes in another project or requires a report, a new checker or a comparison at session start. Verified by VER-009.

## Production and Verification Method — Praxeology

Choices that define the product:

- Ordinary facilities carry everything: files, Git, archives, the repository's
  releases and its comparison view. Nothing bespoke is added for a need they
  meet.
- Guidance lives in the existing guides named in CLM-001. There is no separate
  consumer manual.
- An edition's change account is its release notes, assembled from the pull
  requests integrated since the prior edition. The result of an examination is
  reported in the pull request that carries it and, where a consumer relies on
  it, in the release notes. The repository keeps no second record of either.
- A candidate's archive is taken from the integrated revision's Git objects
  after integration; a later revision needs its own archive.
- A rendered reading edition is regenerated from its Markdown; the HTML is
  never edited by hand.
- Named compatibility is examined by running the consumer's own reader, not a
  Library reimplementation of it.
- Derivations are compared at adoption or on explicit selection, never
  routinely.

- **VER-001** — Judgment by a reader who did not write the guidance (follows it on an identified edition, outside any Git checkout), with comparison with a named reference (the stated revision's Git objects and the release checksum): download the edition's archive from its release, verify the checksum, extract and read a selected role or workflow and its resources without Git, copy one workflow package and compare its files with the revision's blobs, find the licence notice, confirm each tool guide the route points to states its dependencies, confirm the guidance leads to a published edition by default and presents following `main` as an explicit development choice, and report any step that needed something the guidance did not name.
- **VER-002** — Executable check (the probe, which observes the consumer's own reader capturing the stated package) and comparison with a named reference (the consumer's contract at the stated revision, and SHA-256 digests of the package files taken from the Library revision's Git blobs): in a disposable complete export of the consumer at the stated revision, attach the probe as a test module, run it offline against an unmodified export of the package, and read its result for byte equality, identity under relocation and under a changed resource, declaration reading and findings; confirm the export's reader source is unchanged and state both revisions with the result. Judgment by the integration owner (reads any change to the package or its form against the probe result): confirm that an incompatible change has a supported path or coordinated adapter in place, or is held.
- **VER-003** — Comparison with a named reference (the Git objects of the stated revision), an executable check (the renderer's `--check`, which observes only that the committed HTML equals a fresh render of the stated source) and judgment by the integration owner (reads the notes and the rendered form): identify the archive's revision with `git get-tar-commit-id`, compare every archived path, byte and mode with that revision's tracked tree, recompute the SHA-256, confirm `LICENSE.md` and the offered holdings' resources are present, run the render check for each rendered edition the candidate changes and inspect it at desktop and narrow widths, and read the notes for name, dependencies, limitations and standing.
- **VER-004** — Judgment by a reviewer who did not write the account (reads it against `git diff <prior edition> <candidate>` and the pull requests integrated between them): for each changed holding a consumer may have selected, confirm the account gives its old and new basis, the reason, the change in meaning or use and the migration consequence, and that unknown consequences are marked unknown.
- **VER-005** — Executable check (the procedure's own commands, which observe the release listing and the difference between two real bases) and judgment by the integration owner (reads what the exercise reports): from a clone whose selected basis is the prior edition, follow "Decide whether to update" with its command-line details, compare selected paths with the candidate, repeat the comparison against a revision that does not exist, and confirm the failure is reported as a failure and the selected basis is unchanged.
- **VER-006** — Comparison with a named reference (the Git objects at each route's stated repository and revision): follow each recovery route from where it is documented, resolve its tag or revision, and compare the bytes relied on with that object; for a repository the examiner cannot read, say so and report nothing there as verified; read the guidance for anything that would restart archived work.
- **VER-007** — Executable check (the credential scan, which observes only the patterns it holds, in text files added or modified between two revisions) and judgment by the custodian of any consumer-derived fixture (that it is cleared): run `python3 tools/validation/validate_run_record_leaks.py --base <base> --head <head>` over the change and, for a candidate, over its whole tracked tree with the empty tree as base, and state what the scan does not cover.
- **VER-008** — Judgment by a reader who did not write the outputs (reads the guidance, the candidate's notes and the qualification result): take each allocation in CLM-002 and each act in CLM-003 in turn and look for text that takes it over, for any statement of release, adoption or acceptance, and for a register, registry or separate history.
- **VER-009** — Judgment by a reader who did not write the method (works one real adapted project document against its Library source at a prior and a target edition): follow the method step by step, record whether each act in AC-009 can be taken from the text alone, and read it for any write in another project or any required report, checker or routine comparison.

## Governing Values and Decisions — Axiology

- **AX-001** — The consumer chooses. Better is fewer things a consumer must take on trust to know what they hold and what changed: fewer statements in the guidance or the notes that cannot be checked against the release, the archive or Git. That may never be gained by acting for the consumer; no route updates, adopts or implies adoption on a consumer's behalf, and publication stays with the owner.
- **AX-002** — Source identity and truthful standing. Better is fewer claims in the guidance, the notes or a qualification that reach further than the examination behind them. That count may never be improved by leaving out a failed or partial result, or by reporting one as no change.
- **AX-003** — Ordinary means and the least maintained material. Better is less maintained text and fewer bespoke artefacts per edition for the same consumer result. That economy may never drop a notice, a required resource, a stated dependency, a known limitation or a recovery route.

## Output and Evaluation Matrix

AC-007 and AC-008 apply to every output. Each is listed once, against the
output that carries most of what it examines.

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | OBJ-002, OBJ-005 | REQ-001, CLM-001 | AC-001 | VER-001 | What the route must allow, and that a published edition is the default, comes from PRD R13, R15, R17 and A6. The obtained bytes are compared with the stated revision's Git objects and the release checksum, which the guidance did not write. Whether the text is enough is judged by a reader who did not write it. |
| OUT-002 | OBJ-003, OBJ-005 | REQ-002, CLM-005 | AC-002 | VER-002 | The expected behaviour comes from the consumer's own contract and reader at the stated revision, an outside reference that imports no Library code. The expected file digests come from the Library revision's Git blobs. The probe only drives that reader. That a supported path or adapter precedes an incompatible change comes from PRD R13; whether one is in place is judged by the integration owner from the change and the probe result. |
| OUT-003 | OBJ-003, OBJ-005 | REQ-003 | AC-003 | VER-003 | What a candidate must carry comes from PRD R15 and A7 and the definition of an edition in the Ontology. Archive identity is compared with the Git objects of the stated revision. The render check compares committed HTML with the renderer's own fresh output, so it only guards against divergence; the rendered form is judged by reading it. |
| OUT-004 | OBJ-003, OBJ-005 | REQ-004 | AC-004 | VER-004 | What an account must explain comes from PRD R16. It is compared with the actual Git difference between the two bases by a reviewer who did not write it. |
| OUT-004 | OBJ-003, OBJ-005 | REQ-004 | AC-005 | VER-005 | What the procedure must do, including that a failed comparison is not "no change", comes from PRD R16 and A7. The comparison is produced by Git and the hosting service's release listing on two real bases. |
| OUT-004 | OBJ-003, OBJ-005 | REQ-009 | AC-009 | VER-009 | What the method must do is stated in REQ-009, under PRD R13 and R16. Whether the text delivers it is judged on a real adapted document by a reader who did not write the method. |
| OUT-005 | OBJ-003, OBJ-005 | REQ-005, CLM-004 | AC-006 | VER-006 | What must stay recoverable comes from SOW-0026 and PRD R15. Bytes are compared with the Git objects at each route's stated source. |
| OUT-003 | OBJ-002, OBJ-005 | REQ-006, CLM-003 | AC-007 | VER-007 | What may be public comes from PRD R17. The credential scan is the Library's own tool: a pass shows none of the patterns it holds in the text files it read. Clearance is the custodian's judgment. |
| OUT-001 | OBJ-003, OBJ-005 | REQ-007, REQ-008, CLM-002, CLM-003 | AC-008 | VER-008 | The sibling allocation comes from decomposition §9 and the reserved acts from PRD §2.3, R15 and R16. Judged by a reader who did not write the outputs. |
