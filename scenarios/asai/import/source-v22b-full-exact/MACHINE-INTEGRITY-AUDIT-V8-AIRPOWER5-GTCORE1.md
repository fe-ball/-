# MACHINE INTEGRITY AUDIT — V8 AIRPOWER5 GTCORE1

## Source

Source tree: `ASAI-WORLDLINE-HANDOFF-2026-09-03-FULL-V8-1939AIRPOWER4-AIRFRAME1`.

Before AIRPOWER5 edits, source `SHA256SUMS-V8.txt` was rechecked: **402/402 targets OK**.

## Preservation rule

AIRPOWER5 is an overlay. No source file is intentionally deleted. Preserved V7/V6 provenance trees remain intact. Existing V8 files are edited only where explicitly listed below; additions are current overlay/support material.

## Existing files intentionally edited

- `00-START-HERE-CURRENT.md`
- `PACKAGE-STATE-V8.tsv`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/02-GT-E6-E7-CORE-FAMILY-PRODUCTION-CANON-V8.md`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/10-HANDOFF-STATE-MACHINE-CANON-V8.md`

Root V8 inventory/manifest/SHA256 are rebuilt metadata and therefore replaced by design.

## New current files

- `00-START-HERE-2026-09-04-FULL-V8.md`
- `PRECEDENCE-2026-09-04-FULL-V8.tsv`
- `V8-CHANGELOG-1939AIRPOWER5-GTCORE1.md`
- current files 00A, 20, 21, 22, 22A under `50-CURRENT-1939-1941-AIRPOWER-AUDIT/`
- selected GT provenance/calculation support directory under `99-SUPPORT-CURRENT/GT-REBASE-SOURCE-SELECTED/`
- this machine audit MD/JSON pair.

## State invariants checked

- current combat checkpoint remains `1939-04-20 24:00`;
- prior explored `1939-09-01` remains non-current provenance;
- combat replay remains `HOLD_FOR_AVIATION_AUDIT`;
- AIRPOWER3/AIRPOWER4 piston/propeller/airframe closure is retained;
- GTCORE1 does not auto-create procurement/adoption/production/combat history;
- v46 E6-M J/JF installed values are retained unless a specific new physical/accounting error is identified;
- mandatory cheat/capability guard is placed ahead of GT schedule files in current START-HERE and precedence.

## Expected final metadata counts

Final tree expected after this audit and metadata rebuild:

- total files: **429**;
- `PACKAGE-INVENTORY-V8.tsv` data rows: **426** (excludes the three self-referential current metadata files);
- `FULL-PACKAGE-MANIFEST-SHA256-V8.tsv` data rows: **427** (includes rebuilt inventory; excludes itself and SHA list);
- `SHA256SUMS-V8.txt` targets: **427**.

Pre-final packaging verification completed: temporary ZIP unpacked successfully; **429 files present and 427/427 SHA targets OK**. Final metadata is rebuilt after recording this result, and the final ZIP is reverified once more before handoff.
