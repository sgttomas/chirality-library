# Root Loop and Deliverable Scope-of-Work Stage-1 Plan

**Status:** DRAFT PLAN — planning artifact only  
**Owner:** Human owner, supported by HELP_HUMAN and HELPS_HUMANS  
**Target workspace:** `/Users/<owner>/ai-env/projects/chirality`

## Summary

Establish a functioning root-governance loop, then use it to design and pilot
the replacement of each deliverable's four production documents with canonical
`ScopeOfWork.md`.

The root loop owns governance, schema, tools, and cross-project supervision.
Existing App Dev and Piping loops own their project-local pilots. Stage 1 does
not merge converted deliverables or authorize conversion of the remaining
corpus.

Canonical form:

```text
ScopeOfWork.md       authoritative deliverable definition
ScopeOfWork.html     generated on demand; never authoritative or tracked
_STATUS.md           lifecycle and current Remaining work
Other underscore files and registers remain separate
```

## Root Loop and Entry-Surface Repair

1. Create the root coordination home:

   ```text
   execution/_Coordination/
     LOOP_INIT.md
     WORKPLAN_2026-07-12_scope_of_work_stage1.md
     LOOP_RECEIPTS.md
     AgentRuns/<RunID>/
   ```

   Root `execution/` is explicitly a governance control plane, not a project
   decomposition or deliverable root. It contains no `PKG-*` or `DEL-*`
   structure.

2. Rewrite `init/init-prompt.md` §2 as the root-governance loop launcher:

   - Remove the root-wide WORKING_ITEMS persona entry.
   - Remove the dangling `NEXT_INSTANCE_PROMPT.md` reference.
   - Point the thin launcher to `execution/_Coordination/LOOP_INIT.md`.
   - Let LOOP_INIT and its newest standing workplan select HELP_HUMAN,
     HELPS_HUMANS, WORKING_ITEMS, RECONCILIATION, SCOPE_CHANGE, REVIEW, and
     CHANGE as appropriate.

3. Root LOOP_INIT follows the established project pattern:

   - Discover live Git, decisions, latest receipt, active branches, and
     relevant project-loop receipts.
   - Read the newest root `WORKPLAN_*.md`.
   - Apply human direction first.
   - Record orchestration plans and native-agent returns under root
     `AgentRuns`.
   - Stop at rulings, scope changes, lifecycle acceptance, or Stage-2
     authorization.
   - Never treat plans, receipts, or run records as authority.

4. Root standing workplan defines three lanes:

   | Lane | Owner | Purpose |
   |---|---|---|
   | Machinery | HELPS_HUMANS | Schema, skill, tools, validators, registries, compatibility, and deprecation design |
   | Pilot supervision | HELP_HUMAN | Cross-project activation, dependency management, notices, and fan-in |
   | Preservation audit | RECONCILIATION | Claim mapping, parity, source-state binding, and pilot closure evidence |

5. Root Stage-1 write fences:

   - Allowed: root governance candidate documents, agents/skills/tools/tests
     expressly authorized by D-GOV-15, public export regeneration, root
     coordination records, and exact pilot paths.
   - Denied: non-pilot deliverables, DOMAIN/KTY surfaces, archived trees,
     ISSUED deliverables, historical receipts, historical concordance
     artifacts, and lifecycle changes.
   - Git closeout remains CHANGE-owned and owner-merged.

6. Correct existing instruction drift:

   - Root `AGENTS.md` must describe the D-GOV-14-ratified standards as
     ratified, not candidates.
   - Remove the completed proto-run/PR #188 paragraphs from both project
     `LOOP_INIT.md` files without altering historical receipts.
   - Project loops otherwise remain unchanged during Stage 1; pilot variance
     arrives as a per-run steer.

## Governance and Scope-of-Work Contract

1. Produce two commit-bound pre-ruling reports:

   - **Sizing report:** 53 App Dev + 101 Piping = 154 live deliverables;
     explicitly exclude archives, DOMAIN/KTY, templates, fixtures, exports,
     and generated trees.
   - **Consumer inventory:** classify every four-document reference as an
     active caller, historical evidence, analogous independent schema, or
     retirement candidate.

2. Frame D-GOV-15 to authorize:

   - Candidate Scope-of-Work architecture and component implementation.
   - Canonical Markdown and on-demand HTML.
   - First-class output, claim, requirement, acceptance, verification, and
     rationale IDs.
   - Project-deliverable-only scope.
   - Exact path-scoped pilot variance.
   - Native platform-agent orchestration; no App Dev Desktop harness
     dependency.
   - Sequential fallback if equivalent native child records cannot be
     produced.
   - Lifecycle- and content-neutral conversion.
   - Pilot abort and evidence-preservation posture.
   - Stage-2 entry criteria.
   - No corpus-wide conversion and no exact TYPES/SPEC ratification yet.

