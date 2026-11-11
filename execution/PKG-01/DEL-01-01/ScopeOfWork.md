---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-01
package_id: PKG-01
decomposition_basis: execution/_Decomposition/PROJECT_DECOMP.md
project_scope_refs: [SOW-0001, SOW-0002, SOW-0003]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-003, OBJ-005]
---

# A usable route into the selected library

## Purpose and Objective Traceability

Given a bounded maintenance brief, a maintainer finds the holding, the method,
the standing of each source, the deliverable locality and the unresolved
conditions that apply, without treating an index or an inferred relationship
as authority. This deliverable contributes the route that makes that possible:
the entry a session or a reader starts from; the statement, at each holding's
own entry, of what the holding is for and how far it governs; and the
instructions for searching, following references and querying when the entry
does not already lead to the answer.

Its allocation is the DEL-01-01 card of the
[accepted decomposition](../../_Decomposition/PROJECT_DECOMP.md), in package
PKG-01, Library access, with the interface "Entry and consumer guidance" in
that document's §9. It serves [PRD](../../../docs/PRD.md) objective O1 and
contributes to O2, O3 and O5.

| Scope item | What this deliverable contributes | Objectives | PRD |
|---|---|---|---|
| SOW-0001 | A starting route that can itself be located, from a bounded undertaking to the selected basis, the repository and role instructions that apply, the relevant holdings and the deliverable localities; and the way to the entry's own maintenance, each revision of the entry made under the entry that precedes it | OBJ-001, OBJ-002 (O1, O2) | R01, R06; A1 and the entry's part of A5 |
| SOW-0002 | Holdings intelligible where they live: purpose, applicability, standing, resources, outputs and limits, with explanation, instruction, example, proposal and historical source told apart, and the resources and notices a copy must carry named and kept | OBJ-001, OBJ-003, OBJ-005 (O1, O3, O5) | R02; A1 and the source and resource part of A6 |
| SOW-0003 | Instructions for purposeful search, following references and structured queries, with source identity, declared, inferred and unknown relationships and search limits visible; consumed indexes kept and regenerated from their owning sources | OBJ-001, OBJ-003, OBJ-005 (O1, O3, O5) | R03; A1 |

## Deliverable Definition — Ontology

A **bounded brief** is the undertaking a maintainer brings, stated in the
conversation. The entry starts none.

The **selected basis** is the identified source revision or edition that
actually governs a use. A proposed replacement, or a newer publication that
was only examined, does not replace it.

A **holding** is library content: a role, a workflow, a tool and its guide, a
publication, a reference or a deliverable locality. Its **standing** says
whether and how it governs the present use: instruction, explanation, example,
proposal or historical source.

A **discovery pointer** is a stable link, anchor or index entry that locates a
holding. It selects no edition, decides no applicability and confers no
authority.

A **declared relationship** is one its owning source states. An **inferred
relationship** is a labelled interpretation and binds nothing. An **unknown**
is a binding not established or an area not searched, and it stays visible.

A **locality** is `execution/PKG-nn/DEL-nn-nn/`, holding a deliverable's scope
and its needs. A **current-work link** is a link from the route to a locality
as the place where work on a subject is carried. The directory's presence is
not evidence that the work is usable or complete.

A **consumed index** is a listing or named location that tools, products or
other holdings read to find a holding: `workflows/index.json`,
`workflows/catalog.yaml`, and the anchors and section headings that consumers
and other holdings cite.

- **OUT-001** — The entry route. For a session it is `init-prompt.md`, then `AGENTS.md` (which `CLAUDE.md` includes), whose development entry leads to the PRD, the accepted decomposition, the deliverable scopes with their needs, the active role file and the method index. For a reader it is `README.md`, which offers the holdings by purpose and sends a contributor to `AGENTS.md`. Serves SOW-0001 and SOW-0002.
- **OUT-002** — The standing and local-use statements for the holdings the route leads to, each at the holding's own entry or index: the README's selection table, `workflows/README.md`, the publication index `docs/alignment-manual/README.md`, the thesis index `docs/thesis/README.md` and the course index `docs/human-team-courses/README.md`. Serves SOW-0002.
- **OUT-003** — Directed-discovery instructions attached to the entry route, one bounded worked example, and the consumed indexes. The worked example is the entry's own case: from the brief to revise the entry, a purpose search of the scopes locates this scope, and `python3 -m tools.deliverables --project . neighborhood DEL-01-01` shows its declared inputs and its consumers. Serves SOW-0003 and SOW-0001.

