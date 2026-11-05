# OD7-G3 R-A Current-Basis Application Refresh — Run Summary

## Outcome

- Basis: `7b0be4d8772a16e5a4774a17988479587d00acca`
- Closure: `CLOSED_FOR_EXACT_APPLICATION_PLANNING_ONLY`
- Next gate: `OD7-G3-R-A-APPLICATION`
- Validation: `PASS` — 80 checks, 0 failures
- Governed repository writes: none
- P-A work: none

## Accepted identities preserved

- Accepted selected-candidate set:
  `79ce291ec7ec5247543b05ea19078e2e06be7a5f99be0fae91363159e8198bc1`
- Accepted R-A semantic candidate:
  `db7cf8ee6b5ca4e52f65a0aaa37073900d2b22135ba67a2829abdf1aa9166260`
- Accepted rebuilt planning package:
  `7940a9bd8f26497c8e3050b8a31cf6d89c09dbd2934c8e8ead04f1b016ab14d2`
- Accepted rebuilt R-A tranche:
  `37ef01978f1d4ea022870414965cf737e5fcbd4d3e48f377a1cf3083affa7457`

## Refreshed candidate identities

- Application packet:
  `67c5af9b736798b3cd22cd3a851b0c98d0192874931f53524c1119564c99ad40`
- Decision-record candidate:
  `82b7aae2d9ab101b841cb666eeb65da05f85b05cbb16278f7a3c0617ad460c23`
- Candidate-set manifest:
  `2ac9d01be2bd2c36f03d67e4feeb5a47d2860d9e08eccf4d3cb46a05f4fd199c`
- Validation result:
  `7fd8bccf279c189ed2f3d46bdce4de04af1f435117328ce172e501ef1270ad4a`

## Basis refresh proof

The prior accepted basis
`553f62672353e782fff6708f9a11ecc7d972c146` is an ancestor of the current
basis. The Tier-0 register, domain-engine index, D-T0-24 record, D-T0-23
record, and bridge receipts are byte-identical across both bases. D-T0-24's
PublicationSHA and EffectiveSHA are ancestors of current main and its register
row remains current.

## Gate-specific reconciliation

The accepted rebuilt application packet omitted a receipt from its surface
list while its accepted execution-time scan required one to be allocated.
This refreshed gate resolves that mismatch openly by including next-free
bridge Receipt 29 as the fifth exact application surface. Approval or rejection
of that addition belongs to the owner gate; it has not been applied.
