# MACHINE INTEGRITY AUDIT — V11

Status: **PASS**.

- Total files: **858**
- SHA-256 manifest entries: **856**
- Manifest exclusions: exactly `FULL-PACKAGE-MANIFEST-SHA256-V11.tsv` and `SHA256SUMS-V11.txt`
- Missing manifest targets: **0**
- Hash/size mismatches: **0**
- Quarantined surfaced aircraft-source files: **11**
- Combat clock advanced: **NO**

Structural checks:
- V10 tree retained; previous moving `00-START-HERE-CURRENT.md` preserved as `00-START-HERE-2026-09-07-FULL-V10.md` before V11 pointer replacement.
- New V11 aircraft-development/current directory exists.
- Old aircraft branch sources live only in a dedicated `91-...QUARANTINED...` directory with explicit no-current/no-auto-import controls.
- Aircraft master, derivation matrix, designation-gate ledger, industrial closeout and helicopter-next-topic handoff are present.

Final manifest verification is performed again after this audit file is written; a valid distributed package must show zero missing/mismatched files.
