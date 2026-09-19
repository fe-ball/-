# START HERE — 2026-09-08 FULL V11 / AIRCRAFT DEVELOPMENT CLOSE / INDUSTRIAL CLOSE / HARD QUARANTINE

V11 supersedes V10 only where V11 current files explicitly say so. Combat clocks do **not** advance in this package.

## Current clocks
- **CHINA:** 1939-12-31 24:00 CLOSED.
- **NOMONHAN:** revised combat branch CLOSED 1939-08-31 24:00.
- **1940 COMBAT:** NOT STARTED.
- **NEXT COMBAT GATE:** existing 1940 weapon appearance/fielding review remains mandatory before 1940-01-01 replay.
- **NEXT TECHNICAL TOPIC:** helicopter / rotorcraft audit; no helicopter result is pre-recorded by V11.

## Read first
1. `78-CURRENT-2026-09-08-AIRCRAFT-DEVELOPMENT-CLOSE/00-AIRCRAFT-DEVELOPMENT-HANDOFF-V11.md`
2. `78-CURRENT-2026-09-08-AIRCRAFT-DEVELOPMENT-CLOSE/01-AIRCRAFT-DEVELOPMENT-CHRONOLOGY-1935-1941-V1.md`
3. `78-CURRENT-2026-09-08-AIRCRAFT-DEVELOPMENT-CLOSE/02-AIRCRAFT-PERFORMANCE-MASTER-THROUGH-1941-V1.tsv`
4. `78-CURRENT-2026-09-08-AIRCRAFT-DEVELOPMENT-CLOSE/03-AIRCRAFT-DERIVATION-MATRIX-1935-1941-V1.tsv`
5. `78-CURRENT-2026-09-08-AIRCRAFT-DEVELOPMENT-CLOSE/04-AIRCRAFT-DESIGNATION-GATE-LEDGER-V1.tsv`
6. `78-CURRENT-2026-09-08-AIRCRAFT-DEVELOPMENT-CLOSE/07-INDUSTRIAL-CAPACITY-AND-T-AUX-CLOSEOUT-1939-1941-V1.md`
7. `77-CURRENT-2026-09-07-SESSION-CLOSE/00-SESSION-HANDOFF-V10.md` for combat/session state inherited from V10.
8. `76-CURRENT-1940-WEAPON-GATE-V10/` before any 1940 combat replay.
9. `CURRENT-MASTER-FILE-INDEX-V11.tsv`, `PACKAGE-STATE-V11.tsv`, `TERMINOLOGY-AND-SUPERSESSION-GUARD-V11.tsv`.

## V11 aircraft-development closure
V11 restores **development history first, finished aircraft second**. Superseded aircraft branches are evidence of possible research paths, not lost current canon.

- Existing CURRENT aircraft and propulsion figures remain authority unless V11 explicitly changes a missing or stale value.
- Old-branch performance tables never auto-return merely because the airframe concept survives.
- Research, service requirement, prototype order, formal designation, production and combat release are separate gates.
- Official/series designation is not back-dated into earlier paper studies or X-aircraft research.

### 1941-or-earlier branches newly closed at planning/working level
- **E6-B:** E5 attack success naturally generates a 1938H2 fast-heavy-twin study; dedicated 3-crew ~6.7 t / 1.0-1.2 t internal-bomb E6-M-JF branch remains separate from common E6 Twin.
- **P1/P2 -> military STOL:** P1/P2 are the technical school; a cheaper military liaison/observation derivative can pass to an outside airframe maker. P2 itself need not become the mass military aircraft.
- **X-TP fighter -> A7M/Gaifu:** E5 1,000-shp mass-fighter concept stays rejected; 1938-40 X-aircraft research survives as a valuable reducer/propeller/carrier-operation school. A serious fighter requirement reappears with E6.
- **STOL + JF -> A8N/Sakufu:** carrier-jet research starts as prewar technical exploration; 1941 dedicated prototype is plausible, carrier qualification remains naturally 1942+.
- **E5/E6 Twin -> J2N/Hekireki study:** the research requirement survives, but a dedicated J2N airframe is not forced into 1941. Common E6 Single/Twin must first fail a specific heavy/night/all-weather requirement gate.
- **TP high-altitude reconnaissance:** E6-S-N-T single-engine pressurized recon branch can plausibly fly in late 1940 and enter 1941 service test; `Ki-40` remains a designation gate, not an automatic retroactive label.

## V11 working performance anchors — do not substitute older quarantined values
- **A7M/Gaifu E6 working prototype:** ~3.6 t, ~25 m2, E6-S-T 1,300 hp normal / 1,400 short, ~575-600 km/h normal, ~595-615 km/h short-rating class, ~1,600-2,000 km internal range, ~118-125 km/h approach.
- **A8N/Sakufu E6-M-JF working prototype:** ~4.95 t, ~31 m2, 2 x ~984 kgf, ~670-710 km/h, ~1,000-1,300 km internal range, ~125-132 km/h prototype approach with 120-130 target after high-lift tuning.
- **E6-B:** ~6.7 t, ~28 m2, 2 x E6-M-JF, 1.0-1.2 t internal normal bomb load, ~680-710 km/h at 5-7 km, ~550-700 km normal strike radius.
- **TP high-altitude recon:** ~3.9-4.1 t, E6-S-N-T 1,500 hp normal, ~625-650 km/h at 8 km, ~3,000-3,600 km practical internal range.
- **J2N dedicated-airframe 1941 performance:** deliberately **NOT CLOSED**; requirement/design gate first.

## Industrial closure carried into aircraft feasibility
- T-0/T-1 through T-4 non-linear core-capacity growth is accepted as the current prewar industrial envelope.
- T-5 is a 1939Q4 prewar capacity commitment for 1942 demand insurance, not proof of 1941 combat output; T-6 is 1940H1 option-study only.
- 1940-41 aircraft growth is not bulk-aluminum-starved by default; planned light-alloy expansion plus FRP substitution protects primary structure. Processing, gear, brakes, tyres, instruments, weapons, propellers/reducers and QA can still bind.
- JF/pure-J expansion is intentionally favored where it avoids large precision reduction-gear competition with piston/TP production.
- After a Pacific-war opening, if factories physically survive, wartime shifts/overtime/outsourcing may exceed peacetime sustainable rates. This does not waive material science, new-technology qualification, or destroyed capacity.

## HARD QUARANTINE — mandatory
`91-PROVENANCE-QUARANTINED-AIRCRAFT-RESEARCH-V11/` contains the old aircraft-branch sources surfaced during this audit.

They are **NOT CURRENT**. They may be read only for provenance, lost requirement history, possible geometry, or questions to re-test.

Forbidden automatic imports from quarantine include:
- old E6 thrust assumptions;
- old aircraft speeds/ranges/weights without current H->A propagation;
- old production dates/OOB;
- old type/subtype names or numbers;
- E5 Gaifu mass-fighter claims;
- old dedicated Hekireki 14 m2 airframe performance;
- old `Ki-40` labels;
- old Sakufu carrier performance unless it passes the V11 working/current gate.

A quarantined item can return only through: **technical re-test -> development-history fit -> requirement gate -> designation gate -> production/service gate**.

## Inherited V10 controls remain in force
The V10 correction register, 1939 combat closures, E-family matrix, NAMEGUARD1, weapon appearance gate and all V9 technical-control no-backflow rules remain mandatory unless V11 explicitly overrides them.
