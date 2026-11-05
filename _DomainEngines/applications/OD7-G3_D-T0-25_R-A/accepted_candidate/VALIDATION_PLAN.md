# D-T0-25 / R-A Current-Basis Application Validation

1. Reproduce accepted rebuilt package artifact
   `7940a9bd8f26497c8e3050b8a31cf6d89c09dbd2934c8e8ead04f1b016ab14d2`
   and R-A tranche
   `37ef01978f1d4ea022870414965cf737e5fcbd4d3e48f377a1cf3083affa7457`.
2. Require current `origin/main` exactly
   `7b0be4d8772a16e5a4774a17988479587d00acca`.
3. Require D-T0-24 `RULED_EFFECTIVE` and reproduce every preimage in
   `PREIMAGE_MANIFEST.csv`.
4. Require D-T0-25 and its archive absent; require D-T0-26/P-A surfaces
   absent and excluded.
5. Require D-T0-25 next free and bridge Receipt 29 next free.
6. Reproduce accepted R-A gate identity
   `db7cf8ee6b5ca4e52f65a0aaa37073900d2b22135ba67a2829abdf1aa9166260`.
7. Verify candidate register adds exactly one D-T0-25 row and changes no
   other register byte.
8. Verify the domain-engine index changes only the accepted
   `Shared runtime convergence` paragraph.
9. Validate all source-anchor mappings and preserve `ACCEPTED_INPUT.md`
   byte-for-byte.
10. Require exactly five application surfaces, including Receipt 29 and
    excluding every P-A/profile surface.
11. Require candidate-package hash verification, path anchors, whitespace,
    and an independent read-only adversarial backcheck.
12. If approved, transcribe the owner ruling verbatim, apply only the five
    enumerated surfaces, generate applied-byte manifests, validate, and return
    Git closeout separately.
