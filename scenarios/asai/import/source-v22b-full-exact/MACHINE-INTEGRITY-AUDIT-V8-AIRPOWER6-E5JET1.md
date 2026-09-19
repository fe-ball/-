# MACHINE INTEGRITY AUDIT — V8 AIRPOWER6 E5JET1

## Parent

Parent current package: `ASAI-WORLDLINE-HANDOFF-2026-09-04-FULL-V8-1939AIRPOWER5-GTCORE1`. AIRPOWER6 is an overlay; preserved V7/V6 provenance trees are not deleted.

## Scope

AIRPOWER6 closes E5-J / E5-JF installed product coordinates and reverse-audits them into the current 1937-39 E5 aircraft/research roster. Combat checkpoint remains `1939-04-20 24:00`; combat replay remains `HOLD_FOR_AVIATION_AUDIT`.

## New current authority

- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/23-GT-E5-J-JF-INSTALLED-PRODUCT-CANON-V8.md`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/23A-GT-E5-J-JF-PRODUCT-LEDGER-V8.tsv`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/24-E5-E6-AIRCRAFT-PROPULSION-REVERSE-AUDIT-V8.md`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/24A-E5-E6-AIRCRAFT-PROPULSION-STATE-LEDGER-V8.tsv`
- E5 installed-cycle/fan computation support under `99-SUPPORT-CURRENT/GT-REBASE-COMPUTATION/` and selected upstream E4/E5 sources.

## State invariants

- AIRPOWER5 mandatory cheat/capability preflight remains mandatory.
- v46 E6-M installed values are not downrated.
- E5-J old ~300 kgf shorthand is superseded by the closed ~425-455 kgf normal product band; selected short ~470 kgf remains separately logged.
- E5-JF first flight chronology is 1937 Q4. Surviving 1938 first-flight text is superseded only on chronology.
- No procurement/combat history is advanced.

## Expected final metadata counts

After this audit pair and metadata rebuild:

- total files: **442**;
- `PACKAGE-INVENTORY-V8.tsv` data rows: **439** (excludes current inventory/manifest/SHA self-referential trio);
- `FULL-PACKAGE-MANIFEST-SHA256-V8.tsv` data rows: **440** (includes rebuilt inventory; excludes itself and current SHA);
- `SHA256SUMS-V8.txt` targets: **440** (includes inventory, excludes current manifest and itself).

Final ZIP must unpack cleanly and verify **440/440** current SHA targets.
