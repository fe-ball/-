# MACHINE INTEGRITY AUDIT — V13

Status: **PASS**.

- Expected total files after manifest/checksum creation: **896**
- Expected SHA-256 manifest entries: **894**
- Manifest exclusions: exactly `FULL-PACKAGE-MANIFEST-SHA256-V13.tsv` and `SHA256SUMS-V13.txt`
- New V13 helicopter current files: **8**
- New rotorcraft quarantine files: **2**
- Combat clock advanced: **NO**

Structural checks:
- V12 fixed-wing current tree is retained.
- New `80-CURRENT-2026-09-08-HELICOPTER-CLOSE/` has highest prewar helicopter authority.
- H1 1939 inventory = 2 development airframes; ordinary OOB = 0.
- H2 1941YE inventory = 4 development airframes; ordinary OOB = 0.
- H3 1941YE flight airframes = 0.
- Kayaba independence/no-forced-joint-design guard is explicit.
- Old rotorcraft comparator is copied into `92-PROVENANCE-QUARANTINED-ROTORCRAFT-RESEARCH-V13/` and is non-current.
- No V13 file advances China, Nomonhan or 1940 combat clocks.

Final verification: **zero missing files, zero size mismatches, zero SHA-256 mismatches**.
