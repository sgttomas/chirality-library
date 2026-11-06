# Tool Registry

Deterministic tools for the Chirality agent operating system. These tools codify repeatable, LLM-independent operations that agents invoke during pipeline execution.

**Maintained by:** HELPS_HUMANS (Agent 1, `agents/AGENT_HELPS_HUMANS.md`), operating under `docs/WORKFLOW_COMPONENT_STANDARD.md`. HELPS_HUMANS designs workflows and tools: workflows carry reusable reasoning methods; tools remain deterministic.

---

## Scaffolding

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `scaffold_package.sh` | zsh + Python 3/PyYAML for current route | Create an accepted package directory | `--current EXECUTION_ROOT PKG_ID PkgLabel`; unflagged calls retain the legacy phase tree | Numeric PKG directory with no phase folders for current setup; existing contents preserved |
| `scaffold_deliverable.sh` | zsh + Python 3/PyYAML | Prepare a deliverable locality without authoring production scope | `--current PACKAGE_PATH DEL_ID DelLabel`; unflagged calls retain legacy metadata | Numeric DEL directory, Work/ and native deliverable.yaml for current setup; ScopeOfWork authoring follows separately |
| `scaffold_tool_root.sh` | zsh | Create tool root with _Archive/ and _LATEST.md stub | EXECUTION_ROOT, ROOT_NAME | Tool root folder |
| `create_snapshot_folder.sh` | zsh | Create a new timestamped immutable snapshot folder; never reuses an existing folder (appends `_NN` when the name exists, fails when no unique name is free) | TOOL_ROOT, PREFIX, LABEL | Folder path (stdout); exit 1 rather than reuse |
| `update_latest_pointer.sh` | zsh | Overwrite _LATEST.md to point to a snapshot | TOOL_ROOT, SNAPSHOT_NAME | Updated _LATEST.md |
| `write_status.sh` | zsh | Write or update _STATUS.md with lifecycle transition, now guarded: validates transition order and actor class (CHECKING/ISSUED are human-only; backward moves blocked except the human-ruled CHECKING→IN_PROGRESS reversal, which always requires `--ruling` (not overridable) and records `[reversal from CHECKING; ruling: …]` in history, and the human reopening ISSUED→IN_PROGRESS under an accepted scope-change amendment, which requires `--approval-sha` on every root (a reachable commit that is an ancestor of HEAD) and `--amendment` passing `check_amendment_reopen.py --at-commit <approval SHA>` (every amendment record read from that commit; one tool-recorded reopening per amendment, checked against `_STATUS.md`), none of it overridable, and records `[reopened from ISSUED; amendment: …; action: …; approval SHA: …]`), and for CHECKING/ISSUED and the reversal enforces adapter-declared per-root preconditions (flat `guard_*` keys grep-read from the nearest `_harness/adapter.yaml`) — committed ruling path via `--ruling`, git-verifiable approval SHA via `--approval-sha` where the root's schema declares one (absent schema → REVIEW to stderr, proceeds); human-recorded override via `--force-human-override "<reason>"` | DEL_PATH, STATE, ACTOR, `[--ruling <path>]`, `[--approval-sha <sha>]`, `[--amendment <id-or-path>]`, `[--force-human-override <reason>]` | Updated _STATUS.md with history (never edits on refusal); exit 0 success / 1 BLOCK / 2 usage-operational |

## Query

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `count_workspace_state.sh` | zsh | Count packages, deliverables, lifecycle states, tool roots | EXECUTION_ROOT | Summary table |
| `scan_next_amendment_id.sh` | zsh | Scan _ScopeChange/ for next available SCA-{NNN} or SCA-{PREFIX}-{NNN} ID | SCOPE_CHANGE_ROOT [PREFIX] | Next ID string (stdout) |

Deliverable dependency views: `python3 -m tools.deliverables --project <project>
{neighborhood ID|impact ID|touches DIFF|dag-diff TAG|check}`. Reads current
`deliverable.yaml` sources and returns revision-bound JSON facts and unknowns;
no generated register or completion state is written. See
[deliverable queries](deliverables/README.md).

## Software Workflow

Profile-driven deterministic support for WORKING_ITEMS software activations. `tools/software_workflow/software_workflow_common.py` loads and validates the profile; `tools/tools-test-routing.json` is a working example. The former profile contract document is preserved in the private `sgttomas/chirality` repository.

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `discover_repository.py` | Python 3 | Discover manifests and conventional test files without executing project code | root | JSON repository map |
| `select_affected_checks.py` | Python 3 | Map changed project-relative paths to registered checks | profile, paths | JSON check selection and reasons |
| `run_registered_checks.py` | Python 3 | Execute selected profile commands as argument arrays without a shell; optionally own one registered loopback service from automatic port allocation through readiness and guaranteed shutdown | profile, repeated `--check`, `--output` | Normalized JSON evidence; exit 0 PASS / 1 check failure; service setup is check exit 125 |
| `validate_change_scope.py` | Python 3 | Compare explicit or Git-derived changed paths with allowed write roots | repo, repeated `--allowed`, diff or explicit paths | JSON PASS/FAIL scope report |
| `compare_structured.py` | Python 3 | Compare JSON API, schema, or migration artifacts by flattened value path | before, after | JSON added/removed/changed report |
| `verify_generated_manifest.py` | Python 3 | Verify generated files against a path-to-SHA-256 manifest | root, manifest | JSON PASS/FAIL drift report |

