# P5 — Replace hard-coded SOFTWARE_DECOMP section numbers with heading-text binding (request item 6 / OI-A)

**Disposition:** ADOPTED-PROPOSED (AMENDED — escalated from the request's
"lower priority")
**Basis:** VERIFIED by reading both agent tables and both live SOFTWARE_DECOMP
documents in this run.

## 1. Why this is not "lower priority"

The request carries OI-A as a fragility observation. It is not fragile — it is
**already broken**. Across the two agent files there are **five** `§`-bearing
SOFTWARE cells, carrying **four distinct citations**, and every one resolves to
the wrong section today. The `Change Log §8` citation exists only in
`AGENT_SCOPE_CHANGE.md`; `AGENT_AUDIT_DECOMP.md` has no Change Register row.

| Cited as | Cited in | What `§N` actually is in `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` | Drifted? |
|---|---|---|---|
| Packages **§3** | `AGENT_SCOPE_CHANGE.md:192`, `AGENT_AUDIT_DECOMP.md:114` | `## 3. Objectives (Phase 3)` | **YES** |
| Deliverables **§4** | `AGENT_SCOPE_CHANGE.md:193`, `AGENT_AUDIT_DECOMP.md:115` | `## 4. Packages (Phase 4)` | **YES** |
| Scope Ledger **§5** | `AGENT_SCOPE_CHANGE.md:190,191`, `AGENT_AUDIT_DECOMP.md:112,113` | `## 5. Deliverables (Phase 5)` | **YES** |
| Change Log **§8** | `AGENT_SCOPE_CHANGE.md:189` **only** | `## 8. Context Budget QA (Phase 6)` — and **no `Change Log` heading exists in this document at all** | **YES, worse** |

Three are a uniform off-by-one. The fourth is a dangling reference: the
semantic "Change Register" is split across `## 11. Decision Log` (line 615,
carrying the substantive rows — `DL-17` at line 635 records SCA-002) and
`## 12. Revision History (Phase 7 change summary)` (line 637, carrying the
revision rows — `| 1.2 | SCA-002 | … |` at line 651).

An agent following the table lands on Objectives when it wants Packages, on
Packages when it wants Deliverables, and nowhere at all when it wants the
change register.

## 2. Why heading-text binding is forced, not merely preferred

**THREE** live SOFTWARE decomposition documents in this repo, with four
mutually incompatible numbering schemes between them and the protocol:

| Semantic section | Agent tables say | `pec` | `chirality-app-dev` | `chirality-piping` |
|---|---|---|---|---|
| Objectives | via ledger | §3 | §6 | §5 |
| Packages | §3 | §4 | §7 | §6 |
| Deliverables | §4 | §5 | §8 | §7 |
| Scope Ledger | §5 | §6 | §9 | §9 (`Scope ledger summary`) |
| Change Register | §8 | §11 + §12 | §12 | §12 |

Documents:
- `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`
- `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md`

**No fixed number can be correct.** Renumbering the tables to fit `pec` breaks
the other two. Only heading-text binding survives all three.

The correct rule is already written in the repo — `AGENT_SCOPE_CHANGE.md:189`,
DOMAIN column: `` `Decision Log / Change Log` (heading match) ``. That exact
string matches the app-dev document's `## 12. Decision Log / Change Log`
verbatim. The DOMAIN cell's approach is the proven pattern; this proposal
extends it across the table — **with an explicit normalization spec**, because
naive equality does not work (see §3).

Note also `AGENT_AUDIT_DECOMP.md:108` already *claims* semantic binding — "All
protocol steps reference sections by **semantic name**; resolve to the correct
location using this table" — and then the table immediately hard-codes numbers.
The prose and the table contradict each other.

## 3. The normalization spec (this is the load-bearing part)

A rule that strips only a leading `N.` and then demands equality resolves
**1 of 4** bindings against the live `pec` document — its headings carry
`(Phase N)` suffixes — and would halt on the rest. That is strictly worse than
the status quo. The spec must be stated explicitly:

**To resolve a semantic section to a live heading:**

1. Collect every `##` heading in the document.
2. Normalize each: strip the `## ` marker; strip a leading section number of
   the form `N.` or `NA.` (digits, optional letter suffix, period, trailing
   whitespace — e.g. `10A.`); trim; case-fold.
3. Normalize the target text the same way (case-fold, trim).
4. Match in rank order and stop at the first rank that yields a hit:
   **exact**, then **prefix**, then **substring**.
5. **Tie-break:** if a rank yields more than one hit, take the one that appears
   **earliest in the document** and report the ambiguity alongside the result.
