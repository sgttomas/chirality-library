# P-A Accepted-Manifest Line-Ending Correction

**Date:** 2026-07-28
**Reason:** `git diff --cached --check` rejected the accepted
`APPLICATION_MANIFEST.csv` because all 13 lines used CRLF.

## Bounded correction

Only CRLF line endings were normalized to LF in the readable archived copy.
No field, delimiter, ordering, or semantic byte was changed.

- Original SHA-256:
  `eca70cea456f464bf3ddfbd732b6e8fe9d60259fa2701578dbcb9bd0476cf894`
- Normalized SHA-256:
  `1d6b55b256697e93de4c0eb40f084e00bec0ef6ff1949e7372345f06c30a3c76`
- Exact original bytes:
  `accepted_candidate/APPLICATION_MANIFEST.csv.original.base64`

The application validator decodes the Base64 carrier, reproduces the original
SHA-256, verifies that CRLF→LF produces the normalized readable copy, and
verifies the other seven accepted tranche entries directly. The accepted
P-A semantic input, candidate postimages, application packet, and tranche
identity remain unchanged.
