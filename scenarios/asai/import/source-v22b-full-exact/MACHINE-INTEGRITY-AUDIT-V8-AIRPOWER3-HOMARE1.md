# MACHINE INTEGRITY AUDIT — V8 AIRPOWER3 HOMARE1

## Base
Source package: `ASAI-WORLDLINE-HANDOFF-2026-09-03-FULL-V8-1939AIRPOWER2-STATEFIX1.zip`

The source STATEFIX1 tree was verified against its own `SHA256SUMS-V8.txt` before modification: **387/387 entries OK**.

## Patch scope
AIRPOWER3-HOMARE1 advances technical audit only. It does not advance the combat clock or choose the 1943+ NC/war branch.

### Added technical files
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/11-HOMARE-QUARTERLY-DEVELOPMENT-QUALIFICATION-CANON-V8.md`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/12-HOMARE-QUARTERLY-STATE-LEDGER-V8.tsv`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/13-HA43-PREBRANCH-DEVELOPMENT-AUDIT-V8.md`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/14-PISTON-ENGINE-PREBRANCH-ROLLUP-V8.md`
- `V8-CHANGELOG-1939AIRPOWER3-HOMARE1.md`

### Added integrity files
- `MACHINE-INTEGRITY-AUDIT-V8-AIRPOWER3-HOMARE1.md`
- `MACHINE-INTEGRITY-AUDIT-V8-AIRPOWER3-HOMARE1.json`

### Intentionally updated existing files
- `00-START-HERE-CURRENT.md`
- `PACKAGE-STATE-V8.tsv`
- `PRECEDENCE-2026-09-03-FULL-V8.tsv`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/07-HOMARE-DEVELOPMENT-SERVICE-PERFORMANCE-AUDIT-V8.md`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/08-FIGHTER-POWERPLANT-MATERIAL-INTEGRATION-WORKING-V8.md`
- root V8 inventory/manifest/checksum files, rebuilt after all changes.

## Semantic guard
Preserved:
- old furthest explored branch: post-Nomonhan 1939-09-01;
- current revalidated combat checkpoint: 1939-04-20 24:00;
- combat replay status: `HOLD_FOR_AVIATION_AUDIT`;
- active domain: `PISTON_AVIATION`.

New closure:
- Homare branch-neutral engine development/qualification through 1943Q1;
- early Ha-43 branch-neutral development through 1943Q1;
- post-1943 output, supply, TBO/reliability, procurement and combat effects remain open.

## Expected final counts
- files: 396
- inventory entries: 393 (inventory/manifest/SHA files excluded)
- manifest/checksum entries: 394 (manifest and checksum excluded from their hash set)