6. **Halt and report only when a rank-4 search yields zero hits** after
   normalization. Never resolve by position.

For the Change Register, resolve an **ordered alternation** — `Decision Log`,
then `Revision History`, then `Change Log` — and read **every** heading that
resolves, not just the first. Halt only if none of the three resolve.

### Verification against all three live documents

Executed against the three documents above; every non-alternation binding
resolves, and the only `NONE` results are the alternation members that
legitimately do not exist in that document:

```
=== pec (14 '##' headings) ===
  Scope Ledger       -> exact     L509   '6. Scope Ledger'
  Objectives         -> prefix    L310   '3. Objectives (Phase 3)'
  Packages           -> prefix    L349   '4. Packages (Phase 4)'
  Deliverables       -> prefix    L375   '5. Deliverables (Phase 5)'
  Decision Log       -> exact     L615   '11. Decision Log'
  Revision History   -> prefix    L637   '12. Revision History (Phase 7 change summary)'
  Change Log         -> NONE (halt and report)

=== app-dev (15 '##' headings) ===
  Scope Ledger       -> exact     L381   '9. Scope Ledger'
  Objectives         -> exact     L242   '6. Objectives'
  Packages           -> exact     L259   '7. Packages'
  Deliverables       -> exact     L276   '8. Deliverables'
  Decision Log       -> prefix    L564   '12. Decision Log / Change Log'
  Revision History   -> NONE (halt and report)
  Change Log         -> substring L564   '12. Decision Log / Change Log'

=== piping (13 '##' headings) ===
  Scope Ledger       -> prefix    L455   '9. Scope ledger summary'
  Objectives         -> exact     L180   '5. Objectives'
  Packages           -> exact     L204   '6. Packages'
  Deliverables       -> exact     L228   '7. Deliverables'
  Decision Log       -> exact     L578   '12. Decision log'
  Revision History   -> NONE (halt and report)
  Change Log         -> NONE (halt and report)
```

Reading the alternation as specified: `pec` → Decision Log + Revision History;
`app-dev` → the single merged `Decision Log / Change Log`; `piping` →
Decision log. All three resolve. No binding halts.

Three cases prove individual clauses of the spec and would each break a
simpler rule: `piping`'s `Scope ledger summary` (needs prefix, and case-fold —
lowercase `ledger`), `pec`'s `(Phase N)` suffixes (need prefix), and
app-dev's `Decision Log / Change Log` (needs substring for the `Change Log`
target, and is why the alternation must read all hits rather than the first).

## 4. Proposed exact-text changes

### 4a. `agents/AGENT_AUDIT_DECOMP.md` — Variant Section Binding, lines 110–115

REPLACE:

```
| Semantic section | PROJECT_DECOMP | SOFTWARE_DECOMP | DOMAIN_DECOMP |
|------------------|----------------|-----------------|---------------|
| Ledger | §5 (Scope Ledger) | §5 (Scope Ledger) | §2 (Domain Ledger) |
| Objectives | §6 (dedicated section) | (via Scope Ledger §5 `ObjectiveID(s)` column) | Objectives section (dedicated) |
| Partitions (Packages / Categories) | §7 | §3 | Categories section |
| Production Units (Deliverables / Knowledge Types) | §8 | §4 | Knowledge Types section |
```

WITH:

```
Bind by heading text, never by section number. Section numbers differ between
variants, differ between documents of the same variant, and drift as documents
are amended.

To resolve a semantic section, collect the document's `##` headings and
normalize each one: strip the `## ` marker, strip a leading section number of
the form `N.` or `NA.` (digits, optional letter suffix, period, trailing
space — e.g. `10A.`), trim, and case-fold. Normalize the target text the same
way. Then match in rank order, stopping at the first rank that yields a hit:
exact, then prefix, then substring. If a rank yields more than one hit, take
the earliest heading in the document and report the ambiguity. Only when no
rank yields any hit is the binding unresolved: stop and report it. Never
resolve by position.

| Semantic section | PROJECT_DECOMP heading | SOFTWARE_DECOMP heading | DOMAIN_DECOMP heading |
|------------------|------------------------|-------------------------|-----------------------|
| Ledger | `Scope Ledger` | `Scope Ledger` | `Domain Ledger` |
| Objectives | `Objectives` | `Objectives`, or the `ObjectiveID(s)` column of `Scope Ledger` where the variant embeds mapping in the ledger | `Objectives` |
| Partitions (Packages / Categories) | `Packages` | `Packages` | `Categories` |
| Production Units (Deliverables / Knowledge Types) | `Deliverables` | `Deliverables` | `Knowledge Types` |
```

Note the Objectives row is amended in substance, not just in form: the current
SOFTWARE cell says objectives come *only* via the ledger column, but the live
`pec` document has a dedicated `## 3. Objectives (Phase 3)` heading. Both
routes exist; the replacement names both.

