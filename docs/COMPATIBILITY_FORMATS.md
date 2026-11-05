# Retained format reference

Compatibility reference for existing readers, not a development procedure.
New/adopting projects use ScopeOfWork, Work and deliverable.yaml under AGENTS.md;
existing project locality conventions remain as recorded there.
Dependency CSV descriptions below are historical source references, not supported
authoring, query or adapter routes. Current dependencies use the native-only
[deliverable method](../tools/deliverables/README.md); superseded dependency tools
and workflows are recoverable through Git. Other adopted source formats are
unchanged, and no project artifact migration is implied.

## Paths and containment

> Numbering note: this section is placed in the §0 preamble (rather than as a new §1) so the established §1–§13 numbers — and every cross-reference to them, e.g. `SPEC §1.2` (tool roots) and `SPEC §6.5` (provenance) — remain stable.

The retained deployment dialect below describes separately scoped Root
governance/instruction changes, explicitly governed in-tree v1 projects,
registered external v2 projects/domains and desktop-selected working folders.
Its retired Root product working root is historical; current Root library work
uses the accepted PRD, AGENTS.md and the authorized undertaking. The separate
instruction root and M2/G4 tranches below belong to that retained deployment
contract, not to every project that consults the library. They remain requirements
where adopted; this qualification authorizes no change to an adopter's contract.
Instruction reads and write containment follow the selected deployment basis.
K-WRITE-2's containment meaning is retained. A documented rejection rule does
not establish that the current host enforces it.

### 0.2.1 `REPO_ROOT` — the active checkout

`REPO_ROOT` is the root of the active git checkout, resolved as:

```sh
REPO_ROOT="$(git rev-parse --show-toplevel)"
```

`REPO_ROOT` MUST be resolved at session start and never hard-coded. In a linked **git worktree**, `git rev-parse --show-toplevel` returns *that worktree's* root — so a worktree is a fully isolated checkout, and every path derived from `REPO_ROOT` re-anchors to it automatically. This is the mechanism that makes worktree-based isolation safe.

`REPO_ROOT` is the active writable Git checkout. Root governance instruction changes act on the repository only under separate explicit scope/M2 authority. Product WORKING_ROOT remains the selected project directory; external projects use their own checkout with disjoint runtime-declared instructions.

