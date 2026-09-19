
# START HERE — 2026-09-07 FULL V10 / CHINA CLOSED 1939-12-31 / NOMONHAN REVISED CLOSED / 1940 WEAPON GATE NEXT

This V10 package supersedes V9 where V10 current files explicitly say so. All V9/V8/V7/V6 material remains provenance, baseline, technical source, or comparator unless superseded.

## Current clocks
- **CHINA:** 1939-12-31 24:00 CLOSED.
- **NOMONHAN:** revised combat branch CLOSED 1939-08-31.
- **1940 COMBAT:** NOT STARTED.
- **NEXT:** review 1940 weapon appearance/fielding ledger, then resume 1940-01-01.

## Read first
1. `77-CURRENT-2026-09-07-SESSION-CLOSE/00-SESSION-HANDOFF-V10.md`
2. `77-CURRENT-2026-09-07-SESSION-CLOSE/01-NEXT-GATE-1940-WEAPONS-REVIEW-V10.md`
3. `77-CURRENT-2026-09-07-SESSION-CLOSE/02-CORRECTION-REGISTER-V10.tsv`
4. `77-CURRENT-2026-09-07-SESSION-CLOSE/03-CURRENT-CLOCKS-V10.tsv`
5. `CURRENT-MASTER-FILE-INDEX-V10.tsv`
6. `PACKAGE-STATE-V10.tsv`
7. `TERMINOLOGY-AND-SUPERSESSION-GUARD-V10.tsv`
8. V9 technical control remains mandatory: `71-CURRENT-TECHNICAL-CONTROL-V9/`.

## Highest-priority current directories
- `72-CURRENT-RETRO-AIRPOWER-1938-1939/`
- `73-CURRENT-NOMONHAN-REVISED-V10/`
- `74-CURRENT-CHINA-1939-REPLAY-V10/`
- `75-CURRENT-TECHNICAL-ADDENDA-V10/`
- `76-CURRENT-1940-WEAPON-GATE-V10/`
- `77-CURRENT-2026-09-07-SESSION-CLOSE/`

## Critical correction
Operational E5/Ki-42 fleets are near-pure additions vs OLD V8/V9. They existed in China before the Nomonhan ceasefire; late-September E5/Ki-42 flow is additional **reallocation**, not first China appearance.

Do not use the quarantined post-V9 `RETURN-CLOSEOUT-V1` or stale `1940-Q1-WORKING-CLOSEOUT` as current authority.

E6 Twin planning is now closed through **E6FRPORD1**. Use the cost/procurement rebaseline for quantity, E6MISSION1 for the common two-seat mission architecture, and `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-E6-FRP-ORDNANCE-CARRIAGE-HIGHSPEED-STORE-CLOSURE-1939-1940-V1.md` for S6/S4/M1 bay adapters, FRP doors/cassettes/tail-fairing use, HSR 50/60/100/250 qualification and HSC-100F. The earlier 36–60 pilot-production band remains superseded.

E5/E6 production transition is now closed at planning level by `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-E5-E6-1940-PRODUCTION-TRANSITION-FLEET-ACCUMULATION-CLOSEOUT-V1.md`: E5 opens 1940 at 130 military extant, accepts ~36 bridge airframes, then leaves new-airframe production; E6 accepts ~144 center. Actual 1940 losses and theater allocations remain replay events.

E6 Single is now closed by **E6SINGLE1** as a real 1940 serial-production land interceptor/high-cover aircraft rather than a suspended research branch. Use `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-E6-SINGLE-PERFORMANCE-SERVICE-PROCUREMENT-CLOSEOUT-1939-1940-V1.md`: E6-M-J pure-J, 2.85 t center, ~750 km/h at 6 km, ~400-500 km internal radius, 96 firm-order class +48 option, 1940 acceptance 84-108 center ~96. Exact service allocation/combat release remains replay-local.

