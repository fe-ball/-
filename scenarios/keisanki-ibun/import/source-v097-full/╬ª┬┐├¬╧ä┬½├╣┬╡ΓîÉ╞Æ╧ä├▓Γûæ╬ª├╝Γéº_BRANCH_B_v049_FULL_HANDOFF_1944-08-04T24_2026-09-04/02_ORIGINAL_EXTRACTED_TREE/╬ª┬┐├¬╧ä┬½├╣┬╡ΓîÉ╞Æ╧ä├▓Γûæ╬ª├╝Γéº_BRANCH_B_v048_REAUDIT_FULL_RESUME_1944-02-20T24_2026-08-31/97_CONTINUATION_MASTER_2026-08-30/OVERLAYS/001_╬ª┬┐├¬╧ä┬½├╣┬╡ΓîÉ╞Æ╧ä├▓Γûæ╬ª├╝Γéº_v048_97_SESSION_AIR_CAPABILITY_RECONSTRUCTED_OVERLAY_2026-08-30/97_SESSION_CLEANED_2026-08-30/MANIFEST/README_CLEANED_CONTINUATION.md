# CLEANED SESSION CONTINUATION — 2026-08-30

Status: **CLEANED WORKING OVERLAY / NOT PROMOTED**

This directory does not rewrite the v048 authority package or the original `96_SESSION_WORKING_2026-08-30` session. It only normalizes data-quality problems found during restart audit.

## Restart rule

Global clock remains **1944-02-21T24**. HAILSTONE is closed. CATCHPOLE has already been adjudicated as a future-local node through 27 Feb, but it must not move the global clock until the **Eastern Fleet / Andaman / Bay of Bengal 19-22 Feb** cross-theater gate is resolved.

## Cleaned overlays

- `ARMOR/JAPANESE_ARMOR_NATIONAL_CHECKPOINT_1944-02-21_WORKING_v002.json`: explicit Eniwetok Type95 9/3/6 named posting; broad national bands left unchanged to avoid false precision.
- `OPERATIONS/TRUK_HAILSTONE_WARNING_CHAIN_1944-02-15_20_WORKING_v002.json`: artifact parents and COMINT rule inputs separated.
- `RULES_ASW/ASW_RETROACTIVE_AND_FUTURE_ACTIVITY_GUARD_1943_1944Q1_WORKING_v002.json`: loadable canonical inputs separated from catalog-only legacy provenance.
- `MANIFEST/SESSION_MANIFEST_v002.json`: active/superseded files separated and frontier wording corrected.
- `MANIFEST/SESSION_DATA_AUDIT_v001.json`: restart audit record.

## Do not silently promote

Bengal 25th Dragoons remains a reopen gate. June Marianas/Saipan files remain future gates only. Older v001 artifacts remain preserved for traceability but should not be selected over their explicit v002 superseders.

## Resume load order

Use `MANIFEST/RESUME_LOAD_ORDER_v001.json` as the exact restart input list.
