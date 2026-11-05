# FM-01 — `ProfileStatus` enum reconciliation (APPLIED draft; pending approval)

**Target (canonical):** `agents/AGENT_DOMAIN_ENGINE.md`
**Resolves:** D-T0-02. **Gate:** framework-maintenance (human-gated; CHANGE publishes). **Status: APPLIED and PUBLISHED at `77a327727` (committed + pushed to origin/main; owner-directed 2026-06-21).**
**Application record:** Applied by HELPS_HUMANS framework-maintenance pass on 2026-06-22. Applying SHA: `77a327727`. Draft base HEAD observed: `16e723f45813`.
**Recommendation:** keep BOTH `INVALID` and `UNKNOWN` as distinct tokens (7-value enum). Rationale in CONTRACT_DIRECTION §2. **Warrant note:** `docs/TYPES.md` §10 defines *Gap* and a resolved negative as distinct epistemic primitives but does **not** prescribe a profile-status enum mapping; mapping `UNKNOWN`≈Gap and `INVALID`≈resolved-negative is *this proposal's interpretation*, offered for the D-T0-02 ruling — not an existing definition extracted from TYPES.md.

Canonical enum: `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`
- `NONE` no profile exists · `DRAFT` exists, incomplete · `VALIDATED` passes the schema validator · `ADOPTED` human-approved for governed use · `STALE` was adopted, governed inputs changed (mirrors K-VAL-1/K-STALE) · `INVALID` exists but fails schema/conformance (a *determined* negative) · `UNKNOWN` not yet determined at intake (a *Gap*).

---

### Edit 1 — PROTOCOL Fn 1, line 197

```diff
-4. State known profile status: `NONE | DRAFT | VALIDATED | ADOPTED | STALE | UNKNOWN`.
+4. State known profile status: `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`.
```

### Edit 2 — SPEC "Valid Domain Engine Profile", line 378

```diff
-If any required field is missing, the profile status is `DRAFT` or `INVALID`, not `ADOPTED`.
+If any required field is missing, the profile status is `DRAFT` (incomplete-but-well-formed) or
+`INVALID` (present-but-malformed/non-conforming), not `ADOPTED`. Use `UNKNOWN` only at intake before
+the profile has been discovered or scanned; `NONE` when no profile exists.
```

### Edit 3 — Domain Integration Record, line 657

```diff
-| `ProfileStatus` | `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID` |
+| `ProfileStatus` | `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN` |
```

### Edit 4 — Handoff State, line 830 (tighten the free field to the enum)

```diff
-| `ProfileStatus` | Active profile state |
+| `ProfileStatus` | Active profile state — one of `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN` |
```

**Note:** if the owner instead rules app-dev's "INVALID only" default (D-T0-02 option b), Edits 1–4 collapse to the 6-token set and `UNKNOWN` is removed everywhere — but this discards the intake-Gap distinction and is not recommended.
