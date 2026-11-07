# Chirality library development

This entry belongs to the Chirality Library (`sgttomas/chirality-library`).
Chirality Root is the separate private `sgttomas/chirality`, which measures and
improves how agents deliver work across the projects; records here
written before 2026-11-05 use "Root" for the Library. See
[AGENTS.md](../../AGENTS.md#library-and-root).

Develop the library so people and agents can use its contents to maintain and
improve those same contents, and other projects can rely on identified material
under their own authority. Principles and publications, roles and workflows,
tools and their instructions, shared references and the Library's own execution are
all holdings in this work. The [accepted PRD](../../docs/PRD.md) defines the
objectives and the evidence required of the result.

The [accepted decomposition](../_Decomposition/_LATEST_ACCEPTED.md) allocates
the scope to five Package homes and eight bounded Deliverables under
SCA-20261101-UNDERTAKING-EVALUATION. Original seven-locality setup remains
established. DEL-03-02 setup, the deferred DEL-04-02 scope revision and selected
Work/need propagation follow the amendment's actual acceptance and closure record;
the evaluation capability's production is not established by allocation or setup.
Consult the [amendment review](../_ScopeChange/SCA-20261101-UNDERTAKING-EVALUATION/GROUP3_REVIEW.md)
for the current decision and remaining obligations. Continue only the work selected
by actual steering; earlier gate decisions retain their identified historical basis.

The owner approved passing the 60% development gate on 2026-11-01: “I approve
passing the 60% gate and proceeding as you recommend.” The basis is the integrated
work through `047da79894bc5631dca564a30113f2cd26ec7ae1` and the readiness reflection
in [DEL-04-02's Work](../PKG-04/DEL-04-02/Work/ReflectiveBasis.md).
The owner subsequently approved passing the 90% gate on integrated basis
`ce3ae7a405999a730caed807857eecb394ce3be6`: “Approved.” The intended contributions
are integrated, with scope, relationships and applicable evidence examined.
Proceed to final completion and delivery assessment under PRD §4 and manual v9
§8, reusing established evidence and examining any specific unsupported claim.
Named-reader compatibility, labelled procedural custody and the exact source
candidate retain their stated limits. This gate is not final product acceptance,
selection of a release version or publication authority.

The owner requested a post-90% check of every deliverable and a roadmap to
publication. The [approved publication roadmap](PUBLICATION_ROADMAP.md) connects
the existing evidence to remaining delivery work and reserved decisions; the
owner approved that course with “Proceed accordingly.” The owner subsequently approved the
publication notes and `library-v1.0.0` edition name at `c444ec139e3a65c5707264087ac89022abd190dc`
in PR #1790 with “Approved.” The owner then approved final acceptance of source
`fc73de583d25bf792d5c3abb3bf1ac8e0c38f7d6` and its public release: “I approve both decisions.”
[Chirality library 1.0.0](https://github.com/sgttomas/chirality/releases/tag/library-v1.0.0)
is published at that exact source. The agreed library undertaking is complete
within its stated evidence limits; subsequent work comes from new steering.
Consumer adoption and reliance remain independent.

## Find and carry the work

Read [Library AGENTS.md](../../AGENTS.md) for standing instructions, roles and
authority. The conversation supplies the undertaking. From its purpose or the
affected holding, locate the relevant ScopeOfWork under
`execution/PKG-nn/DEL-nn-nn/`. Search the scopes' purposes and outputs when the
locality is not already known, then read its `Work/` and `deliverable.yaml`.
Consult the PRD and selected source material for the requirements and interfaces
that this work involves. A source or code pointer indicates relevance, not
exclusive ownership.

Agents examine and refine input conditions while planning and carrying their
undertakings. Follow the sources and affected uses needed for the particular
action; judge suitability from evidence. Existing usable inputs need not wait
for an entire neighboring Deliverable to finish. Unknowns and reciprocal
relationships remain visible while unaffected work continues.

For work on this entry, begin with the
[discovery ScopeOfWork](../PKG-01/DEL-01-01/ScopeOfWork.md) and its linked Work.
From the repository root, inspect its declared neighborhood with:

```sh
python3 -m tools.deliverables --project . neighborhood DEL-01-01
```

The [query guide](../../tools/deliverables/README.md) gives the other queries,
Git/HEAD and Python/PyYAML prerequisites, observation limits and direct-reading
fallback. Queries reveal declared relationships; they do not decide whether an
input is suitable or the work is complete.

Use [coordinated knowledge work](../../workflows/coordinated-knowledge-work/WORKFLOW.md)
to carry related contributions into one usable, examined result. Agent 0 retains
purpose and continuity with the owner; implementation owners carry their
undertakings through contributions, repairs and integration. Reconcile the
actual result and verification with affected commitments, Work and needs in the
same PR, as AGENTS.md and the
[reconciliation method](../../workflows/bounded-reconciliation/WORKFLOW.md)
describe. When a finding calls purpose, commitments, explanatory framing or the
chosen practice into question, use [reflect-on-work](../../workflows/reflect-on-work/WORKFLOW.md)
with the human and Agent 0. Reconciliation compares results under commitments;
reflection examines whether that basis or practice still serves the purpose.
Select further methods as the undertaking needs them.

## Content review

The owner wants to understand proposed library content changes in broad strokes
and review and approve them before integration. Present the affected material,
what would change, why and the consequences, with the actual edits available.
This applies to meaning and behavior, organization and selection, and mechanical
maintenance; no document type or improvement class is exempt unless the owner
says so. Investigation, drafting and verification may proceed within the
authorized undertaking. Apply decisions already given; obtain approval for
changes outside the approved proposal before integration. Proposed replacement
instructions are examined under their preceding basis and do not authorize their own adoption.

## Examination and boundaries

Use the local ScopeOfWork's output and evaluation criteria and the proportionate
verification rule in AGENTS.md. Reuse evidence where it supports the actual
claim, and identify what remains unverified. `tools/run_affected_tests.py`
selects the tool checks and CI supplies the required hosted result; the
[workflow guide](../../workflows/README.md) covers checking and regenerating
consumed indexes when their sources change.

App v4 and SWBPIPE own adoption and product work in their repositories; the Library's
instructions and Git grant do not transfer to them. Follow AGENTS.md for any
needed coordination. App v3 and Runtime remain frozen. Old execution survives
only in the private `sgttomas/chirality` Git history (at or before `05d96f3e11`),
as history, not a standing backlog. Private information
stays outside this public library. Acceptance and release remain owner acts;
initialization alone assigns no undertaking.