NAVALJETTORP1 closes the E5/E6 Navy mission/naming line: Army E5 recon = 九八式司令部偵察機; Navy E5 = 九八式高速陸上偵察機/R1As; E6 Navy recon = 零式高速陸上偵察機/R2As; E6 Navy high-speed land attack = 零式陸上攻撃機一一型/G4As1. G4As drives a 1940-41 Type 91 high-speed air-drop program; 1941 Mod 2 normal qualification is ~400-430 km/h class with selected ~450 km/h development growth. B6N inherits that torpedo interface; B5N2/D3A1 remain evolutionary. See `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-E5-E6-NAVAL-RECON-LAND-ATTACK-TORPEDO-LINEAGE-1938-1941-V1.md`.

B5NAUDIT1 closes the first full conventional-carrier-aircraft wash: B5N2 remains Sakae-powered in serial service; applicable later EX2/QC lots are ~382-384 km/h class with ~980-1020 km normal mission range. E5-S-T B5N conversion is technically plausible but **test-only (2-4 aircraft)** because the turbine loses too much medium-altitude/range economy for a mature carrier torpedo aircraft. The 1941 Type91 high-speed envelope therefore raises the opportunity value of the existing piston B5N2 rather than forcing a re-engine program. See `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-B5N2-PISTON-TP-COMPARATIVE-CLOSEOUT-1939-1941-V1.md`.


G3MAUDIT1 closes the second conventional naval-aircraft wash: G3M2 remains the gasoline long-range land-attack baseline. Applicable later EX2 lots are ~377-381 km/h class; H->A ordinary torpedo radius is ~650-800 km class. E5-S-T direct conversion is rejected even as a physical priority, and E6-S-T G3M derivative is also rejected for serial service: both trade away the reach that makes G3M valuable while overlapping faster G4As. Mixed avgas/kerosene Navy aviation therefore remains intentional. See `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-G3M2-PISTON-TP-COMPARATIVE-CLOSEOUT-1939-1941-V1.md`.

TORPEDO41CLOSE1 closes the **1941 year-end aerial-torpedo effectiveness model** without advancing combat: Type91 Mod1 remains useful; Mod2 is the premium 1941 weapon (~935kg / 205kg Type97) with normal high-speed qualification ~400-430km/h. Replay must count valid releases first, then apply entry/run reliability and target-geometry hit bands. Working post-release bands are ~45-60% for anchored/restricted targets, ~16-24% for maneuvering capital ships under coordinated multi-axis attack, lower for cruiser/destroyer targets, and ~25-40% when a capital target is already slowed/boxed. See `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-1941-YEAREND-NAVAL-AERIAL-TORPEDO-EFFECTIVENESS-EMPLOYMENT-CLOSEOUT-V1.md`.

D3AAUDIT1 closes the Type 99 carrier-bomber wash: later EX2/QC D3A1 remains piston-powered and ~391-393 km/h class; dive bombing is now modeled as attack-area arrival -> valid dive/release -> target-geometry hit rather than a fixed aircraft hit rate. Ordinary maneuvering-large-ship direct-hit planning is ~18-28% per valid release, with explicit favorable/disrupted bands. E5-S-T D3A conversion is test-only (2 aircraft + optional third); fixed-gear drag and TP range penalty make serial conversion irrational. The successor advantage should come from earlier D4Y replacement readiness, with a ~3-6 month opportunity band to be tested in a separate D4Y audit. See `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-D3A1-PISTON-TP-DIVE-BOMBING-COMPARATIVE-CLOSEOUT-1939-1941-V1.md`.

G4MAUDIT1 closes the Type 1 conventional land-attack wash: applicable early EX2/QC G4M1 is ~433-436km/h class at ~4.2km and retains the very-long-range gasoline role, with ordinary Type91 torpedo radius ~900-1,150km (favorable ~1,200-1,300km sensitivity only). E6-S-T serial conversion is rejected because lower power/cruise economy destroys the reason to own G4M; E6-M-T implies a new aircraft. No generic 1941 armor/self-sealing back-port is granted. Improved test/QC gives ~2-4 months earlier effective ramp opportunity, potentially ~20-50 additional late-1941 acceptances if factory rate is otherwise matched, but no future inventory is pre-recorded. See `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-G4M1-PISTON-TP-LONGRANGE-ATTACK-COMPARATIVE-CLOSEOUT-1939-1941-V1.md`.

