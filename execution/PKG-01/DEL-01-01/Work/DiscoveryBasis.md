# Discovery basis and open work

> **Naming (2026-11-05):** "Root" in this record means what is now the
> Chirality Library (`sgttomas/chirality-library`). Chirality Root is now the
> separate private `sgttomas/chirality`. See
> [AGENTS.md](../../../../AGENTS.md#library-and-root).

For the accepted R18/A9 increment, see [Evaluation extension](#evaluation-extension).
Earlier case/basis statements below retain their recorded subjects and limits.

Maturity: maintained entry route; product-wide fulfillment remains unestablished. Use the
adjacent ScopeOfWork for commitments and evaluation; this note holds the source
assessment, design choices and limits of the current bounded work.

## Current route

The maintained entry route connects `init/init-prompt.md`, `AGENTS.md` and
`loop/LOOP_INIT.md` to the selected maintenance basis and actual local work.
The loop identifies the product aim and the route into the discovery locality;
the PRD, decomposition, scopes and methods retain their own commitments.
[Top-level operating entry](#top-level-operating-entry) describes the current
arrangement. Product-wide fulfillment remains unestablished.

Comparable public entry files inspected at their identified revisions were
[App](https://github.com/sgttomas/chirality-app/blob/032725d32b67e117b8e1fb2b5fa9aa47b30de12e/loop/LOOP_INIT.md)
and [SWBPIPE](https://github.com/sgttomas/SWBPIPE/blob/bc9f7961acee72441ec06c104ed97d4f1c77faa4/loop/LOOP_INIT.md).
Their pattern connects purpose and governing basis to the affected locality;
their product-specific permissions and arrangements do not govern the Library.

## Available sources

The initial setup assessment used repository commit
`fd847ac9ac68250b2f35d2e9c0087c16e86b510a`. The following holdings remain reusable:

- `README.md`, `AGENTS.md` and `loop/LOOP_INIT.md` provide the current entry
  route and connect it to the accepted decomposition and discovery locality.
  The earlier assessment used `execution/_Coordination/LOOP_INIT.md`.
- `workflows/README.md` describes explicit selection, reading selected resources,
  source-qualified identity and collisions. `workflows/catalog.yaml` supplies
  library identity/central selection; `workflows/index.json` is generated from
  owning package metadata. Preserve those consumed surfaces rather than create
  a parallel inventory. Which entries fit a later brief still requires inspection.
- `docs/alignment-manual/README.md` provides a stable discovery route to a named
  edition. A source-dependent claim needs the resolved edition and revision;
  following a versionless pointer does not amend an accepted basis.
- `docs/thesis/README.md` labels the thesis as explanatory, nonbinding research
  and distinguishes its source/evidence standing from development authority.
- `tools/deliverables/README.md` states the actual Git/HEAD, Python and PyYAML
  prerequisites, explicit project selection and limits of query results.
  Direct source inspection is its documented fallback; it is not a Git-free
  implementation of the query commands.

## How the parts fit

Discovery starts with the undertaking's question, follows relevant references
and reads selected sources. A useful route can cross publications, instructions,
tools and local work without declaring a complete inventory or global graph.
An index locates a source; it neither decides applicability nor confers authority.

DEL-05-01 owns obtaining/version/update/compatibility guidance. This deliverable
locates and interprets that guidance for the selected inquiry. A shared README
edit needs one editor and combined examination of both contributions. Disputed
reference meaning goes to DEL-02-02, while executable query behavior belongs to
DEL-03-01. These boundaries do not prevent ordinary navigation work using the
existing maintained sources.

Formation material is supplied through the actual localities, with DEL-04-01
accounting for setup/reconciliation practice. Before presenting a current-work
link as usable, inspect that particular locality's scope, work and input
conditions. An accepted identity and a prepared directory establish less than
an authored, examined contribution. Do not wait for an entire supplier deliverable
to be complete where the particular source is already fit for use.

## Bounded discovery examination

At the entry-revision basis `11bdb448323877268c90296a5497fd71ede1baee`,
the question was where to carry the requested revision and what would govern it. The session prompt leads through unchanged AGENTS and HELP_HUMAN
to the proposed loop. The loop identifies the accepted product/decomposition
basis and gives a concrete route back to this ScopeOfWork and Work. Search is
bounded to current Root scope files, not archives or an inferred global backlog:

```sh
rg -n 'LOOP_INIT' execution/PKG-*/DEL-*/ScopeOfWork.md
python3 -m tools.deliverables --project . neighborhood DEL-01-01
```

The first command locates the entry's output home. The second exposes the
declared input/use conditions and native consumers. Read their owning sources
before judging relevance or suitability. The accepted formation/localities and
maintained query guide support this entry case; the query's unknown-suitability
fields are not a refusal or a completion claim. Its references to shared-meaning
and consumer-use work are conditional: this proposal changes neither adopted
product contracts nor publication/compatibility claims.

This bounded examination does not establish all publication traversal, command
failure behavior, consumer qualification or the complete A1/A5 result.

Needs in `../deliverable.yaml` retain these cases and conditions. They
do not assert satisfaction or assign work to another contributor. Unknown
consumer qualification/publication bases remain with DEL-05-01 and matter here
only if the route repeats such claims. Additional archival disposition and
conditional tooling remain under their accepted authority limits.


## Fresh-reader maintenance route examination after the 60% decision

A fresh-reader examination considered how a maintainer should preserve
workflow-package identity when revising an explanatory companion, identify
affected uses and leave the work recoverable.
The source basis was `047da79894bc5631dca564a30113f2cd26ec7ae1`; the loop also
contained Agent 0's uncommitted record of the owner's 60% decision. This was
first-use evidence for this brief, not an independent review or universal
usability claim. No package amendment was assumed or invented.

The route went from AGENTS and LOOP_INIT to a purpose search of current scopes,
which selected DEL-02-01. Its scope, Work and needs led through the workflow
guide and canonical package metadata to create-workflow. The manual index led
to Consolidated v9 Authorship/use and §§6.1–6.6. AGENTS directly supplied the
consumer and recovery routes. Reading those sources distinguished mutable
navigation from exact-content reliance, a content change from consumer adoption,
and recoverable historical work from authority to restart it. The contributor
found no substantive gap requiring a package or companion edit.

Actual read-only resolver, neighborhood and impact commands succeeded:

```sh
python3 -B tools/workflow_runtime/resolve_workflow.py --root . --role TASK --workflow create-workflow
python3 -B -m tools.deliverables --project . neighborhood DEL-02-01
python3 -B -m tools.deliverables --project . impact DEL-02-01
```

The resolver retained source-qualified identity and fingerprints. The direct
consumer view named DEL-03-01, DEL-04-01 and DEL-05-01; transitive impact reached
all six other deliverables. The contributor inspected conditions and treated
that breadth as a discovery lead, not an edit list or suitability verdict.
The optional execution.json was absent in the selected package; that matched
its documented optional status and required no invented companion.

The inspected v9 Markdown hash was
`e7efc7c22515f62964af344fe6058bab96240af3f9a96fe32323d10b8128b6f7`.
Its bytes matched the HTML's named rendering source at
`6472b49b2a6c7ebf4db1356d7bf83fa3af412305`. This verifies the selected source
identity, not a fresh rendering or visual examination.

For the unavailable-command case, one isolated subprocess set PATH to a
nonexistent controlled location; python3 was unavailable and returned exit127.
This was a labelled simulation, not an actual host outage. The contributor then
read the supplier YAML and the three direct consumers' declarations as the
documented fallback. Their conditions and triggers were inspectable, but this
manual reading did not reproduce transitive closure or prove complete coverage.
The host environment and repository source bytes remained unchanged.

Q-04/Q-05 are claim-specific: the named-reader and manual cases in ConsumerBasis
do not resolve every neighboring adopted-interface need. This adds bounded
publication traversal and fallback evidence toward AC-002/003/004; it does not
claim all discovery, tool failure, compatibility or product criteria complete.

## Consumer entry after publication

This and the next three sections record successive historical navigation changes;
the maintained sources govern the current route.

The consumer route precedes the background explanation, names the Project
Management Manual explicitly and places it first in a purpose-based selection
table. Courses, roles, workflow/tool guides and shared references retain their
existing homes. Explicit anchors preserve the prior shared-library, obtaining
and change-inspection links. Relative links follow the viewed source; the guide
explains selecting the published tag/archive for edition-specific use. No manual
body, role, workflow or acceptance criterion changes. First-use source inspection
traces version selection to the manual index, Markdown/HTML and required-resource
guidance; this is a documentation walkthrough, not agent or tool execution.

## Reflective successor discovery

The book supports reflection on Chirality as practiced across projects. The
README and publication index retain prominence but remove the blanket instruction to start execution by reading it.
They distinguish the reflective successor from retained agent-directed
v9 and point external users to selected roles/workflows under local authority.
The old manual anchor still names v9; no edition or historical reliance is
silently redirected. The course entry has the same distinction; its lessons remain
at their existing source references. The current source characterization in
CLM-002 is reconciled, with other commitments and criteria unchanged.

## Independent book entry

README presents the book's own purpose without a parallel earlier-manual pitch.
The publication index moves retained manual references into a historical section
while preserving their named anchors and source files. The book's thesis/case
sources remain available. The index distinguishes the revised maintained text
from the unchanged published first edition in library 1.0.1. This is navigation
reconciliation, not retirement of a consumer's selected source.

## Course entry and teaching-route revision

Source inspection found that the course README had changed while index.html
still gave the earlier manual-as-agent-instruction direction. The same mismatch
exists in the source commits for library 1.0.1 and 1.0.2. The course entry now identifies both audiences
(agent instructor and human learner) and offers Markdown sources for agent use.
The maintenance instructions require checking every pair and regenerating only
changed sources with their actual committed basis. The course lessons and
assessment changes are the separately authorized teaching undertaking; this
locality owns their entry/discovery connection, not their assessment authority.

## Evaluation extension

This section records the original R18 allocation. Its accepted historical
standing and source recovery are identified in
[DEL-03-02’s current evaluation basis](../../../PKG-03/DEL-03-02/Work/EvaluationBasis.md#holding-transfer-and-current-availability).

The owner accepted SCA-20261101-UNDERTAKING-EVALUATION, including its audited
corrections, on 2026-11-01 against `e157d14910e84cf149f2ead524d585467b18e0f7`. PRD R18/A9 allocate the optional
work-and-repository evaluation capability. The state change and the conditions
under which it justifies effort are the evaluative subject; traces of work are
supporting observations. No tool implementation, host qualification or product
release is established by this scope amendment.

The accepted decomposition pointer now identifies eight allocated contributions,
and the Root entry distinguishes original seven-locality formation from the new
setup/production obligation. For this increment, enter the amended DEL-04-02
ScopeOfWork and the new DEL-03-02 ScopeOfWork/Work basis. The local amendment's
GROUP3_REVIEW.md identifies the decision and actual propagation standing.

No evaluation command or registered workflow is advertised as available. Once an
implemented route is examined, connect its real source, resources, requirements
and limits through the existing entry/catalogs. A new accepted scope is not an
implemented capability. Existing discovery guidance and acceptance criteria remain
unchanged; public consumer-facing entry changes await an actual supported result.


## Top-level operating entry

The maintained `init/` → `loop/LOOP_INIT.md` route separates ongoing operation
from execution records. The old entry path retains a dated compatibility
pointer for earlier links. Git and accepted snapshots preserve earlier bases.

AGENTS holds authority, ownership, reconciliation, cleanup and record rules;
the loop holds the work sequence and query syntax. The `Working cycle` heading
is retained because App v4 DEL-10-01/02 cite the Library's named sections at
their selected basis. OUT-001 and YAML code pointers identify the maintained
entry; historical CLM-001 and source examinations retain their inspected paths.

The loop's intake guidance establishes the basis, bounds, rights and return
route for contributions through Library Agent 0. Publication and consumer
adoption remain separate acts. The shared entry convention is maintained in
[project-setup's project-entry resource](../../../../workflows/project-setup/resources/project-entry.md).
