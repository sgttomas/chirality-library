# FM-04 — Merge app-dev's richer OperationProposal into the canonical contract (APPLIED draft; pending approval)

**Targets (canonical):** `agents/AGENT_DOMAIN_ENGINE.md` SPEC "Valid Operation Proposal" (`:393-404`) + Minimal Profile Shape; the merged result is the spec app-dev `docs/TYPES.md §11.2` conforms to.
**Resolves:** D-T0-01 flow (iii). **Gate:** framework-maintenance (human-gated). **Status: APPLIED and PUBLISHED at `77a327727` (committed + pushed to origin/main; owner-directed 2026-06-21).**
**Application record:** Applied by HELPS_HUMANS framework-maintenance pass on 2026-06-22. Applying SHA: `77a327727`. Draft base HEAD observed: `16e723f45813`.

**Why:** Before application, the persona stated 8 prose validity criteria; app-dev formalized a richer typed record + lifecycle. The working-root work is **better** on field/provenance shape — absorb it UP into the canon (precedence-canonical does not discard good downstream work). Add the generic trust fields from piping §6.

> **Genericness + citation prerequisites.** Before promotion, app-dev's `OperationProposal` shape is verified piping-free (see CONTRACT_DIRECTION §4 "Genericness verification"). Tier-0's citation of persona line numbers here is lawful (framework-root authoring); the `_REFERENCES.md` SHA-pin of `AGENT_DOMAIN_ENGINE.md` into DEL-10-03 is the app-dev-side prerequisite recommended in `D-T0-01`, gating app-dev's conformance edits, not this draft.

---

### Proposed canonical OperationProposal (generic — no piping-specific vocab)

```yaml
operation_proposal:
  proposal_id: "<stable ID>"                 # persona: stable proposal ID (:399)
  profile_id: "<domain_engine_id>"
  base_state: "<state/model ref or TBD>"     # persona SHOULD name base state (:398); app-dev: + optional
  operation_name: "<declared operation>"
  status: "proposal_only"                     # persona umbrella (:399,:404)
  lifecycle: "draft | ready_for_review | accepted | rejected | applied"  # app-dev (merged up)
                                              #   proposal_only := {draft, ready_for_review}
                                              #   accepted/applied := human-gated + domain-engine apply (K-DOMAIN-3) + SHA (K-AUTH-2)
  created_at: "<ts>"                          # app-dev provenance
  created_by: "<actor>"                       # app-dev provenance
  input_refs: ["<manifest/run/comparison ID or path>"]   # persona cite-evidence (:400) + app-dev inputRefs
  intended_changes: [ ... ]                   # app-dev
  deterministic_checks: [ ... ]               # app-dev (validate via declared tool)
  expected_output_refs: [ ... ]               # app-dev
  risks: [ ... ]                              # app-dev
  assumptions: [ ... ]                        # persona MUST list assumptions (:401) — distinct from risks
  blockers: [ ... ]                           # persona MUST list blockers (:401)
  boundary_notice: "<professional-boundary language>"    # persona record MUST contain (:402)
  required_human_gate: "<gate token>"         # app-dev; binds to AnalysisStatus terminal transition
  operation_risk_class: "engine_checkable | engine_silent"   # GENERIC (piping §2; not the change_kind taxonomy)
  provenance_on_judgment_values: "<required for engine_silent values>"  # GENERIC (piping §3; distinct from DEC-043)
  storage_path: "<MUST be under profile agent_writable_paths>"   # persona (:403)
```

### Persona-criterion → field mapping (so nothing in `:393-404` is lost)

| Persona criterion (`:393-404`) | Merged field |
|---|---|
| stable proposal ID | `proposal_id` |
| names base state | `base_state` |
| `status: proposal_only` | `status` (umbrella) + `lifecycle` band |
| cites evidence | `input_refs` (admits manifest/run/comparison IDs) |
| lists assumptions + blockers | `assumptions`, `blockers` |
| professional-boundary language | `boundary_notice` |
| under agent-writable path | `storage_path` |
| not represented as accepted truth | enforced: `accepted/applied` require human gate + domain apply |

### Genuine gaps to close while merging (from DEL-10-03's 7 TBDs)

- **`required_human_gate ↔ approval-SHA`**: bind to K-AUTH-2 (approval binds to a git SHA) + the engine's `HUMAN_APPROVED_FOR_PROJECT` external hash-bound record.
- **adapter validate/apply result schema** + **deterministic-check result schema**: cross-reference the piping `operation_applier`/`rule_check_runner` result shapes (verified to exist) rather than leaving TBD.

**Provenance:** persona `:393-404`, Minimal Profile Shape `:694`; app-dev `docs/TYPES.md:517-533` (OperationProposal), DEL-10-03 Specification TBD list; piping §2/§3/§6.