`INSTRUCTION_ROOT` is the runtime-declared, read-only home of the **shared instruction surface** (`AGENTS.md`, `CLAUDE.md`, `agents/`, `workflows/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) — the release-managed agent operating system (see `DIRECTIVE.md` §2.6). The runtime resolves it from `CHIRALITY_INSTRUCTION_ROOT`; a V2 project registration fails if it is missing, unreadable, or overlaps the working root. `CLAUDE.md` imports `AGENTS.md` without adding another instruction layer. The instruction surface is read-mostly: changing it is a repo-wide governance action, not ordinary working-root execution.

### 0.2.2 `WORKING_ROOT` — the active workspace

`WORKING_ROOT` is the selected project or domain workspace, explicitly governed in-tree project, or desktop-selected folder. It contains governed product truth and remains subject to ScopePath containment. Historical Root product execution is retained evidence after accepted retirement; Root governance maintenance uses separately authorized repository scopes.

- `WORKING_ROOT` MUST resolve to an absolute path under the active writable `REPO_ROOT`.
- One `INSTRUCTION_ROOT` serves **many** working repositories without per-workspace instruction drift.
- Project writes MUST remain within the selected WORKING_ROOT. Explicit in-tree v1 instruction references may resolve outside it, but never grant instruction writes. External v2 instruction roots MUST be physically disjoint. Root instruction changes require independently owner-authorized M2/G4 tranches; containment itself grants no authority.

### 0.2.3 ScopePath containment (binding)

Every `ScopePath` and every `AllowedWriteTarget` (see `AGENT_WORKFLOW_RUNTIME.md`) MUST:

1. normalize to an absolute path, and
2. resolve **under `WORKING_ROOT`**, which is itself contained by the active checkout returned by `git rev-parse --show-toplevel`.

A `ScopePath` or write target that resolves outside the selected working root — including a sibling pack, the instruction root, a symlink escape, or `..` traversal — MUST be rejected (`SCOPE_OUTSIDE_WORKTREE` or `WRITE_TARGET_OUTSIDE_WORKTREE`); the task stops rather than writing. This is the deterministic backstop that prevents a run from writing into another checkout or pack. This preserves the path-containment meaning of legacy invariant **K-WRITE-2**.

The registered tool roots and their registered subtrees (§1.2) are allowed write locations under this rule when a brief names them and they resolve under `WORKING_ROOT`. This includes `{DAG_ROOT}/cases/<CASE-ID>/`, the home for SCC resolution cases (§1.2, §5.4). Containment itself grants no authority to write there.

### 0.2.4 Path reference discipline

- **Instruction-surface references** (to `agents/`, `workflows/`, `tools/`, root `docs/`, `AGENTS.md`) resolve **`INSTRUCTION_ROOT`-relative**.
- **Working-root references** (to `{EXECUTION_ROOT}`, tool roots, deliverables, `_Coordination/`, decomposition state) resolve **`WORKING_ROOT`-relative**.
- Instruction, coordination, and plan files MUST NOT embed machine-absolute paths (e.g. `/Users/<name>/...`). Absolute paths are permitted only in run records and evidence artifacts, where they record what actually happened and are never re-executed.

---

## Legacy dependency CSV

### 6.1 Schema Version

The `RegisterSchemaVersion` column MUST be present in every row and set to `v3.1`.

### 6.2 Column Specification

#### Core Columns (MUST be present)

| # | Column | Type | Required | Description |
|---|---|---|---|---|
| 1 | `RegisterSchemaVersion` | string | MUST | Schema version identifier (`v3.1`) |
| 2 | `DependencyID` | string | MUST | Unique within the deliverable register (e.g., `DEP-01-01-001`) |
| 3 | `FromPackageID` | string | MUST | Package ID of the host deliverable |
| 4 | `FromDeliverableID` | string | MUST | Deliverable ID of the host deliverable |
| 5 | `FromDeliverableName` | string | MUST | Human-readable name of the host deliverable |
| 6 | `DependencyClass` | enum | MUST | `ANCHOR` or `EXECUTION` |
| 7 | `AnchorType` | enum | MUST | See Section 6.3 |
| 8 | `Direction` | enum | MUST | `UPSTREAM` or `DOWNSTREAM` |
| 9 | `DependencyType` | enum | MUST | See Section 6.3 |
| 10 | `TargetType` | enum | MUST | See Section 6.3 |
| 11 | `TargetPackageID` | string | optional | Package ID of the target (when target is a deliverable) |
| 12 | `TargetDeliverableID` | string | optional | Deliverable ID of the target (when `TargetType=DELIVERABLE`) |
| 13 | `TargetRefID` | string | optional | Stable reference ID for non-deliverable targets (e.g., `SOW-003`, `OBJ-001`) |
| 14 | `TargetName` | string | SHOULD | Human-readable name/description of the target |
| 15 | `TargetLocation` | string | optional | Path, URL, or document identifier for the target |
| 16 | `Statement` | string | SHOULD | Human-readable dependency statement |
| 17 | `EvidenceFile` | string | MUST* | Source document containing evidence (* or `location TBD`) |
| 18 | `SourceRef` | string | MUST* | Path + heading/section within the evidence file (* or `location TBD`) |
| 19 | `EvidenceQuote` | string | SHOULD | Short quote from source (<= 30 words) |
| 20 | `Explicitness` | enum | SHOULD (REQUIRED in an accepted DAG version, §5.4) | `EXPLICIT` or `IMPLICIT` |
| 21 | `RequiredMaturity` | string | optional | Maturity level required for the dependency to be satisfied |
| 22 | `ProposedMaturity` | string | optional | Proposed maturity level (agent suggestion) |
| 23 | `SatisfactionStatus` | enum | SHOULD (REQUIRED in an accepted DAG version, §5.4) | See Section 6.3 |
| 24 | `Confidence` | enum | SHOULD (REQUIRED in an accepted DAG version, §5.4) | `HIGH`, `MEDIUM`, or `LOW` |
| 25 | `Origin` | enum | MUST | `DECLARED` or `EXTRACTED` |
| 26 | `FirstSeen` | date | MUST | ISO date of first extraction (`YYYY-MM-DD`) |
| 27 | `LastSeen` | date | MUST | ISO date of most recent confirmation (`YYYY-MM-DD`) |
| 28 | `Status` | enum | MUST | `ACTIVE` or `RETIRED` |
| 29 | `Notes` | string | optional | Explanatory remarks; epistemic labels (`FACT`, `ASSUMPTION`, `PROPOSAL`) |

#### Extension Columns (MAY be present; non-breaking)

| Column | Type | Description |
|---|---|---|
| `EstimateImpactClass` | enum | `BLOCKING`, `ADVISORY`, `INFO`, `TBD` |
| `ConsumerHint` | enum | `TASK`, `TASK_ESTIMATING`, `AGGREGATION`, `EVALUATION`, `RECONCILIATION_LEGACY`, `TBD` |

### 6.3 Canonical Enum Values

**DependencyClass:**
| Value | Meaning |
|---|---|
| `ANCHOR` | Tree edge: connects deliverable to a definition/traceability node |
| `EXECUTION` | DAG edge: information flow, prerequisite, handoff, or constraint |

**AnchorType:**
| Value | Meaning |
|---|---|
| `IMPLEMENTS_NODE` | Parent definition node (exactly one per deliverable) |
| `TRACES_TO_REQUIREMENT` | Requirement trace link (zero or more) |
| `NOT_APPLICABLE` | Used for EXECUTION rows |

**Direction:**
| Value | Meaning |
|---|---|
| `UPSTREAM` | This deliverable requires information FROM the target |
| `DOWNSTREAM` | This deliverable produces information FOR the target |

**DependencyType:**
| Value | Usage | Meaning |
|---|---|---|
| `PREREQUISITE` | Preferred | Required input or approval before work can proceed |
| `INTERFACE` | Preferred | Explicit data/artifact exchange between deliverables |
| `HANDOVER` | Preferred | Output of one deliverable consumed as input to another |
| `CONSTRAINT` | Preferred | Explicit constraint or condition |
| `ENABLES` | Preferred | This deliverable enables downstream work |
| `OTHER` | Preferred | Dependency that does not fit other categories; used for ANCHOR rows |

**TargetType:**
| Value | Meaning |
|---|---|
| `DELIVERABLE` | Another deliverable in the project |
| `PACKAGE` | A package (used in ANCHOR rows) |
| `WBS_NODE` | Work breakdown structure or scope node |
| `REQUIREMENT` | A specific requirement (SOW item, objective, etc.) |
| `DOCUMENT` | An external or reference document |
| `EQUIPMENT` | Physical equipment or asset |
| `EXTERNAL` | External entity (organization, standard, etc.) |
| `UNKNOWN` | Target cannot be confidently resolved |

**Explicitness:**
| Value | Meaning |
|---|---|
| `EXPLICIT` | Dependency is explicitly stated in source text |
| `IMPLICIT` | Dependency is implied but not directly stated |

**SatisfactionStatus:**
| Value | Meaning |
|---|---|
| `TBD` | Not yet assessed |
| `PENDING` | Assessed but not yet satisfied |
| `IN_PROGRESS` | Actively being worked toward satisfaction |
| `SATISFIED` | Dependency has been fulfilled |
| `WAIVED` | Dependency waived by human decision |
| `NOT_APPLICABLE` | Dependency determined to be not applicable |

**Confidence:**
| Value | Meaning |
|---|---|
| `HIGH` | Strong evidence; explicit source reference |
| `MEDIUM` | Reasonable evidence; some interpretation required |
| `LOW` | Weak evidence; significant interpretation or assumption |

**Origin:**
| Value | Meaning |
|---|---|
| `DECLARED` | Human-declared dependency |
| `EXTRACTED` | Agent-extracted from source documents |

**Status:**
| Value | Meaning |
|---|---|
| `ACTIVE` | Dependency is currently observed and relevant |
| `RETIRED` | Dependency was previously observed but is no longer found in source text |

### 6.4 Row Classification

**ANCHOR rows** connect a deliverable to the project's definition tree:
- Exactly one `IMPLEMENTS_NODE` row SHOULD exist per deliverable (connects to parent package/WBS node)
- Zero or more `TRACES_TO_REQUIREMENT` rows (connect to scope items, objectives, requirements)
- `DependencyType` MUST be `OTHER` for ANCHOR rows
- `AnchorType` MUST NOT be `NOT_APPLICABLE` for ANCHOR rows

**EXECUTION rows** capture information flow and constraints:
- `DependencyClass` MUST be `EXECUTION`
- `AnchorType` MUST be `NOT_APPLICABLE`
- `DependencyType` uses the preferred execution enums (`PREREQUISITE`, `INTERFACE`, `HANDOVER`, `CONSTRAINT`, `ENABLES`, `OTHER`)

## Scope-of-work format

Current development keeps commitments and acceptance criteria in the deliverable's ScopeOfWork. The detailed formats below support existing readers and explicitly selected methods; they do not require new lifecycle files, append registers or review packets.

The document begins with this YAML subset:

```yaml
---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-XX-YY
package_id: PKG-XX
decomposition_basis: path/to/accepted/decomposition@<commit>
project_scope_refs: [SOW-NNN]
package_objective_refs: [OBJ-NNN]
---
```

The exact `deliverable_id` and `package_id` widths are supplied by the active
project decomposition rather than inferred from examples. Both reference
lists must be non-empty. A schema marker selects a parser; it does not prove
acceptance, lifecycle, or professional reliance.

The required level-two headings, in order, are:

1. `Purpose and Objective Traceability`
2. `Deliverable Definition — Ontology`
3. `Completion and Reliance Basis — Epistemology`
4. `Production and Verification Method — Praxeology`
5. `Governing Values and Decisions — Axiology`
6. `Output and Evaluation Matrix`

Headings state the practical question first. Content must remain grounded in
accepted decomposition, sources, and decisions; philosophical labels do not
license unsupported abstraction.

## 4. Identifier grammar

The machine-readable catalog is `tools/scope_of_work/id_catalog.json`.
Validators and converters consume that catalog rather than hard-coding
independent prefix lists. Local definitions use this form:

```markdown
- **REQ-017** — The output shall ...
```

External references qualify the local identifier with the deliverable ID:
`DEL-03-02-REQ-017`. Local IDs use exactly three decimal digits and are unique
within one Scope of Work.

During deterministic finalization of a converted contract, preserved literal
legacy text is rendered as Markdown blockquotes. ID-shaped text inside those
quotations is source context, not a local definition or reference. Canonical
SOW definitions and references remain outside quotations.

| Prefix | Meaning | Primary section |
|---|---|---|
| `OUT` | Expected output | Ontology |
| `CLM` | Descriptive claim | Any substantive section |
| `REQ` | Normative requirement | Epistemology |
| `AC` | Acceptance criterion | Epistemology |
| `VER` | Verification method | Praxeology |
| `AX` | Governing value, rationale, or authority constraint | Axiology |
| `TBD` | Unresolved information | Any substantive section |
| `CON` | Unresolved conflict | Any substantive section |
| `REM` | Legacy Remaining identifier, retained for historical or still-pinned programs | `_STATUS.md` under that accepted convention |

The registered deterministic checklist tool consumes the validated
deliverable `AC-*` definitions and emits them in source order with exact text,
qualified identity, production-contract hash and source location, and matrix-linked
`VER-*` records or explicit `HUMAN_REVIEW: <method>`. The review workflow consumes that
artifact; it must not mint a second acceptance-criterion namespace,
re-extract, paraphrase, reorder, renumber, or silently omit criteria. Agent or
human judgment begins only in an actual human-gated review and remains
distinct from checklist compilation.

Every `OUT-*` cites at least one project-scope and package-objective reference.
Every `AC-*` cites at least one `VER-*` or uses the matrix syntax
`HUMAN_REVIEW: <method>`. Every declared `OUT-*`, `AC-*`, and `VER-*` is
consumed by at least one matrix row; orphan evaluation definitions fail
validation.

## 5. Output and evaluation matrix

The matrix binds expected production to evaluation intent. Its required
columns are:

```text
Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation
```

Tests implement verification methods and produce evidence; tests do not
silently define scope or acceptance criteria. For loops adopting the local-graph
arrangement, the graph carries selected execution against this stable target,
referencing qualified Scope-of-Work IDs where applicable. Candidate-bound
evidence accounts for the applicable production obligations; an empty graph or
absent Remaining list does not establish fulfillment. `_STATUS.md ## Remaining`
retains its current-delta role only for programs whose accepted method basis
still requires that legacy convention. Preserve their source identities and
historical records until an explicitly authorized transition accounts for them.

## Legacy production-format resolution

For localities using the current `SOW_V1` method and validator, the classification
below and the one-canonical-format rule remain applicable. Current setup and
validation distinguish `SOW_V1`, `INVALID` and `AMBIGUOUS`; invalid or unauthorized
dual input fails closed. `MIGRATION_DUAL` is permitted only in an isolated
conversion workspace with the exact migration authority bound in the contract.
This does not impose the `SOW_V1` schema on independent or domain-specific formats.

The legacy transition/conversion obligations and retirement provisions below
retain their adopted contract and D-GOV-16 activation basis. They do not require
current Root setup to create lifecycle/phase files, enter conversion, or restore
legacy authoring tools. Historical formats retain their identities.

| Files present | Interpretation |
|---|---|
| Four valid legacy production documents only | `LEGACY_FOUR_DOC`; transitional compatibility for an existing unconverted deliverable |
| One valid `ScopeOfWork.md` only | `SOW_V1`; canonical production contract |
| Both complete formats | `MIGRATION_DUAL` only in an isolated, explicitly authorized conversion workspace; otherwise `AMBIGUOUS` and invalid |
| Partial legacy kit, invalid `ScopeOfWork.md`, or neither at or beyond `INITIALIZED` | `INVALID` |

An accepted deliverable state contains exactly one canonical production
format. New deliverables use `SOW_V1`. Legacy-only deliverables remain valid
during the authorized transition window but must not receive new
four-document production initialization after activation.

The `four-documents` skill and legacy readers remain supported compatibility
surfaces until all authorized conversions, caller migrations, audit closure,
and rollback windows complete. Retirement requires a later evidence-backed
owner act; D-GOV-16 activation alone does not delete them.

## Decomposition data

#### Atomic Unit
- `UnitID` (stable; format defined by conforming workflow)
- `Statement` (normalized atomic statement)
- `InOutStatus` (`IN|OUT|TBD`)
- `SourceRef` (best-effort; `TBD` allowed)
- `Notes`

#### Objective
- `ObjectiveID` (stable; `OBJ-NNN`)
- `Statement`
- `Notes`
- `MappedProductionUnits` (best-effort; may be empty but must be flagged)

#### Partition
- `PartitionID` (stable; format defined by conforming workflow)
- `Name`
- `ScopeDescription`
- `InclusionCriteria` (optional)
- `Exclusions` (optional)

#### Production Unit
- `ProductionUnitID` (stable; mechanically coupled to `ParentPartitionID`; format defined by conforming workflow)
- `Name`
- `ParentPartitionID`
- `Description`
- `ResponsibleParty` (`TBD` allowed)
- `Type` (domain-specific taxonomy defined by conforming workflow)
- `AnticipatedArtifacts` (list; `TBD` allowed)
- `CoversUnits` (best-effort; atomic unit IDs)
- `SupportsObjectives` (best-effort; objective IDs)

Conforming workflows MAY add fields (for example, `ContextEnvelope` in
`software-decomp`, `CanonicalSchema` in `domain-decomp`, or `CBSHint` in
`project-decomp`). Added fields MUST NOT conflict with the base schema.

#### Artifact
- `ArtifactID` (optional stable ID)
- `Name`
- `ParentProductionUnitID`
- `Type` (domain-specific taxonomy defined by conforming workflow)
- `Notes`

---

## Historical authoring identifiers

R1–R17 identify prior audit references, not additional development obligations.


| ID | Historical meaning |
|---|---|
| R1 | Preserve explicit human decision rights. |
| R2 | Type 2 returns decisions to its caller and does not delegate. |
| R3 | Give runs explicit write boundaries; derived outputs do not replace source truth. |
| R4 | Match snapshot requirements to authority and phase boundaries; preserve immutable snapshots. |
| R5 | Cite evidence for nontrivial governed claims or record the source-location gap. |
| R6 | Expose unknowns and missing evidence. |
| R7 | Surface conflicts; human semantic rulings remain distinct from execution. |
| R8 | Bound Type 2 context, permissions, outputs, and failure returns through the brief. |
| R9 | Keep publication and Git operations reviewable; they do not establish semantic approval. |
| R10 | Make applicable workflow tool restrictions explicit in execution configuration. |
| R11 | Give deterministic tools explicit I/O, scope, errors, verification, and rerun behavior. |
| R12 | Distinguish role, runtime, workflow, tool, and brief responsibilities. |
| R13 | Calibrate claims to their warrant. |
| R14 | Preserve accepted-source, derivative, snapshot, handoff, closure, sequencing, and cycle requirements. |
| R15 | Keep registry membership and lifecycle status explicit; surface narrative drift. |
| R16 | Contain writes within the authorized active checkout. |
| R17 | Cover applicable execution and authority concerns with proportionate design evidence. |


## Legacy decomposition document shape

### Required sections in the Decomposition Document

Every conforming workflow's output MUST include these sections. Order is recommended but not mandatory.

#### 1) Vocabulary Map (table)
Minimum columns:
- `CanonicalTerm`
- `Synonyms`
- `Notes`

#### 2) Decomposition Ledger (table)
Minimum columns:
- `UnitID`
- `InOutStatus`
- `UnitStatement`
- `SourceRef`
- `PartitionID` (PROJECT, SOFTWARE: exactly one for every unit, whether IN, OUT or TBD; DOMAIN: required for IN units)
- `ProductionUnitID(s)` (one or many; or `TBD`)
- `ObjectiveID(s)` (zero or many; or `TBD`)
- `DecisionRef` (optional; points to Decision Log entry)
- `OpenIssue` (`TRUE|FALSE`)
- `Notes`

**Hard rule:** every `UnitID` that I4 requires to have a partition has exactly
one `PartitionID`: every unit in PROJECT and SOFTWARE, every IN-scope unit in
DOMAIN.

Conforming workflows use domain-specific column names (for example,
`ScopeItemID` / `PackageID` / `DeliverableID(s)` in `project-decomp`, or
`UnitID` / `CategoryID` / `KnowledgeTypeID(s)` in `domain-decomp`). The
structural contract — every unit I4 requires to have a partition maps to
exactly one partition (in PROJECT and SOFTWARE every unit, whether IN, OUT or
TBD; in DOMAIN every IN unit), and only IN units require production-unit
mappings — is invariant.

#### 3) Coverage & Telemetry (summary block)
Minimum fields:
- `UnitCount`
- `PartitionCount`
- `ProductionUnitCount`
- `ObjectiveCount`
- `UnassignedINUnits` (must be 0 for acceptance; PROJECT and SOFTWARE report
  every unit without a partition, whatever its status, as
  `UnassignedScopeItems`, which must also be 0)
- `UnitsWithoutProductionUnitMapping` (count)
- `UnmappedObjectives` (count)
- `OpenIssuesByType` (counts, with IDs)
- `Revision` identifier and date

Conforming workflows MAY add domain-specific telemetry fields (for example,
`ContextEnvelopeCounts` in `software-decomp`). They MUST NOT omit the base fields.

#### 4) Open Issues list
Unresolved items referencing stable IDs.

#### 5) Decision Log / Change Log
Non-trivial assignment and boundary decisions, recorded so later work can trace rationale.

---

### Extension contract (what a conforming workflow MUST provide)

When creating a new decomposition workflow that conforms to this standard, its
package MUST:

1. **Reference this standard.** State conformance to `docs/DECOMPOSITION_STANDARD.md`.
2. **Bind abstract entities to domain-specific names.** Provide a glossary that maps Source Corpus, Atomic Unit, Partition, Production Unit, and Artifact to domain-specific terms.
3. **Define ID formats.** Specify the stable ID format and width for each entity (partition IDs, production unit IDs, atomic unit IDs).
4. **Define the production-unit type taxonomy.** Provide the domain-specific type values (e.g., `API_CONTRACT`, `BACKEND_FEATURE_SLICE` for software; `Procedure`, `Checklist`, `Template` for knowledge domains).
5. **Extend stage actions.** Add domain-specific actions and outputs while
   preserving the applicable grouped checkpoint semantics and count.
6. **Declare execution restrictions when needed.** Put workflow-specific
   capability or command restrictions in `execution.json`; actual writes remain
   supplied by the run brief and host.
7. **Add domain-specific fields, anti-patterns, and SPEC requirements** as needed. These extend the base; they do not replace it.
8. **Declare domain-specific telemetry fields** beyond the base Coverage & Telemetry schema.

9. **Declare package architecture.** Specify which output surfaces are authoritative working surfaces, which are authoritative companion registers, and which (if any) are derived publication artifacts. Include a companion inventory section in the main decomposition document so downstream agents can discover the package layout.

A conforming workflow SHOULD also:
- Include domain-specific rationale explaining why the extensions exist.
- Document any deviations from the base specification with explicit justification.

[[END:STRUCTURE]]

---

[[BEGIN:RATIONALE]]

## 10. Epistemic Ontology

The epistemology pillar (see `DIRECTIVE.md` §2) operates on a set of formally defined entities. These entities constitute the ontology of the epistemic layer — the things that the epistemic mechanisms (mandatory provenance, no invention, conflict surfacing, epistemic labeling) act upon.

### 10.1 Epistemic Primitives

| Primitive | Definition | Canonical Location |
|---|---|---|
| **Claim** | An assertion that something is the case. The atomic unit of the epistemology. Every non-trivial assertion produced by an agent in a governed workflow is a claim. | Dependency rows, document content, agent outputs |
| **Warrant** | The justification for believing a claim. Always extrinsic — a source citation (file + section + quote) — never intrinsic (model confidence or plausibility). | `EvidenceFile`, `SourceRef`, `EvidenceQuote` columns in `Dependencies.csv` (`SPEC.md` §6.5) |
| **Status** | The epistemic classification of a claim's certainty, expressed as one of four labels. | `Notes` fields, dependency records, agent output prose |
| **Gap** | The explicit, positive assertion that a warrant has not been found. A gap is not the absence of information — it is an entity representing that absence, making it visible and actionable. | `TBD` markers, `location TBD` in provenance fields, open issues |
| **Conflict** | Two or more claims with incompatible warrants about the same key. The existence of a conflict is itself an epistemic entity that must be resolved before the deliverable can advance. | Conflict Tables (`ConflictID`, `Key`, `Contenders`, `ProposedAuthority`, `HumanRuling`) |
| **Ruling** | A human decision that resolves a gap or conflict, transforming epistemic status. Rulings are binding and recorded in versioned files. | `HumanRuling` column in Conflict Tables, finding dispositions in REVIEW, gate decisions |

### 10.2 Epistemic Relationships

| Relationship | Description |
|---|---|
| A claim HAS a status | Exactly one of FACT, ASSUMPTION, PROPOSAL, or TBD |
| A claim MAY HAVE a warrant | Source file + section reference + optional quote; absence is structurally visible |
| A claim WITHOUT a warrant | Is a gap; status is TBD or uncited PROPOSAL; the absence of warrant is itself a finding |
| Two claims may be IN CONFLICT | Same key, incompatible values, different sources |
| A conflict REQUIRES a ruling | HumanRuling = TBD until the licensed professional adjudicates |
| A ruling TRANSFORMS status | Resolves gaps (TBD → FACT or ASSUMPTION), accepts or rejects proposals, and resolves conflicts (competing claims → one accepted) |

### 10.3 Epistemic Labels

The four epistemic labels classify the certainty status of claims:

| Label | Meaning | Reviewer Action |
|---|---|---|
| `FACT` | Directly observed in source text with citation | Verify citation; accept if source is authoritative |
| `ASSUMPTION` | Reasonable inference grounded in cited material; not directly stated and still requiring validation | Validate or reject; document decision |
| `PROPOSAL` | Suggested interpretation, action, or design move; may cite supporting context, but requires human decision to become binding | Decide; record rationale |
| `TBD` | Unknown; placeholder requiring resolution | Resolve before reliance |

### 10.4 Warrant Lifecycle

Claims within a deliverable progress through a warrant lifecycle that tracks their epistemic state, interleaved with the deliverable lifecycle (`§5`) that tracks production state:

```
UNWARRANTED → CITED → REVIEWED → AUTHENTICATED
```

| Warrant State | Meaning | Transition Mechanism |
|---|---|---|
| `UNWARRANTED` | Claim exists but has no source citation; status is TBD or uncited PROPOSAL | Agent produces claim; K-INVENT-1 requires TBD marking for gaps |
| `CITED` | Claim has a source citation; status is FACT, ASSUMPTION, or cited PROPOSAL | Agent attaches provenance; K-PROV-1 enforces |
| `REVIEWED` | Claim has been examined by a licensed professional; findings dispositioned | REVIEW gates; human rules on findings |
| `AUTHENTICATED` | Claim is part of an authenticated PWP; the professional warrants it under duty of care | Authentication binds to git SHA; K-AUTH-2 enforces |

The deliverable lifecycle asks: *what state is this work product in?* The warrant lifecycle asks: *what state is our knowledge about this work product in?* A deliverable is ready for issuance when its warrants are sufficient — when the licensed professional has determined that the epistemic state of the claims supports authentication under professional responsibility.

The two lifecycles are correlated but not identical. A deliverable in `IN_PROGRESS` contains a mixture of warranted and unwarranted claims. The transition to `CHECKING` requires layered entry conditions (`SPEC.md` §3.4): the universal entry minimums — that critical claims have been warranted (all CRITICAL findings must have non-TBD human disposition; see §10.6) and that current candidate-bound evidence accounts for fulfillment of the deliverable's applicable production obligations — together with a candidate-specific declared checking basis and the human declaration that freezes the candidate. The transition to `ISSUED` requires that the professional has authenticated the work — the act of warranting the deliverable's claims under professional responsibility; post-issuance changes flow only through the governed scope-change process.

### 10.5 Enforcing Invariants

| Invariant | Epistemic Primitive Governed |
|---|---|
| K-PROV-1 (mandatory provenance) | Warrant — every claim must have an extrinsic warrant or explicit `location TBD` |
| Audit-time assessment (TASK with `Workflow: audit-epistemic`; future harness `evidence-check`), bounded by K-CLAIM-1 | Status — the labeling act is assessed at audit time, not producer-emitted; per D-GOV-08 (ruled 2026-07-01) |
| K-INVENT-1 (no invention) | Gap — missing data must be represented as a gap (TBD), not filled with a fabrication |
| K-CONFLICT-1 (conflict surfacing) | Conflict — disagreements must be exposed as conflicts, not silently resolved |
| K-AUTH-1 (human authority) | Ruling — only humans may author binding rulings and approval records |
| K-AUTH-2 (SHA-bound approval) | Authentication — the warrant-to-content binding is mechanically verifiable |

### 10.6 Review Finding Severity

Registered per D-GOV-08 (`docs/governance_harness/_DECISIONS/D-GOV-08_epistemic_vocabulary_operationalization.md`), ruled by the owner 2026-07-01.

Review-gate findings are classified with the four-level enum defined by the review type system in `docs/thesis/SE_Design_Analysis.md` §7.3 (`FindingSeverity`):

```
CRITICAL | MAJOR | MINOR | OBSERVATION
```

This is the finding vocabulary that the "CRITICAL findings" gate conditions in §10.4 reference.

Distinctness:

- This enum is distinct from the governance-verifier taxonomy (`BLOCK`, `REVIEW`, `WARN`, `INFO`, `NOT_APPLICABLE`; §11): review severities classify review-gate findings about deliverable content; verifier severities classify governance harness findings.
- It is also distinct from the agent-conformance rubric's Blocker/High/Medium/Low (`docs/rubrics/AUDIT_AGENT.md`): that rubric grades agent-file conformance, not deliverable review findings.

---


## Legacy path tokens

Agent instructions and workflows reference roots through `{*_ROOT}` tokens. Each token resolves against exactly one anchor. Projects and domains MAY bind additional workspace-local tokens, but every such token MUST resolve under `WORKING_ROOT`.

| Token | Anchor | Resolves to |
|---|---|---|
| `{REPO_ROOT}` | self | `git rev-parse --show-toplevel` (the active checkout) |
| `{INSTRUCTION_ROOT}` | runtime-declared | the shared instruction surface; the Chirality checkout, packaged app resources, or the separately governed repository instruction root |
| `{WORKING_ROOT}` | `REPO_ROOT`-relative | the selected project/domain pack or user-selected folder; Root governance maintenance is separately scoped and is not project product execution |
| `{EXECUTION_ROOT}` | `WORKING_ROOT`-relative | the execution instance root (project-defined; often `WORKING_ROOT` or `WORKING_ROOT/execution`) |
| `{COORDINATION_ROOT}` | `EXECUTION_ROOT`-relative | `{EXECUTION_ROOT}/_Coordination/` |
| `{DECOMP_ROOT}` / `{DECOMPOSITION_ROOT}` | `EXECUTION_ROOT`-relative | `{EXECUTION_ROOT}/_Decomposition/` (or a domain pack's `_Decomposition/`) |
| `{AGGREGATION_ROOT}` | tool-root-relative | `{EXECUTION_ROOT}/_Aggregation/` |
| `{EVALUATION_ROOT}` | tool-root-relative | `{EXECUTION_ROOT}/_Evaluation/` |
| `{RECONCILIATION_ROOT}` | tool-root-relative | `{EXECUTION_ROOT}/_Reconciliation/` |
| `{ESTIMATES_ROOT}` | tool-root-relative | `{EXECUTION_ROOT}/_Estimates/` |
| `{DAG_ROOT}` | tool-root-relative | `{EXECUTION_ROOT}/_DAG/`: accepted project DAG versions, their `_LATEST.md` pointer, candidates and SCC cases (§1.2, §5.4) |
| `{SOURCE_AUDIT_ROOT}`, `{ASSETS_ROOT}`, `{PUBLICATION_ROOT}`, `{RESEARCH_ROOT}`, `{PLANNING_ROOT}`, `{RUN_ROOT}`, `{CONTEXT_ROOT}` | `WORKING_ROOT`-relative | domain/workspace-local roots bound by the owning role/workflow; MUST resolve under `WORKING_ROOT` |
| `{WORKFLOW_ROOT}` | `INSTRUCTION_ROOT`-relative | `{INSTRUCTION_ROOT}/workflows/<name>/` |
| `{SKILL_ROOT}` | historical adapter token | Historical briefs retain their recorded binding; the migration adapter maps a selected legacy package to `{WORKFLOW_ROOT}` without granting writes. |
| `{TOOL_ROOT}` | context-dependent | `{INSTRUCTION_ROOT}/tools/` when referring to the deterministic tool layer; a project tool root (`{EXECUTION_ROOT}/_<Name>/`) when referring to a derived-output root (see §1.2) |

The token vocabulary above is the registry; an agent that introduces a new `{*_ROOT}` token MUST declare its anchor in the applicable runtime or workflow contract and keep it consistent with this table.

---

## Stable dependency identities

- `DependencyID` MUST be unique within a single deliverable's register
- `DependencyID` format: `DEP-{PKG}-{DEL}-{SEQ}` (e.g., `DEP-01-01-001`)
- `FromDeliverableID` MUST match the host deliverable's ID
- For `TargetType=DELIVERABLE`: `TargetDeliverableID` MUST contain the target's stable deliverable ID
- For non-deliverable targets: `TargetDeliverableID` MUST be empty; use `TargetRefID` and `TargetName`

---

## Historical source contracts

The following links preserve exact source meaning for legacy workflows and readers.
They are consulted only when that legacy method is deliberately selected; they are
not current development procedures. Section numbers in legacy method citations
refer to these archived editions, not to this reference's section numbering.

### Historical specification

[Archived SPEC](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/SPEC.md).

### Historical vocabulary

[Archived TYPES](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/TYPES.md).

### Historical invariants

[Archived CONTRACT](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/CONTRACT.md).

### Historical founding direction

[Archived DIRECTIVE](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/DIRECTIVE.md).

### Historical decomposition contract

[Archived DECOMPOSITION_STANDARD](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/DECOMPOSITION_STANDARD.md).

### Historical scope conversion contract

[Archived DELIVERABLE_SCOPE_OF_WORK_STANDARD](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md).

### Historical concordance method

[Archived DELIVERABLE_CONCORDANCE_METHOD](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/DELIVERABLE_CONCORDANCE_METHOD.md).

### Historical cycle method

[Archived CYCLE_DRIVEN_RESOLUTION](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/CYCLE_DRIVEN_RESOLUTION.md).

### Historical component contract

[Archived WORKFLOW_COMPONENT_STANDARD](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/WORKFLOW_COMPONENT_STANDARD.md).

### Historical instruction architecture

[Archived DBM_Agent_Instruction_Architecture](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/DBM_Agent_Instruction_Architecture.md).

### Historical roadmap

[Archived PLAN](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/PLAN.md).

### Historical Root programme

[Archived PRD_ROOT](https://github.com/sgttomas/chirality/blob/fa927aac8c0e3be6bfa8f7ce8ec49daa6e112ee4/docs/PRD_ROOT.md).
