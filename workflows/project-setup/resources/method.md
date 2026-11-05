# project-setup — method

**Applicability:** Retained DOMAIN and explicitly adopted legacy phase/control-file
setup only. Use [current-project.md](current-project.md) for the current
PROJECT/SOFTWARE locality and pre-integration reconciliation. The historical
control-file and run-log steps below do not apply to that route.

## Method

### Schedule workflow (when selected)

1. **Ingest and validate:** bind accepted decomposition and the local needs used for this undertaking; confirm scope, schedule basis, and edge-classification rules.
2. **Structure and sequence:** use deterministic graph tools where possible; present the candidate network or constraint matrix for human correction.
3. **Durations and calendars:** generate a blank duration template by default; collect human durations, calendars, milestones, and gates.
4. **Render:** compute dates and produce reviewable CSV/Mermaid plus basis-appropriate critical-path or risk analysis.
5. **Publish:** after human acceptance, freeze a new `_Schedule/{RunID}/` snapshot and record source provenance, assumptions, waivers, and rerun requirements.

No schedule gate may be skipped. Repetitive graph analysis, calculation, and rendering belong in TASK workflows or deterministic tools; WORKING_ITEMS presents and records human decisions and validates fan-in.

### Function 1: Initialize (once per workspace; `INITIAL` mode)

**Goal:** Ingest the decomposition, record the human's coordination arrangements and establish local dependency authoring.

An accepted scope-change amendment does not re-run Functions 1 and 2; its amended scope is set up by Function 5.

#### Phase 1.1: Ingest decomposition

**Action:**
- Receive the path to the decomposition document from the human (or locate it under `{DECOMP_ROOT}/`).
- Read the decomposition document.
- Extract all packages and deliverables, preserving all present fields.
  - Minimum expected fields: IDs, names, package membership, descriptions, types, anticipated artifacts.
  - Preserve optional metadata/hints (do not drop unknown columns/fields).

**Output:** A short ingestion summary for the human.

**Gate question:** “I ingested a decomposition with [N] packages and [M] deliverables. Is this the correct decomposition to use?”

---

#### Phase 1.2: Record coordination arrangements

**Action:**
- Resolve the human's intended use of schedules, dependency-informed sequencing
  or both. Reuse arrangements already supplied; request only a missing decision
  that matters to the selected undertaking.
- Record those arrangements in `{COORDINATION_ROOT}/_COORDINATION.md`.
  Bootstrap its root with
  `tools/scaffolding/scaffold_tool_root.sh {EXECUTION_ROOT} _Coordination`.
- Dependencies have one current authoring form: consumer-local
  `deliverable.yaml`. Do not select tracking modes or infer input satisfaction
  from a default lifecycle threshold. Existing policy and accepted holds remain
  in force; no format migration is implicit in setup.

#### Phase 1.3: Establish dependency authoring scope

**Action:**
- Identify the accepted deliverables and the responsible consumers who can
  state what each actual input must support. Use accepted scope, relevant
  material in the project's adopted work locality (`Work/` by the shared
  default), sources and intended use, rather than textual extraction
  alone. A need may be reasoned from that evidence; do not invent a producer
  commitment or claim every need is captured.
- Keep source uncertainty, maturity/case/use conditions and actual triggers in
  the declaration. Preserve distinct conditions between the same endpoints.
- Use `dependency-extract` after production scope exists (Phase 2.2b) to author
  or refresh needs. Ordinary need updates do not add an acceptance checkpoint;
  changes to scope, reserved decisions or technical holds follow their actual
  authority.

---

### Function 2: Scaffold + run setup-time pipelines (once per workspace, human-gated; `INITIAL` mode)

**Goal:** Create the workspace and populate it with the minimum viable fileset, then run initialization pipelines.

#### Phase 2.0: Initialize project tool roots

**Action:**
- Ensure `{EXECUTION_ROOT}/` exists.
- Bootstrap required tool roots using `tools/scaffolding/scaffold_tool_root.sh {EXECUTION_ROOT} {ROOT_NAME}` for each of: `_Coordination`, `_Decomposition`, `_Sources`. Additional tool roots (e.g., `_Aggregation`, `_Estimates`, `_Reconciliation`) may be created if the project uses them, but WORKING_ITEMS should not invent tool roots beyond what the human requests or what the project standard requires.

**Deterministic-first rule for setup pipelines:**
- Use deterministic tools for folder creation, status initialization, validation, counting, and other repeatable filesystem operations.
- Use sub-agent language-model work only where text must be extracted, normalized, or written from decomposition/source material and no deterministic tool exists for that operation.

---

#### Phase 2.1: Apply the preparation skill (scaffolding)

**Action:**
- Discover the effective `preparation` skill descriptor. Preserve its complete
  source-qualified identity in the ordered `methods` field as
  `[{kind: "skill", name: "preparation", source: <descriptor.source>, sourceRootId: <descriptor.sourceRootId>}]`.
  Do not hardcode an origin or reduce the selected identity to its basename.
- Select `PREPARATION_ACTOR` from the skill's eligible roles under the active
  host, role, and brief. WORKING_ITEMS may apply the bounded method directly or
  dispatch TASK; using the skill does not force delegation.
- **WORKING_ITEMS (workflow: project-decomp) / WORKING_ITEMS (workflow: software-decomp):** For each package in the decomposition, `PREPARATION_ACTOR` uses deterministic scaffolding/status tools for filesystem operations:
  - `tools/scaffolding/scaffold_package.sh {EXECUTION_ROOT} {PKG_ID} {PkgLabel}` — creates the package folder with all 9 lifecycle subfolders.
  - `tools/scaffolding/scaffold_deliverable.sh {pkg_folder}/1_Working {DEL_ID} {DelLabel}` — creates each deliverable folder with four metadata stubs and `deliverable.yaml` (`id` plus `needs: []`).
  - A newly created `_STATUS.md` stub is written to `OPEN` in the exact form given by the `preparation` skill's scaffold contract, naming the actual actor; `write_status.sh` handles later transitions but cannot initialize the empty stub.
