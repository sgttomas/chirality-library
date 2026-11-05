# Consumer use and publication inputs

For the accepted R18/A9 increment, see [Evaluation extension](#evaluation-extension).
Earlier case/basis statements below retain their recorded subjects and limits.

Maturity: obtaining/use and change-inspection candidate with bounded named-reader
evidence and independent examination. The owner approved the six-file content
proposal at `4d33dfed9e2388efad504d7736275e8d55d41722` with “approved.”
Integration is recorded in PR #1784; product acceptance and release remain separate. Initial assessment
used `fd847ac9ac68250b2f35d2e9c0087c16e86b510a`. The current undertaking uses the
integrated F-02 result at `1357d706ea77497903976bf159f3880bea4d1360` as its real
source candidate, compared with `257ab4c18014bf872a1c72eeb7593a7ad3d135c0`.
No library release or consumer adoption is performed.

## Current undertaking and outputs

Give an independent consumer a usable way to select material, obtain its actual
bytes/resources/notices, examine changes and decide adoption. The owner-approved README
route and workflow-package guidance are the maintained outputs. This locality
holds their source basis, actual examination and limits. The existing F-02
change account supplies the reason and meaning of that candidate's changes;
it is not reproduced as a new version/history register.

## Reusable sources

`README.md`, the selected tool/workflow guides and `LICENSE.md` provide pieces
of an obtaining/use route. Select the actual surface and its required resources
and component-specific notices before evaluating a use claim. Ordinary reading
can use files without Git; executable operations retain their declared dependencies.
Root-specific execution and grants do not automatically become consumer instructions.

`docs/alignment-manual/README.md` distinguishes stable discovery from reliance
on an exact edition/source and gives the maintained rendering route.
`sgttomas/chirality:projects/FROZEN.md` preserves the completed archive transition and frozen-product
recovery references. Use those existing homes; do not create a second edition
history or re-run the completed removal.

## Selected consumer and publication bases

For Q-04, App Agent 0 identified the actual package reader at App revision
`366e7a6656d807142e7bdeda0ccf99c37d7227b1`:
`app/src-tauri/src/workflow_workspace.rs::Snapshot` and
`workflow_declaration.rs`, governed by
`execution/PKG-02/DEL-02-01/Work/WORKFLOW_DECLARATION.md` §§6.1 and 7 and
`execution/PKG-02/DEL-02-02/Work/WORKSPACE_AND_REGISTRATION.md` §4.5.
Capture is read-only; registration and execution are separate acts. The selected
claim is limited to capturing the current Root coordinated-knowledge-work package,
preserving its two files/content identity and parsing its declaration standing.

The maintained App fixture
`workflow_catalog_tests::actual_embedded_package_preserves_full_tuple_and_both_files`
examines App's existing embedded package. Its admitted revision is
`1b1733864cd89fd6d8ca74bf3e2084ff1105c1fc7d76537eefb42e2ae9a41e83`.
The current Root package's two source files differ from those embedded bytes,
so that fixture's result cannot qualify the newer input by itself. App has no
maintained standalone entrypoint accepting an arbitrary external package path.
The [isolated fixture wrapper](fixtures/app_workflow_reader.rs) exercised the exact
App reader source successfully, as described below. No pinned App input or
maintained consumer source was overwritten. This binds the selected reader claim;
it is not qualification of every possible consumer operation or library holding.

## Named-reader examination and reproduction

One filtered test ran against a complete immutable App source export at the
revision above. The only additions were the test wrapper and its `cfg(test)`
attachment in `app/src-tauri/src/lib.rs`; the production reader/parser, embedded
resources and pins were unchanged. Source comparison covered all 3,597 archived
regular files. The fixture binds the two Root source-file SHA-256 values and
checks exact captured bytes, declaration standing, hygiene and identity behavior.

The actual reader captured both files, totaling 22,621 bytes, with no declaration
or hygiene findings. The declaration and all five categories were `Undeclared`:
requirements are undeclared, not established absent. Its package method was
`chirality.app.workflow-package.sha256/v1`, with value
`3730d84debb5d77582a0c26211a5f380cdb1a44c7e26eeb537f334db43fdd881`.
Relocation preserved that value. A controlled resource-byte change in a separate
copy changed it while leaving the original input intact. LICENSE.md was checked
separately and is outside this package identity.

To reproduce, export the exact App revision and selected Root package/license
from their repositories into owned temporary directories. Copy the fixture into
the exported App's `app/src-tauri/src/` and append
`#[cfg(test)] mod app_workflow_reader;` to that export's `src/lib.rs` only. Set
`CHIRALITY_READER_PACKAGE` to the exported package and `CHIRALITY_READER_SCRATCH`
to an owned empty directory. From the exported `app/src-tauri`, run:

```sh
cargo test --offline --locked --jobs 2 --lib \
  app_workflow_reader::root_package_capture -- \
  --exact --nocapture --test-threads=1
```

Use an isolated Cargo home and target directory and follow any local build-resource
policy. This Snapshot path does not require Codex state; the observed run also
isolated a Codex home to comply with its host policy. It used ordinary copied
cached dependencies, no
downloads, original-target writes or writable links back to another checkout.
One test passed with 1,977 other tests filtered out. Existing compilation warnings
were not changed. Reproduction needs that complete source and available offline
dependencies; the fixture is not part of ordinary library use or Root's default CI.
The tested fixture at `5ff58130db0a85916bdc4cccf79da5f2a8e9e471` has SHA-256
`bb7404921047839c463eeac0f71539df8563ddd89dd288192f6aac8ca913ebb2`.
Independent-review clarification subsequently changed only its reproduction
comment; executable test code is identical, so the passing behavior evidence is reused.

This is actual capture/declaration/content-identity evidence at the two named
revisions. It establishes neither registration, workflow execution, supplier
capability, user approval, product adoption nor a release. The original embedded
package remains at its own identity. Later source changes require examining
which parts of this evidence remain applicable.

For Q-05, the candidate is the F-02 source revision named above, including
Consolidated v9 and its maintained HTML, compared with the pre-F-02 source basis.
This is an identified candidate using an existing edition name, not a newly
published library version. PR #1783 supplies the actual consequential change
account and source/render examination. The manual's rendered source identity
remains its recorded commit; the later integration revision does not rewrite it.
The actual delivery candidate is a source archive containing LICENSE.md and the
v9 Markdown/HTML from that revision. Extracted bytes were compared with their
source blobs; the HTML retains renderer source commit
`6472b49b2a6c7ebf4db1356d7bf83fa3af412305` and the matching Markdown hash.
Its source/render and desktop/narrow examination from PR #1783 remain applicable
because those bytes are unchanged. The archive is identified as a source candidate,
not a published edition or a replacement for the complete library.
No library GitHub release was returned by the bounded release-list query during
this undertaking. Discovery of no suitable publication requires an explicit
development-source choice, not silently calling main or an archive tag a release.

## Copy and change-inspection exercise

An isolated Git archive of LICENSE.md and the complete selected workflow package
at Root `1357d706ea77497903976bf159f3880bea4d1360` was extracted without Git metadata.
The copied bytes matched their source blobs. Reading the method and contained
REVIEW-NOTES resource needs no Git installation or invocation. This exercise
covers the selected copy, not every file in a full-repository download.

The source comparison from `257ab4c18014bf872a1c72eeb7593a7ad3d135c0` to
`1357d706ea77497903976bf159f3880bea4d1360` identified the six selected maintained
documentation outputs changed by F-02: three shared references, the corrected
PRD, and v9 Markdown/HTML. The full revision comparison also changes two
DEL-02-02 locality records (ScopeOfWork.md and Work/Applicability.md); those were
excluded from this consumer-output comparison, not represented as unchanged.
The selected outputs' meaning/use account is in PR #1783. A deliberately
unavailable comparison revision was rejected; it was not reported as no change.
Inspection leaves the consumer's selected basis unchanged.

## Remaining use and decisions

Q-04 is now bound for the selected App reader claim. Q-05 has the identified
source/edition candidate and prior comparison basis; no owner publication is
claimed. Other interfaces and uses still need their own bindings and evidence.
Independent review found no blockers; its clarity corrections are incorporated.
The owner approved this content for integration. Bind only the resources and conditions
needed by a selected use.
Coordinate shared README edits with DEL-01-01, which owns navigation; this
locality owns obtaining/version/compatibility meaning. DEL-02-02 may need a
named adopter's basis before changing a disputed clause; DEL-03-01 owns any
separately justified executable repair. Existing maintenance and reconciliation
methods remain usable without whole-deliverable completion gates.

Verify historical bytes actually relied upon, preserving original pins and
editions; do not extend that into a global history audit. Consumer adoption,
private operational data and product releases stay with their owners. Initial
native needs preserve these conditional uses and unresolved source bindings.

Neighboring adopted-clause and exported-interface conditions remain unresolved
where they require evidence beyond the bounded App package-reader case. The
publication conditions in DEL-02-02 and DEL-04-01 now identify the already-bound
F-02/v9 candidate and prior comparison; calling those particular Q-05 uses
unresolved was stale. Other publication uses still require their own bindings.

## Complete library source candidate after the 60% decision

The broader delivery subject is the complete tracked library repository at
`7c334bf5cb529a814e0f96f68bc8d9500b15cdd5`, described as **Chirality library source
candidate at that revision**. The owner approved this exact source-delivery candidate and the six-file
content proposal at `4a4e6452931e78c0ebdb405b651e434bcf40bdc7` with “Approved”.
That decision is not an owner release or semantic-version selection. Its preceding comparison basis is
`547e7d7f833f9bec351f7a034bddd7c1a37db15a`. The source candidate adds the structured
brief's PyYAML dependency explanation and the corresponding toolkit examination;
no executable capability changed. The current PR's subsequent evidence updates
are not silently included in that identified archive.

The complete archive was produced with `git archive --format=tar` at the exact
revision. Its SHA-256 is
`b442c2476ae532ca2223731e6697eae050d11f2f0edb37bac3a87218043a49cd`.
`git get-tar-commit-id` identifies that revision. All 1,052 files, totaling
13,514,094 bytes, matched the selected Git blobs and modes before and after the
selected operations; no extra source files appeared. No tracked links or gitlinks
were present. Extraction was outside every Git repository, with no `.git` metadata.
The archive preserves LICENSE.md and other tracked notices. Selected surfaces had
no separate component notice; this is not a universal licensing/support assessment.

The actual extracted form supplied these bounded operations:

- Source-qualified preparation, current-project and ScopeOfWork resource loading
  succeeded under their compatible roles. Requested resources retained matching
  hashes; incompatible TASK/project-setup selection and a missing resource were
  rejected. No write targets or write capability were inferred from selection.
- Archived DEL-05-01 validated as SOW_V1, derived eight checklist criteria and
  passed its boundary-owner check without site packages. Format validity is not
  substantive acceptance.
- Current scaffolding created a disposable accepted-identity locality outside the
  source tree. Repeating it preserved declaration bytes and existing Work content.
  The prepared check passed without a blank ScopeOfWork or lifecycle files.
- The same read-only JSON brief failed before normalization without PyYAML and
  succeeded using an existing suitable interpreter, returning no writable targets.
  The updated guide accurately describes this dependency and its fallback limits.
- Native dependency querying refused the non-Git source directory. Direct reading
  of its existing declaration exposed conditions and evidence pointers without
  deriving reverse links, Git observations or input suitability.

The first project-setup probe selected TASK and was refused; that was corrected
to the method's declared WORKING_ITEMS role for context selection. The first
missing-resource probe was also masked by that role mismatch. Only the subsequent
compatible-role refusal establishes the missing-resource observation. No role
execution, delegation or host permission was inferred from either selection.

Reproduction uses the full `git archive` at the named revision, safe extraction
outside a checkout and the maintained commands in the selected guides. Keep
Python bytecode disabled to observe source preservation. Use Python/PyYAML and
zsh where required, and the documented PYTHON override for shell helpers; no
install or network access was needed. ScopeOfWork tools retain common.py and
id_catalog.json; resolution retains roles, registry, catalog, selected package
resources and applicable legacy maps. Query Git/HEAD prerequisites remain in force.

Full-tree correspondence establishes source-delivery identity; behavioral evidence
is limited to the operations above on the observed platform/filesystem. Historical
and Root-only holdings keep their declared standing. No frozen product was run,
no broader App qualification is inferred, and owner content/delivery approval is recorded in PR #1787. The earlier named App-reader and manual-edition cases retain
their own exact bases and limits.

## Post-90 publication preparation

The owner requested a deliverable-by-deliverable publication roadmap and approved
its course with “Proceed accordingly.” The [roadmap](../../../_Coordination/PUBLICATION_ROADMAP.md)
connects existing bounded evidence to remaining delivery work. The
[publication notes](PublicationNotes.md) consolidate the change account,
obtaining route, dependencies and limitations and propose `library-v1.0.0` as a
distinct library edition name. The owner approved their content and edition name
at `c444ec139e3a65c5707264087ac89022abd190dc` in PR #1790 with “Approved.”
The subsequent acceptance and release decision is recorded below. Existing
scopes, output homes and criteria are unchanged.

The preparation basis is `35273905a90ee6c1032a7f49db2236ed19371029`; its complete
source archive has SHA-256
`c8823062887f536db8c201a7cd9c38b900f6bb333d9a54d35d5ec77a16932f3a`.
Its 1,052 files match Git bytes/modes. Compared with the earlier examined
`7c334bf5cb529a814e0f96f68bc8d9500b15cdd5` archive, ten execution/needs/loop files
changed and operational sources are unchanged. The earlier archive remains its
own approved subject. This proposal adds publication records only. Its PR binds
the actual candidate head, archive identity, scoped checks and evidence reuse;
a later integrated release source requires its own correspondence check.

## Accepted and published library edition

The owner approved final product acceptance and public release of
`fc73de583d25bf792d5c3abb3bf1ac8e0c38f7d6` as `library-v1.0.0`: “I approve both
decisions.” [The release](https://github.com/sgttomas/chirality/releases/tag/library-v1.0.0)
publishes that exact source with approved notes, the 1,054-file tracked-source
archive and SHA256SUMS. Its SHA-256 is
`e75ce1396e8bb92d4e2f144ba13336ee93a7ad7579494b2a6d21117857733567`.
The tag target, anonymous archive download, embedded tar commit identity and
checksum download were verified on 2026-11-01. Every file matches its Git blob
and executable mode; operational sources are unchanged from the earlier examined
archive, so selected behavioral evidence is reused with its original limits.
Full-archive credential and three locally available private-term checks returned
zero findings; required hosted checks passed on the identical integrated PR tree.

Current standing and discovery-pointer annotations are later source changes, not
changes to the published archive. Its pre-release records remain historical.
The accepted undertaking is complete within its stated scope and qualifications;
consumer adoption, broader compatibility and future publication remain distinct.

## Consumer subscription and update guidance

The owner approved the four-step consumer-entry proposal and directed integration
via PR. README now explains choosing a version and material, GitHub release
notifications, the Atom feed, manual discovery and deliberate update inspection.
Optional CLI discovery retains failed-query and partial-comparison limits.
Copies retain source identity, resources and notices; consumers retain authority.
The subscription routes use GitHub/feed-reader facilities: no subscription was
configured for a user and no notification delivery was tested. The returning-user
walkthrough follows release discovery, notes and comparison without assuming
adoption. Library 1.0.0 remains unchanged; these development instructions require
a separate publication decision to become a later edition.

## Reflective successor and consumer standing

The approved new book changes the character of the publication, so the current
README/index explicitly preserve v9's agent-directed use as a separate selection.
The successor is material for reflection; roles and workflows remain the route
to operational methods under each project's own instructions. The owner approved the book and rendered form at
`43c4d414304e436a7f9cdceb21ed2b4e05c26543` and authorized library 1.0.1. Named App-reader evidence
and all archive/publication pins above retain their actual subjects. No external
consumer adoption or source repinning is performed. The discovery changes are
coordinated with DEL-01-01; no new obtaining mechanism or interface is claimed.

## Library 1.0.1 approval and release basis

The owner approved the complete candidate at
`43c4d414304e436a7f9cdceb21ed2b4e05c26543`: “Approved. This will increment the
published library to v1.0.1”. This includes the book, explicit DEL-04-02 addition,
consumer/discovery reconciliation and optional method reference. Publication uses
the normally checked integration revision, with approval annotations only after
that reviewed subject. The [release](https://github.com/sgttomas/chirality/releases/tag/library-v1.0.1)
identifies the exact merged source, source-archive checksum and change account;
the actual artifact/download verification is recorded in PR #1793. The approved
book's Markdown and rendered bytes remain unchanged by these annotations.
Library 1.0.0 remains recoverable at its original tag and archive. Consumers
choose whether to adopt 1.0.1; neither publication nor the new book changes their
selected v9 instructions, operational authority or product behavior.

## Book framing after library 1.0.1

The owner authorized removing predecessor-manual continuity from the maintained
book. Its current presentation and source-basis note do not require familiarity
with an earlier manual. Historical sources and consumer-selected pins remain
available separately; library 1.0.1 retains its actual published bytes. The
publication index explicitly distinguishes this later maintained text. The
change does not publish a replacement archive or adopt it in a consumer project.

## Course source and reading-edition repair

The owner approved preparation of a bounded course revision, including repair of
the mismatched course README/index.html discovered in the published 1.0.1 and
1.0.2 source trees. Other existing course pairs matched their source fingerprints
at investigation. The revised reading files are regenerated from committed
Markdown; changed course content and the explicit practicum assessment addition
remain reviewable together in the candidate PR. Northbank's records and keyed
numeric answers remain their original exercise basis. The courses remain
host-independent, with no claim of App course integration or improved learner
outcomes. No released archive is overwritten; a later edition requires its own
publication decision.


The course review identified cross-file inconsistencies in the initial draft.
Repairs align Course 12 setup, rotation, companion guidance and Criterion 6:
production direction includes consequential agent-written briefs, and examination
covers the returns relied on rather than requiring every child message. This is
an explicit assessment change for owner review. Course 06 and its companion's
keyed answer 7 now permit retained but stale history; the expected reasoning
about potentially lossy context transfer remains. No numeric keyed answer or
Northbank case record changes. A scoped capability/responsibility pass repairs
categorical memory and transmission claims without transferring A01 appointments.

## Evaluation extension

The owner accepted SCA-20261101-UNDERTAKING-EVALUATION, including its audited
corrections, on 2026-11-01 against `e157d14910e84cf149f2ead524d585467b18e0f7`. PRD R18/A9 allocate the optional
work-and-repository evaluation capability. The state change and the conditions
under which it justifies effort are the evaluative subject; traces of work are
supporting observations. No tool implementation, host qualification or product
release is established by this scope amendment.

This increment remains local source development. Published Library editions keep
their bytes and original evidence. A later publication candidate must identify
its supported evaluation interfaces, required resources/dependencies, case data
boundaries and limitations, and compare it with the consumer's retained basis.
No consumer installation, host permission, subscription or automatic adoption
follows from this amendment.

Private operational records remain local to the selected consumer. Public fixtures
or summaries must be cleared. Before a named host/consumer compatibility claim,
require the actual supported contract and evidence from DEL-03-02; prior generic
utility/archive evidence is not sufficient. PR #1799 now supplies the initial
implementation and selected actual-use evidence in DEL-03-02's Work. The
[1.1.0 publication notes](PublicationNotes-1.1.0.md) identify that supported route
and its limits alongside the other changes since 1.0.2. Existing publication
criteria and owner release authority remain unchanged.

## Library 1.1.0 preparation

The owner selected 1.1.0 (“I agree with 1.1.0”) and authorized integration after
repair, independent review and passing CI: “If you fix those and review it and
the CI is green you can merge the PR on this delegated approval.” This is
preparation and merge authority; publication remains a separate owner decision.

[Publication notes](PublicationNotes-1.1.0.md) cover the complete change from
`library-v1.0.2` at `59433388627773f008f550481c4159514f43c7e5`: courses, the
book subtitle, current-locality scope amendments and the new evaluation route.
The preparation PR binds the exact checked candidate, complete tracked-source
archive, SHA-256 and selected extracted-source operations. A subsequent merge
revision must have its own archive identity checked before release. Earlier
editions and consumer pins remain unchanged.

The evaluation route uses Python 3.10+ and Git, with optional authorized frozen
Codex per-response records; no private inputs are needed for ordinary source
reading, workflow resolution or the public fixture suite. Render examination
uses labelled cases over public committed paths, not private operational data.
DEL-03-02's Work distinguishes that representation evidence from the pilot's
inconclusive result and remaining R18/A9 qualification. This candidate makes no
new App/SWBPIPE adoption, compatibility or efficiency claim. The existing needs
remain applicable; the candidate need now points to these edition-specific notes.
