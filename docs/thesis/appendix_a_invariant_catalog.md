# Appendix A — Historical Invariant Catalog and Current Interpretation

This appendix explains the R-, I- and K-series catalogs discussed in earlier
versions of the thesis. It is a historical crosswalk, **not a live inventory of
binding development duties**. It does not reinstate retired lifecycle status,
run approval, receipts, registers, agent personas or snapshot requirements.

The original definitions are recoverable at `archive/pre-docs-cleanup-1` in the
[workflow-component standard](https://github.com/sgttomas/chirality/blob/archive/pre-docs-cleanup-1/docs/WORKFLOW_COMPONENT_STANDARD.md),
[decomposition standard](https://github.com/sgttomas/chirality/blob/archive/pre-docs-cleanup-1/docs/DECOMPOSITION_STANDARD.md)
and [CONTRACT.md](https://github.com/sgttomas/chirality/blob/archive/pre-docs-cleanup-1/docs/CONTRACT.md).
These sources contain different historical amendments; the table below explains
the families rather than claiming to reproduce a single original catalog as it
stood at one time.

Current repository authority comes from [AGENTS.md](../../AGENTS.md), the
conversation and applicable project commitments. Some historical identifiers
remain in [Product boundaries](../PRODUCT_BOUNDARIES.md) for adopted consumers;
[Compatibility formats](../COMPATIBILITY_FORMATS.md) preserves formats still
read by tools. Those sources determine applicability. This appendix neither
widens nor retires their contracts.

The distinction this analysis draws is between a commitment, a proposed
mechanism and evidence that the mechanism does its job. The historical word
“invariant” was used for all three, often without a mathematical specification.
Identifying that mixture is part of the revision, not a reason to discard every
concern the catalog expressed.

The catalogs below retain the identifiers needed to interpret earlier sources.
[Appendix E](appendix_e_development_history.md#e3-representations-of-work-and-warrant)
explains how their representations developed and why the current argument separates
commitments, methods and observed properties.

## A.1 Workflow Design Requirements (R1–R17)

| Historical IDs | Concern and former mechanism | Current interpretation |
|---|---|---|
| R1 | Explicit human decision rights | Preserve reserved commitments and the person's judgment throughout work; no mandatory gate at every iteration follows |
| R2 | Straight-through task execution | TASK owns a bounded assignment through ordinary repairs, reports blockers and continues unaffected work; no delegation |
| R3, R16 | Declared write quarantine and checkout containment | Scope comes from assignment and host; actual checks must cover the execution path, not merely a role header |
| R4 | An immutable snapshot folder for each run | Routine copies are retired; preserve records when a consumer, acceptance or recovery requires them |
| R5 | Mandatory provenance fields | Make relevant grounds inspectable; fields alone do not establish warrant |
| R6 | Unknowns represented rather than invented | Distinguish evidence, assumptions and proposals; legitimate design creation is not prohibited |
| R7 | Expose conflicts and duplicates | Resolve ordinary implementation matters within authority; surface material conflicts and reserved choices |
| R8 | Structured briefs and deterministic outputs | Assignments can be conversational; tool inputs can be strict; equivalent model outputs are not guaranteed |
| R9 | Reviewable, non-destructive publication | Current Git authority and product release boundaries apply |
| R10, R11 | Skill tool policy and explicit deterministic tool contracts | Methods and tools need clear applicability, inputs, effects and limits appropriate to their use |
| R12 | Separation of skills, tools and design roles | Distinguish method from execution mechanism without prescribing a manager for every tool change |
| R13 | Claim-strength calibration | Claims must remain within their supporting evidence; this thesis is subject to the same constraint |
| R14 | Multi-phase integration rules | Own integration and corrections; no compulsory derivative packets or handoff chain |
| R15 | Explicit registry membership and retirement | Identify active sources and consumers; a registry is useful only where something consumes it |
| R17 | Proportional design evidence | Include the evidence needed for consequences and recovery; count the attention and maintenance costs of control |

These are interpretations of concerns, not replacement R-series instructions.
The role files, workflows and tool contracts are the operational sources.

## A.2 Decomposition Invariants (I1–I10)

| Historical IDs | Concern and former mechanism | Current interpretation |
|---|---|---|
| I1 | Human confirmation at each decomposition gate | Preserve owner decisions about commitments and accepted baselines; routine refinement can proceed within authorization |
| I2 | Source-faithful scope allocation | Do not present unsupported scope as accepted; proposals and unknowns remain distinguishable |
| I3, I4 | Flat, gap-free, non-overlapping partitions | A useful repository convention and a coverage question, not a universal ontology or proof of complete scope |
| I5, I6 | Stable IDs with deterministic parent coupling | Support navigation and machine joins; identity does not by itself establish unchanged meaning |
| I7 | Best-effort objective mapping | Expose missing mappings without manufacturing precision or blocking unrelated work |
| I8 | Recorded assignment rationale | Put non-obvious current reasoning where it governs the work and use existing change history |
| I9 | Required ledger and coverage telemetry | Generate an accounting view when a real consumer needs it; a populated ledger does not prove requirement adequacy |
| I10 | Required vocabulary map | Preserve meaningful distinctions and resolve ambiguity; use a separate map only when it helps its consumer |

The old decomposition protocol made every family compulsory for every conforming
run. The current interpretation preserves the questions while leaving their
representation and examination to the work. Current accepted project
commitments still govern any particular decomposition change.

## A.3 System-Wide Invariants (K-*)

### A.3.1 Hierarchy and Identity

**K-HIER-1** prescribed flat packages containing deliverables. **K-ID-1**
distinguished stable identity from changing paths. The active project layout
retains a predictable package/deliverable structure, but this does not make the
folder tree an exhaustive ontology or every path move a scope change. See the
[deliverable-query contract](../../tools/deliverables/README.md).

### A.3.2 Authority and Approval

**K-AUTH-1**, **K-AUTH-2** and **K-BIND-1** concerned human approval, identified
subjects and the distinction between binding acceptance and guidance. Adopted
product consumers retain the applicable definitions in
[Product boundaries](../PRODUCT_BOUNDARIES.md#retained-invariant-identifiers).
Their scope must be respected rather than inferred from this historical account.

A content binding makes an acceptance's subject identifiable, but it neither
performs the human act nor makes the subject correct. Judgment shapes the
purpose, questions and reliance throughout the work. An acceptance record is one
expression of judgment, not its exhaustive definition.

### A.3.3 Sealing and Context

**K-SEAL-1** required sealed context, run approval and a cited approval record.
**K-GHOST-1** limited a delegated agent to declared sources and its sealed brief.
These former development procedures are not current universal duties.

The continuing concern is an understandable assignment and result basis,
together with real privacy and access boundaries. A metadata check cannot
authenticate a human decision or erase the model's learned priors. Current
assignments and host permissions do not, by implication, replace any applicable
product-specific restriction.

### A.3.4 Dependencies

**K-DEP-1** made local dependency registers authoritative and prescribed
aggregation surfaces. **K-DEP-2** required resolvable deliverable targets or an
explicit unknown representation. The active source is now the consumer's
`deliverable.yaml`; reverse links and graphs are generated on demand.

The checker rejects malformed input but reports well-formed unresolved needs,
planned paths and cycles. A declared or present supplier is not automatically
suitable. Ordinary edge changes do not inherit a new approval gate from the
historical catalog; reserved changes remain reserved.

### A.3.5 Status and Lifecycle

**K-STATUS-1** designated `_STATUS.md` as the canonical deliverable lifecycle
indicator. The active development model retired that file and its lifecycle.
The work's condition is assessed from current artifacts and evidence. Acceptance
and release remain attributable acts rather than labels inferred from progress
or a merge.

### A.3.6 Staleness and Change Propagation

**K-STALE-1**, **K-STALE-2** and **K-VAL-1** prescribed transitive staleness,
human triage and comparison with an approved SHA. Current impact queries identify
potential consumers; the meaning of the change determines what must be revisited.
A graph edge alone cannot establish that a result has become invalid.

Specific version-binding contracts still apply to their adopted product subjects.
Retiring a general stale-flag workflow does not remove those contracts.

### A.3.7 Gates

**K-GATE-1** prescribed minimum sealing and run-approval gates while allowing
project variation. The current repository instead distinguishes standing authority
from reserved decisions. A gate is justified by the actual commitment, operation
or consequence it protects; the historical minimum does not govern every new
undertaking.

### A.3.8 Merge and Publication

**K-MERGE-1** underwent historical amendments governing integration and review.
The active repository's standing Git grant and consequence-based verification
rule are in [AGENTS.md](../../AGENTS.md). Required checks concern the exact
candidate. Authorized integration is distinct from acceptance for professional
reliance, and releases remain owner acts.

### A.3.9 Provenance and Epistemic Integrity

**K-PROV-1**, **K-INVENT-1**, **K-CONFLICT-1** and **K-CLAIM-1** addressed sources,
unknowns, disagreements and claim strength. Their wording, as retained for
adopted products, is in
[Product boundaries](../PRODUCT_BOUNDARIES.md#retained-invariant-identifiers).

The important limitation is that a citation can be wrong or irrelevant, an unknown
can remain undetected, and several reviewers can share a mistaken premise. These
rules direct attention and support examination, but their existence does not
guarantee that unsupported output is always found. The chapter's earlier claims
of universal assurance therefore exceeded what the catalog established.

### A.3.10 Write Scope and Snapshots

**K-WRITE-1** prescribed role-header scopes, **K-WRITE-2** specified checkout
path containment, and **K-SNAP-1** required immutable tool-root outputs. The
current repository derives write authority from assignment and host, not a role's
fixed directory category. Explicit read-only conditions remain in effect.

The [resolver](../../tools/workflow_runtime/resolve_workflow.py) reports policy
and checks declared inputs, but it is not itself a sandbox. Applicable
containment formats are still described in
[Compatibility formats](../COMPATIBILITY_FORMATS.md#paths-and-containment).
Historical snapshot duties do not require new run folders. Evidence needed for a
particular consumer or recovery still requires appropriate preservation.

### A.3.11 Agent Index and Governance Surface

**K-AGENTS-1** coupled the entry file, registry and former runtime hierarchy.
The current four roles describe contributions. Agent 0's continuity is the
given; other contributions are engaged as useful. TASK's no-delegation boundary
remains. A registry cannot grant host permissions or silently override the
authorized assignment. The active entry and role files, rather than an archived
index, govern repository work.

### A.3.12 Domain Engine Integration

**K-DOMAIN-1** through **K-DOMAIN-4** distinguish engine-owned state, protected
writes, controlled proposal/application and professional acceptance. The adopted
definitions remain in [Product boundaries](../PRODUCT_BOUNDARIES.md#domain-integration).
Removing administrative development records does not retire them.

The phrase “authoritative domain truth” in the historical definition is read as
canonical domain state under the engine's control, not a claim of guaranteed
physical truth. A proposed operation, a validation result, an applied model change
and human reliance are different things. Current product contracts determine the
required path between them. This appendix does not create or remove an approval
requirement for a particular product operation.

## A.4 Enforcement Map: Analytical Limits

The old map assigned IDs to instruction, runtime, human-review and future-tooling
layers. That allocation proposed a design and documented some mechanisms, but it
did not establish full implementation, independent failures or a comprehensive
assurance argument.

| Kind of mechanism | Evidence it can supply | Limit that remains |
|---|---|---|
| Prose instruction | An explicit expected behaviour and responsibility | Compliance is not guaranteed by reading it |
| Schema or resolver | Rejection of particular malformed or disallowed declarations | Effects outside the checked representation require host enforcement |
| Host permission or protected operation | Restricted behaviour on covered execution paths | Coverage and bypass resistance must be examined |
| Regression or numerical check | Observed behaviour for the tested case and basis | Untested cases and incorrect shared expectations remain possible |
| Independent examination | Criticism from a separate contribution | Independence of assumptions and complete detection are not guaranteed |
| Human decision record | An inspectable representation of a decision and subject | The record does not supply the person's situated judgment or guarantee truth |

The current thesis therefore uses the catalog as evidence of what was learned
about the architecture. Some concerns survived in simpler forms; some product
boundaries remain explicit contracts; several general mechanisms were retired.
This supports a relationship between principles and design that remains open to
revision, not the claim that every named invariant was necessary or that its
removal is automatically safe in every domain.