E7OUTLOOK1 restores the continuous E-generation clock to future-aircraft planning. E7 is active hardware research through 1940, targets full-core ground development in 1941H1 and ground-qualified development core in 1941H2; an inherited aft-fan limited flight-release candidate is therefore plausible before a historical-date late-1941 Pacific-war expansion if the program remains healthy. Selected E6 Single/Twin retrofit articles are a 1941H2 conditional outlook, while the earliest E7-dedicated new-aircraft first-flight target remains 1942Q1-Q2. Use `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-E7-E6-AIRFRAME-RETROFIT-PREWAR-OUTLOOK-1940-1942-V1.md`. No future procurement/combat is pre-recorded.

E7TPOUTLOOK1 extends the continuous E-generation rule to shaft/turboprop products. E7 small-core TP remains ~1.45-1.50k shp normal class, while the **lower edge of the E7 medium scale (~10-11 kg/s) opens ~1.75-1.85k shp normal / ~1.9-2.0k short**, making it the correct future TP comparator for B6N-size carrier attack aircraft. E7 medium central products move toward ~2.25-2.45k shp normal but become propeller/reducer-gated; E7 large cores are heavy-aircraft products and should initially be flat-rated ~3.5-4.0k shp unless a very-large propeller is qualified. B5N/D3A/G3M/G4M no-serial-retrofit verdicts remain; AT-3 gains a four-E7-M growth path. See `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-E7-TURBOPROP-SHAFT-PRODUCT-PREWAR-OUTLOOK-1940-1942-V1.md`.

B6NAUDIT1 closes the 14-Shi Tenzan propulsion outlook. The historical-sized B6N remains the carrier-geometry anchor; E6-S-T 1.3/1.4khp is test/fallback only, while **E7-M lower-flow TP (~1.75-1.85k shp normal / ~1.9-2.0k short)** becomes the conditional main-production candidate if late-1941/early-1942 reducer/prop/TBO/flight gates pass. H->A aircraft screening is ~520-535km/h normal max speed, ~7.5-8.5min to 5km and ~650-800km ordinary torpedo radius, with piston ~1.75-1.85khp retained as schedule hedge. A ~6-12 month earlier effective replacement opportunity versus the historical B6N ramp is an outlook only; no future service date is pre-recorded. See `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-B6N-TENZAN-PISTON-E6ST-E7M-TP-COMPARATIVE-OUTLOOK-1939-1942-V1.md`.

D4Y future design is now screened through **D4YAUDIT1**: healthy piston Atsuta remains the schedule baseline; E7-S-T is a conditional small-core carrier-recon/fast-strike competitor rather than an automatic speed win. D4Y E7-S and B6N E7-M occupy different core scales.
E6BOMBER1 closes the **dedicated fast-heavy-bomber requirement/outlook** created by E5 attack success. The common E6 Twin remains ~0.40t multi-role; the separate E6-B working branch is a 3-crew ~6.7t / 1.0-1.2t internal-bomb derivative using 2x E6-M-JF, screened at ~680-710km/h at 5-7km and ~550-700km standard strike radius. A ~1.5t overload and 1941H2 E7-JF retrofit/growth path are future gates only. No 1940 adoption/production/combat is pre-recorded. See `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-E5-DERIVED-E6-FAST-HEAVY-BOMBER-OUTLOOK-1938-1941-V1.md`.


EFAMILY1 closes the cross-generation **aircraft/engine family architecture**: read propulsion as generation + S/M/L scale + backend + airframe family + service fit, not as one E-number = one engine or one aircraft. It explicitly maps E5/E6/E7 same-engine/multiple-airframe and same-generation/different-core branches, including Army/Navy service splits. See `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-AIRCRAFT-ENGINE-GENERATION-FAMILY-ARMY-NAVY-MATRIX-1937-1942-V1.md`.

NAMEGUARD1 adds a nomenclature-control overlay: technical family identities remain closed, while newly coined 2026-09-07 Army/Navy type-year names and project codes are **working aliases** unless independently attested earlier. Older designations/evaluation labels are not deleted and can be formally restored at a later naming gate. See `75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-AIRCRAFT-NOMENCLATURE-ALIAS-RESTORATION-GUARD-V1.md`.
