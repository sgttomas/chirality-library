> **Generated view — not authority.** Produced by tools/practitioner_harness (command: brief).
> Sources cited per finding; on any disagreement the cited source files govern.
> Regenerate from project files; safe to delete. Structural checks are not approval,
> issue, authentication, or acceptance of residual risk (K-AUTH-1; D-GOV-01).

# Tranche brief TRB-chirality-app-dev-DEL-03-01-2026-07-03 — HUMAN_ADOPTED

- tranche_id: `TRB-chirality-app-dev-DEL-03-01-2026-07-03`
- state: HUMAN_ADOPTED
  - lifecycle: CANDIDATE → HUMAN_ADOPTED → EXECUTED → CHECKED → HUMAN_REVIEWED → CLOSED/SUPERSEDED
  - (brief lifecycle is metadata on harness artifacts only — never the deliverable lifecycle)
- objective: Absorb the merged D-APP-46 extraction (PR #21, `ecc9c5a35`) into this
  deliverable's contract records and record the package-consumption readiness baseline —
  doc-only, within-fence: (1) close the Datasheet.md:58 "Exact final source path"
  CANDIDATE/TBD by cross-reference to the accepted placement
  (`frontend/packages/harness-contract/src/agent-engine-port.ts`; D-APP-46
  established the package placement, and D-APP-47 later retired the former
  frontend shim); (2) annotate — never rewrite — the contract-surface
  paths recorded in Assessment_INSP-03_DEL-03-01.md:23-35 and
  Evidence_CODEV-001_Runtime_Engine_Conformance.md:38-43 with their post-extraction
  homes (10 `frontend/src/lib/harness/*.ts` entries are now package re-export shims;
  the assessments stay true as written for their date — forward-correction pattern per
  the Loop 1 INSP-03 precedent); (3) record the consumption-readiness baseline as
  measured 2026-07-03 in a deliverable-local record: `@chirality/harness-contract`
  version `0.0.0-private`, `private: true`, exports map = root + 10 module subpaths +
  package.json (`frontend/packages/harness-contract/package.json`);
  `FLOW_A_CONTRACT_VERSION = 'TBD_BY_TIER_0'` +
  `CLAUDE_AGENT_SDK_PACKAGE_VERSION = '0.3.150'`
  (`projects/chirality-app-dev/frontend/packages/harness-contract/src/sdk-version.ts:1-2`) and
  `HARNESS_TOOL_REGISTRY_VERSION = 'harness-tools.v6.mutating-mcp'`
  (`projects/chirality-app-dev/frontend/packages/harness-contract/src/tool-descriptor.ts:9`)
  per the D-APP-45 ruled wiring; 64 files under
  `frontend/src` (45 tests / 10 app / 9 components) still import via the shim paths, 0
  import the package directly; dependency lint
  `frontend/scripts/assert-harness-contract-deps.mjs` wired as
  `harness:validate:contract-deps` (frontend/package.json:26) — the measured baseline
  the DEC-041 automation condition
  (`projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:611`) is
  judged against. Cross-reference, never invent (K-INVENT-1); residual TBDs stay
  explicit. _STATUS.md stays CHECKING — no lifecycle advance (F4 untouched); no
  frontend code edits (wrapper/importer disposition, version settlement, publication,
  and piping consumption remain owner-gated: D-APP-45 ruling §Scope, D-APP-46 ruling
  §Scope, DEC-042 bar at SOFTWARE_DECOMP.md:612). Work recorded as WORKING_ITEMS agent
  decisions (D-APP-45 conformance pattern).
  - source: practitioner-proposed 2026-07-03 from the cited files; owner may amend at adoption
- adopted_by: Ryan Tufts
- adopted_on: 2026-07-03
  - adoption provenance: owner adoption directed in-session 2026-07-03 ("I want it to
    become a governed record. Take care of it."); metadata recorded by agent at owner
    direction. The adoption act is the owner's (K-AUTH-1; D-GOV-04); this record binds
    to the publication commit (K-AUTH-2).

## source_basis

- status: Current State 'CHECKING' (line 3)
  - source: `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/_STATUS.md`
- plan posture: **Status:** vNext governance rewrite aligned to the approved `docs/PRD.md` dated 2026-05-20
  - source: `projects/chirality-app-dev/docs/PLAN.md:3`
- coordination pointer: artifact present
  - source: `projects/chirality-app-dev/execution/_Coordination/_LATEST.md`
- decision register: no rows mentioning DEL-03-01
  - source: `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md`
- DAG pointer: dag.CurrentClosureSnapshot = execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/
  - source: `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DAG_CLOSURE_CONTROL.md (line 9)`
- DAG pointer: dag.StrictFullGraphStatus = ACYCLIC
  - source: `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DAG_CLOSURE_CONTROL.md (line 10)`
- DAG pointer: dag.StrictSCCCount = 0
  - source: `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DAG_CLOSURE_CONTROL.md (line 11)`

## read_scope

- `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/**`
- `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/_REFERENCES.md (declared references surface)`
  - source: deliverable directory located via manifest `status_glob` (`execution/PKG-*/1_Working/DEL-*/_STATUS.md`)

## write_scope

- `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/**`
  - source: plan v3 tranche-brief schema — deliverable directory only

## prohibited_paths

- `_DomainEngines/**`
- `projects/chirality-piping/core/**`
- `projects/chirality-piping/schemas/**`
- `projects/chirality-piping/core/handoff/**`
- `projects/chirality-piping/**`
- `tools/**`
- `agents/**`
- `skills/**`
- `docs/**`
  - source: profile `protected_write_paths` (`_DomainEngines/profiles/open_pipe_stress.yaml`), the other project root, and the instruction surface (SPEC §0.2.2)

## validations (declared, not run)

- npm run typecheck (cwd: frontend) — declared in the adapter manifest; NOT run by this command
- npm run test (cwd: frontend) — declared in the adapter manifest; NOT run by this command
- npm run validate:release-quality (cwd: frontend) — declared in the adapter manifest; NOT run by this command
  - source: `projects/chirality-app-dev/_harness/adapter.yaml`

## evidence_targets

- `_harness_generated/briefs/TRB-chirality-app-dev-DEL-03-01-2026-07-03.md` (under the declared generated root; D-GOV-01)
- `_harness_generated/briefs/TRB-chirality-app-dev-DEL-03-01-2026-07-03.json` (under the declared generated root; D-GOV-01)
- `_harness_generated/evidence/TRB-chirality-app-dev-DEL-03-01-2026-07-03/` (under the declared generated root; D-GOV-01)

## stop_conditions

- an out-of-scope write attempt (outside write_scope or into prohibited_paths)
- conflicting current-truth discovered — stop and surface it per K-CONFLICT-1; never resolve silently
- a human decision point reached (see human_decision_points)

## human_decision_points

- adoption of this brief itself (human edits state to HUMAN_ADOPTED and commits; D-GOV-04)
- any CHECKING or ISSUED lifecycle advance — human-only (SPEC §3.3)

## adoption

Adoption is a human act (D-GOV-04); the harness never performs any of these steps and never flips this brief's state:

- a human edits `state:` above to HUMAN_ADOPTED
- the same human fills `adopted_by:` (must match `docs/governance_harness/human_actors.md`) and `adopted_on:`
- the file is moved to a governed path OUTSIDE `_harness_generated/` — the generated root is gitignored scratch; an adoption there does not exist for reliance (D-GOV-04)
- the file is committed — adoption binds to committed content at the publication commit (K-AUTH-2); check with `brief --verify-adoption <path>`

---

HUMAN_ADOPTED brief — an active fence, human-adopted and bound to committed content at the publication commit (K-AUTH-2; D-GOV-04); the cited sources govern on any disagreement.

## Summary

Finding severities: none
- tranche_id: TRB-chirality-app-dev-DEL-03-01-2026-07-03
- deliverable: DEL-03-01
- state: HUMAN_ADOPTED
