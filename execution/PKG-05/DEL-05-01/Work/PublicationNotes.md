# Chirality library 1.0.0 — publication notes

**Content and edition name approved by the owner: “Approved.”** The reviewed
basis is `c444ec139e3a65c5707264087ac89022abd190dc` in PR #1790.
Release title: **Chirality library 1.0.0**; selected tag name: `library-v1.0.0`. The prefix distinguishes this library
edition from historical application versions and the manual's Consolidated v9
edition. The owner subsequently approved final acceptance and release: “I approve both
decisions.” [The published edition](https://github.com/sgttomas/chirality/releases/tag/library-v1.0.0)
is bound to `fc73de583d25bf792d5c3abb3bf1ac8e0c38f7d6`. Its archive retains the
pre-release standing at that commit; this current annotation records the later
decision and publication without altering those bytes. These notes are owned
by DEL-05-01 under the
[publication roadmap](../../../_Coordination/PUBLICATION_ROADMAP.md).

## What this edition provides

Chirality is a source library of principles and publications, agent roles,
workflows, executable tools and their usage instructions, shared references, and
its own maintenance execution material. It supports people and agents locating,
maintaining, examining and reusing identified holdings under their own authority.
It requires no companion application merely to read or use its instructions.

The delivery is the complete tracked source archive of the approved
publication revision. Historical and Root-only holdings retain their stated
standing; inclusion does not make every archived tool a supported current product.
The release supplies the exact source commit and archive SHA-256.
The candidate PR identifies the reviewed source and locally checked archive;
any later integration revision needs its own correspondence check before release.

## Obtain, use and inspect changes

Start with the repository [README](../../../../README.md#obtain-and-use-the-library).
For a published edition, obtain the source archive attached to its named release
or the repository archive of the exact published tag/commit. Preserve its source
identity, original relative paths, required resources, [MIT notice](../../../../LICENSE.md)
and applicable component notices. A clone is useful for Git-dependent tools;
ordinary file reading does not need Git. Until a release is actually published,
selecting a commit or `main` remains an explicit development choice.

Read each holding's applicability and limits. Preserve a selected workflow's
complete package and its [required resources](../../../../workflows/README.md).
For maintenance of Root itself, enter through [AGENTS.md](../../../../AGENTS.md)
and its linked loop. Consumer projects choose their own instructions and authority;
copying the library does not transfer Root's grants, project governance or hosts.

Use the [change-inspection procedure](../../../../README.md#inspect-changes-before-adopting-them)
to compare the exact basis in use with the proposed edition, read the applicable
change accounts and examine affected local uses. Inspection does not adopt an
update. Historical sources remain recoverable through Git and the
[frozen-project recovery route](../../../../projects/FROZEN.md).

## Consequential changes in this development increment

This account covers the integrated library development in PRs #1779–1789, through
`35273905a90ee6c1032a7f49db2236ed19371029`, plus the publication preparation in
this proposal. It is not a comparison against a previous published library version.
Each PR retains its actual preceding basis and validation; the following links
are the change accounts for the individual changes.

- **Current maintenance setup and discovery.** [#1779](https://github.com/sgttomas/chirality/pull/1779),
  [#1780](https://github.com/sgttomas/chirality/pull/1780) and
  [#1781](https://github.com/sgttomas/chirality/pull/1781) connect current locality
  preparation, seven accepted deliverables, consumer-local needs and the entry.
  Explicit current setup preserves existing work and does not manufacture blank
  acceptance contracts. Retained legacy routes keep their compatibility standing.
- **Accurate tool prerequisites.** [#1782](https://github.com/sgttomas/chirality/pull/1782)
  makes the native queries' required `--project` argument explicit.
  [#1787](https://github.com/sgttomas/chirality/pull/1787) documents that resolver
  `--brief` needs PyYAML even for JSON input; without it, normalization currently
  raises an import traceback. These are usage repairs, not new host capabilities.
- **Shared reference applicability.** [#1783](https://github.com/sgttomas/chirality/pull/1783)
  clarifies current Work locality and the scope of historical product contracts.
  Current ScopeOfWork format validation remains current, not legacy-only.
  Shared definitions do not appoint a runtime provider or impose Root authority
  on independent consumers. Existing adopted clauses and pins retain their basis.
- **Consumer use.** [#1784](https://github.com/sgttomas/chirality/pull/1784)
  supplies obtaining, resource-preservation, source-identity and update-inspection
  guidance, with a bounded named App-reader case. #1787 extends the examined
  delivery subject to a complete source archive and selected standalone operations.
- **Retired Git layers and focused reflection.** [#1785](https://github.com/sgttomas/chirality/pull/1785)
  removes `workflows/change/` and `.agents/skills/chirality-change/`.
  Explicit selections of these packages and legacy `CHANGE` fail; there is no
  canonical successor or silent fallback. For ordinary authorized work, use the
  actual brief and applicable repository conventions. Root's concise Git rules
  remain in AGENTS, with detailed [recovery guidance](../../../../docs/MAINTENANCE_RECOVERY.md)
  loaded when needed. Historical enum/schema identities and source pins remain
  unchanged. The distinct [reflect-on-work](../../../../workflows/reflect-on-work/WORKFLOW.md)
  method supports human–Agent 0 examination of purpose and practice; it grants no
  authority and is compatible with HELP_HUMAN, HELPS_HUMANS and WORKING_ITEMS.
  TASK can supply evidence through its caller, not select ownership of this method.
- **Evidence and current standing.** [#1786](https://github.com/sgttomas/chirality/pull/1786),
  [#1788](https://github.com/sgttomas/chirality/pull/1788) and
  [#1789](https://github.com/sgttomas/chirality/pull/1789) reconcile bounded
  discovery evidence, adopted method/publication bindings and the owner's gate
  decisions. Those decisions do not themselves accept or publish the product.

## Dependencies and qualification limits

Consult the selected tool's guide before execution. Preparation uses zsh and
Python/PyYAML with the documented helper/module resources. Native deliverable
queries need Git, a resolvable HEAD and PyYAML; an archive supports direct reading
of declarations but not computed reverse links or Git observations. ScopeOfWork
utilities retain their shared `common.py` and `id_catalog.json`. Workflow resolution
needs roles, registry, catalog, selected packages/resources and applicable legacy
maps; structured briefs additionally require PyYAML. Resolution selects context
and composes policy; it does not launch work or enforce host permissions.

The [owning evidence](ConsumerBasis.md) establishes exact archive correspondence
and selected extracted-source operations on the observed platform. Broader runtime
or cross-platform qualification is not claimed. The named App reader case covers
capture, declaration and content identity at the recorded revisions; it does not
establish registration, execution, adoption or all consumers' compatibility.

The seven deliverables' 44 criteria have bounded applicable support as described
in the roadmap and owning Work. Actual maintenance repairs, the F-02 counterexample
and repair, and adopted reflection supply substantive use evidence. The fresh-reader
amendment brief was hypothetical. Eight maintenance operations were examined as
routes, not all executed separately. The labelled custody case used the same
holder and maintainer; transfer, timeout and enforced exclusion were not established.
Procedural coordination is not filesystem exclusion. No productivity improvement
was measured.

Incompatible reinterpretation of adopted shared clauses remains held until the
actual consumer basis is bound. Independent consumer adoption, frozen-product
reactivation, further archival disposition and bespoke tooling are not implied.
Local public-content screening and hosted private-term/secret-set checks have
separate coverage; the candidate's check results identify their actual subjects.

## Continuing responsibility and release standing

Root maintains the shared source and change explanations. Consumers retain their
selected source, local adaptations, product operations, acceptance and adoption.
Interrupted Root work follows the existing maintenance recovery instructions;
elapsed time alone grants no right to discard retained work.

The owner approved acceptance and release of the exact source above. Publication
and anonymous archive/checksum download verification are complete. The release
page carries these notes with commit-qualified links and the actual release
standing. Consumers retain their separate adoption and reliance decisions.