- **WORKING_ITEMS (workflow: domain-decomp):** For each category in the decomposition, `PREPARATION_ACTOR` uses deterministic scaffolding/status tools for filesystem operations:
  - `tools/scaffolding/scaffold_package.sh {EXECUTION_ROOT} {CAT_ID} {CatLabel}` — creates the category folder with all 9 lifecycle subfolders.
  - `tools/scaffolding/scaffold_deliverable.sh {cat_folder}/1_Working {KTY_ID} {KtyLabel}` — creates each Knowledge Type folder with four non-dependency metadata stubs. The DEL-native needs method does not assess KTY declarations or add KTY dependency files; preserve existing artifacts.
  - A newly created `_STATUS.md` stub is written to `OPEN` in the exact form given by the `preparation` skill's scaffold contract, naming the actual actor; `write_status.sh` handles later transitions but cannot initialize the empty stub.
  - If the domain pipeline requires structural prereqs for hypergraph/closure work, `PREPARATION_ACTOR` also uses `tools/scaffolding/scaffold_tool_root.sh` to initialize the required domain-level tool roots.
- Scaffolding order and ownership:
  - `scaffold_deliverable.sh` creates four empty metadata stubs (`_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_SEMANTIC.md`) and, for DEL only, schema-valid `deliverable.yaml` in one call. Inventory targets first, capture each `CREATED_PATH`, and populate only files created by that invocation; an existing empty file is existing work.
  - `write_status.sh` cannot initialize an empty `_STATUS.md`; the `preparation` skill writes the exact `OPEN` form into the newly created stub, and `write_status.sh` is used only for later transitions.
  - When file ownership is split (for example, a local needs declaration belongs to another owner or stage), the actor may instead use inventoried exclusive creation of exactly its accepted targets: record target existence before writing, create each target only if absent, and report created paths and hashes. Do not create placeholder files outside the actor's ownership.
  - Folder labels follow the project's recorded label rule where one exists; the `preparation` skill's sanitization rule is the default for new workspaces.
- `PREPARATION_ACTOR` uses the language model only to populate metadata text from the decomposition and any human-confirmed declarations:
  - `_CONTEXT.md`
  - `_REFERENCES.md`
- `PREPARATION_ACTOR` validates each newly created DEL with `tools/validation/check_min_viable_fileset.sh {folder} {accepted_DEL_ID}`. The YAML ID must agree with the numeric accepted identity and folder; preserve accepted suffix bindings and numbering. An initial empty needs list means none declared yet, with no completeness/readiness claim. For KTY, omit the accepted DEL argument; only non-dependency metadata are assessed.

**Gate question:** “Scaffolding complete. [N] packages/categories and [M] deliverables/knowledge types created. Minimum viable fileset validation passed for all newly created folders. Any missing references flagged. Ready to run document drafting?”

---

#### Phase 2.1b: Retrieval-driven preflight (WORKING_ITEMS (workflow: domain-decomp) only; when a retrieval index is present)

**Precondition:** A V2 source database snapshot exists at
`{RETRIEVAL_INDEX_PATH}` (normally `<domain-root>/_LocalIndexes/_LATEST.md`)
and its retrieval sidecars are current with respect to source/audit/decomposition
state. If the precondition is not met (no index, or stale index), skip Phase
2.1b and proceed to Phase 2.2 with a note that Pass 4 audit-on-write will be
skipped.

**Action:**
1. **Coverage inventory.** Run `python3 tools/diagnostics/ka_coverage_audit.py --all` to enumerate per-KTY MISSING / LEAN_BUT_SUBSTANTIVE / WELL_COVERED status. Inventory is informational — it surfaces authoring priority order, not a target. Limitation: the tool currently hard-codes `domains/piping-design/` ledger and KA paths; for another domain root, report the inventory as unavailable rather than relying on its output.
2. **KTY-scope ratification — uniform pass across all KTYs.** Every KTY in `Knowledge_Type_Register.csv` is ratified, regardless of historical lifecycle status. Decomposition acceptance is decomposition acceptance; under the new retrieval-driven preflight, baseline KTYs and recently-admitted KTYs both undergo the same scope-vs-content alignment check. For each KTY, dispatch TASK with:
   - `Workflow: domain-documents`
   - `ScopePath: {KTY_PATH}`
   - `DECOMP_VARIANT: DOMAIN`
   - `RUN_SCOPE_RATIFICATION: true`
   - `RETRIEVAL_INDEX_PATH: {resolved index path}`
   - The workflow runs only the ratification subroutine (see `workflows/domain-documents/resources/checks.md`), returns a verdict (`CLUSTER_COHERENT` / `SCOPE_REFINEMENT_NEEDED` / `SCOPE_TOO_NARROW` / `SCOPE_TOO_BROAD`), and exits without drafting any KA files.
3. **Aggregate verdicts.** WORKING_ITEMS compiles a per-KTY verdict report.
4. **Halt at any non-COHERENT verdict.** Surface the verdict, the dominant retrieved atoms, and the divergence rationale to the human. Do not proceed to Phase 2.2 for any KTY whose scope ratification is not `CLUSTER_COHERENT`. Scope refinements are SCA-class operations and are out of scope for the authoring run; record them and route them to a future scope-change cycle.

**Gate question:** “Scope ratification complete. [N] KTYs verdicted `CLUSTER_COHERENT`; [M] verdicted non-COHERENT (listed below). Proceed to Phase 2.2 dispatch for the [N] coherent KTYs only?”

**Note:** Phase 2.1b is skipped for WORKING_ITEMS (workflow: project-decomp) / WORKING_ITEMS (workflow: software-decomp) variants. They have no atomic-ledger retrieval index by design.

---

#### Phase 2.2: Dispatch document drafting (Pass 1 + Pass 2)

**Action (variant-routed):**
- **WORKING_ITEMS (workflow: project-decomp) / WORKING_ITEMS (workflow: software-decomp):** After human confirmation, dispatch TASK for each new deliverable with:
  - `Workflow: scope-of-work`
  - `ScopePath: {DELIVERABLE_PATH}`
  - `MODE: INIT`
  - `DECOMP_VARIANT: {variant}`
  - `STATUS_POLICY: NO_STATUS_TOUCH` and the exact `ScopeOfWork.md` write target, plus the other required fields in `workflows/scope-of-work/resources/brief.md`. `scope-of-work` accepts only `MODE=INIT|CONVERT|REVISE|VERIFY` (`REVISE` only under an accepted scope-change amendment, Phase 5.5) and never edits `_STATUS.md`; recording `INITIALIZED` is a separate authorized status act.
  - Existing `LEGACY_FOUR_DOC` maintenance may use `four-documents` only when
    the resolver confirms a complete legacy-only contract; never infer mode
    from a filename or create a new legacy kit.
  - Conversion is a separate `MODE=CONVERT` isolated workflow with exact
    authority, lossless mapping, status preservation, and atomic integration.