## Validation

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `validate_enum.py` | Python 3 | Validate a value against 24 named enum sets; legacy read values (`TRACKING_MODE` `TRACKED` → `FULL_GRAPH`) are accepted and name their write form | enum_name, value | VALID/INVALID (exit code) |
| `validate_id_format.sh` | zsh | Validate ID against format pattern (PKG, DEL, DEP, SOW, OBJ, CAT, KTY, SUB) | ID_TYPE, ID_VALUE | VALID/INVALID (exit code) |
| `validate_decomposition_registers.py` | Python 3 | Read-only XRG consistency across Deliverables.csv, ScopeLedger.csv and ContextBudgetQA.csv; preserves scope/package/objective/context checks independently of dependency storage and locality layout | EXECUTION_ROOT, optional --families XRG, --registers-dir, --json, --strict, --max-per-code, --list-checks | Findings with row IDs; exit 0 clean / 1 findings / 2 operational |
| `check_min_viable_fileset.sh` | zsh + Python 3/PyYAML | Check the selected locality structure and identities | `--current [--prepared] DEL_PATH [ACCEPTED_DEL_ID]`; unflagged checks retain legacy metadata requirements | Current preparation requires Work/ and valid native YAML; authored structure also requires matching ScopeOfWork frontmatter. Substantive contract validation remains separate; no readiness/acceptance claim |
| `check_four_documents.sh` | zsh | Compatibility-only validation of an existing complete `LEGACY_FOUR_DOC`; not a new-initialization route | DELIVERABLE_PATH | PASS/FAIL (exit code) + missing list |
| `scan_deliverable_consistency.py` | Python 3 | Resolve the production format fail-closed and scan the selected contract for missing files, unresolved markers, identity mismatches, and unsourced numeric lines | deliverable_path, format-authority options, [--output-json], [--focus-doc], [--strictness], [--max-findings], [--check-identity], [--check-unsourced-numerics] | JSON report to stdout or file |
| `validate_skill_metadata.py` | Python 3 | Compatibility entrypoint: defaults to workflow metadata validation; explicit historical skill folders retain the old contract | [skills_root], [--json] | PASS/FAIL summary or JSON report |
| `validate_agent_instructions.py` | Python 3 | Validate four-section `AGENT_*.md` role prose, registry types, direct entry, delegation and capability configuration from `agents/registry.json` (absent registry → exit 2) | [agent paths], [--repo-root], [--json] | Findings + summary; exit 0 no errors / 1 errors / 2 operational failure |
| `discover_test_surfaces.py` | Python 3 | Read-only discovery of test surfaces by repository convention across root tools, Chirality app frontend tests, OpenPipeStress Python tests, OpenPipeStress desktop Vitest tests, and OpenPipeStress Rust test attributes | [repo_root], [--json], [--text] | JSON or text report with discovered paths, runner family, suggested command, and generated counts |
| `validate_path_anchors.py` | Python 3 | Validate live agent instruction and executable handoff surfaces for literal machine-local home-dir absolute paths while ignoring archives, run records, generated decomposition/source provenance, exports, and plans | [repo_root], [--json], [--text] | PASS/FAIL text or JSON report; exit 0/1 |
| `validate_candidate_whitespace.py` | Python 3 | Optional local diagnostic: preserve Git whitespace checks for tracked candidates and scan non-ignored, non-binary untracked text candidates for trailing whitespace and surplus terminal blank lines without mutation | `[--repo-root]`, `[--base-ref REF]`, `[--paths PATH ...]`, `[--no-untracked]` | Exact path/line findings; exit 0 clean / 1 findings / 2 operational error |
| `validate_conflict_markers.py` | Python 3 | Detect added unresolved Git conflict markers without blocking cosmetic whitespace | `--base REF`, `[--head REF]` | PASS or conflict diagnostics; exit 0 clean / 1 markers or Git error |
| `validate_kty_remediation_manifest.py` | Python 3 | Validate SCOPE_CHANGE `KTY_Remediation_Manifest.csv` rows for required schema, dispatch mapping, content-action assignment, evidence paths, closure states, factual-use gates, and optional `.Archive/` leakage in downstream input files. Accepts foreign-key `SourceActionRef` of the form `<AmendmentID>:<ActionSeq>` (e.g. `SCA-004:1`) in addition to bare `ActionSeq`/`D-NNN` forms; resolves manifest-relative `EvidencePaths`/`ArchivePath` against the snapshot folder first and falls back to the auto-detected DOMAIN package root (nearest ancestor with `_Sources/` or `_Decomposition/`) or an explicit `--workspace-root` override | `--manifest`, `[--amendment-actions]`, repeatable `[--downstream-input]`, `[--workspace-root]`, `[--output-findings]` | PASS/finding summary to stdout; optional findings CSV; exit 0/1/2 |
| `check_amendment_reopen.py` | Python 3 | Decide whether an accepted scope-change amendment authorizes reopening an ISSUED deliverable (SPEC §3.3, D-GOV-50/51): a group-3 decision snapshot (`{ID}_GROUP-3_[AMENDMENT-K_]YYYY-MM-DD[_N]`) whose first-line heading reads `… checkpoint group 3 — accepted`; the action register bound by SHA-256 in the governing (latest) group-2 `ACCEPTED_MANIFEST.csv` and unchanged; no `REMOVE` of the deliverable and a `DELIVERABLE` row with `MODIFY`, or `RECLASSIFY` with `ScopeChanging` `YES` (legacy registers without the column: `RECLASSIFY` refused); with `--status-file`, no reopening already recorded under the amendment. `--at-commit <sha>` reads every record from that commit (an ancestor of HEAD) via git; without it the working tree is read and the result is marked unanchored (inspection only). Reads only the `_ScopeChange/` of the deliverable's execution root; refuses path and symlink escapes. Importable `check_reopen(at_commit=…, status_file=…)`; run by `write_status.sh --amendment` in at-commit mode only | `--deliverable <DEL-ID or folder>`, `--amendment <ID or snapshot path>`, `[--at-commit <sha>]`, `[--status-file <_STATUS.md>]`, `[--scope-change-root]`, `[--project-root]`, `[--json]` | `ADMIT`/`REFUSE <CODE>: <reason>` or JSON decision (with `mode`, `anchored`, `at_commit`); exit 0 admitted / 1 refused / 2 usage-operational |
| `validate_domain_decomposition_integrity.py` | Python 3 | Validate DOMAIN decomposition annex referential integrity, lifecycle/cardinality constraints, coverage telemetry reconciliation, active snapshot artifact completeness, `_LATEST.md` parity, and KTY remediation rollup consistency. Optional `--package-subfolder NAME` flag for transitional dual-layout support; auto-descends into a single eligible subfolder when annexes not at root | `--decomposition-root`, `[--scope-change-snapshot]`, `--output-report`, `--output-findings`, `[--package-subfolder]` | DOMAIN integrity report markdown + findings CSV; exit 0/1/2 |

