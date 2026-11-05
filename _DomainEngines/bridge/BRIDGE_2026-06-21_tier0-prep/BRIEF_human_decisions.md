# BRIEF — Tier-0 Bridge: Human-Only Decisions (framed + recommended; never ruled)

Each decision: the decision, why it is the owner's, verified facts (`file:line`), live options, my recommendation + rationale, what it unblocks/forecloses. **Agents propose; the owner decides.** Per-decision records with `HumanRuling: TBD` are in `../../_DECISIONS/`.

> APEGA ceiling (absolute, all output): no professional / code-compliance / certification / sealing / ready-for-construction / EOR claim. "Validation passed" is **necessary, not sufficient**; a green check guards STRUCTURE and refuses to invent values, but is SILENT on engineering correctness, premise completeness, and code-compliance.

> **STATUS — all 8 decisions RULED 2026-06-21** (canonical: `../../_DECISIONS/_REGISTER.md` + `../../RULINGS_PUBLISHED.md`). The recommendations below were the framing the owner ruled on. **D-T0-04 was ruled OPEN RESIDENCY** — the "L3 may be unreachable / hold to the Anthropic loopback" framing in its section below is **SUPERSEDED**; residency no longer blocks L3 (the 4 live-build conditions still gate it).

---

## D-T0-01 — Precedence of the domain-engine contract

- **Why yours:** choosing the canonical governance authoring is a Type-0/maintainer decision; neither project loop may pre-rule it.
- **Facts:** Two-layer rule — `docs/PLAN.md:17`, `docs/CONTRACT.md:9` (working roots extend but MUST NOT weaken), K-AGENTS-1 `docs/CONTRACT.md:123`. `AGENT_DOMAIN_ENGINE.md` is **absent** from DEL-10-01/03 `_REFERENCES.md` (root cause of drift). Root `docs/CONTRACT.md` has **no K-DOMAIN**; app-dev `docs/CONTRACT.md:131-138` has K-DOMAIN-1..4; app-dev `docs/TYPES.md:499-545` has the §11 contract.
- **Options:** (a) framework-root persona canonical; (b) app-dev `TYPES §11`/PKG-10 canonical; (c) co-equal.
- **Counter-position (recorded per persona `:76`):** under the two-layer rule (`docs/CONTRACT.md:9`) a working root *may* extend framework invariants, so app-dev's K-DOMAIN-1..4 (`projects/chirality-app-dev/docs/CONTRACT.md:131-138`) are already lawfully authoritative *within the app-dev working root*. A defensible alternative is therefore "no promotion needed — leave the contract working-root-local." I recommend against it because the contract governs **all** future domain engines (structural, load-flow, cost, scheduling), not just app-dev; an all-engine invariant belongs at framework altitude. So choose explicitly: does promotion (FM-02) **establish new framework policy** that app-dev then conforms to, or **ratify/elevate** app-dev's existing local invariants? I recommend the former (framework policy); either reading keeps app-dev's IDs stable and citing the root family.
- **Recommendation:** **(a), reconciled as a two-way merge that lands at root** (see CONTRACT_DIRECTION §1).
- **SHA-pin sequencing (resolves the citation prerequisite):** after you rule, and after FM-01..04 are applied, the DOMAIN_ENGINE authors `_REFERENCES.md` updates pinning the *ruled* SHA of `agents/AGENT_DOMAIN_ENGINE.md` into app-dev DEL-10-01/03 (and the piping working root where it cites the persona). Tier-0's own citations of the persona in this package are already lawful (tier-0 authors at the framework root); the `_REFERENCES.md` pin is the prerequisite for the **app-dev-side** conformance work, not for this package.
- **Unblocks:** PKG-10 re-draft against a single canon; K-DOMAIN promotion (FM-02). **Forecloses:** independent drift between the two corpora.

## D-T0-02 — `ProfileStatus` `INVALID` / `UNKNOWN`