- **WORKING_ITEMS (workflow: domain-decomp):** After human confirmation, dispatch TASK for each Knowledge Type with:
  - `Workflow: domain-documents`
  - `ScopePath: {KTY_PATH}`
  - `RUN_PASSES: FULL`
  - `DECOMP_VARIANT: DOMAIN`
  - `RETRIEVAL_INDEX_PATH: {resolved index path}` (when a retrieval index is present and current — see Phase 2.1b; omit when absent)
  - `RETRIEVAL_COSINE_THRESHOLD: 0.75` (default; tune per domain after the first authoring batch)
  - **Precondition:** Phase 2.1b scope ratification returned `CLUSTER_COHERENT` for this KTY.
  - The workflow executes Pass 1 (draft `Scoping.md` + variable `KA-*.md` Knowledge Artifacts derived one-per-Subject), Pass 2 (cross-artifact consistency), Pass 3 (source-fidelity verification against the authoritative source document), and Pass 4 (audit-on-write retrieval check, when `RETRIEVAL_INDEX_PATH` is set).
  - The `domain-documents` workflow does not use the semantic lensing pipeline; Phases 2.3, 2.4, and 2.5 are skipped for DOMAIN variants.
  - **Halt cadence:** halt-per-KTY by default (review the KTY's full KA set before the next dispatch). Relax to per-batch only after the first 2–3 KTYs prove the protocol clean end-to-end.

See `workflows/scope-of-work/WORKFLOW.md`, the retained compatibility
`workflows/four-documents/WORKFLOW.md`, and `workflows/domain-documents/WORKFLOW.md`.

**Gate question:** “Pass 1+2 complete. Ready for local need authoring (Phase 2.2b, PROJECT/SOFTWARE only) or semantic lenses (if using semantic lensing)?”

---

#### Phase 2.2a: Optional DOMAIN source-fidelity enrichment rerun

Run this phase only when the human requests a DOMAIN KTY enrichment or verification rerun after Phase 2.2 has already produced `Scoping.md` and `KA-*.md`.

**Action:**
- Dispatch `TASK + domain-documents` for selected KTY folders with:
  - `Workflow: domain-documents`
  - `ScopePath: {KTY_PATH}`
  - `RUN_PASSES: P3_ONLY`
  - `DECOMP_VARIANT: DOMAIN`
- Before dispatch, check `{EXECUTION_ROOT}/_ScopeChange/_LATEST.md`.
- If active SCA state exists, resolve the active SCA snapshot from `_LATEST.md` and include these runtime overrides in every enrichment brief:
  - `AUTHORITY_MODE: SCA_DRIVEN`
  - `SCA_SNAPSHOT_PATH: {ACTIVE_SCA_SNAPSHOT_PATH}`
  - `SUPERSESSION_MAP_PATH: {ACTIVE_SCA_SNAPSHOT_PATH}/Supersession_Map.csv`
- Enrichment without supersession awareness on a post-SCA root is a design defect because it can restore superseded source-authority values into current KTY content.
- If active SCA state exists but the cumulative `Supersession_Map.csv` is missing, halt and report the missing governance input. Do not run `SOURCE_FIDELITY` enrichment on a post-SCA root unless the human explicitly confirms there is no accepted supersession state to preserve.
- If no active SCA state exists, use `AUTHORITY_MODE: SOURCE_FIDELITY`.
- If this rerun occurs after a DOMAIN hypergraph snapshot exists, report that snapshot as stale and rerun Phase 2.6 before downstream publication, audit, or aggregation consumes it.

---

#### Phase 2.2b: Author local needs and query their structure (PROJECT/SOFTWARE)

**Action:**
1. Once Phase 2.2 has supplied the actual production scope, use
   **TASK + `dependency-extract`** for each selected DEL, one consumer per brief.
   Resolve its accepted identity, `ScopeOfWork.md`, the adopted work locality, source
   conditions, existing `deliverable.yaml` and the workflow's bounded write
   contract. Author the actual input/use conditions, preserving unchanged
   declarations, case multiplicity, uncertainty and technical holds. A later
   scan's failure to rediscover wording is no reason to retire a need.
2. Use **`audit-dep-closure`** for a bounded read-only query over the selected
   declarations and inventory. Inspect malformed needs, unknown bindings,
   selected coverage and reciprocal relationships. Where available, run
   `python3 -m tools.deliverables --project <PROJECT_ROOT> check`, then
   `neighborhood <DEL>` or `impact <DEL>` for an actual coordination question.
   The CLI requires an existing Git repository/HEAD and the shared tools on
   its import path; if unavailable, inspect declarations and the schema
   directly and report query coverage/limits. Do not require Git for setup.
3. Assess reciprocal conditions for the selected activity with
   `construct-local-work-graph` as needed. Preserve each need's actual
   `gating` meaning and technical release condition; cycles do not automatically
   change those values or create an approval/case route. Continue unaffected
   work whose inputs permit it.
4. Return the authored changes, query findings and actual remaining conditions.
   A structural pass, supplier declaration or file presence is not suitability,
   acceptance or project-wide dependency completeness. Do not maintain a
   second central dependency map or copy reverse links into local needs.

This DEL-native phase does not assess KTY dependency declarations. Report that
limit for a DOMAIN undertaking; do not fabricate KTY schema or invoke a removed
CSV/central-network dependency route.

---

#### Phase 2.3: Dispatch semantic matrix generation

**Action:**
- **WORKING_ITEMS (workflow: domain-decomp):** Skip this phase. DOMAIN variants do not use the semantic lensing pipeline; source-fidelity verification is handled by the `domain-documents` workflow's Pass 3 (run in Phase 2.2 with `RUN_PASSES: FULL`). Do not dispatch `semantic-matrix-build` for DOMAIN unless the human explicitly overrides the DOMAIN pipeline routing.
- **WORKING_ITEMS (workflow: project-decomp) / WORKING_ITEMS (workflow: software-decomp):** If the project uses semantic lensing, dispatch **TASK + `semantic-matrix-build`** for each deliverable. Do not create or use a dedicated semantic-matrix persona agent for normal execution.
- Run this phase as a sealed TASK step: one deliverable, one workflow, one brief-defined write authorization. The WORKING_ITEMS (workflow: project-setup)/parent must not author `_SEMANTIC.md` inline and must not repair or rewrite matrix cells after TASK returns. If a semantic product needs review, dispatch a separate bounded review task after the semantic run has completed.
- WORKING_ITEMS must write or resolve a complete TASK brief. The brief must include the TASK run/context anchor and the workflow's semantic fields so that `ScopePath`, `deliverable_folder`, and `decomposition_path` are unambiguous.

**Canonical Phase 2.3 TASK brief template:**

```markdown
PURPOSE: Generate the deliverable-local semantic lens for one production unit.
RequestedBy: WORKING_ITEMS

ScopePath: {DELIVERABLE_PATH}
Workflow: semantic-matrix-build

Tasks:
  - Load `workflows/semantic-matrix-build/WORKFLOW.md` and resources required for the current stage.
  - Read the deliverable-local truth set before deriving matrices.
  - Generate or overwrite `{DELIVERABLE_PATH}/_SEMANTIC.md` for this deliverable only.
  - Audit final matrix cells and return PASS/FAIL with failing cells if any.

ApplyEdits: true
AllowedWriteTargets:
  - {DELIVERABLE_PATH}/_SEMANTIC.md
  - {DELIVERABLE_PATH}/_STATUS.md
  - {DELIVERABLE_PATH}/_run_records/

RuntimeOverrides:
  DECOMP_VARIANT: {PROJECT|SOFTWARE}
  deliverable_folder: {DELIVERABLE_PATH}
  DELIVERABLE_PATH: {DELIVERABLE_PATH}
  decomposition_path: {DECOMPOSITION_PATH}
  PHASE: PROJECT_SETUP_PHASE_2_3
  PRODUCTION_FORMAT: {SOW_V1|LEGACY_FOUR_DOC}   # resolver-selected
  STATUS_POLICY: PRESERVE_CURRENT

CustomInstructions:
  - Treat `_SEMANTIC.md` as a semantic lens scaffold, not an engineering authority.
  - Keep production documents read-only.
  - Use deliverable-conditioned semantic categories; do not restate implementation particulars as matrix cell values.
  - Preserve the current `_STATUS.md` lifecycle state during Phase 2.3. On audit PASS, append history noting semantic matrix generation/validation and that readiness advancement is reserved for a later authorized status act. On audit FAIL, append failure history only and do not advance state.
  - If the active workflow's default status-advancement rule conflicts with this Phase 2.3 status policy, follow this explicit WORKING_ITEMS brief policy and record the override in the run report and `_SEMANTIC.md` phase note.

ExpectedOutputs:
  - `{DELIVERABLE_PATH}/_SEMANTIC.md`
  - `{DELIVERABLE_PATH}/_run_records/TASK_RUN_*.md`
```

**Status policy:**
- Default PROJECT/SOFTWARE setup pipeline policy: Phase 2.3 uses `STATUS_POLICY: PRESERVE_CURRENT`. `_SEMANTIC.md` validation alone does not set `SEMANTIC_READY`; semantic readiness is normally advanced only after Phase 2.4 (`lens-register`) and Phase 2.5 enrichment where an enrichment method exists for the production format (see Phase 2.5).
- If a project explicitly chooses semantic-matrix validation as the readiness gate, the TASK brief must say so directly by setting `STATUS_POLICY: ADVANCE_ON_PASS`, authorizing the exact `_STATUS.md` change, and listing `_STATUS.md` as an allowed write target. Use `NO_STATUS_TOUCH` when the brief must not edit `_STATUS.md` at all (required for authorized `MIGRATION_DUAL`). Do not silently rely on the workflow default when project policy is ambiguous.

**Required post-run review:**
- Confirm TASK returned a run report with `Workflow: semantic-matrix-build`, resolved workflow version, companion-file status, tool policy compliance, outputs, missing inputs, and dependency notes.
- Confirm `_SEMANTIC.md` exists and contains the Phase Note when state advancement was intentionally suppressed.
- Do not treat `_SEMANTIC.md` as an engineering authority; it is a lens scaffold.
- Before Phase 2.4, validate each deliverable with:
  - `python3 tools/validation/validate_semantic_matrix.py "{DELIVERABLE_PATH}"`
  - `python3 tools/validation/validate_semantic_pipeline_scope.py "{DELIVERABLE_PATH}" --step semantic` when the worktree contains only that semantic TASK's changes, or the equivalent parent review of touched files when multiple workers have fanned in.

See `workflows/semantic-matrix-build/WORKFLOW.md` for the method contract.

**Gate question:** “Semantic matrices generated and Phase 2.3 status policy verified. Ready to run semantic lensing registers?”

---

#### Phase 2.4: Dispatch semantic lensing register generation

**Action:**
- **WORKING_ITEMS (workflow: domain-decomp):** Skip this phase. DOMAIN variants do not use the semantic lensing pipeline.
- Dispatch TASK for each deliverable with:
  - `Workflow: lens-register`
  - `ScopePath: {DELIVERABLE_PATH}`
  - `DECOMP_VARIANT: {variant}`
  - The workflow generates `_SEMANTIC_LENSING.md` for the deliverable.
- The `lens-register` workflow does not edit production documents; it produces a read-only enrichment register.
- Run this phase as a sealed TASK step after `_SEMANTIC.md` validates. The WORKING_ITEMS (workflow: project-setup)/parent must not author `_SEMANTIC_LENSING.md` inline.
- Before Phase 2.5, validate each deliverable with:
  - `python3 tools/validation/validate_lens_register.py "{DELIVERABLE_PATH}"`
  - `python3 tools/validation/validate_semantic_pipeline_scope.py "{DELIVERABLE_PATH}" --step lens` when the worktree contains only that lens TASK's changes, or the equivalent parent review of touched files when multiple workers have fanned in.

See `workflows/lens-register/WORKFLOW.md` for the method contract.

**Gate question:** “Semantic lensing complete. Ready to run Pass 3 enrichment (apply the register)?”

---

#### Phase 2.5: Dispatch document enrichment (Pass 3 only — apply semantic lensing)

**Action (variant-routed):**
- **WORKING_ITEMS (workflow: project-decomp) / WORKING_ITEMS (workflow: software-decomp), existing complete `LEGACY_FOUR_DOC`:** Dispatch TASK for each deliverable with:
  - `Workflow: four-documents`
  - `ScopePath: {DELIVERABLE_PATH}`
  - `RUN_PASSES: P3_ONLY`
  - `DECOMP_VARIANT: {variant}`
  - The workflow applies warranted enrichments and performs a final consistency sweep.
  - If the project uses `SEMANTIC_READY` as a lifecycle marker, its Pass 3 may set `_STATUS.md` from `INITIALIZED → SEMANTIC_READY` (only if that is the local policy and the brief authorizes the `_STATUS.md` write).
- **`SOW_V1`:** applying `_SEMANTIC_LENSING.md` to `ScopeOfWork.md` is not currently provided by a bundled workflow. `scope-of-work` accepts only `MODE=INIT|CONVERT|REVISE|VERIFY`, has no Pass 3, and never touches `_STATUS.md`; its `REVISE` mode serves accepted scope-change amendments only, not lensing proposals; `semantic-lensing` can produce reviewable `PROPOSAL:` blocks but does not edit the contract. Report the step as not provided, route any accepted proposal through the project's authorized contract-amendment path, and record `SEMANTIC_READY` only through a separately authorized status act.
- Run the legacy enrichment as a sealed TASK step after `_SEMANTIC_LENSING.md` validates. The WORKING_ITEMS (workflow: project-setup)/parent must not apply Pass 3 document edits inline.
- Before reporting Phase 2.5 complete, validate each deliverable with:
  - `python3 tools/validation/validate_p3_disposition.py "{DELIVERABLE_PATH}"`
  - `python3 tools/validation/validate_semantic_pipeline_scope.py "{DELIVERABLE_PATH}" --step p3` when the worktree contains only that P3 TASK's changes, or the equivalent parent review of touched files when multiple workers have fanned in.
- **WORKING_ITEMS (workflow: domain-decomp):** Skip this phase. DOMAIN variants run Pass 3 (source-fidelity verification) as part of the `RUN_PASSES=FULL` directive in Phase 2.2. There is no separate Pass 3 enrichment phase for DOMAIN.

See retained compatibility `workflows/four-documents/WORKFLOW.md`,
`workflows/scope-of-work/WORKFLOW.md`, and `workflows/semantic-lensing/WORKFLOW.md`
for the method contracts.

**Report to human (PROJECT/SOFTWARE):** “Enrichment pass complete for legacy kits; `SOW_V1` lensing application not provided (listed). Production units are ready for WORKING_ITEMS sessions.”
**Report to human (DOMAIN):** Phase 2.5 skipped for DOMAIN variant — source-fidelity verification was completed in Phase 2.2. Production units are ready for TASK (workflow: domain-hypergraph) (Phase 2.6).

---

#### Phase 2.6: Spawn TASK (workflow: domain-hypergraph) sub-agent (DOMAIN variant only)

**Precondition:** Phase 2.2 is complete (the `domain-documents` workflow executed Passes 1, 2, and 3 via `RUN_PASSES: FULL`, completing source-fidelity verification).

**Action (WORKING_ITEMS (workflow: domain-decomp) only):**
- Spawn **TASK (workflow: domain-hypergraph)** to build the normalized hypergraph from the workspace folders (pass `EXECUTION_ROOT`, `SCOPE=ALL`, `DECOMPOSITION_PATH`).
- TASK (workflow: domain-hypergraph) reads the final state of Category/Knowledge Type folders — after the actual eligible actor using the selected `preparation` skill scaffolded them and the `domain-documents` workflow drafted, cross-validated, and source-verified them (Passes 1, 2, and 3 via `RUN_PASSES: FULL`).
- Output: immutable snapshot under `{EXECUTION_ROOT}/_Aggregation/Hypergraph/` containing `nodes.csv`, `hyperedges.csv`, `incidence.csv`, `hypergraph.json`, and QA evidence.
- TASK (workflow: domain-hypergraph) is read-only on all Category/Knowledge Type folders.

**Gate:** Human confirms hypergraph snapshot is acceptable (or skips if hypergraph is not needed for this project).

**Report to human:** “DOMAIN hypergraph built. Initialization pipelines complete. Production units are ready for WORKING_ITEMS sessions.”

**Note:** For WORKING_ITEMS (workflow: project-decomp) and WORKING_ITEMS (workflow: software-decomp) variants, Phase 2.6 is skipped — these variants do not use the DOMAIN hypergraph.

---

#### Phase 2.7: Record the setup baseline (all variants)

**Action:** When the human confirms the last applicable Function 2 gate, create `{COORDINATION_ROOT}/SETUP_LOG.md` from the [contract template](contract.md#setup_logmd-project-level-agent-owned-append-only) if absent and append its one `BASELINE` line, in the log's line format: `- [YYYY-MM-DD] — BASELINE: incremental setup adopted; amendments accepted up to [YYYY-MM-DD] (latest none) are already set up and are not reprocessed; confirmed by [human]`, with both dates the completion date and the human who confirmed that gate. Where the decomposition set up here already included accepted amendments, name the latest of them instead of `none`. A project set up this way never needs the Phase 5.0 adoption step. Skip this phase when `SETUP_LOG.md` already has a `BASELINE` line.

---

### Function 3: Scan & report (on demand)

**Goal:** Report filesystem-grounded status for human decision-making.

#### Phase 3.1: Scan

**Action:**
- Run `tools/query/count_workspace_state.sh {EXECUTION_ROOT}` for the project-wide summary (packages, deliverables, lifecycle state distribution, tool root presence).
- Read `_STATUS.md` in every deliverable folder under `{EXECUTION_ROOT}/` for per-deliverable detail.
- Check `2_Checking/` zones for items awaiting review.
- Check `3_Issued/` zones for issued items.

Dependencies:
- Read the selected DELs' `deliverable.yaml` and derive neighbourhood/impact
  views for the actual question using Phase 2.2b's tools or direct inspection
  fallback. State query scope, malformed declarations, source unknowns and
  reciprocal conditions.
- Assess whether each actual input meets the selected use from evidence and
  responsible judgment. Keep an unassessed condition unknown; lifecycle state,
  file presence and structural validity do not establish satisfaction.
- Preserve all case/trigger distinctions and technical holds. No automatic
  blocker computation from lifecycle thresholds, endpoint deduplication or
  blanket non-gating treatment follows from the query.

---

#### Phase 3.2: Report

Always report by lifecycle state:
- OPEN
- INITIALIZED
- SEMANTIC_READY
- IN_PROGRESS
- CHECKING
- ISSUED

For the selected undertaking, report the actual input conditions assessed,
the evidence and judgment supporting their use, unresolved sources, technical
holds and work that can proceed independently. Name any needed owner decision
and its effect. Query results are a partial observed view; they do not establish
a complete or accepted network, lifecycle advancement or readiness.

WORKING_ITEMS does not assign or recommend priorities.

---

### Function 4: Estimating Pipeline (human-gated, multi-tier)

**Goal:** Read the estimation strategy documents (INIT → BOE → INDEX), resolve all `estimate-snapshot` brief inputs per deliverable, and execute tier-sequenced `estimate-snapshot` runs via bounded TASK+workflow dispatches.

WORKING_ITEMS does not produce estimates or interpret pricing data. It reads the BOE and INDEX.md as structured documents, resolves paths and parameters for `estimate-snapshot`, and enforces the tier sequence defined in the BOE. Domain judgment stays in the BOE (human-authored).

#### Phase 4.0: Load estimation strategy

**Action:**
- Read `{EXECUTION_ROOT}/INIT.md`.
- Follow the `Basis of Estimate` path → read the BOE document.
- Follow the `Price Sources` path → read `_PriceSources/INDEX.md`.
- Extract from the BOE:
  - **Section 3** (Estimation Strategy): common run parameters — CURRENCY, FALLBACK_POLICY, ALLOW_MIXED_METHODS, ROUNDING, and any project-wide defaults.
  - **Section 4** (Per-Deliverable Estimation Plan): per-deliverable `BASIS_OF_ESTIMATE` substance classification, method, exclusions, and parameter overrides.
  - **Section 5** (Dependency-Informed Run Sequence): tier definitions and tier order. Tier sequencing comes from the BOE, not WORKING_ITEMS (workflow: project-setup).
  - **Section 6** (Missing PRICE_SOURCES Register): gaps that may block or degrade specific runs.
- Extract from `_PriceSources/INDEX.md`:
  - Per-package `PRICE_SOURCES` file mapping (which files exist and where they are).
  - Any gaps register entries in INDEX.md.
- Compile an estimation plan summary for the human:
  - Total deliverable count and tier count.
  - Deliverables per tier (with tier order).
  - Exclusions (deliverables excluded from estimation, with reason from BOE Section 4).
  - External gates or open issues that affect estimation (from BOE Section 2 / Section 6).
  - LOW-confidence or missing price sources (from BOE Section 6 + INDEX.md gaps).

**Gate question:** "Estimation plan loaded: [N] deliverables across [T] tiers. [X] exclusions. [Y] gaps flagged. Ready to begin Tier [first tier label]?"

---

#### Phase 4.1: Execute tier (repeats per tier, in tier order)

**Action:**
- For each deliverable in the current tier, resolve `estimate-snapshot` brief inputs:
  - **Required:** `RUN_ROOT` (deliverable folder path), `ESTIMATES_ROOT` (`{EXECUTION_ROOT}/_Estimates/`), `SCOPE` (deliverable ID), `BASIS_OF_ESTIMATE` (from BOE Section 4 per-deliverable entry), `CURRENCY` (from BOE Section 3).
  - **Recommended:** `DECOMPOSITION_PATH` (from INIT.md decomposition path), `DEPENDENCY_SOURCES` (consumer-local `deliverable.yaml`, or a bounded view derived from those needs for the estimate), `PRICE_SOURCES` (resolved from INDEX.md per-package mapping → absolute file paths within `_PriceSources/`).
  - **Optional:** `FALLBACK_POLICY`, `ALLOW_MIXED_METHODS`, `ROUNDING`, `OUTPUT_LABEL`, `UPDATE_LATEST_POINTER`, `EXCLUSIONS` — sourced from BOE per-deliverable table (Section 4) with fallback to common run parameters (Section 3).
- Spawn one TASK+`Workflow: estimate-snapshot` per deliverable in the tier. Dispatches run in parallel within a tier, unless the BOE specifies sequential constraints within that tier.
- Collect per-deliverable results: snapshot folder path, `RUN_STATUS`, key warnings.
- Report tier results to human: deliverables run, statuses, warnings.

**Gate question:** "Tier [label] complete: [N] runs. [summary of statuses]. Ready to proceed to Tier [next tier label]?"

Repeat Phase 4.1 for each subsequent tier until all tiers are complete.

---

#### Phase 4.2: Post-estimation summary

**Action:**
- Report across all tiers:
  - Total runs by `RUN_STATUS` (COMPLETE, PARTIAL, FAILED, SKIPPED).
  - Coverage: deliverables estimated vs. total deliverables in decomposition.
  - Aggregate warnings (e.g., missing provenance, LOW-confidence sources used, fallback methods applied).
  - Any deliverables that were excluded or skipped, with reasons.

**Gate question:** "Estimation complete: [N] of [M] deliverables estimated. [summary]. Ready to spawn TASK (workflow: aggregation)?"

---

#### Phase 4.3 (Optional): Spawn TASK (workflow: aggregation)

**Action:**
- If the human confirms, spawn TASK (workflow: aggregation) using the aggregation strategy defined in BOE Section 7.
- Pass the aggregation strategy parameters and the list of completed estimation snapshot paths.
- Report TASK (workflow: aggregation) results to the human.

**Report to human:** "Aggregation complete. Results at [path]."

---

### Function 5: Incremental setup after an accepted amendment (`INCREMENTAL` mode)

**Goal:** Set up the amended scope of an accepted `scope-change` amendment: scaffold what was added, record what was retired, route what was modified to its production contract, and refresh dependency and coordination records only where the amendment reaches. The inputs and action treatment are in [the contract](contract.md#setup-modes).

**Precondition:** The amendment has passed `scope-change` checkpoint group 3 and its snapshot is accepted (normally the `_LATEST.md` target). An amendment still in progress is finished through `scope-change` first; a candidate or returned snapshot is not an input. This function does not edit decomposition truth or the immutable amendment snapshot. A discrepancy between the accepted poststate and the workspace returns to `scope-change`.

Apply the paired read throughout: whenever this function reads a deliverable `_STATUS.md`, it also reads a sibling `MEMORY.md` or `_MEMORY.md` when present, as non-authoritative context only.

Setup evidence goes to the agent-owned, append-only `{COORDINATION_ROOT}/SETUP_LOG.md` ([contract](contract.md#setup_logmd-project-level-agent-owned-append-only)). This function reads `_COORDINATION.md` but does not write it.

#### Phase 5.0: Adopt incremental setup (once per project)

Run this phase when `SETUP_LOG.md` has no `BASELINE` line: a project set up before incremental setup existed. A project whose `INITIAL` setup completed Phase 2.7 already has its baseline.

**Action:**
- List the accepted amendments under `{EXECUTION_ROOT}/_ScopeChange/` in amendment order with their acceptance dates, and for each whether its `Handoff_State.md` hands setup to `project-setup` in `INCREMENTAL` mode.
- Propose one baseline. By default it names the latest accepted amendment whose `Handoff_State.md` does not hand setup to `project-setup` `INCREMENTAL` (one accepted before incremental setup existed), with its acceptance date, or `none` when there is no such amendment. The human confirms it or names another.
- The baseline covers the amendment it names and the accepted amendments before it. An amendment whose `Handoff_State.md` hands setup to `project-setup` `INCREMENTAL` is never covered, whatever its date or position: it enters the Phase 5.1 queue. This keeps the amendment that prompted adoption from being treated as already set up.
- Covered amendments are never reprocessed by this mode, whatever their handoff records say; setup work a human still wants for one of them is a separate authorized undertaking.

**Gate question:** "Adopt incremental setup with baseline [ID or none] (accepted [date]): [n] earlier accepted amendments treated as already set up and not reprocessed; [k] amendments that hand setup to `INCREMENTAL` ([IDs]) stay in the queue. Confirm?"

**On confirmation:** create `SETUP_LOG.md` from the contract template if absent and append the one `BASELINE` line, naming the confirmed amendment (or `none`) and, after "accepted up to", its acceptance date (the adoption date when `none`). Do not edit `_COORDINATION.md`, accepted snapshots or earlier run records.

---

#### Phase 5.1: Resolve the accepted amendment and confirm the incremental plan

**Action:**
- Resolve the accepted snapshot from `{EXECUTION_ROOT}/_ScopeChange/_LATEST.md`. List any earlier accepted `SCA-*` snapshots not covered by the `SETUP_LOG.md` baseline whose setup hand-back has no `COMPLETE` line there, and take them in amendment order in the same plan. Where later amendments act on the same entity, the latest accepted state governs; show such cases in the plan. An amendment covered by the baseline never enters the plan.
- Resolve the accepted action register through the snapshot's group-2 `ACCEPTED_MANIFEST.csv` (`Amendment_Actions.csv` or its bound distinct name) and verify its hash. Read `Propagation_Plan.md` and `Handoff_State.md` for the hand-back, deferred items and blockers.
- Read each affected entity's row in the amended decomposition, and the coordination arrangements and technical holds in `_COORDINATION.md`. Do not re-run Phases 1.2–1.3.
- For each affected deliverable, resolve its production format (`docs/COMPATIBILITY_FORMATS.md#historical-specification` §2.2) and lifecycle state. Derive the neighbours (contract, *`INCREMENTAL` action treatment*).
- Prepare the incremental plan: each entity with its action, treatment, stages, write targets and actor; the local need review/query scope (Phase 5.6); semantic or DOMAIN stages the project uses; derivatives made stale (estimates, schedules, hypergraph, semantic artifacts) with their owners; and any decisions the stages reserve for the human.

**Gate question:** "Accepted amendment [ID] (register hash [H]): [a] to scaffold, [r] retired, [m] modified ([h] held at `CHECKING` or `ISSUED`), [n] neighbours for local need review. Confirm this incremental plan?"

**Do not write before the human confirms the plan.**

---

#### Phase 5.2: Scaffold added entities

**Action:**
- For each `ADD` (and each new `MERGE`/`SPLIT` successor), apply Phase 2.1 with the source-qualified `preparation` skill: `scaffold_package.sh` for a new package or category, `scaffold_deliverable.sh` for a new deliverable or knowledge type. Inventory first and populate only files created by this invocation. A path that already exists for an added ID is existing work: report it and do not overwrite it.
- A new DEL receives `deliverable.yaml` with the accepted numeric ID and `needs: []`; author actual conditions after its scope exists. An empty list is no completeness or readiness claim. Preserve existing files; no dependency format migration is implied.
- Initialize `OPEN` only in a newly created `_STATUS.md`, and run `tools/validation/check_min_viable_fileset.sh` on each new folder.
- **DOMAIN:** before drafting a new Knowledge Type, reuse the amendment's recorded `CLUSTER_COHERENT` ratification when the retrieval index has not changed since it; otherwise run Phase 2.1b for the new Knowledge Types only.

---

#### Phase 5.3: Initialize production for added entities

**Action:**
- **PROJECT/SOFTWARE:** dispatch Phase 2.2's `scope-of-work` brief (`MODE: INIT`, `STATUS_POLICY: NO_STATUS_TOUCH`) for each new deliverable, naming the amended decomposition and the accepted snapshot as its basis. Recording `INITIALIZED` remains a separate authorized status act.
- **DOMAIN:** dispatch Phase 2.2's `domain-documents` brief for each new Knowledge Type in its `SCA_DRIVEN` mode, with the supersession inputs of Phase 2.2a: `AUTHORITY_MODE: SCA_DRIVEN`, `SCA_SNAPSHOT_PATH` set to the accepted snapshot, and `SUPERSESSION_MAP_PATH` set to its cumulative `Supersession_Map.csv`. This dispatch carries out the accepted amendment's hand-off. A missing cumulative map halts the dispatch as in Phase 2.2a.
- Run Phases 2.3–2.5 for added deliverables only where the project already uses semantic lensing.

---

#### Phase 5.4: Record retirements

**Action:**
- For each `REMOVE` (and each retired `MERGE`/`SPLIT` source), delete nothing. Confirm the decomposition row carries `[RETIRED — {AMENDMENT_ID}]`. A missing annotation returns to `scope-change`: the annotation is decomposition truth, which this function does not edit.
- Confirm `_STATUS.md` holds one history line recording the retirement under the amendment. Where the accepted poststate lacks it, append exactly one, for example `- {YYYY-MM-DD} — Retired under {AMENDMENT_ID}; lifecycle state remains {CURRENT_STATE} ({ACTOR})`. Leave `**Current State:**` unchanged and do not use `write_status.sh`. This line is appended here rather than returned because `_STATUS.md` history is deliverable-local lifecycle evidence, not decomposition truth, and appending it changes no state.
- Identify retired deliverables and the accepted action for the bounded query. Ask their actual consumers to review affected needs: retirement does not by itself make an existing artifact unusable or justify deleting/retargeting a condition. Preserve usable historical evidence and technical holds.
- **DOMAIN:** KTY content retirement belongs to the amendment's `KTY_Remediation_Manifest.csv` lanes. Report rows that are not `COMPLETE`; do not archive content here.

---

#### Phase 5.5: Route modified deliverables to their update path

**Action:** Do not re-scaffold a modified deliverable or re-run `MODE=INIT` over an existing contract. Route each `MODIFY` or `RECLASSIFY` deliverable by production format and lifecycle state:

| State | Route |
|---|---|
| `OPEN`, no production contract | Nothing to update. The amended `_CONTEXT.md` is the basis for a later `MODE=INIT`. |
| `SOW_V1` at `INITIALIZED`, `SEMANTIC_READY` or `IN_PROGRESS` | If the accepted group-2 write boundary named `ScopeOfWork.md`, the amendment already changed it: dispatch `scope-of-work` `MODE=VERIFY`. Otherwise dispatch `scope-of-work` `MODE=REVISE` (`STATUS_POLICY: NO_STATUS_TOUCH`) with the amendment reference, the accepted action rows naming the deliverable, the register hash, the `REVISION_SCOPE` the amendment names and the prior contract hash; it ends with `MODE=VERIFY`. |
| `LEGACY_FOUR_DOC` | `four-documents` with `RUN_PASSES: P1_P2`, only when the resolver confirms a complete legacy-only kit. Conversion remains a separate `MODE=CONVERT` undertaking. |
| `CHECKING` | Frozen and held for the human. Report it; the update waits for a human reversal to `IN_PROGRESS` (`docs/COMPATIBILITY_FORMATS.md#historical-specification` §3.3), after which the `SOW_V1` route above applies. |
| `ISSUED` | Held for the human; do not edit. This amendment's accepted action register names the deliverable with `MODIFY` (or `RECLASSIFY` with `ScopeChanging` `YES`), so it is the record that authorizes reopening under `docs/COMPATIBILITY_FORMATS.md#historical-specification` §3.3. Present the reopening as a human decision: the human records `ISSUED → IN_PROGRESS` in `_STATUS.md`, citing the accepted amendment snapshot, with `tools/scaffolding/write_status.sh <DEL_PATH> IN_PROGRESS human --amendment {AMENDMENT_ID} --approval-sha <commit that holds the committed amendment records and is an ancestor of HEAD>`. The tool first runs `tools/validation/check_amendment_reopen.py` on the amendment records as committed at that SHA; uncommitted records do not count. Where it refuses a lawful reopening (a `RECLASSIFY` in a legacy register without `ScopeChanging`, a run without hash-bound decision snapshots, or a further reopening under an amendment already recorded in `_STATUS.md`), report the refusal; the human records the transition directly. After that, the `SOW_V1` route above applies. No agent writes it. |

- Report existing `_SEMANTIC.md` or `_SEMANTIC_LENSING.md` of a modified deliverable as stale; rerun them only where the project uses semantic lensing.
- **DOMAIN:** modified KTY content goes through the amendment's KTY remediation lanes (`REGENERATE_CONTENT`, `VERIFY_ONLY`). Report rows that are not `COMPLETE`.

---

#### Phase 5.6: Refresh dependency stages for the affected scope

Use Phase 2.2b's local authoring and read-only query methods for the affected
DELs and their derived neighbours:

- Derive the actual affected consumers from `deliverable.yaml` and the accepted
  impact assessment. A changed relation may reach a reciprocal path through
  unchanged deliverables; expand the read scope when that actual path matters.
- Use `dependency-extract` to review each affected consumer's actual scope,
  work material, sources and intended input/use conditions. Preserve unchanged needs,
  distinct case/trigger records and unknown sources. Do not create a producer
  commitment or retire a declaration solely because extraction missed wording.
- Use `audit-dep-closure` for a bounded query over the resulting declarations.
  Report changes, malformed declarations, unresolved references, query scope
  and reciprocal conditions. Do not maintain a second map or infer satisfaction
  from the query result.
- Review needs that target retired producers against the actual retained
  artifact/use condition. Modify or remove only the meaning affected by the
  accepted amendment; do not automatically delete or retarget the relation.
- Author a new DEL's needs once Phase 5.3 supplies its production scope. Report
  a wait if that input is absent. Existing scope/technical/acceptance holds
  remain in force. DOMAIN/KTY dependency declarations are outside this native
  DEL method; do not invent a schema or new dependency output for them.

---

#### Phase 5.7: Refresh coordination and report

**Action:**
- Run Phase 3.1 and report per Phase 3.2. List retired deliverables separately with their unchanged lifecycle state and identify the actual input conditions affected by their retirement.
- Write the run record under `{COORDINATION_ROOT}/AgentRuns/<RunID>/`: the confirmed plan, snapshot path and register hash, briefs, returns, created and skipped paths, update routes, dependency evidence and the report.
- Append one line to `SETUP_LOG.md`: `COMPLETE` when every planned item is done, otherwise `PARTIAL` or `BLOCKED` with the remaining items named in the run record.
- The accepted amendment snapshot stays immutable. The run record and setup-log line are this function's setup evidence, for the human and for resuming an interrupted run.
- **Closure check:** propose `audit-scope-closure` against the accepted amendment (normally after a `COMPLETE` line). It is the check that the added scope was scaffolded after acceptance. It audits the workspace itself against the amended basis: its ADD checks confirm each added folder and its minimum viable fileset, its REMOVE checks the retirement records, and its dependency checks inspect the accepted change and actual resulting local declarations and sources. A dependency refresh is evidenced by its meaningful result, not a mandatory extraction receipt. It takes dispositions from the amendment's `scope-change` handoff records; it does not read `SETUP_LOG.md` or this run record. Its findings route repair work back into this function.
- **DOMAIN:** report an existing hypergraph snapshot as stale and propose Phase 2.6.

**Report to human:** "Incremental setup for [ID]: [a] scaffolded ([paths]), [r] retirements recorded, [m] modified routed ([routes and outcomes]); [h] held for the human (`CHECKING`, `ISSUED` awaiting a recorded reopening); local need review/query [scope, changes and remaining conditions]; stale derivatives [list with owners]; decisions pending [list]; closure check `audit-scope-closure` [proposed | dispatched]."

An interrupted run resumes from Phase 5.1 by inspecting what exists: preparation and need authoring are per-item and idempotent, and completed items are skipped. A `PARTIAL` or `BLOCKED` line in `SETUP_LOG.md` keeps the amendment in the Function 5 queue.

---
