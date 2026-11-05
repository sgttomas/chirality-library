# D-T0-04 — Data-residency for live binding  (RULED 2026-06-21)

**Decision:** May any private model + Class-B inputs (allowables, SIFs, design basis) be exposed to an agent worker for L3 — and under what residency constraints?

**Why the owner's:** trades private-data/IP exposure against capability; a public-welfare/IP-risk call. **This determines whether L3 is reachable at all.**

**Verified facts:** piping no-required-network `docs/SPEC.md:376-381`; OPS-K-PRIV-1 `docs/CONTRACT.md:41`; app-dev fence F1 (provider/network beyond Anthropic) `D-APP-39_RULING_2026-06-20.md:23`. An L3 worker must see the private model to be useful.

**Options to rule (framed, not chosen):** local/on-prem inference · redaction · per-session consent · stay on the Anthropic key-aware loopback only (`PLAN.md:351`).

**Recommendation:** none — this is yours.

**DEFAULT (if deferred — gate-safe):** remain on the Anthropic key-aware loopback; L3 does **not** advance; status stays `MANUAL_BRIDGE` (L0). No private-data egress occurs absent an explicit ruling.

**Unblocks/forecloses:** the existence of L3.

---
**HumanRuling:** **OPEN RESIDENCY (current stance).** The agent harness may see the private model + Class-B inputs; the app does **not** enforce privacy/residency; **any** model provider (local / Anthropic / other) is permitted. **L3 is therefore not residency-blocked.** Owner's words (2026-06-21): "It doesn't concern me that the agent sees the private model, for now. The app shouldn't try to enforce privacy either. Local models or Anthropic models or even other providers could all be used."
**Follow-on `RES-RECONCILE` — RESOLVED 2026-06-21 (published + tier-0-verified):** app-dev fence **F1** reconciled via **`D-APP-44` @ `d83e63b95`** (amended to owner-permitted, default-closed; F2/F3/F4 intact); piping **`OPS-K-PRIV-1`** / SPEC §4.4 / `IP_AND_DATA_BOUNDARY` reconciled via **`DEC-051` @ `9db0eef27`** (provider channel relaxed; `OPS-K-IP-*` + `IP_AND_DATA_BOUNDARY` + telemetry-off preserved). **Net posture (owner-confirmed): keep default-closed** — harness egresses only under explicit owner config; engine adds no independent guard. K-CONFLICT-1 conflict cleared.
**RuledBy:** owner (in-session)   **Ruling SHA:** 6e70b5aace4a3a7c4ebb20490a3bf57bfd912f45 (publication commit, 2026-06-21; backfilled 2026-07-02 per owner ruling)   **Date:** 2026-06-21
