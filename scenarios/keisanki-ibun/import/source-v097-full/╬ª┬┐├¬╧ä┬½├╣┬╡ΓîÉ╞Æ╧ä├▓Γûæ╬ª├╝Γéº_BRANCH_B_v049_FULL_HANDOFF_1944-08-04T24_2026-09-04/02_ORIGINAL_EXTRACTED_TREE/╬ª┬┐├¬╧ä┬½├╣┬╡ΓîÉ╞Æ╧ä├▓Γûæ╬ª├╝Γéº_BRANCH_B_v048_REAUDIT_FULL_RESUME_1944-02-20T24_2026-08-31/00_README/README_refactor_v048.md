# 計算機異聞 refactor v048 — Bengal/Arakan land+vehicle rollback

CURRENT authority time remains **1944-01-01**. The authority revision advances to `CHECKPOINT_1943-12-31T24_BRANCH_B_v006` because the Bengal/Arakan campaign was reopened to 1943-10-28 and reclosed with the v047 integrated land+vehicle system. WORKING discussion clock remains **1944-02-06 18:00 Marshall local**.

## Result

GALVANIC remains unchanged from v047. Its direct revisions are still higher US Tarawa casualties, worse US ground exchange and vehicle losses, and a roughly one-day later secure declaration. No GALVANIC casualty number is transferred to Bengal.

Bengal v001 had no physical vehicle OOB, serviceability, damage classification or repair/reappearance ledger. v048 therefore rolls back to the pre-Naf-crossing start rather than applying a flat casualty factor.

- No Japanese tank regiment is added; centered combat tanks remain zero.
- Japanese land motor/prime-mover/engineer-plant physical band: 430-560.
- Start-serviceable/crewed/fueled: 355-465.
- Japanese vehicle permanent writeoff: 55-95; temporary mission-kill: 45-80; 24-72h return: 25-50.
- Japanese combat casualties: 5,300-7,600, center about 6,300 (old center about 6,900).
- British/Commonwealth combat casualties: 7,700-11,100, center about 9,300 (old center about 8,700).
- Chittagong entry: late 14 Dec-early 15 Dec, centered late 14 Dec (about one day earlier).

British demolition and the escape of the field army still occur. Chittagong remains damaged; Feni/Comilla/Agartala remains the defensive arc. The stronger Japanese year-end state hardens the January stalemate but does not create a Feni offensive, new carrier allocation or U-Go GO.

## Load first

1. `00_README/CURRENT_DISCUSSION_FRONTIER_v015.json`
2. `06_RUNTIME/BENGAL_ARAKAN_CHITTAGONG_1943-10_12_SETTLEMENT_v002.md`
3. `06_RUNTIME/BENGAL_ARAKAN_LAND_VEHICLE_EVENT_LEDGER_1943-10_12_v001.json`
4. `06_RUNTIME/JAPANESE_LAND_COMBAT_INTEGRATED_SYNTHESIS_1932_1944_WORKING_v002.json`
5. `06_RUNTIME/ALLIED_DEATH_TALLY_RETROACTIVE_LAND_HARDWARE_RESERVATION_1941_1944_WORKING_v003.json`
6. `06_RUNTIME/PARALLEL_THEATER_STATE_1944-02-06T1800_WORKING_v002.json`

Next exact action remains 7-9 Feb Kwajalein/Roi-Namur ground reduction from the 6-Feb 18:00 WORKING clock. Bengal is now reclosed and should not be rerun again unless a named unit/vehicle return or dated logistics source displaces the v048 OOB band.