## Deliverable Scope of Work — Active transition

These tools implement the ratified `SOW_V1` contract and transitional
`LEGACY_FOUR_DOC` compatibility. They do not authorize conversion, lifecycle
change, ISSUED replacement, integration, or legacy retirement.

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `scope_of_work/validate_scope_of_work.py` | Python 3 | Resolve `LEGACY_FOUR_DOC`, `SOW_V1`, authorized `MIGRATION_DUAL`, or fail-closed invalid/ambiguous state; validate frontmatter, ordered sections, IDs, references, and matrix | `target`, format-authority options, `[--json]` | PASS/FAIL report; exit 0/1 |
| `scope_of_work/render_scope_of_work.py` | Python 3 | Render validated canonical Markdown into deterministic, source-hash-bound, script-free HTML for on-demand viewing | `source`, `[--output]` | HTML on stdout or at the explicit output path; exit 0/1 |
| `scope_of_work/convert_four_documents_to_scope_of_work.py` | Python 3 | Produce a lifecycle-neutral, lossless candidate from one legacy kit under exact isolated migration authority; ISSUED preparation requires bound source commit/source/status hashes and never satisfies H1; preserves `_STATUS.md` | `--deliverable`, identity/basis/objective fields, grounded output/acceptance/verification text, exact migration authority, optional ISSUED preparation bindings, `[--force]` | Isolated candidate `ScopeOfWork.md`; exit 0/1 |
| `scope_of_work/finalize_scope_of_work.py` | Python 3 | Deterministically externalize migration-only metadata and finalize an evidence-rich candidate into the clean production contract; preserve legacy source text as literal quotations | `--evidence-candidate`, `--output`, `--report` | Clean `ScopeOfWork.md` plus `chirality-sow-finalization/v1` JSON; exit 0/1 |
| `scope_of_work/map_scope_of_work_claims.py` | Python 3 | Emit source-range, source-hash, target-ID, final-target-hash, and migration-disposition mappings from embedded evidence markers; optionally require exact deterministic production finalization | `--scope-of-work`, `[--production-scope-of-work]`, `--source-dir`, `--output-csv` | Deterministic claim-map CSV; exit 0/1 |
| `scope_of_work/report_scope_of_work_parity.py` | Python 3 | Verify source hashes, exact mapped text, line coverage, target IDs, schema validity, and optional exact clean production finalization without changing authoritative inputs | `--scope-of-work`, `[--production-scope-of-work]`, `--source-dir`, `--output-json`, `[--output-md]` | Machine-readable parity JSON and optional Markdown summary; exit 0/1 |
| `scope_of_work/check_boundary_owner_resolution.py` | Python 3 | Deterministic half of the B8 boundary-owner rule: every owner ID excluded by a whole-requirement boundary exclusion is named by a claim that requirement cites; expands `X through Y` deliverable spans, ignores blockquoted source, reports per-act exclusion clauses as `NOT_CHECKABLE` (skill QA territory) and contracts without `REQ-NNN` as out-of-grammar | `target` (contract, deliverable, or tree), `[--json]`, `[--show-not-checkable]` | Findings on stdout, optional JSON report; exit 0/1, 2 operational |
| `scope_of_work/derive_review_checklist.py` | Python 3 | Deterministically compile validated `SOW_V1` `AC-*` definitions in source order without paraphrase, with exact source/matrix binding; fail closed for invalid, legacy-only, or unauthorized dual input | `target`, format-authority options, `[--output]` | Byte-stable `chirality-review-checklist/v1` JSON; source read-only and output-idempotent; exit 0/1 |

## Reporting

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `merge_detail_csvs.py` | Python 3 | Merge multiple Detail.csv files with SourcePath provenance | output_path, csv_paths or --glob | Project_Detail.csv |
| `generate_index_md.sh` | zsh | List folder contents into an INDEX.md manifest | FOLDER_PATH | INDEX.md |
| `summarize_by_wbs.py` | Python 3 | Group and sum Amount by WBS (Package/Deliverable) | input_csv, output_csv | Project_Summary_WBS.csv |
| `summarize_by_cbs.py` | Python 3 | Group and sum Amount by CBS category | input_csv, output_csv | Project_Summary_CBS.csv |
| `generate_wbs_cbs_matrix.py` | Python 3 | Pivot detail data into WBS x CBS cost matrix | input_csv, output_csv | Project_WBS_CBS_Matrix.csv |
| `generate_coverage_csv.py` | Python 3 | Cross-reference deliverables vs found artifacts (deps, estimates, doc kit) | EXECUTION_ROOT, output_csv | Coverage.csv with per-deliverable presence flags |
| `clean_pdf2md_output.py` | Python 3 | Remove repeating page headers, separators, and boilerplate from PDF-to-markdown conversion output | file.md [file2.md ...] | Cleaned files in-place + line removal counts |
| `merge_equipment_costing_csv.py` | Python 3 | Merge per-KTY Equipment_Costing_Extract CSV files into a single consolidated CSV | OUTPUT_CSV, INPUT_DIR, [--sort-by COLUMN] | Consolidated Equipment_Costing_Extract.csv |
| `synthesize_domain_coverage_json.py` | Python 3 | Serialize DOMAIN `annex_coverage_telemetry.csv` plus optional SCA KTY remediation manifest rollup into governed pre/post coverage JSON for SCOPE_CHANGE baselines. Optional `--package-subfolder NAME` flag for transitional dual-layout support; auto-descends into a single eligible subfolder when annexes not at root | `--decomposition-root`, `--output-json`, `[--scope-change-snapshot]`, `[--missing-manifest-state]`, `[--note]`, `[--package-subfolder]` | `Pre_Change_Coverage.json` or `Post_Change_Coverage.json`; exit 0/1 |