- **Why yours:** it edits the canonical persona enum (framework maintenance).
- **Facts:** `UNKNOWN` at `AGENT_DOMAIN_ENGINE.md:197`; `INVALID` at `:657` and `:378` (prose); free field at `:830`. `docs/TYPES.md` §10 defines *Gap* and a resolved negative as distinct epistemic primitives — but does **not** prescribe any profile-status enum mapping.
- **Options:** (a) keep both (7 tokens); (b) `INVALID` only (app-dev default); (c) `UNKNOWN` only.
- **Recommendation:** **(a)** — `NONE|DRAFT|VALIDATED|ADOPTED|STALE|INVALID|UNKNOWN`. **Interpretation (this proposal's, not a citation):** map `UNKNOWN`≈Gap (not yet determined at intake) and `INVALID`≈resolved-negative (malformed). The Gap-vs-resolved-negative distinction is real in the source ontology; the *enum mapping* is the working rationale offered for your ruling, not something TYPES.md already defines. Collapsing the two tokens would erase a distinction the ontology motivates. *I explicitly disagree with app-dev's "INVALID wins."* See FM-01 for the exact diff.
- **Unblocks:** clean ProfileStatus semantics in the profile + Handoff State. **Forecloses:** ambiguity at intake vs validation.

## D-T0-03 — `INTEGRATION_LEVEL` target + staging

- **Why yours:** sets how far automation may go; consequential, irreversible at the top.
- **Facts:** ladder `AGENT_DOMAIN_ENGINE.md:162-172`; today L0. Risk-classing not implemented (engine has no `risk_class`).
- **Options:** (a) L3 destination, reached per-operation; (b) cap at L2; (c) L1 read-only only.
- **Recommendation:** **(a)** with risk-graded staging: L0→L1 (read) → L2 (validated-kernel headless runs) → L3 **per operation risk class, not wholesale**; **L4 future-only**. Subordinate to your ruling. Rationale: piping §6.6 + the engine-checkable/engine-silent axis.
- **Unblocks:** the staged build plan. **Forecloses:** a single undifferentiated "proposal" bucket that mis-sets trust.

## D-T0-04 — Data-residency for live binding (determines whether L3 is reachable at all)

- **Why yours:** trades private-data exposure against capability; a public-welfare/IP risk decision.
- **Facts:** piping no-required-network `docs/SPEC.md:376-381`, OPS-K-PRIV-1 `docs/CONTRACT.md:41`; app-dev fence **F1** bars provider/network beyond Anthropic `D-APP-39_RULING_2026-06-20.md:23`. An L3 worker must see the **private model + Class-B inputs** (allowables, SIFs, design basis) to be useful.
- **Options (frame, do not choose):** local/on-prem inference · redaction · per-session consent · stay on the Anthropic key-aware loopback only.
- **Recommendation:** **none** — this is yours. Flag: until ruled, **L3 may be unreachable**; hold to the existing Anthropic loopback (`PLAN.md:351`).
- **DEFAULT (if deferred — gate-safe):** remain on the Anthropic key-aware loopback; L3 does **not** advance; status stays `MANUAL_BRIDGE` (L0). No private-data egress occurs absent an explicit ruling.
- **Unblocks/forecloses:** gates whether L3 exists at all.

## D-T0-05 — Four-gate sequence

- **Why yours:** confirms the gate ordering the whole build runs on.
- **Facts:** maps onto PROTOCOL Fn 1–8 / Gates 1–5 (no parallel scheme).
- **Recommendation:** confirm the sequence in PLAN_cross_tier §Gates.
- **Unblocks:** lawful sequencing of every later step.

## D-T0-06 — Profile adoption lifecycle (`DRAFT→VALIDATED→ADOPTED`) + sub-gates

- **Why yours:** adoption, protected-write policy, mutating-tool calls, proposal application, external-prover interpretation, and reliance are all human gates.
- **Facts:** persona Gates 2–5; QA contract. `VALIDATED` needs a deterministic validator (not built).
- **Recommendation:** adopt the persona cadence; bind `VALIDATED` to a **TOOLMAKER** profile-schema validator (requirement brief, not inline).
- **Unblocks:** moving the profile off DRAFT. **Forecloses:** "adopted" claims without a validator.

## D-T0-07 — Contract versioning / pinning + DEC-041 confirmation

- **Why yours:** cross-repo version governance is a maintainer decision; DEC-041's status needs your confirmation.
- **Facts:** `CLAUDE_AGENT_SDK_PACKAGE_VERSION='0.3.150'` (`sdk-version.ts`); `HARNESS_TOOL_REGISTRY_VERSION` (`tool-descriptor.ts:13`). **DEC-041 EXISTS** at piping `SOFTWARE_DECOMP.md:611` (refutes app-dev's "not found").
- **Options:** (a) tier-0-owned scheme that *references* both app-dev versions; (b) extend `CLAUDE_AGENT_SDK_PACKAGE_VERSION`; (c) extend `HARNESS_TOOL_REGISTRY_VERSION`.
- **Recommendation:** **(a)** — neither repo's version should own the cross-repo contract; pin a tier-0 flow-A contract-package version that references both. Confirm DEC-041 as decision-of-record and cross-reference it into app-dev (it is written, just invisible from app-dev's tree).
- **Unblocks:** app-dev open-Q5; deterministic package pull (DEC-041 automation condition). **Forecloses:** import-graph-derived (decision-unbacked) boundaries.

## D-T0-08 (sub-decision) — Fence-3 opening sequence

- **Why yours:** opening fence F3 authorizes source-type implementation and domain MCP tooling — consequential R7 scope.
- **Facts:** F3 = "R7 domain-engine impl; PKG-10 stays future-boundary/doc-only" (`D-APP-39_RULING_2026-06-20.md:26`). Both (a) source types and (b) domain MCP tools (e.g. `piping_propose_operation`) are currently doc-only and GATED.
- **Options:** (a) sequential — source types first, then MCP tools (each its own PROPOSAL packet); (b) parallel; (c) keep both held until L2 is proven.
- **Recommendation:** (a) sequential, gated behind D-T0-01 (single canon) and a proven L2 — source types before MCP tools, since the tool surface depends on the type contract. Full record: `../../_DECISIONS/D-T0-08_fence3_sequence.md`.
- **Unblocks:** the R7 build lane. **Forecloses:** standing up MCP tools against an unsettled type contract.
