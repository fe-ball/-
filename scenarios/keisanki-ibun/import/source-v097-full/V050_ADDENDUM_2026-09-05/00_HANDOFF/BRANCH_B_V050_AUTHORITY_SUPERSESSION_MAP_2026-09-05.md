# BRANCH B v050 — Authority / Supersession Map (2026-09-05)

This file prevents stale Santo/New-Caledonia results from being resurrected.

## Current authorities
- `BRANCH_B_1942H2_NAVAL_COMBAT_FIRE_SUPPORT_LEDGER_v002.*`
  - current general naval/fire-support rules for the 1942H2 re-audit.
  - supersedes v001 for working use.

- `SANTO_1942-09_AIR_TECH_INPUT_v001.md`
  - current Santo-period aviation-tech input.

- `BRANCH_B_SANTO_1942-09_NAVAL_REBUILD_v003.md`
  - current destroyer/night-action modeling framework and named-force reconstruction baseline.

- `BRANCH_B_SANTO_1942-09-24_NIGHT_ACTION_READJUDICATION_v004.*`
  - current 24 Sep night result.

- `BRANCH_B_SANTO_1942-09-25_DDAY_DAYLIGHT_v005.*`
  - current D-Day daylight landing/air/transport result.
  - remains valid under v009 except where a later cumulative ledger explicitly adjusts totals.

- `BRANCH_B_SANTO_TF64_CORRECTION_AND_DPLUS3_v009.*`
  - **primary Santo campaign authority after D-Day daylight.**
  - retroactively corrects TF64 arrival and replaces parts of v006, v007 and v008.
  - use its corrected 25 Sep night, corrected D+1, corrected D+2, and D+3/final evacuation settlement.

- `BRANCH_B_SANTO_POSTCAPTURE_ASSET_SETTLEMENT_v010.*`
  - current Santo captured-base/material/restoration authority.

- `BRANCH_B_SANTO_POSTCAPTURE_COMBINED_FLEET_INTENT_v011.*`
  - current Combined Fleet post-Santo strategic intent.

- `BRANCH_B_NC_1942-11-08_COMBINED_FLEET_READINESS_v012.*`
  - current Japanese 1 Oct demand / 8 Nov working readiness authority.

- `BRANCH_B_OCT1942_JAPAN_DEPLOYMENT_ALLIED_INTEL_v013.*`
  - current October Japanese deployment + Allied target-estimate authority.

## Audit trail / partially superseded files
- `BRANCH_B_SANTO_1942-09-25_DDAY_NIGHT_v006.*`
  - audit trail only for original D-Day-night reasoning.
  - **do not use its Atlanta torpedo mission kill or ~250-round bombardment as current.**
  - v009 replaces those with Duncan loss and ~165-round center bombardment; Atlanta remains combat-capable.

- `BRANCH_B_SANTO_1942-09-26_DPLUS1_v007.*`
  - audit trail only for pre-TF64-correction D+1.
  - v009 supersedes capture timing, U.S. dawn sortie generation, heavy-equipment percentage and related losses.

- `BRANCH_B_SANTO_1942-09-27_DPLUS2_v008.*`
  - audit trail only for pre-TF64-correction D+2.
  - v009 supersedes Pallikulo timing, evacuation volume and remaining U.S. strength.

- `BRANCH_B_1942H2_NAVAL_COMBAT_FIRE_SUPPORT_LEDGER_v001.*`
  - superseded by v002.

## Non-resurrection rules
- Astoria / Pensacola / Northampton remain Branch MI losses; no later no-Savo logic can resurrect them.
- Benham remains Branch MI loss.
- six named Branch MI DD losses remain paid.
- Atlanta is alive/available after Santo in current corrected line.
- Quincy is not available after 24 Sep Santo night without repair adjudication.
- Preston and Duncan are sunk in current Santo line.
- Wasp is mission-killed in Santo; exact 8 Nov return status is OPEN, not automatically recovered or sunk.
- Kongo carries Santo damage into October; no automatic reset.
- Santo carrier/aircrew/transport/tanker attrition must feed New Caledonia; no reset at 8 Nov.

## Historical learning rule
No unit receives historical Guadalcanal/Savo/Cape Esperance/Tassafaronga/Nov-Guadalcanal combat learning merely because the calendar date has passed.
Use only:
- pre-existing doctrine/technology;
- Branch MI experience;
- Branch Santo experience;
- subsequent Branch exercises/work-up.
