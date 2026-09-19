# V9 DATAFIX1 CHANGELOG — 2026-09-05

Scope: package-control/index normalization only. No campaign outcome, force count, loss center, current theater clock, or next-gate substantive value was changed.

Changes:
- Added `TERMINOLOGY-AND-SUPERSESSION-GUARD-V9.tsv` so retained V8 no-backflow rules remain current without restoring stale V8 current-clock rows.
- Added `DECISION-INTENT-INDEX-V9.tsv`; `DECISION-INTENT-INDEX-V7.tsv` is now explicitly provenance/fallback only.
- Added the previously unindexed `03A` air/ammo and `04A` replacement TSV companions to master index, precedence, package state, session handoff and parent narratives.
- Replaced ambiguous master-index pointers `./` and `01-BASE-V6/ and archives` with explicit resolvable control/tree pointers.
- Added `PACKAGE-STATE-V9.tsv` to precedence/master control flow as a machine-readable cross-check, without elevating it above the narrative authorities it points to.
- Repaired six malformed current V9 TSV rows that had 7 fields under 8-field headers: five missing trailing `note` cells in `70-CURRENT-2026-09-05-SESSION-CLOSE/02-NOMONHAN-LOSS-LEDGER-V9.tsv` and one in `70-CURRENT-2026-09-05-SESSION-CLOSE/03A-NOMONHAN-AIR-SPECIAL-AMMO-WORKING-V9.tsv`; missing cells are explicitly empty and no numeric value changed.
- Corrected the metric identifier typo `ank_destroyed_crippled_major_repair` to `tank_destroyed_crippled_major_repair`.
- Regenerated V9 inventory, manifest, SHA256 list and integrity audits after the patch.
