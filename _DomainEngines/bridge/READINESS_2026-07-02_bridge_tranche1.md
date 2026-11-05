# Bridge Readiness Assessment — app-dev ↔ piping tier-0 bridge (2026-07-02)

> **Epistemic status: agent-authored assessment — not authority.** Produced in-session
> at owner direction (Ryan Tufts, K-AUTH-1) as the durable record of the 2026-07-02
> readiness assessment. Sources cited per claim; on any disagreement the cited source
> files govern. Every load-bearing claim below was adversarially re-verified against
> the live tree in the producing session (multi-agent read + verify sweep, ~40 claims,
> zero refuted).

- **Assessed at:** main `565cc2b749755f489a3b79db922f22403a84f383`, working tree clean.
- **Ruling basis:** D-T0 rulings SHA-bound at `6e70b5aac` (`_DomainEngines/RULINGS_PUBLISHED.md`;
  records backfilled 2026-07-02 per owner ruling).
- **Scope:** readiness of `projects/chirality-app-dev` and `projects/chirality-piping`
  for the tier-0 bridge; selection of the first bounded tranche. No governed files were
  changed by the assessment.

## Verdict

The ruling basis is fully in place. Both projects are ready for **fenced, doc-only /
design-level bridge work now**; live binding remains gated behind four conditions of
which only tier-0 adoption is cleared. First recommended tranche: **app-dev DEL-10-03
result-schema tranche** via a harness CANDIDATE brief (§6).

## 1. Corrections to naive record-reading (highest-value findings)

These are the facts a fresh reader of the headings alone would get wrong:

