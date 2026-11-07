# Chirality library 2.1.0

The owner authorized adoption of INTERLOCUTOR as an official role, opt-in per
session, and publication: “this also means you need to publish a new official
library package incrementing to v2.1.0”. The edition name is **Chirality library
2.1.0**, tag `library-v2.1.0`. Its release identifies the exact integrated source,
complete tracked-source archive and SHA-256. These source notes do not claim
publication before that release exists.

## Changes since 2.0.0

The comparison basis is `library-v2.0.0`, source
`2f981163d76772d3779697d9def1a9e951d978e7`.

- **Opt-in INTERLOCUTOR role.** A fifth official role supplies a bounded Type 2
  second opinion on Agent 0's effectiveness and direction. In sessions selecting
  it, Agent 0 supplies periodic summaries and consults it before every PR merge.
  After three rounds without convergence, Agent 0 explains its own decision and
  continues within its authority. Advice carries no sign-off or veto. Model and
  effort choices remain session steering.
- **Registration and method compatibility.** All direct-entry roles can delegate
  INTERLOCUTOR; neither Type 2 role delegates. Existing method eligibility stays
  unchanged: methods without an execution companion inherit the original four
  roles. INTERLOCUTOR needs explicit `compatible_roles` to select a method and
  needs no method for its ordinary advisory brief. Existing resolver behavior for
  other registered roles and omitted role lists is preserved. Strings are rejected
  as malformed role lists. Explicit write targets and
  actual host permissions remain necessary for writes.
- **Restored methods and tools.** [PR #5](https://github.com/sgttomas/chirality-library/pull/5)
  restored workflows and supporting tools removed before 2.0.0, including
  document, domain, drawing, evaluation and research methods. The consumed index
  now contains 76 method entries, compared with 43 in 2.0.0. Inclusion preserves
  each holding's own applicability and evidence limits; it does not qualify every
  method for every project or role.
- **Library and Root identity.** [PR #4](https://github.com/sgttomas/chirality-library/pull/4)
  and [PR #6](https://github.com/sgttomas/chirality-library/pull/6) distinguish this
  public Library from private Root and correct current entry/discovery wording.
  Earlier records keep their identified historical meaning.
- **Root-owned evaluation holdings.** [PR #7](https://github.com/sgttomas/chirality-library/pull/7)
  removes `tools/undertaking_evaluation/` and excludes `audit-agents` and
  `evaluate-repository-change` from current Library discovery after verified
  byte-preserving transfer to Root. Its owner-approved R18/A9 and scope amendment
  ends the corresponding continuing Library executable/workflow obligation;
  original contracts, editions and evidence remain recoverable. Current public
  Library source supplies no runnable repository-change evaluator. Private Root
  starting material is not a required dependency or replacement public service.
  `evaluation-protocol`, `evaluation-report` and `tools/evaluation/` remain here.

## Consumer adoption

**Removed:** `tools/undertaking_evaluation/` shipped in 2.0.0 and is absent from
2.1.0, with no public replacement. Keep 2.0.0 or the identified pre-removal public
source if you depend on that evaluator; private Root is not an adoption route.

Consumers that enumerate exactly four roles must deliberately support the fifth
descriptor, its Type 2 nondelegation and session opt-in. The method index schema
remains `chirality-method-index/v1`; the discovery fixture adds the role and
compatibility cases. Existing custom-role inheritance remains as before. To use a
method with INTERLOCUTOR, give that method an explicit roles list including it.

Choose adoption under your project's authority. Preserve complete packages,
relative resources and notices, and compare the exact edition currently used.
Start from [README](../../../../README.md#obtain-and-use-the-library). The attached
source archive is for in-place reading/tools; it is not a Python wheel or new
application runtime. `pyproject.toml`'s dependency-only version is unchanged.
Python tool prerequisites remain in the selected tool guide and that manifest.

## Verification and limits

The release and its integration PR supply the exact checked revisions, test and
review results, archive manifest correspondence, extracted-source checks and
checksum. The archive is built from integrated Git objects, not uncommitted
files. Check every archived byte and executable mode against that source before
publication. Git-dependent tools may require a clone rather than an extracted
archive; ordinary role reading and selected method resolution need no sibling
checkout or private operational evidence.

Root, App v4 and SWBPIPE own their adoption work. Notification does not establish
consumer integration. This edition implements no new adherence-result format.
No new comparative
productivity, host enforcement or broad product compatibility claim is supplied.
