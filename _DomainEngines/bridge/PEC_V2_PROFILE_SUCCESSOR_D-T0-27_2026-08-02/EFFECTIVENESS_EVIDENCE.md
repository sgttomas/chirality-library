# D-T0-27 / D-T0-28 / D-T0-29 effectiveness evidence

**State:** `EFFECTIVE_IDENTITY_PROVEN / CLOSEOUT_RECORD_READY_FOR_CHANGE`

| Identity | Git SHA |
|---|---|
| Approved publication source | `0e47c218c26830a4efeb29eb2d2f3ea99142b987` |
| PR #459 effective merge | `d9dc65804a0719fdf869af1ef60d53dc8cb0a895` |
| Current descendant basis | `556ae59a34ac2f06ef924d367843a72ea00d1f37` |

The effective merge's second parent is the exact approved publication source.
Current main descends from the effective merge. The later PR #461 changes only
`projects/chirality-app-dev/**`; no D-T0-27/28/29 application surface changed
between the publication source and this closeout basis.

## Exact live identities

| Surface | SHA-256 |
|---|---|
| PEC profile | `be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d` |
| Portable PEC validation | `54bd06c61db9c57597a5c02e242c124f3190f7699d47c9caaadca00b899c6d6c` |
| Live-baseline test | `7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638` |
| D-T0-28 patch evidence | `db807bef647db3ef6cd7f4208e5bb5ac5e8ee2775b6a8a19eaeb70434476a499` |
| Root `.gitattributes` | `c0d9e5b7e3bbca1f41087959d6095e75d578fef172123050da7145f52fb9d89f` |
| PEC project check registry | `46f8495444de922d5f85bd71ee473d8ff980fac0b8c30392d7ddf76fee4fff82` |
| PEC project manifest | `7e31d03d80535c2a2f70d6e5657d7136bbd69cc7da2b331a4ed08b0fa133dce2` |

## Verification

- ancestry and exact second-parent identity: PASS;
- publication-source-to-current-main relevant-path diff: empty;
- D-T0-27, D-T0-28, and D-T0-29 application manifests on merged bytes:
  PASS;
- targeted practitioner-harness evidence: 18 passed;
- profile-validator evidence: 8 passed;
- bridge-status: exit 0, no findings;
- self-check: exit 0 at `INFO=14`, `NOT_APPLICABLE=1`, `REVIEW=4`,
  `WARN=27`;
- committed PR #459 `coord-check`: exit 0; `INFO=1`, `REVIEW=7`, all seven
  REVIEW rows are pre-existing unresolved-reference observations and create no
  D-T0-27/28/29 identity blocker; and
- `git diff --check`: required after closeout assembly.

## Effect and boundary

D-T0-27 is effective at `ADOPTED / READ_ONLY`. D-T0-28 and D-T0-29 are
applied/effective supporting amendments. This establishes only the governed
profile boundary and satisfies the successor-profile prerequisite. It creates
no profile-mediated invocation by itself and no source, ScopeOfWork, review,
lifecycle, project-workflow, release, professional-reliance, or cross-loop
authority.
