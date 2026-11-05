# OP mirror — D-APP-52 bridge rehearsal proposals (IPR-0001..0002, batch form disclosed)

> Non-authoritative mirror of the proposal CSVs and reports captured in
> `_DomainEngines/pec/PEC_2026-07-06_BRIDGE-evidence-01/` (D-T0-13; brief §7). Scratch
> basis only; synthetic data; the scratch DB was deleted after capture.

## IPR-0001 — mdl, applied after the ruled staleness-recovery loop

- Source CSV: `inputs/mdl-syn-v1.csv` (sha256 `b53971bfaa3cffc470c0bcf6c3a8543bd7b802c9d88ffc4fbfeaf9c0994fcc30`), 3 synthetic MDL rows.
- Path: propose (agent tool) → validate → demo-cast accept → owner screen act →
  demo-cast apply `force: false` → **409 STALE_PROPOSAL** → tool refresh
  (acceptance voided) → validate → demo-cast re-accept → demo-cast apply
  `force: false` → applied.
- Dry-run and apply reports: verbatim in artifacts `01`, `06b`, `08b`.

```json
{
  "dryRun": {
    "contract": "mdl",
    "accepted": 3,
    "updated": 0,
    "conflicts": [],
    "rejected": [],
    "intakeCreated": 0
  },
  "applyReport": {
    "contract": "mdl",
    "accepted": 3,
    "updated": 0,
    "conflicts": [],
    "rejected": [],
    "intakeCreated": 0
  }
}
```

## IPR-0002 — mdl, ready_for_review (taxonomy exercise only; never accepted)

- Same synthetic CSV content (sha256 `b53971bfaa3cffc470c0bcf6c3a8543bd7b802c9d88ffc4fbfeaf9c0994fcc30`); used to capture the 409
  version-conflict taxonomy (artifact `09c2`); left un-accepted by design.

```json
{
  "dryRun": {
    "contract": "mdl",
    "accepted": 0,
    "updated": 3,
    "conflicts": [],
    "rejected": [],
    "intakeCreated": 0
  }
}
```