3. Pilot variance:

   - Applies only in isolated worktrees to:
     - `projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/`
     - `projects/chirality-piping/execution/PKG-13_Physical Design Knowledge and Constraint Engine/1_Working/`
   - Candidate `chirality-deliverable-sow/v1` files may coexist with the four
     ratified documents only under this variance.
   - The four source documents remain authoritative throughout Stage 1.
   - Candidate conversions do not merge into `main`.
   - The variance overrides only the named TYPES/SPEC document-kit
     requirements for those pilot worktrees; all authority, lifecycle,
     provenance, write-scope, and human-gate rules remain in force.

4. Lifecycle neutrality:

   - `_STATUS.md` remains byte-identical during Stage-1 conversion.
   - Existing `IN_PROGRESS` state is preserved.
   - REVIEW derives and evaluates a candidate checklist but performs no
     lifecycle transition.
   - The ISSUED Piping baseline is excluded.
   - Any substantive scope or acceptance change becomes `CONFLICT` and routes
     to SCOPE_CHANGE or the human.

5. Candidate frontmatter:

   ```yaml
   schema: chirality-deliverable-sow/v1
   deliverable_id: DEL-XX-YY
   package_id: PKG-XX
   decomposition_basis: <path@commit>
   project_scope_refs: [SOW-NNN]
   package_objective_refs: [OBJ-NNN]
   ```

6. Required sections:

   - Purpose and Objective Traceability
   - Deliverable Definition — Ontology
   - Completion and Reliance Basis — Epistemology
   - Production and Verification Method — Praxeology
   - Governing Values and Decisions — Axiology
   - Output and Evaluation Matrix

7. Registered local IDs:

   | Prefix | Meaning |
   |---|---|
   | `OUT-NNN` | Expected output |
   | `CLM-NNN` | Descriptive claim |
   | `REQ-NNN` | Normative requirement |
   | `AC-NNN` | Acceptance criterion |
   | `VER-NNN` | Verification method |
   | `AX-NNN` | Governing value or rationale |
   | `TBD-NNN` | Unresolved information |
   | `CON-NNN` | Unresolved conflict |
   | `REM-NNN` | `_STATUS.md ## Remaining` item |

   External references use `DEL-XX-YY-<LocalID>`. REVIEW consumes the
   deliverable's `AC-*` IDs directly. Validators derive prefixes, membership,
   and widths from the registered catalog.

8. Migration dispositions:

   ```text
   PRESERVED | MERGED | SPLIT | SUPERSEDED | DEFERRED | CONFLICT
   ```

   These do not replace epistemic labels, lifecycle states, or rulings.

## Components and Pilot Workflow

1. HELPS_HUMANS designs and registers:

   - `validate_scope_of_work.py`
   - `render_scope_of_work.py`
   - `convert_four_documents_to_scope_of_work.py`
   - `map_scope_of_work_claims.py`
   - `report_scope_of_work_parity.py`
   - `skills/scope-of-work/`

   Each component conforms to `WORKFLOW_COMPONENT_STANDARD.md`, receives
   registry metadata and tests, and has explicit inputs, outputs, refusal
   behavior, and recovery rules.

2. Retain `skills/four-documents/` and all legacy callers during Stage 1.
   Retirement follows the replacement-first rule only after Stage-2 conversion
   and caller removal.

3. HTML renderer contract:

   - Input: validated `ScopeOfWork.md`.
   - Output: deterministic HTML carrying source hash, schema version, and
     renderer version.
   - No JavaScript, external assets, network dependencies, or authority
     claims.
   - HTML is generated for viewing, review, export, or publication and is not
     tracked per deliverable.
   - Repeated rendering of the same source and version must be byte-identical.

4. Format resolver:

   | Files present | Result |
   |---|---|
   | Four legacy documents only | `LEGACY_FOUR_DOC` |
   | Valid `ScopeOfWork.md` only | `SOW_V1` |
   | Both | `AMBIGUOUS`, permitted only by the pilot variance |
   | Neither at or beyond INITIALIZED | `INVALID` |

   The frontmatter marker chooses the parser but does not establish acceptance.

