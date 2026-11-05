# D-T0-28 O-A application evidence

**State:** `VALIDATED / READY_FOR_CHANGE / NOT_EFFECTIVE`

**Application basis:**
`23d15899fd0acf5d1d0513f3fe396438375c9e25`

**Owner ruling:** D-T0-28 O-A; complete verbatim owner message is recorded in
`_DomainEngines/_DECISIONS/D-T0-28_pec_v2_profile_live_pin_amendment.md` and
bridge Receipt 34.

## Exact application

| Surface | SHA-256 |
|---|---|
| Test preimage | `80823ee8dea253f91145302f37e618bdf8feb753f032a741d0aa0e4f0df1e70c` |
| Exact patch | `db807bef647db3ef6cd7f4208e5bb5ac5e8ee2775b6a8a19eaeb70434476a499` |
| Test postimage | `7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638` |
| PEC profile | `be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d` |
| Portable PEC validation | `54bd06c61db9c57597a5c02e242c124f3190f7699d47c9caaadca00b899c6d6c` |

Only `tools/practitioner_harness/test_live_baseline.py` changed for D-T0-28
execution. The amendment corrects the two frozen observations named in the
packet and changes no harness production behavior.

## Verification results

- exact preimage and postimage: PASS;
- exact patch applicability: PASS;
- targeted practitioner-harness suite: 18 passed;
- profile-validator suite: 8 passed;
- `bridge-status`: PASS, no findings; PEC observation
  `ADOPTED / Gate 2 adopted / READ_ONLY`;
- `self-check`: exit 0; `INFO=14`, `NOT_APPLICABLE=1`, `REVIEW=4`, `WARN=27`;
- D-T0-28 candidate manifest: 2/2;
- D-T0-27 application manifest: reproduced before final ruling-record refresh
  and regenerated against the final uncommitted application surfaces;
- D-PEC-74 accepted API schema/test/fixture bytes: unchanged;
- `projects/pec/software-workflow.json`: unchanged SHA-256
  `46f8495444de922d5f85bd71ee473d8ff980fac0b8c30392d7ddf76fee4fff82`;
- `projects/pec/chirality.project.json`: unchanged SHA-256
  `7e31d03d80535c2a2f70d6e5657d7136bbd69cc7da2b331a4ed08b0fa133dce2`;
- `git diff --check`: required after final evidence assembly; and
- committed-range `coord-check`: deferred to CHANGE because no commit exists
  in this DOMAIN_ENGINE application worktree.

## Handoff

The D-T0-27/D-T0-28 application is validated and ready for CHANGE. It remains
not effective until exact publication, committed-range checks, and merge
identity. No commit or push is performed by this application.

The owner's DEL-01-06 REVIEW Gate-1 direction belongs to the PEC loop. This
Tier-0 application neither executes nor narrows that direction and touches no
DEL-01-06 review, source, ScopeOfWork, workflow, or lifecycle surface.
