# MACHINE INTEGRITY AUDIT — V12

Status: **PASS**.

- Total files after manifest/checksum creation: **874**
- SHA-256 manifest entries: **872**
- Manifest exclusions: exactly `FULL-PACKAGE-MANIFEST-SHA256-V12.tsv` and `SHA256SUMS-V12.txt`
- New V12 fixed-wing current files: **7**
- Quarantine directory retained: `91-PROVENANCE-QUARANTINED-AIRCRAFT-RESEARCH-V11/`
- Combat clock advanced: **NO**

Structural checks:
- V11 tree retained and V11 moving start pointer preserved as `00-START-HERE-2026-09-08-FULL-V11.md`.
- New `79-CURRENT-2026-09-08-FIXED-WING-PROCUREMENT-CLOSE/` exists and has highest fixed-wing precedence.
- 1941 procurement and OOB-counting boundaries are explicit.
- Ki-40 naming collision, J2N 1941 zero-order rule, A7M/A8N prime assignments, E6-B prime, and powered-lift limits are represented in V12 guard/control files.
- Rotorcraft remains a separate open branch.
- Old aircraft research remains quarantined and no quarantined file is made current by this package.

Final verification after manifest generation must produce zero missing files, zero size mismatches and zero SHA-256 mismatches.