5. Add feature-gated dual-format support to:

   - ORCHESTRATOR and the production/enrichment pipeline.
   - WORKING_ITEMS briefs and integration-owner rules.
   - REVIEW and epistemic/structure audits.
   - RECONCILIATION claim extraction and migration mapping.
   - Semantic matrix, lens-register, P3 disposition, consistency, and coverage
     tooling.
   - App Dev's deliverable scanner and Markdown document viewer.

   Legacy behavior remains authoritative outside an explicit variance until
   Stage 2.

6. Pilot orchestration:

   - Root HELP_HUMAN supervises two project-local WORKING_ITEMS managers using
     the platform-native agent harness.
   - App Dev and Piping project loops receive the D-GOV-15 variance as an
     explicit per-run steer.
   - Each WORKING_ITEMS manager owns one pilot package and dispatches bounded
     TASK children per deliverable.
   - Children use sealed briefs, declared reads/writes, one candidate output,
     and structured returns.
   - One integration owner per deliverable writes the candidate
     `ScopeOfWork.md`.
   - Project-local Agent 2 records remain under each project's
     `execution/_Coordination/AgentRuns/`.
   - Cross-project notices and final fan-in remain under the root run.
   - If native execution cannot produce equivalent briefs, parentage, scopes,
     and returns, record the substrate defect and use the
     D-GOV-15-authorized sequential fallback. Do not classify substrate
     failure as schema failure.

7. Calibration wave:

   - App Dev: `DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts`
   - Piping: `DEL-13-01_Design knowledge schema and provenance model`

   Use these to refine the candidate schema. Freeze the schema revision before
   measuring steady-state repeatability.

8. Frozen-schema wave:

   - Reconvert both calibration deliverables from their frozen source basis.
   - Convert the remaining eight deliverables in PKG-07 and PKG-13.
   - Preserve all source hashes.
   - Produce one claim map, parity report, conversion receipt, and independent
     verifier return per deliverable.
   - RECONCILIATION performs the preservation audit and project/package
     fan-in.
   - Candidate deliverables remain unmerged Stage-1 artifacts.

9. Abort posture:

   - Any silent claim loss, invalid mapping, lifecycle change, unresolved
     authority conflict, or variance breach fails the affected pilot.
   - Main remains unchanged.
   - Preserve a FAILED handoff containing evidence and rerun requirements.
   - Retire the pilot worktree/branch after evidence capture.
   - Never leave dual-format state on an accepted branch.

## Stage-2 Entry Gates

D-GOV-16 may be proposed only if:

- 100% of source claims are dispositioned.
- No claim is silently dropped.
- Merged and split claims preserve every source reference.
- Every output maps to project scope and package objectives.
- Every `AC-*` maps to a `VER-*` or an explicit human-review method.
- REVIEW derives the same checklist on repeated runs directly from `AC-*`.
- Legacy-only and SOW-only consumers pass.
- Ambiguous and missing forms fail outside the variance.
- `_STATUS.md` and lifecycle state remain byte-identical.
- HTML rendering is byte-identical, source-bound, and script-free.
- Historical receipts, plans, briefs, and concordance artifacts remain
  unchanged.
- DOMAIN/KTY and analogous packet/case schemas remain unaffected.
- After schema freeze, each deliverable uses no more than one conversion run
  and one verifier run.
- Across ten frozen-schema conversions, no more than one fresh rerun is
  required.
- Human intervention occurs only for genuine content or authority conflicts.
- Schema, project-content, and native-substrate failures are reported
  separately.
- Root governance, agent, skill, path, export, and practitioner-harness checks
  pass.
- App Dev and Piping registered checks run once per commit-shaped pilot wave.
- Root and both project loop receipts close with accepted basis, evidence,
  blockers, derivative status, and Stage-2 recommendation.

D-GOV-16 then ratifies exact Scope-of-Work, TYPES, and SPEC texts; authorizes
project-specific loop amendments; determines ISSUED handling; and authorizes or
rejects conversion of the remaining 144 deliverables.

## Assumptions and Defaults

- Root coordination records live under root `execution/_Coordination/`.
- Root `execution/` is control-plane-only and does not make the repository a
  decomposed project.
- Stage 1 covers ten IN_PROGRESS deliverables and no ISSUED deliverable.
- `ScopeOfWork.md` is canonical; HTML is generated on demand.
- `_STATUS.md` and other control/generated files remain separate.
- Project loops remain the execution vehicles for project-local pilots.
- Native platform agents are used; the App Dev Desktop harness is not part of
  Stage 1.
- Main remains governed by the ratified four-document contract until D-GOV-16.
