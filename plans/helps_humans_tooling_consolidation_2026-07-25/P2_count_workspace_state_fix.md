# P2 — `tools/query/count_workspace_state.sh` (request item 3)

**Disposition:** ADOPTED-PROPOSED
**Basis:** VERIFIED by execution against `projects/pec/execution` in this run.
**New finding:** the request names one defect. There are **two**. The second
(deliverable miscount) is not in the request and was found while confirming the
first.

## 1. Defect A — history-substring state counting (the reported one)

Line 37: `grep -l "$state"` is an unanchored substring match over the **entire**
`_STATUS.md`, including the append-only `## History` section, which records
every prior state name verbatim.

VERIFIED reproduction, `projects/pec/execution`:

| State | Tool reports | Truth (`grep -h '^\*\*Current State:\*\*'`) |
|---|---|---|
| OPEN | **64** | **32** |
| INITIALIZED | 32 | 32 |
| others | 0 | 0 |

The `OPEN` row is inflated by exactly the 32 files whose History still contains
`- 2026-07-25 — State set to OPEN (PREPARATION)`. `INITIALIZED` is correct here
only by coincidence — no PEC deliverable has yet left `INITIALIZED` — which is
why the defect is intermittently invisible and why it survived this long.

## 2. Defect B — deliverable count includes subdirectories (NOT in the request)

Line 28: `find "$EXROOT" -path "*/1_Working/DEL-*" -maxdepth 4 -type d`.

The glob `DEL-*` with `-maxdepth 4` matches the deliverable directory **and**
every directory inside it — in PEC, each `_run_records/` folder.

VERIFIED, `projects/pec/execution`: the tool reports `Deliverables: 96`; the
true count is **64**. The 32 excess are `_run_records` directories created by
the D-PEC-63 wave. `Packages: 11` (line 24) is correct — `-maxdepth 1` bounds it
properly.

This matters more than it looks: every state count is reported against a
denominator that is itself wrong, so "32 of 96" reads as one-third complete when
the truth is one-half.

## 3. Proposed exact-text change

REPLACE lines 27–29:

```
# Count deliverables
del_count=$(find "$EXROOT" -path "*/1_Working/DEL-*" -maxdepth 4 -type d | wc -l | tr -d ' ')
echo "Deliverables: $del_count"
```

WITH:

```
# Count deliverables (the DEL-* directory itself, not its subdirectories)
del_count=$(find "$EXROOT" -mindepth 3 -maxdepth 3 -type d -path "*/1_Working/DEL-*" | wc -l | tr -d ' ')
echo "Deliverables: $del_count"
```

REPLACE lines 36–39:

```
for state in OPEN INITIALIZED SEMANTIC_READY IN_PROGRESS CHECKING ISSUED; do
  count=$(find "$EXROOT" -path "*/1_Working/DEL-*/_STATUS.md" -type f -exec grep -l "$state" {} \; 2>/dev/null | wc -l | tr -d ' ')
  echo "| $state | $count |"
done
```

WITH:

```
# Match the single current-state declaration line only. A whole-file match
# also hits the append-only History section, which names every prior state.
for state in OPEN INITIALIZED SEMANTIC_READY IN_PROGRESS CHECKING ISSUED; do
  count=$(find "$EXROOT" -path "*/1_Working/DEL-*/_STATUS.md" -type f \
    -exec grep -l "^\*\*Current State:\*\* ${state}[[:space:]]*$" {} \; 2>/dev/null | wc -l | tr -d ' ')
  echo "| $state | $count |"
done
```

The anchor `^\*\*Current State:\*\* ` plus the trailing `[[:space:]]*$` is
required in both directions: without the leading anchor, History lines match;
without the trailing anchor, `IN_PROGRESS` would be matched by a hypothetical
`IN_PROGRESS_REVIEW` and, more immediately, nothing distinguishes a state name
that is a prefix of another.

**Verified current-state line format** (line 3 of every `_STATUS.md` inspected
across `pec` and `chirality-app-dev`): `**Current State:** <STATE>`.

## 4. Optional hardening (owner's call, not required)

The loop enumerates six state names and silently drops any state not in that
list. A single pass would be both faster and total:

```
grep -h "^\*\*Current State:\*\*" "$EXROOT"/PKG-*/1_Working/DEL-*/_STATUS.md \
  | sed 's/^\*\*Current State:\*\* //' | sort | uniq -c
```

This is the idiom the PEC loop already adopted as its census replacement
(`PLAN_2026-07-25_pec_phase_2_2_sow_wave.md` line 404). It is **not** proposed
as the fix because it changes the output shape — the tool currently emits a
fixed-order Markdown table that four agent instruction files read. The anchored
loop above preserves that table exactly. If the owner wants totality (unknown
states surfaced rather than dropped), the clean form is to keep the table and
add a trailing "unrecognized states" line.

## 5. Compatibility

**The fix is caller-free.** There are no shell or CI callers. Every reference is
protocol prose that invokes the script by path and reads its table:

- `agents/AGENT_PROJECT_SETUP.md:494`
- `agents/AGENT_EVALUATION_STRUCTURE_AUDIT.md:105`, `:108`
- `agents/AGENT_EVALUATION_REPORT.md:79`
- `agents/AGENT_AUDIT_HYPERGRAPH_CLOSURE.md:237`
- `tools/REGISTRY.md:24` (registry row)

Both proposed edits preserve stdout shape exactly — same lines, same order,
same table. Only the numbers change, from wrong to right.

**Standing workarounds that can be retired after this lands** (ASSERTED-UPSTREAM
— these are PEC-loop instruments and their retirement is the PEC loop's call,
not this packet's): the "never `count_workspace_state.sh` post-transition"
prohibitions recorded in `D-PEC-63`, `D-PEC-64`, the phase-2.2 wave plan, and
the SCA-002 propagation/impact documents.

**Recommended verification after the change** (both are exact expected values
for the current PEC state):

```
bash tools/query/count_workspace_state.sh projects/pec/execution
#   Deliverables: 64
#   | OPEN | 32 | ; | INITIALIZED | 32 | ; all others 0
```

## 6. Not proposed

This tool has no test file. Given two independent counting defects in a
51-line script, a `tools/validation/`-style fixture test would be justified —
but adding a shell-test harness where none exists is a separate design decision
about test conventions for `.sh` tools, and is out of this packet's scope. Noted
as a candidate.