These are parts of one route, not three files. An existing entry, index or
guide carries a statement before any new file does. A separate guide file
exists only where a reader's need requires one, and it is linked from the
entry.

- **CLM-002** — The publication standings the route presents. *Chirality in Practice* is a maintained reflective book: material for reflection, not an execution instruction and not required reading before work. Consolidated v9 is a retained historical manual, and earlier manual editions are historical sources recoverable from the private `sgttomas/chirality` repository. The thesis is explanatory, nonbinding research. Each keeps its own discovery link and anchor. A reader who wants a working method is sent to the roles and the workflow guide, to be used under their own project's instructions.

Boundary:

- **CLM-003** — What a disputed shared definition or reference means, and where it applies, is settled by `DEL-02-02`. What a query, resolver or validator does, and its usage contract, belong to `DEL-03-01`. How `workflows/index.json` is generated from package metadata is the generator `tools/validation/build_workflow_index.py`'s; this deliverable answers for the index being present, connected to its source and current. Which deliverable answers for that generator is undecided. The route locates those sources and reports their limits.
- **CLM-004** — Obtaining and copying, version selection, update inspection, named compatibility evidence and publication preparation belong to `DEL-05-01`. In `README.md` this deliverable's part is the opening identity, the table that offers holdings by purpose and the section that sends a contributor to `AGENTS.md` and the PRD. In `workflows/README.md` it is how a method is selected, loaded and identified and how the catalog and index relate to package metadata. In `docs/alignment-manual/README.md` it is what each publication is for, its standing, and the difference between a discovery link and the edition a claim relies on. In those files `DEL-05-01`'s part is choosing a version, copying material or a package, staying informed, deciding whether to update, edition recovery, and reading and rendering. A shared file has one editor per change, and the combined result is checked together.
- **CLM-005** — The deliverable localities, their formation and their needs belong to `DEL-04-01`, and the accepted decomposition to `DEL-04-02`. In `AGENTS.md` this deliverable's part is the opening identity and the table of where work happens; the development entry's opening and its section on locating the selected work; the sentences that send a reader to the active role file, the method index and the selection rule; and the rule that consumed indexes are regenerated from their owning sources. In that file the working cycle's reconciliation rule and method pointer are `DEL-04-01`'s, and the standing rules on holding changes, recovery, review and integration are maintenance guidance of `DEL-02-01`. In the course index this deliverable's part is the opening passage that says who the series is for and where the book, the roles and the methods are, not the lessons or their assessment.
- **CLM-006** — PKG-01 holds the boundary of SOW-0028: a standing global audit, a central relationship graph, a subscriber or notice registry, automated project management and a complete census or dependency graph are outside the Library. Consumed indexes and bounded views derived on demand stay in scope. Further tooling or a companion enters only on a demonstrated gap, under SOW-0033 in PKG-03. Changes to commitments and protected baselines, risk acceptance, acceptance of a result, release, further archival removal and reactivation of frozen work belong to the owner; discovery and recovery supply no authority for them.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The entry connects a bounded brief to the selected basis, the repository and role instructions that apply, the relevant holdings, the method, the deliverable locality and the conditions still unresolved. It says which repository this is and that records written before 2026-11-05 call it "Root". Opening a session starts no undertaking. The entry is found from the repository root and leads to where the entry itself is changed. A revision of the entry is reviewed under the entry that precedes it, which stays usable and recoverable until the replacement is verified and adopted; proposed entry text does not authorise itself and does not change the basis of its own review. The rule for revising any holding is `DEL-02-01`'s; this deliverable answers for it being kept for the entry. Source: SOW-0001; PRD R01, R06, A5.
- **REQ-002** — For each holding the route traverses for a brief, the holding's own entry says what it is for, when it applies, its standing, the inputs, resources and notices it requires, what it yields and its limits. Explanation, instruction, example, proposal and historical source are told apart; a historical or frozen holding is presented as such, with where it is recoverable. A publication pointer resolves to the maintained source and names its edition; where a claim relies on exact content, the route says to identify the edition and source revision. A discovery link or anchor is not repointed to a different edition without saying so. Required resources and notices are preserved when material is copied or packaged: a holding's entry names them so that a copy can carry them, and a traversed holding that is itself a copy or a package of other material carries those its source requires. The routes by which a consumer obtains and copies material, and what those routes keep, are `DEL-05-01`'s (CLM-004). The standings in CLM-002 are presented as stated there. Source: SOW-0002; PRD R02.
- **REQ-003** — The route gives instructions for purposeful file and content search, for following references and for structured queries. They have the inquirer state the question, the source basis, the bounds and what was not searched, tell declarations from inferences and unknowns, and read the selected material; no index substitutes for that reading. A consumed index is kept, or migrated deliberately with its readers checked. A generated index is regenerated from its owning source when that source changes and is never edited by hand. An anchor or heading that a consumer or another holding cites keeps resolving to the same subject; `Working cycle` in `AGENTS.md`, which App v4 cites, is one. Source: SOW-0003; PRD R03.
- **REQ-004** — A current-work link uses the accepted numeric identity and resolves to a locality that exists with its scope and declared needs. What the route says of a locality, including how far its work has come, rests on its scope, its needs and the code its pointers name, with unresolved input conditions shown. A proposed path, a present directory, an empty needs list, a merge or a structural pass is never presented as usable work, suitability or completion. Source: decomposition card and §8.1; PRD R08, R09, R10; CLM-005.
- **REQ-005** — Each command the route shows states where it is run, its prerequisites and its limits, and behaves as the route says. The deliverable queries require Python 3, PyYAML, Git and a resolvable `HEAD`; ordinary reading requires none of them, and the route does not imply that the queries run without Git. Where a query cannot run, the route gives direct reading of the declarations as the fallback and says what that reading does not reproduce, such as the transitive view a query computes. A command, workflow or capability is advertised only where it exists at the revision viewed; an accepted scope or allocation is not an available capability. Source: decomposition card and §9; PRD R03, R05, R17; CLM-003.
- **REQ-006** — The route contains no act that belongs to another deliverable. It does not settle what a disputed shared definition or reference means (`DEL-02-02`, CLM-003); define the behaviour of a query, resolver or validator (`DEL-03-01`, CLM-003) or of the index generator (CLM-003); state obtaining, version, update, compatibility or publication obligations, linking to the owning guidance where it would repeat such a claim (`DEL-05-01`, CLM-004); form or reconcile another locality (`DEL-04-01`, CLM-005); or restate the decomposition (`DEL-04-02`, CLM-005). It locates and explains those sources, and a change one of them needs goes to its owner.
- **REQ-007** — The route is not, and does not require, a global inventory, a central relationship graph or a registry, and it makes no claim to list every holding or relationship. It requires no companion installation and calls for no tool the Library does not already hold; a gap found in discovery is reported under SOW-0033, not filled here. It claims or implies no consumer's adoption of Library material and imposes none; App v4 and SWBPIPE decide their own adoption. It removes no retained archival holding, reactivates no frozen work, changes no commitment or protected baseline, accepts no risk or result and publishes no release; those stay with the owner (CLM-006). It contains no credentials, private source content or machine-specific private detail. Source: CLM-006; decomposition card, Boundary; PRD §2.3, R17.

