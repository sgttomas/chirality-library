# software-decomp — method

## Method

### Operational — "How to do?"

This section defines the grouped-checkpoint conversational procedure for software development decomposition.

### Output Target

The agent maintains a **canonical working package** (living draft consisting of the main decomposition document and any companion registers) and revises it after human feedback until it passes the grouped checkpoints and the [Validity](contract.md#validity) requirements in the contract.

For each accepted group, finalize
`{DECOMP_ROOT}/checkpoint_snapshots/<group>-<UTC>/{DECISION.md,ACCEPTED_MANIFEST.csv,HANDOFF_STATE.md}`
and then update `_LATEST_GROUP1.md`, `_LATEST_GROUP2.md`, or
`_LATEST_ACCEPTED.md` as applicable. The manifest binds paths, package roles,
and hashes. The handoff names the accepted upstream snapshot, derivative
status, closure verdict, rerun requirements, and blockers. A later preparation
stage (except in a combined review sitting; see below) begins by resolving
the preceding pointer and reading that immutable
snapshot. Reopened decisions create successors; never overwrite a snapshot.

### Combined review for a small, reversible undertaking

For a small, reversible undertaking, the human may choose to decide all three
checkpoint groups in one sitting (`docs/COMPATIBILITY_FORMATS.md#historical-decomposition-contract`, PROTOCOL,
combined review sitting). Propose it where it fits; the human chooses it. Then:

- Prepare group 2 on the proposed group-1 state and group 3 on the proposed
  group-2 state, and complete the independent audit of the final package
  before the human decides.
- Present the three groups together. The human's decision records which
  groups it covers, and the audit and decision record the hashes of the
  presented package.
- After the decision, write the group-1, group-2, and group-3 snapshots in
  that order, each naming the preceding snapshot as its upstream basis, and
  update each pointer only after its snapshot is complete. The snapshots must
  match the recorded hashes; any difference reopens the affected groups and
  every later group.
- A material change found during the sitting reopens the groups it affects
  and every later group. Refresh their dependent preparation and audit
  before they are decided; only earlier, unaffected groups may still be
  decided in the sitting.

Otherwise, the groups below are decided in separate sittings.

### Preparation and checkpoint groups

#### Group 1 preparation — basis, normalized scope, vocabulary, objectives

Record the accepted basis before normalizing it: its path, content hash, the
separate acceptance decision record, and the accepted portions and shared
constraints that record names. For a partial or qualified acceptance (for
example, a `reverse-engineer-software` handoff), normalize only the accepted
portions as candidate `IN` scope. Record material outside them as `TBD` Scope
Items with a `SourceRef` to its location in the basis, using `OUT` only where
the decision record excludes it; do not treat it as accepted scope. Packages
do not exist yet, so these items receive their Package home at group 2. Carry the basis identity into the group-1 `DECISION.md`
and `HANDOFF_STATE.md`.

Collect requirements, tickets, notes, architecture, constraints, non-functional
requirements, target platforms, rollout expectations, prior decompositions, and
references. Normalize these into atomic Scope Items with stable IDs and explicit
`IN | OUT | TBD` status. Identify source-grounded work-domain signals without
planning implementation. Build the Vocabulary Map. Derive a small, testable
objective set from stated intent and success conditions and map it to Scope
Items on a best-effort basis.

Before the checkpoint, prepare the complete draft basis and run available
identity, provenance, classification, and internal-consistency checks. Record
gaps, conflicts, and proposals rather than creating a prompt for each one.

**Checkpoint group 1:** Present the basis, normalized scope, vocabulary, and
objectives together. The human confirms or corrects this group as the basis for
structural proposals.

After acceptance, finalize the group-1 snapshot and pointer before preparing
group 2.

#### Group 2 preparation — Packages, Deliverables, coverage, exceptions

Resolve and consume the accepted group-1 snapshot before developing this
proposal.

Propose flat Packages as cohesive work domains, supported by the accepted
domain signals rather than a timeline. Assign every Scope Item, whether `IN`,
`OUT` or `TBD`, to exactly one Package as its accountable home; this includes
material recorded as `TBD` at group 1, before Packages existed. The home
allocates responsibility for accounting for the item. Only IN Scope Items map
to Deliverables; an OUT or TBD item keeps its home and `SourceRef` for
traceability and needs no production mapping. Resolve overlap by proposing an
evidenced split or presenting the boundary as a human decision.

Within each Package, propose agent-executable Deliverables with stable coupled
`DEL-XX-YY` IDs, descriptions, responsible parties, types, anticipated
artifacts, objective links, Scope Item links, and a `ContextEnvelope`. Keep each
Deliverable within one Package and one cohesive verification context. Split `XL`
items where possible; otherwise identify the precise exception and risk.

Run coverage, ID-coupling, Context Budget, interface, artifact, responsibility,
and objective-mapping checks, including the register validator in the
contract's [Inputs and outputs](contract.md#inputs-and-outputs) and its
identifier-format invariants. Prepare Coverage & Telemetry and the specific
exception/open-issue list before asking for a decision.

**Checkpoint group 2:** Present the proposed Packages and Deliverables together
with coverage findings and exceptions. The human confirms or revises the
structure and the recorded treatment of exceptions.

After acceptance, finalize the group-2 snapshot and pointer before preparing
the final audit.

#### Group 3 preparation — independent audit and final package

Resolve and consume the accepted group-2 snapshot before assembling and
auditing the final package.

Incorporate the first two decisions into the canonical working package. Ensure
it contains the SSOW, Scope Ledger, Coverage & Telemetry, Vocabulary Map,
Packages, Deliverables, Artifacts, Objectives, Context Budget QA, companion
inventory, and decision/change log. Dispatch a separate review instance that
did not author the candidate to audit it against the accepted basis and group-2 decisions.
Resolve mechanical defects and present remaining substantive findings without
silently ruling them.

**Checkpoint group 3:** Present the audited final decomposition. The human
accepts it as the basis for downstream use or returns affected parts for repair.
Write or render the accepted output around that accepted state; output writing
does not add another checkpoint.

After acceptance, finalize the group-3 snapshot and update
`_LATEST_ACCEPTED.md` before any downstream handoff. Carry actual source-grounded needed
inputs with the responsible consuming Deliverable, intended use/condition,
case/trigger and source location; retain unknown sources and technical holds.
Setup authors the corresponding local needs after scope exists. Do not create
producer commitments or a second authoritative dependency network during this
handoff.

If accepted source material changes, identify which prior decisions depended on
it, reopen only those decisions, and refresh their dependent checks before the
next applicable checkpoint. Preserve unaffected IDs, mappings, and decisions.
