# Land Combat Hardware / Retroactive Allied-Death Reservation — v046

## Finding
The active package had strong coverage of Japanese land-war **software/process** (command succession, registered fires, distributed stores, local reserves, landing/logistics process), but no dedicated, consolidated **non-software land-combat hardware** lineage. That omission matters because the Branch’s foundational compute / metrology / QC changes should also affect the technical repeatability and serviceability of equipment already present.

## What is now closed
The new working layer covers: artillery/mortar firing tables and lot/tube/temperature correction; grenade-discharger/short-mortar consistency; small-arms/MG zero/feed/spares; existing direct-fire and anti-LVT weapons; mines/fuzes/explosives QC; earth/timber revetments and small protected magazines; field telephone/radio batteries/spares/test practice; engineer plant/vehicles; ammunition packaging/storage/issue.

No new guns, tanks, radios, engineers, manpower or explosive energy are created. No 20/37-mm weapon becomes a magical M4 frontal killer. No Iwo-Jima cave system is back-ported.

## Maturity is dated
The effect is not a single 1944 scalar. Prewar firing-table and measurement work means a real opening-war dividend already exists, especially in prepared artillery. Field-service, comms hardware, fortification standardization and engineer uptime mature more gradually through 1942-43. Retroactive accounting therefore uses the event date and the domain-specific maturity state.

## Artillery guard
The package still forbids a Japan-wide Army-artillery hit-rate multiplier. In a prepared, registered position with observation/comms intact, the mature working band may use roughly 8-15% fewer correction rounds/time to useful fire and lower technical dispersion. If observation, crew, ammunition or the weapon is suppressed, the benefit collapses.

## User-directed retro rule
Past ground-casualty ledgers are **not** individually rewritten in v046. The new file `ALLIED_DEATH_TALLY_RETROACTIVE_LAND_HARDWARE_RESERVATION_1941_1944_WORKING_v001.json` reserves an event-by-event correction for the next consolidated **「連合死者出納表」** / Allied death tally.

At that trigger:
- scan only active-path realized ground events; never legacy/future snapshots;
- separate deaths/KIA from wounded/MIA/POW rather than converting broad casualty bands blindly;
- apply the hardware layer only at the stage where traced equipment survived and could function;
- use the maturity period appropriate to the date;
- produce old/new/delta by event;
- do not alter geography/timing/strategic outcomes unless a local re-audit proves the old outcome inconsistent.

Known candidate classes include GALVANIC ground losses, Bengal/Arakan ground actions and the 6-Feb Kwajalein/Roi-Namur first day, but inclusion is determined from the active current/working ledgers at tally-build time.

## Current Kwajalein status
The v043 D-Day outcome and its current casualty bands are preserved exactly in `FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_v002.json`. They are now explicitly marked **provisional for the future consolidated death/casualty ledger**. No hidden v046 casualty uplift has been booked.

## Prospective rule
Any land combat adjudicated **after 1944-02-06 18:00 working time** must load the new hardware lineage immediately. Thus the omission is deferred only for already-realized casualty accounting; it is not deferred for future fighting.