1. **FM-01..04 are APPLIED and PUBLISHED at commit `77a327727`** (2026-06-21,
   git-confirmed). `_DomainEngines/RULINGS_PUBLISHED.md:20` ("authorized in direction
   but gated") is ruling *posture*; `RULINGS_PUBLISHED.md:41` and each FM record header
   record the applied state. Do not re-plan FM application.
2. **The REF-008 SHA-pin is landed.** `agents/AGENT_DOMAIN_ENGINE.md @ 77a327727` is
   pinned into app-dev DEL-10-01/03 `_REFERENCES.md` — landed doc-only as WORKING_ITEMS
   *agent decisions* under the D-APP-45 conformance tranche (DEL-10-01 `MEMORY.md:7`).
   D-APP-45's register row remains AWAITING_RULING for its Flow-A-versioning half; the
   pin is not an owner ruling.
3. **Event-vocabulary count is RULED at 43.** Piping D-28 (RULED by owner 2026-07-01,
   `projects/chirality-piping/execution/_Coordination/_DECISIONS/_REGISTER.md:52`) binds
   any Flow-A pin to the live `event-schema.ts` enumeration (43 as of 2026-07-01) and
   discharges app-dev's 2026-06-24 correction flag. DEC-041's "42-type" prose
   (`SOFTWARE_DECOMP.md:611`) is immutable history — never edit. The codifying DEC entry
   (would be DEC-055) is still pending per D-28 packet §8.
4. **DEC-051 residency reconciliation IS published** at `9db0eef27` (git-confirmed)
   despite the §12 entry's pre-commit "staged for CHANGE" wording
   (`SOFTWARE_DECOMP.md:621`). Residency is not a bridge blocker post D-T0-04.
5. **Two deliverables share the id DEL-10-03.** App-dev's
   (`PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow`,
   CHECKING) owns the OperationProposal Specification TBD list FM-04:54 cites. Piping's
   (`PKG-10.../DEL-10-03_Local FEA handoff data contract`, IN_PROGRESS) owns the Rust
   result shapes the ADOPTED profile's TBDs cite
   (`_DomainEngines/profiles/open_pipe_stress.yaml:72-74,81,88,101,115`). Always name
   the repo.
6. **`PLAN_cross_tier.md` is a PROPOSAL and is stale in two places:** its tier-1 row
   still says "blocked by D-T0-01" (ruled), and its tier-2 row bundles "headless CLI
   entrypoint" into the prep lane. The governing piping ruling, DEC-042
   (`SOFTWARE_DECOMP.md:612`), sanctions exactly three design/spec items (proposal→apply
   bridge + OperationSet→Plan schema extension; candidate-generation +
   operation-schema-reconciliation design; piping-design domain retrieval index) and
   does NOT sanction the entrypoint — which is an un-built TOOLMAKER handoff
   (`open_pipe_stress.yaml:103-107`) needing its own piping-loop decision.

## 2. app-dev readiness

Posture: D-APP-19 Option-D INSPECTION phase — all 53 deliverables CHECKING, issuance
(F4) deferred, one-way. Drift 0/53. PKG-10 conformance to ruled canon is **done**
(DEL-10-01/03 re-drafted, REF-008 pinned, K-DOMAIN-1..4 annotated as specializing
framework §1.12). Ready for doc-only bridge work.

Blockers (all owner-ruling shaped, not tranche work):
- **D-APP-46** AWAITING_RULING — harness-contract package extraction greenlight
  (internal-only; "no F1/F2/F3/F4 crossing, no piping coupling"). Keystone: without a
  consumable package (`frontend/package.json` is `private:true`, no workspaces/bin),
  the DEC-041 automated-pull condition and a "proven L2" (D-T0-08's precondition for
  opening F3) are unreachable.
- **D-APP-45** AWAITING_RULING — Flow-A cross-repo contract version (`TBD_BY_TIER_0`).
- Fences F1 (posture-only opened by D-APP-44, no implementation), F2, F3, F4 all intact.

## 3. piping readiness

Posture: target stage advanced R4 → **PRD R5** (D-27 RULED 2026-06-23; DEC-054 at
`SOFTWARE_DECOMP.md:624`). R5 is the current PRD's terminal milestone; R6/R7 carry no
roadmap weight until D-21. Deliverables 8 CHECKING / 92 IN_PROGRESS / 1 ISSUED; the
92/101 STATUS_HISTORY_MISMATCH drift baseline is flat vs recorded (known state).

- **D-21** (`_REGISTER.md:45`) remains `NOT_PREPARED (held)`, but its named prerequisite
  D-27 is RULED ("prerequisite to `D-21` preparation", `_REGISTER.md:51`) and
  `docs/PLAN.md:84` lists D-21 preparation as open Phase E/R5 work. **Prep may begin;
  the hold on adoption stands.**
- DEC-042 design/spec prep lane is open (three items, §1.6 above).
- Piping DEL-10-03 result schemas are unpublished as standalone files; publishing them
  is lawful piping-loop deliverable work (the profile fence binds bridge/agent writes,
  not piping's own governed lane over `core/**`/`schemas/**`).

## 4. Shared gates

Live binding (L2–L3) gated ×4 (`open_pipe_stress.yaml:143`):

| Gate | State | Owner lane |
|---|---|---|
| tier-0 adoption | **cleared** (profile ADOPTED, D-T0-06) | — |
| app-dev F3 | gated; D-T0-08 sequence (source types → MCP tools, each its own PROPOSAL, only after a proven L2) | app-dev, after D-APP-46 → extraction → L2 |
| piping D-21 | held; prep now permitted (D-27 cleared) | piping SCOPE_CHANGE packet |
| DEC-041 automation | unmet; needs consumable package | app-dev D-APP-46 → extraction |

Plus: root `docs/CONTRACT.md` (promoted K-DOMAIN family) DRAFT pending ratification;
profile result-schema TBDs ×4 (the FM-04 "genuine gap"); headless CLI entrypoint
un-sanctioned/un-built.

## 5. Lawful now (no live binding opened)

- **app-dev:** DEL-10-03/DEL-10-01 doc-only refinement — close/annotate result-schema
  TBDs by cross-referencing piping `operation_applier`/`rule_check_runner` Rust shapes
  per FM-04:57.
- **piping:** D-21 packet preparation; the three DEC-042 design/spec items; append the
  owner-ruled D-28 DEC entry to §12; ordinary Phase E/R5 work; publish DEL-10-03 result
  schemas (piping-loop lane).
- **tier-0 control root:** writes only under `_DomainEngines/proposals/open_pipe_stress/**`
  and `_DomainEngines/bridge/**`.
- **harness:** brief → adopt → checks cycle built and idle; no briefs adopted to date.

## 6. First recommended bounded tranche

App-dev DEL-10-03 result-schema tranche (doc-only, no fence crossing), governed by a
harness CANDIDATE brief:

```
python3 tools/practitioner_harness/harness.py brief --project app-dev --deliverable DEL-10-03
```

Adoption is the owner's act; the generated brief's `## adoption` section carries the
steps (D-GOV-04 / K-AUTH-2).

## 7. Evidence run (2026-07-02, all at HEAD 565cc2b74)

- `harness.py status` app-dev / piping / --domain-engines: findings none; profile
  ADOPTED/VALID; 9 RULED tier-0 register rows.
- `harness.py drift --all`: 92/154, all chirality-piping, flat vs baseline.
- `harness.py self-check`: exit 0; REVIEW pinned at STALE_RULING_ANNOTATION=2,
  TITLE_CONTRADICTS_RULING=1, RULING_SHA_TBD=0, STALE_DRAFT_DIRECTIVE=1,
  DRAFT_BASIS_RULED_CLOSED=7 (INFO), 19-file GEN-8 abs-path baseline. The three
  owner-retained fixtures (governance register item 3) verified alive; they are test
  material, never to be cleaned.
- `python3 -m pytest tools/practitioner_harness -q`: 235 passed (built primary checkout).
- Multi-agent verification sweep: 4 readers + 3 verifiers + completeness critic;
  ~40 claims re-checked against the live tree; zero refuted.