- **AC-001** — A maintainer with an actual bounded brief, starting from `init-prompt.md` or from `README.md` and following only what the route says, reaches the selected basis; `AGENTS.md` and the role file that applies; the PRD and the accepted decomposition; the scope and needs of the deliverable the brief concerns; the relevant holding and method; and the conditions on them that are unresolved. With the brief to revise the entry, the same route leads to this scope and to the files that hold the entry. Nothing on the route starts work the brief did not ask for. Verify with VER-001. PRD A1 and the entry's part of A5.
- **AC-002** — Each holding traversed for the brief in AC-001 states at its own entry its purpose, applicability, standing, required resources and notices, outputs and limits. Each publication link resolves to the named edition's source file. The publication index presents *Chirality in Practice* as material for reflection, with its edition and source paths, separate from execution instructions and from the historical manuals; the thesis index presents the thesis as explanatory and nonbinding; and `README.md` links to both. Historical and frozen holdings read as historical. A traversed holding that is a copy or a package of other material carries the resources and notices its source requires. The route separates following a discovery link from citing an exact edition and revision. Verify with VER-002. PRD R02 and A1, and the source and resource part of A6 without any claim of named compatibility.
- **AC-003** — The discovery instructions cover file and content search, reference following and structured queries, and have the inquirer state the question, the basis, the bounds and what was not searched. The worked example, replayed against the sources it names, returns what the route says, with each relationship labelled declared, inferred or unknown and each source named by its identity. `workflows/index.json` equals what the generator produces from the workflow packages' metadata, and every workflow `workflows/catalog.yaml` names is a package that exists. Every anchor and heading the Library's own holdings cite in the route's files resolves, and the headings REQ-003 names are present. Nothing in the route claims a complete inventory or graph. Verify with VER-003. PRD R03 and A1.
- **AC-004** — Every command the route shows, run from the stated location with the stated prerequisites, returns what the route says. With a prerequisite absent, the failure and the fallback are the ones the route states, with the fallback's limit. No command, workflow or capability is shown that does not exist at the revision examined. A reading of the text is not evidence of a command's behaviour. Verify with VER-004.
- **AC-005** — Every current-work link in the route resolves to a locality whose numeric identity the accepted decomposition allocates and whose scope and needs exist. Nothing the route says about a locality presents a path, an empty needs list, a merge or a structural pass as usable work or completion. Where a locality the brief needs is not usable, the route still leads to everything else in AC-001. Verify with VER-005.
- **AC-006** — The route contains none of the acts REQ-006 and REQ-007 exclude: no settled disputed meaning, no tool behaviour defined in navigation text, no obtaining, version, update, compatibility or publication obligation, no formation of another locality, no inventory, graph or registry, no required companion, no claim of a consumer's adoption, and no archival removal, reactivation of frozen work or other act CLM-006 leaves with the owner. Navigation text in a shared file stays within the parts CLM-004 and CLM-005 give this deliverable. The route's files pass the credential scan. Verify with VER-006.
- **AC-007** — For a revision of the entry, the review was made under the entry that preceded it; both the revised entry and the route used to maintain it were checked; the preceding entry is recoverable from Git and stayed usable until the replacement was adopted; and the adoption names who adopted it and under what authority. Verify with VER-007. PRD R06 and the entry's part of A5.