## Runtime telemetry

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `workflow_runtime/runtime_telemetry.py` | Python 3 | Append concurrency-safe, run-contained session/check/retry/remediation events and summarize durations, failure categories, reason codes, and native context-occupancy availability without inferring missing telemetry | `record` or `summarize`, `--run-root`, stable event/session/instance IDs, event type/outcome, optional package/member/attempt/reason/token fields | `RUNTIME_EVENTS.jsonl`, `RUNTIME_SUMMARY.json`; exit 0 complete / 1 incomplete session pairs / 2 invalid or operational input |

## PDF-to-Markdown

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `rasterize_pdf.py` | Python 3 | Render PDF pages to numbered PNG files via pymupdf (idempotent — skips existing PNGs). Writes `manifest.json` with `pdf_path`, `pdf_sha256` (content hash, closes the same-path-different-content gap), `page_count`, `dpi`, `pages_rendered`, `files`, `timestamp` | pdf_path, output_dir, [--dpi 300], [--pages 1-5,7] | `page_{NNNN}.png` files + `manifest.json` |
| `postprocess_page.py` | Python 3 | Apply 10-rule deterministic cleanup to VLM-generated markdown (strip fences, fix tables, remove hallucinations, normalise whitespace) | input.md, [output.md] | Cleaned markdown file |
| `assemble_markdown.py` | Python 3 | Join per-page markdown files into a single assembled document with page separators; optionally consume alternate per-page filename templates such as anchored pages | pages_dir, output_file, [--separator "---"], [--page-template "page_{page:04d}.md"] | Assembled `.md` file |
| `build_page_brief.py` | Python 3 | Render an INIT-TASK brief for one `pdf2md-page` dispatch. One brief per page; embeds IMAGE_PATH, OUTPUT_PATH, PAGE_NUM, TOTAL_PAGES. Used by the pdf2md-orchestration workflow Phase 2 to render briefs uniformly (mirrors `build_page_assets_brief.py` for Phase 3.5 and the EQUATION_AUDIT brief-builders) | --work-dir, --page, --total-pages, [--output-md] | INIT-TASK brief on stdout |
| `build_page_assets_brief.py` | Python 3 | Render a valid INIT-TASK brief for one `pdf2md-page-assets` dispatch | --work-dir, --doc-stem, --page, --total-pages, [--page-md], [--output-json], [--asset-policy] | INIT-TASK brief on stdout |
| `materialize_page_assets.py` | Python 3 | Crop page assets from VLM bbox JSON (strict kind/bbox/caption shape), write figure/image/table PNGs, delegate to `render_table_xlsx.py` for one deterministic XLSX per `table_data` block (honors `needs_extraction: true` skip), record `xlsx_path` / `xlsx_sha256` / `table_data_sha256` on each entry, and append deterministic asset references to a draft anchored page Markdown. Rejects the legacy `csv_text` field with a contract-pointing error. | --page-image, --page-md, --asset-json, --assets-root, --doc-stem, --page, --output-md, --manifest-output, [--padding-ratio] | Asset files (PNG + XLSX), draft `page_NNNN.anchored.md`, per-page materialization manifest (schema `pdf2md-assets-materialized/v2`) |
| `render_table_xlsx.py` | Python 3 | Deterministically render one `pdf2md-table/v1` `table_data` block into a single XLSX (pinned 1970 timestamps, fixed column widths, footnote-as-Comment, merge_cells from spans); byte-identical output across runs. Invoked by `materialize_page_assets.py`; usable standalone for re-rendering. | --table-data-json, --output-xlsx, --caption, --doc-stem, --page, --ordinal, [--slug] | One `.xlsx` workbook per call |
| `rewrite_inline_asset_refs.py` | Python 3 | Rewrite inline figure/table/oddball-image placeholders in a per-page Markdown so they point at materialized asset paths; emits a trailing "Unmatched Page Assets" block only for assets without an inline match. Table replacements use `[XLSX](...)` and surface `needs_extraction` markers; drift-detects legacy `[CSV](...)` links. | --page-md, --materialized-manifest, --output-md | Canonical anchored `page_NNNN.anchored.md` |
| `aggregate_asset_manifest.py` | Python 3 | Merge per-page asset materialization manifests into one document-level public asset manifest (schema `pdf2md-assets-document/v3` — additive bump over v2: every page record carries `page_label` (string or null) and `page_label_source` ∈ {vlm, vlm_failed, unreviewed, human}). Reads optional `<work_dir>/page_folios.json` to inject folio fields | work_dir, output_json, [--doc-stem] | `{doc_stem}_assets_manifest.json` |
| `build_folio_extract_brief.py` | Python 3 | Render an INIT-TASK brief for one `pdf2md-folio-extract` dispatch. Per-page brief that points the skill at one page raster and writes the JSON result to `{WORK_DIR}/page_folios/page_NNNN.json` | --work-dir, --page, [--output-path] | INIT-TASK brief on stdout |
| `run_folio_extraction.py` | Python 3 | Aggregate per-page folio JSONs (`{WORK_DIR}/page_folios/page_NNNN.json`) into a single `page_folios.json` keyed by physical page number. Run after the `pdf2md-folio-extract` TASK fan-out completes | --work-dir, [--output] | `page_folios.json` |
| `migrate_csv_assets_to_archive.py` | Python 3 | One-shot cleanup utility for the Phase 4 table-handling migration: walks a `tables/` directory, moves each legacy `.csv` whose paired `.xlsx` exists into `tables/.archive/`; refuses (exit 3) if any `.csv` has no paired `.xlsx`. Idempotent. | --tables-dir, [--dry-run] | Files relocated under `.archive/` and a per-file action log |
| `redispatch_csv_text_tables.py` | Python 3 | Phase 4a orchestration helper: enumerates pages whose existing `page_NNNN_assets.json` still carries legacy `csv_text` tables, renders one `pdf2md-page-assets` brief per page, and emits a `_queue.json` for the orchestrator to fan out as TASK+pdf2md-page-assets dispatches (dispatch model named by the user at run time; requires a vision-capable mid-tier model). Each subagent emits the new `table_data` JSON in place of the legacy `csv_text`. | --sources-root, [--briefs-dir], [--source], [--limit] | One brief `.md` per page + `_queue.json` |
| `validate_asset_resume.py` | Python 3 | Validate existing per-page asset materialization manifests against current page rasters and referenced anchored Markdown / asset files before reuse | work_dir, [--pages 1-10,12] | `resume_safety=OK` or mismatch report (exit 0/1/2) |
| `validate_assets.py` | Python 3 | Validate assembled Markdown asset links against the public asset manifest and files on disk; reports missing files, orphan links, manifest widows, and unmanifested files | --markdown, --manifest, --assets-root | PASS/FAIL summary (exit 0/1/2) |

