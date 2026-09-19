# 計算機異聞 refactor v046 — Branch B land-hardware / retro-casualty reservation WORKING

CURRENT authority remains **1944-01-01**. WORKING discussion clock remains **1944-02-06 18:00 Marshall local**; v046 does **not** advance the war clock.

This revision repairs a missing non-software Japanese land-combat layer. It closes bounded, maturity-dated effects for artillery/mortar firing tables and ammunition QC, existing direct-fire weapons, small-arms/MG reliability, mines/fuzes, physical fortification, tactical communications hardware, engineer plant/vehicles and ammunition storage/issue. It creates no new weapon family, gun/tank/radio count or manpower and authorizes no universal Army-artillery hit-rate multiplier.

Per user direction, already-realized ground casualty ledgers are **not individually rewritten now**. A machine-readable reservation defers their event-by-event correction to the next consolidated **「連合死者出納表」 / Allied death tally**. That pass must use the date-appropriate maturity of each hardware domain, separate deaths from broader casualty categories and show old/new/delta per event.

The 6-Feb Kwajalein/Roi-Namur D-Day result remains exactly at v043 geography/timing and current casualty bands; `FLINTLOCK_DDAY_DECISION_AND_LANDING...v002` only marks those casualty figures provisional for the future consolidated accounting.

Load first:
1. `00_README/CURRENT_DISCUSSION_FRONTIER_v013.json`
2. `06_RUNTIME/JAPANESE_LAND_COMBAT_HARDWARE_LINEAGE_1932_1944_WORKING_v001.json`
3. `06_RUNTIME/ALLIED_DEATH_TALLY_RETROACTIVE_LAND_HARDWARE_RESERVATION_1941_1944_WORKING_v001.json`
4. `06_RUNTIME/FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_v002.json`
5. `06_RUNTIME/PARALLEL_THEATER_STATE_1944-02-06T1800_WORKING_v001.json`

Next exact action: resume from 6-Feb 18:00 and adjudicate 7-9 Feb ground reduction **with the land-hardware layer active prospectively**, while leaving the older casualty adjustment parked for the later Allied-death accounting pass.