## Production and Verification Method — Praxeology

Choices that define the product:

- The route lives in the existing entry files and in each holding's own index
  or guide. Publications, tools and instructions keep their homes, and the
  route points to them without copying them.
- The undertaking comes from the conversation. The entry orients and waits.
- An index locates a source, and reading the source decides what applies.
  Generated indexes come from package metadata through the generator.
- A stable link is for discovery, and a named edition and source revision are
  for reliance.
- Structured queries are used where they run. Elsewhere the declarations are
  read directly and the limit of that reading is stated.
- Discovery is bounded by the brief. A view may be partial, cyclic and revised
  as the inquiry changes, provided it is labelled.

- **VER-001** — Judgment by a reader who did not write the route (reads only what the route says, against the repository files it leads to): starting from `init-prompt.md` and again from `README.md` with an actual bounded brief, follow the route and record, for each item AC-001 names, whether the text led there, which paths were read and where the reader relied on something the route did not say. Repeat with the brief to revise the entry.
- **VER-002** — Judgment by a reader who did not write the statements, with comparison against each holding's owning source: for each holding traversed for the brief, read its entry for the six facets and its standing. Follow each publication link to the edition and source file it names and compare what the index says of the publication with the publication's own header and contents. Inspect any traversed copy or package for the resources and notices its source requires. Compare each discovery anchor with the edition it resolved to before the change under examination.
- **VER-003** — Comparison with a named reference (the sources the worked example names) and executable checks (`python3 tools/validation/build_workflow_index.py --check`, which observes whether the committed index equals what the package metadata generate, and a link check, which observes whether cited paths and anchors resolve): replay the example's search and query steps and compare what they return with what the route says. Read each relationship's label against the declaration it cites, and read the route for any claim of a complete inventory or graph. The result covers only the holdings the example reached.
- **VER-004** — Executable check (observes each command's exit status and output against what the route states and what the tool's own guide states): run every command the route shows from the location and with the prerequisites it gives. Run one query with a prerequisite removed in an isolated process and compare the failure and the fallback with the route's statement. Search the route for commands, workflows and capabilities and confirm each exists at the revision examined.
- **VER-005** — Executable checks (`python3 -m tools.deliverables --project . check` and `zsh tools/validation/check_min_viable_fileset.sh --current <locality> <DEL-ID>`, which observe structure only) and judgment by a reader who did not write the route: resolve every locality link in the route against the identities the accepted decomposition allocates and the files present, and read what the route says of each locality for any claim of usability, suitability or completion that rests on a path, an empty needs list, a merge or a structural pass. The structural result and the reading are separate findings.
- **VER-006** — Judgment by a reader who did not write the route, with an executable check (the credential scan `python3 tools/validation/validate_run_record_leaks.py --base <base> --head <head>`, which observes only the patterns it holds): read the route's files for each act REQ-006 and REQ-007 exclude and, in each shared file, for navigation text outside the parts CLM-004 and CLM-005 give this deliverable. State what the scan did not cover.
- **VER-007** — Comparison with a named reference (the preceding entry, recovered from Git history) and judgment by a reader who did not make the revision: for a revision of the entry, recover the entry files as they stood before it. Confirm from the review record that the revision was judged under them, that the revised entry was checked as in VER-001 and the route used to maintain it was checked as well, that the preceding entry stayed usable until adoption, and who adopted the replacement under what authority.