### 4b. `agents/AGENT_SCOPE_CHANGE.md` — Variant Section Binding, lines 189–193

REPLACE:

```
| Change Register | `Change Log` §3 | `Change Log` §8 | `Decision Log / Change Log` (heading match) | Bind by heading text when section numbers are absent |
| Unit Ledger | `Scope Ledger` §5 | `Scope Ledger` §5 | `Domain Ledger` | Authoritative row-level mapping table |
| Objectives | `Objectives` §6 | via `Scope Ledger` §5 | — | `DOMAIN_DECOMP` does not have an Objectives layer; `SOFTWARE` embeds objective mapping in the ledger |
| Primary Partitions | `Packages` §7 | `Packages` §3 | `Categories` | Flat partition primitive |
| Secondary Entities | `Deliverables` §8 | `Deliverables` §4 | `Knowledge Types` | Parented to the primary partition |
```

WITH:

```
| Change Register | `Change Log` | `Decision Log` and/or `Revision History` | `Decision Log / Change Log` | Bind by heading text, never by number. `SOFTWARE_DECOMP` may split this across two headings; read both when both exist |
| Unit Ledger | `Scope Ledger` | `Scope Ledger` | `Domain Ledger` | Authoritative row-level mapping table |
| Objectives | `Objectives` | `Objectives` where present, otherwise the `ObjectiveID(s)` column of `Scope Ledger` | — | `DOMAIN_DECOMP` does not have an Objectives layer |
| Primary Partitions | `Packages` | `Packages` | `Categories` | Flat partition primitive |
| Secondary Entities | `Deliverables` | `Deliverables` | `Knowledge Types` | Parented to the primary partition |
```

And REPLACE line 185's lead-in to make the rule normative:

```
All protocol steps reference sections by **semantic name** and then bind those semantics to the originating decomposition variant.
```

WITH:

```
All protocol steps reference sections by **semantic name** and then bind those semantics to the originating decomposition variant **by heading text, never by section number**, using the normalization and rank-order matching defined in `AGENT_AUDIT_DECOMP.md`'s Variant Section Binding block. If no rank yields a hit, stop and report an unresolved binding rather than resolving by position.
```

The `Change Register` row is the one that changes meaning, not just form: it
now names two possible SOFTWARE headings, because the `pec` document splits the
change register across `Decision Log` and `Revision History` while the app-dev
document merges them into one `Decision Log / Change Log` and `piping` has only
`Decision log`. A single-heading binding cannot cover all three.

## 5. The live documents' own `§` references are CORRECT — do not "repair" them

An earlier draft of this proposal claimed the `pec` document's internal
cross-references carried the same off-by-one and needed a PEC-loop repair.
**That claim was wrong and is withdrawn.** Verified against the live section
map:

| Cite | Context | Resolves to | Correct? |
|---|---|---|---|
| L536 `§3` | "every objective backed … §3" | `## 3. Objectives (Phase 3)` | **YES** |
| L635 `§3` | "§3's parser derivation" | `## 3. Objectives (Phase 3)` | **YES** |
| L635/L651 `§5` | "§5's stale envelope-posture line" | `## 5. Deliverables (Phase 5)` | **YES** |
| L651 `§7` | "§7 metric 31→11" | `## 7. Coverage & Telemetry (Phase 6)` | **YES** |

Every one resolves correctly against its own document's headings.

This inverts the evidential reading. These references are **independent
corroboration that the agent tables are wrong**: the document's authors, working
from the live headings, consistently used the document's real numbering — which
disagrees with the agent tables at every point. They are not a second instance
of the defect; they are the control group.

**No PEC-loop repair is required here, and none should be requested.** Editing
these correct references to match the (wrong) agent tables would introduce the
very defect this proposal removes.

## 6. Compatibility

- Both edits are contract text in agent instruction files. No tools parse these
  tables (VERIFIED: they are read by agents, not code), so there is no caller
  to migrate.
- The change is strictly more permissive at resolution time — anything that
  resolved correctly by number will still resolve by heading text, because
  every cited heading text exists somewhere in each live document (except
  `Change Log` in the `pec` doc, which is exactly the case being fixed).
- Rerun `python3 tools/validation/validate_agent_instructions.py` after the
  change.
- P4 in this packet also edits `AGENT_AUDIT_DECOMP.md`, at lines 424–426 and
  498. Disjoint from this proposal's lines 110–115; the two can land together.