## Restored and removed tool families

The restored workflows use tools in `drawing_extract/`, `equation_audit/`,
`domain_extract/`, `publication/`, `aggregation/`, and `diagnostics/`. Their
workflow contracts name their operations and inputs. The pipe-spec tools remain
removed and are preserved in the private `sgttomas/chirality` repository.

The practitioner harness (frozen App v3/PEC/Piping observation CLI), runtime-analysis
inventory, domain-engine profile validator, AgentRuns archiver, Chirality
self-domain Gate 3–5 and batch adapters, and App v3 harness-contract pull check
were removed on 2026-11-05 (owner item #35). They remain recoverable from this
repository's Git history.

## Decomposition

Per-source skeleton lift, dispatch-unit planning, HTML rendering, and atom/vocabulary merge tools for per-source decomposition fan-out (the per-item dispatch pattern PDF2MD also uses). The restored `domain-decomp` workflow can use these tools.

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `build_source_skeleton.py` | Python 3 | Deterministic TOC tree from `<book>.md` (`#`/`##`/`###` headings) with line ranges per section, inline `Fig./Table/Eq.` reference labels, asset_ids inlined within each line range, heuristic front/back-matter flags, and a per-dispatch-unit plan. Section clustering rules: (a) never split mid-section under threshold; (b) cluster adjacent in-scope sections up to `--budget-tokens`; (c) when a single section >= `--section-split-threshold`, split into preamble + per-child `###` units. Front/back-matter sections excluded from the dispatch plan | `--md`, `--asset-manifest`, `--output-skeleton`, `--output-dispatch-plan`, `[--source-prefix]`, `[--budget-tokens]` (default 15000), `[--section-split-threshold]` (default 25000), `[--front-matter-overrides JSON]`, `[--back-matter-overrides JSON]` | `<book>_skeleton.json` + `<book>_dispatch_plan.json` |
| `build_toc_priors.py` | Python 3 | Cross-source TOC reconciliation prior for Phase 3. Reads multiple `<book>_skeleton.json` (or `.reviewed.json`) inputs; emits a human-readable side-by-side TOC matrix MD and a deterministic title-keyword-overlap alignment CSV (source-A vs source-B section pairs with shared keywords and Jaccard similarity). Tokenizer drops stopwords + bibliographic noise. No semantic alignment — keyword-overlap prior only; final reconciliation is the persona's role at Gate 3 | `--skeleton` (repeatable), `--output-md`, `--output-csv`, `[--min-shared]` (default 2), `[--max-depth]` (default 3) | `cross_source_toc_matrix.md` + `cross_source_toc_matrix.csv` |
| `merge_vocabulary_seeds.py` | Python 3 | Consolidate per-source vocabulary seed CSVs into a single `Vocabulary_Map.csv`. Case-insensitive grouping on CandidateTerm; Synonyms / SourceRefs / Definitions / Notes unioned across sources (semicolon-separated, dedup-preserving order); SourceDocs + SourceCount columns added for prioritizing persona review at Gate 2 | Repeated `--seed <book>_vocabulary_seed.csv --source-doc <book>` pairs, `--output Vocabulary_Map.csv` | Merged `Vocabulary_Map.csv` |
| `merge_source_atomizations.py` | Python 3 | Two-stage merge of per-unit atomization CSVs into the domain ledger. **per-source** stage walks one source's dispatch units in plan order, assigns stable `HBA-<PREFIX>-NNNNN` IDs, validates LocalSeq monotonicity within each unit and ContentHash = sha1(UnitStatement)[:12], dedupes by ContentHash, writes `<book>_atomic_units.csv`. **cross-source** stage concatenates per-source ledgers, fails on prefix collisions or duplicate `AtomicUnitID`s, warns on unresolved cross-source `Corrects` refs, adds `SourceDoc` + `SourcePrefix` columns, writes `Atomic_Domain_Ledger.csv` | `per-source --dispatch-plan <plan>.json --unit-csv-glob <pattern> --source-prefix PSE --source-name <doc> --output <book>_atomic_units.csv [--strict-coverage]` ; `cross-source --per-source <p1> --per-source <p2> ... --output Atomic_Domain_Ledger.csv` | Per-source ledger or cross-source `Atomic_Domain_Ledger.csv` |
| `build_atomization_brief.py` | Python 3 | Render an INIT-TASK brief for one `domain-source-atomize` dispatch unit. Emits the documented INIT-TASK shape (PURPOSE, RequestedBy: WORKING_ITEMS, ActingSurface: TASK, ScopePath, Workflow, AllowedWriteTargets [per-unit CSV paths only], RuntimeOverrides [SOURCE_NAME, SOURCE_PREFIX, DISPATCH_UNIT_ID, MD_PATH, LINE_START, LINE_END, SKELETON_PATH, ASSET_MANIFEST_PATH, OUTPUT_LEDGER_PATH, OUTPUT_VOCAB_SEED_PATH, TARGET_SECTION_IDS, optional MAX_ATOMS], CustomInstructions [defensive format reminders], ExpectedOutputs) | `--dispatch-plan`, `--unit-id`, `--md`, `--skeleton`, `--asset-manifest`, `--output-ledger-path`, `--output-vocab-seed-path`, `[--scope-path]`, `[--max-atoms]` | INIT-TASK brief on stdout |
| `render_source_html.py` | Python 3 | Render `<book>.html` — the per-source **section + atom** review surface (Gate 1.5-S / Gate 2 / Gate 5). Each chapter/section becomes a content-hash-keyed reviewable chunk with sticky page-image strip on the left and section body on the right; three-state radio chips + flag-note textarea; localStorage state + timestamped `*_sections_*.json` / `*_atoms_*.json` sidecar exports. Section-heading page-badge ("p. 47" / "pp. 23–25") aids PDF cross-reference. Modes: `structure` (Gate 1.5-S skeleton), `atom-review` (Gate 2; reads `--atomic-units-csv`), `coverage-review` (Gate 5 atom-density CSS classes cov-empty/low/mid/high). Inline `Fig./Table` refs in prose are rewritten to anchors into the per-kind surfaces (`figures.html#asset-{id}` / `tables.html#asset-{id}`). Per-asset and per-equation review live in their own surfaces (`equations.html` / `figures.html` / `tables.html` / `images.html`); this surface no longer renders them. Existing `audit/verified.json` / `audit/flagged.json` sidecars load via `load_sidecar_with_fallback`. Companion `<book>_section_nodes.csv` emitted for section-level retrieval indexing | `--md`, `--asset-manifest`, `--skeleton`, `--audit-dir`, `--output-html`, `--output-section-nodes`, `[--mode structure\|atom-review\|coverage-review]`, `[--atomic-units-csv]`, `[--pages-dir-rel]`, `[--title]` | `<book>.html` (section+atom review surface) + `<book>_section_nodes.csv` |
| `source_audit/audit_figures.py` | Python 3 | Render `figures.html` — the per-figure Gate 1.5-F review surface. One reviewable chunk per `kind=fig` asset (bbox crop image + caption + accept/flag radio controls), grouped per source page with the page raster sticky on the left. Sidecars: `<source>_figures_verified_<TS>.json` / `<source>_figures_flagged_<TS>.json`, re-loaded via shared `load_sidecar_with_fallback`. Built on `tools/source_audit/` shared base (sidecar, chunk, page_strip, html_shell) | `--asset-manifest`, `--audit-dir`, `--output-html`, `[--pages-dir-rel]`, `[--title]` | `figures.html` |
| `source_audit/audit_tables.py` | Python 3 | Render `tables.html` — the per-table Gate 1.5-T review surface. One chunk per `kind=tbl` asset (bbox crop + caption + XLSX link + JSON sidecar link + accept/flag controls); tables flagged `needs_extraction: true` render with a distinct chip and no XLSX/JSON links. Sidecars: `<source>_tables_verified_<TS>.json` / `<source>_tables_flagged_<TS>.json` | `--asset-manifest`, `--audit-dir`, `--output-html`, `[--pages-dir-rel]`, `[--title]` | `tables.html` |
| `source_audit/audit_images.py` | Python 3 | Render `images.html` — the per-image Gate 1.5-I review surface. One chunk per `kind=img` asset (bbox crop + caption + accept/flag). Bucket is the catch-all for non-figure/non-table raster assets (mastheads, logos, decorative ornaments, photographs); review motion is mostly false-positive triage. Sidecars: `<source>_images_verified_<TS>.json` / `<source>_images_flagged_<TS>.json` | `--asset-manifest`, `--audit-dir`, `--output-html`, `[--pages-dir-rel]`, `[--title]` | `images.html` |
| `source_audit/audit_folios.py` | Python 3 | Render `folios.html` — the per-page Gate 1.5-Fo review surface (conditionally required when folio extraction has been run on the source). One chunk per page showing the VLM-emitted printed folio + confidence + location chips + page raster. Sidecars: `<source>_folios_verified_<TS>.json` / `<source>_folios_flagged_<TS>.json` | `--page-folios-json`, `--audit-dir`, `--output-html`, `[--pages-dir-rel]`, `[--title]` | `folios.html` |
| `source_audit/equations.py` | Python 3 | Kind-specific module for the equations audit surface. `scan_pages` extracts every `$$..$$`; `render_equations_audit_page` composes the shared base with optional per-equation source crops from `crops/page_NNNN_eq_NN.png`, KaTeX preview, 4-state Backcheck UI, `1.5-P-machine` / `EQUATION_AUDIT-phase3` source badges on Backcheck entries, and a Reject-proposal action that writes `equations_rejected.json` keyed by `(equation_hash, proposal_hash)` for sticky-per-proposal rejection of 1.5-P proposals. The restored `tools/equation_audit/` is a consumer | — (library) | — |
| `source_audit/tokenize_md.py` | Python 3 | Gate 1.5-P helper: Markdown tokenizer that splits a per-page extract into a typed stream (`ProseLine`, `EquationBlock`, `AssetRef`, `Placeholder`, `Blank`) for the deterministic comparator | — (library) | — |
| `source_audit/normalize_prose.py` | Python 3 | Gate 1.5-P helper: deterministic prose normalization (NFKC, ligatures, smart quotes, soft hyphens, line-break hyphenation, multi-space). `normalize_for_diff` adds whitespace and trailing-punctuation collapse for the strict prose compare | — (library) | — |
| `source_audit/canonicalize_latex.py` | Python 3 | Gate 1.5-P helper: textual v1 LaTeX canonicalizer (`\frac` ≡ `\dfrac` ≡ `\tfrac`, `\mathrm{}` ≡ `{\rm }`, `\operatorname{}` → `\mathrm{}`, thin spaces dropped, `\left`/`\right` dropped, brace-around-single-decorative-token stripped). v2 (AST) deferred | — (library) | — |
| `source_audit/compare_extracts.py` | Python 3 | Gate 1.5-P Stage 2: deterministic three-class compare. Returns `PageComparison` with `prose_hunks`, `equation_structural_fails`, `equation_content_proposals`, `asset_structural_fails`, `caption_notes`. Proposal hashes are content-hashed over the canonicalized LaTeX (so cosmetic re-extractions don't reset rejection). **Purely additive — never writes a verification or exemption signal** | — (library) | — |
| `source_audit/validate_prose.py` | Python 3 | Gate 1.5-P Stage 2 CLI: walks `(work_dir, reextract_dir)` and aggregates per-page comparisons into `<audit-dir>/prose_validation.json` (schema `pdf2md-prose-validate/v1`) | `--work-dir`, `--reextract-dir`, `--audit-dir`, `[--output]` | `prose_validation.json` |
| `source_audit/run_prose_validation.py` | Python 3 | Gate 1.5-P orchestration helper invoked AFTER the `domain-prose-validate` TASK fan-out lands per-page re-extracts. Calls `validate_prose.py` with the conventional path layout | `--work-dir`, `--audit-dir`, `[--reextract-dir]` | passthrough |
| `source_audit/` (shared base) | Python 3 | Shared module for per-kind audit surfaces: `sidecar.py` (`content_hash`, `load_sidecar`, `load_sidecar_with_fallback`), `chunk.py` (`render_chunk_controls`, `initial_status_for_key` — 4-state-capable via optional `backcheck` arg), `page_strip.py` (`render_page_section` with optional `page_label`, `render_nav`), `html_shell.py` (`render_audit_page` — toolbar, sticky nav, localStorage state machine, kind-scoped timestamped sidecar export, optional `extra_states=["backcheck"]` + `head_extras` + `js_extensions` for the 4-state KaTeX variant used by equations.html) | — (library) | — |

## Coordination

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `accumulate_supersession_map.py` | Python 3 | Deterministically accumulate cumulative `Supersession_Map.csv` rows from accepted prior maps plus current SCA delta rows, with optional check-mode comparison for closure audit | repeatable `[--prior-map]`, repeatable `[--delta]`, `--output-map`, `[--allow-empty]`, `[--check-map]`, `[--output-findings]` | Cumulative `Supersession_Map.csv`; optional findings CSV; exit 0/1/2 |

---

## Evaluation

Canonical versions at `tools/evaluation/`. Project-specific variants may also exist at `{EXECUTION_ROOT}/_Evaluation/tools/`.

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `verify_digest_coverage.sh` | zsh | Verify 1:1 deliverable-to-digest mapping | EXECUTION_ROOT | PASS/FAIL (exit code) |
| `count_deliverable_files.sh` | zsh | Count MUST/SHOULD/MAY files across all deliverables | EXECUTION_ROOT | Per-file count table |
| `extract_lifecycle_states.sh` | zsh | Extract and summarize lifecycle state distribution | EXECUTION_ROOT | State distribution |
| `count_deliverables_per_package.sh` | zsh | Count deliverable folders per package | EXECUTION_ROOT | Per-package count |
| `extract_agent_output.py` | Python 3 | Extract final assistant text from Claude agent JSONL output files | agent_output_file, [output_file] | Extracted text |

---

## Review

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `scan_section_coverage.py` | Python 3 | Compare draft/authored DBM section headings against Publication_Schema.md, optionally enriched by Section_Map.csv | `--draft`, `--schema`, `[--section-map]`, `[--output]` | Section coverage CSV; exit 0/1 |
| `extract_claims.py` | Python 3 | Locate engineering values, design parameters, configuration statements, and controlled terms in DBM text | `--draft`, `[--section-map]`, `[--output]` | Claims CSV; exit 0/1 |
| `scan_tbd_markers.py` | Python 3 | Locate TBD/TBC/ASSUMPTION markers with line numbers and optional KB cross-reference via Scoping.md | `--draft`, `[--section-map]`, `[--domain-root]`, `[--output]` | TBD inventory CSV; exit 0/1 |
| `check_body_thinness.py` | Python 3 | Smoke test for section body underdevelopment signals (line counts, density ratios, table presence) | `--draft`, `[--section-map]`, `[--schema]`, `[--output]` | Body thinness signals CSV; exit 0/1 |

## Retrieval

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `build_source_index.py` | Python 3 | Build V2 BM25 + optional dense embedding sidecars from a source database snapshot's `chunks` table. Uses stable `chunk_id` / `artifact_id` public identity and stores internal row alignment in SQLite `index_rows` | `--snapshot`, `[--domain-root]`, `[--model]`, `[--dim]`, `[--batch]`, `[--no-embeddings]`, `[--force]` | Snapshot-local `bm25/`, optional `embeddings.npy` / `embeddings_norm.npy`, updated `catalog.sqlite.index_rows` and `index_builds` |
| `query_source_index.py` | Python 3 | Query a V2 source database snapshot with selectable `hybrid`, `dense`, or `bm25` retrieval, returning stable chunk/artifact IDs and provenance paths. Supports filters over source doc, artifact role, chunk type, audit kind, structural IDs, and archive state. Optionally appends one canonical `Query_Log.csv` row per query for research-packet provenance (off by default; never writes inside an immutable snapshot) | `--snapshot`, `--query` or `--batch`, `[--mode]`, `[--k]`, `[--json]`, `[--source-doc]`, `[--artifact-role]`, `[--chunk-type]`, `[--audit-kind]`, `[--category-id]`, `[--knowledge-type-id]`, `[--subject-id]`, `[--archive-state]`, `[--run-log]`, `[--log-dir]` | Ranked result rows with `chunk_id`, `artifact_id`, `rel_path`, `source_ref`, retrieval mode, retrieval scores, metadata, and text preview; optional appended `Query_Log.csv` row |
| `scaffold_research_packet.py` | Python 3 | Create one immutable `RCH_<UTC>_<slug>/` research packet (RESEARCH_NOTE.md, Query_Log.csv, Evidence_Map.csv, Amendment_Candidates.csv, Open_Questions.csv, Conflicts.csv, HANDOFF_STATE.md) with canonical headers defined in `research_packet.py` (used by `research-orchestration`), and refresh `_Research/_LATEST.md`. Refuses to overwrite an existing packet (immutable) | `--research-root`, `--slug`, `[--topic]`, `[--utc]`, `[--no-update-latest]`, `[--json]` | New packet dir + 7 seeded files + updated `_LATEST.md`; exit 0 created / 1 packet exists / 2 invalid |

## Source Catalog

| Name | Language | Purpose | Inputs | Outputs |
|------|----------|---------|--------|---------|
| `build_source_database.py` | Python 3 | Build a domain-local V2 source catalog snapshot over filesystem artifacts or a source manifest. Manifest-backed rows reference live repo files as `@repo/<RepoRelPath>` plus SHA-256 and do not copy source assets. Excludes archive paths unless archive metadata is explicitly requested | `[--domain-root]`, `[--out-root]`, `[--repo-root]`, `[--source-manifest]`, `[--include-archive-metadata]` | `<domain-root>/_LocalIndexes/snapshots/SRCIDX_<UTC>/{catalog.sqlite,SourceDocs.csv,Artifacts.csv,AuditState.csv,Chunks.csv,meta.json,QA_Report.md}` and `_LocalIndexes/_LATEST.md` |
| `validate_source_database.py` | Python 3 | Validate a V2 source catalog snapshot: schema, exports, counts, path existence, `@repo/` path resolution, hash freshness, FK integrity, chunk hashes, audit surface warnings, and source-copy policy | `[--snapshot]`, `[--domain-root]`, `[--repo-root]`, `[--skip-hash-verify]`, `[--json]` | PASS/FAIL summary or JSON findings; exit 0/1/2 |
| `check_snapshot_freshness.py` | Python 3 | Compare a snapshot's recorded artifact SHA-256s against the current live source tree and report changed/missing/unchanged counts plus a FRESH\|STALE verdict, without rebuilding (honours "no silent refresh"). Answers "is the retrieval evidence still current?" before it enters authority | `--snapshot`, `[--domain-root]`, `[--repo-root]`, `[--json]`, `[--csv]`, `[--skip-hash-verify]` | JSON/CSV drift report + FRESH\|STALE verdict; exit 0 fresh / 1 stale / 2 invalid |

## Backlog (CREATE LATER)

Tools identified as useful but not yet needed — either used by only one agent, already handled inline by existing tools, or the agent currently manages the operation via LLM reasoning with an adequate fallback.

| Name | Category | Purpose | Why deferred |
|------|----------|---------|--------------|
| `find_estimate_snapshots.sh` | query | Glob all EST_* snapshot folders | AGGREGATION already uses `merge_detail_csvs.py --glob` which embeds the lookup |
| `find_detail_csvs.sh` | query | Find Detail.csv within estimate snapshots | Same — embedded in `merge_detail_csvs.py --glob` pattern |
| `extract_decomp_ids.py` | query | Parse decomposition markdown to extract PKG/DEL IDs, names, fields | PROJECT_SETUP and PREPARATION currently parse via LLM reading; useful for deterministic coverage checks once decomposition format stabilizes further |
| `serialize_workspace_state.py` | reporting | Serialize filesystem state to JSON | Superseded by AUDIT_DECOMP's `coverage_summary.json`; no agent protocol invokes a generic filesystem-to-JSON dump |

**Promotion criteria:** A backlog tool should be promoted to CREATE NOW when (1) a second agent needs the same operation, or (2) an existing agent's inline implementation diverges across runs and needs standardization.

---

EOF


## Four-role workflow runtime (D-GOV-41)

- `tools/workflow_runtime/resolve_workflow.py`: explicit workflow and method resolution, selected context fingerprints and independent policy intersections.
- `tools/workflow_runtime/normalize_brief.py`: structured inline/file brief normalization and explicit writable-root containment; imported by the resolver.
- `tools/validation/validate_workflow_metadata.py`: workflow entrypoint and optional execution-policy validation.
- `tools/validation/validate_agent_instructions.py`: four-role registry and four-section instruction validation; requires `agents/registry.json`.
- `tools/validation/validate_skill_metadata.py`: compatibility CLI; defaults to the workflow validator, while explicit historical skills directories use historical validation.

For invocation and returned policy semantics, see `tools/workflow_runtime/README.md`.


### Historical tool inputs

`tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md` is the frozen industry-practices pilot
campaign brief, including its campaign-specific model and dispatch parameters.
Its bytes remain historical evidence; current PDF work selects
`workflows/pdf2md-orchestration/WORKFLOW.md`.
Current workflow inventory comes from immediate `workflows/*/WORKFLOW.md`
packages.