## Governing Values and Decisions — Axiology

- **AX-001** — Discovery serves the brief. Better is fewer steps and less reading between a bounded brief and the scope, holding and method that govern it. That may never be gained by presenting an index, an inferred relationship or a present path as authority, or by hiding an unknown or an area not searched.
- **AX-002** — Standing governs reliance. Better is fewer holdings whose entry leaves a reader unsure what the holding is for or whether it governs their use. That may never be gained by moving a reader off the edition or basis they selected without saying so, or by letting an explanation read as an instruction.
- **AX-003** — Reuse and locality. Better is less navigation text to keep true: a statement lives once, at the holding it describes, and the route links to it. That may never be gained by leaving a cited anchor or a consumed index broken, by editing a generated index by hand, or by adding an inventory or registry.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-0001, OBJ-001, OBJ-002 | REQ-001 | AC-001 | VER-001 | What the route must reach comes from PRD R01 and A1. Whether it reaches it is judged by a reader who did not write the route, against the repository files the route leads to. |
| OUT-002 | SOW-0002, OBJ-001, OBJ-003, OBJ-005 | REQ-002, CLM-002 | AC-002 | VER-002 | The facets come from PRD R02, and the publication standings are those CLM-002 states. What each entry must agree with is the holding's own source, which the route did not write. |
| OUT-003 | SOW-0003, OBJ-001, OBJ-003, OBJ-005 | REQ-003 | AC-003 | VER-003 | What discovery must show comes from PRD R03. The example's expected result is what its named sources return on replay. The index's expected content is what the workflow packages' metadata generate; the generator is the Library's own tool and shows agreement between index and metadata, not that the metadata are right. |
| OUT-003 | SOW-0003, OBJ-001, OBJ-002 | REQ-005, CLM-003 | AC-004 | VER-004 | The expected behaviour of a command comes from the tool's own guide, which DEL-03-01 owns, and from running the command. The route's text is the thing compared, not the source of the expected result. |
| OUT-001 | SOW-0001, OBJ-001, OBJ-002 | REQ-004, CLM-005 | AC-005 | VER-005 | The identities come from the accepted decomposition, and the localities are read as they stand. The deliverables check and the locality check are the Library's own tools and show structure only. |
| OUT-001 | SOW-0001, SOW-0002, SOW-0003, OBJ-001, OBJ-003, OBJ-005 | REQ-006, REQ-007, CLM-003, CLM-004, CLM-005, CLM-006 | AC-006 | VER-006 | The excluded acts and their owners come from decomposition §9, the Boundary of the DEL-01-01 card, the PKG-01 boundary of SOW-0028 and PRD §2.3 and R17. The reading is by someone who did not write the route. The credential scan is the Library's own tool and covers only the patterns it holds. |
| OUT-001 | SOW-0001, OBJ-001, OBJ-002 | REQ-001 | AC-007 | VER-007 | The rule comes from PRD R06 and A5. The preceding entry is read from Git history, which the revision did not write, and the judgment is by a reader who did not make the revision. |
