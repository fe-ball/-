# MACHINE INTEGRITY AUDIT V10 — DATAFIX1 THROUGH EFAMILY1-NAMEGUARD1

- Status: **PASS**
- Datafix scope: **integrity/provenance metadata only; no worldline facts changed by DATAFIX1**
- Technical revisions: **E6 performance/cost/mission/FRP + E5/E6 transition + E6 Single + Navy recon/land-attack/Type91 + B5N2/G3M2/D3A1/G4M1/B6N comparative wash + 1941 torpedo/dive-bombing effectiveness + E7 jet/TP outlook closures**
- China clock: **1939-12-31 24:00**
- Nomonhan: **1939-08-31 24:00 revised closed**
- Next gate: **1940 weapon appearance review; combat clock not advanced**
- V10 current-layer files (`72`–`77`): **87**
- Missing required current files: **0**
- Superseded post-V9 quarantine present: **True**

## File-count semantics

`PACKAGE-INVENTORY-V10.tsv` excludes itself and the two final cryptographic files. The manifest includes the inventory but excludes `FULL-PACKAGE-MANIFEST-SHA256-V10.tsv` and `SHA256SUMS-V10.txt`.

Live counts after EFAMILY1-NAMEGUARD1: inventory **819**, manifest **820**, final files **822**.

## Historical provenance drift classification

- V7: one intentional later STATEFIX1 mutation of a V7-named provenance file.
- V8: mutable `00-START-HERE-CURRENT.md` plus the later accepted `PACKAGE-STATE-V8.tsv` artifact.
- V9: mutable `00-START-HERE-CURRENT.md` only.
- V10: current manifest is the cryptographic authority.

## E5E6TRANS1

- E5 1939 program: **142 total = 2 development + 140 military accepted** by 1939-07-31.
- 1940 opening E5: **130 military extant +2 development**.
- 1940 Twin transition: **E5 30–42 / center 36** bridge accepted; **E6 Twin 120–156 / center 144**.
- Planning year-end Twin physical stock center: **E5 ~152 / E6 Twin ~136**; exact replay losses remain open.

## E6SINGLE1

- Closes the May10 chronology gap with E6 Single No.1 first flight on **1939-05-31**; no 1939 combat backflow.
- Correct propulsion identity: **1× E6-M-J**, ~850 kgf normal / ~900 kgf selected short; E6-S-J remains HS-2's small-core package.
- Service center: **~2.85 t / ~17.5 m² / ~0.73 t internal kerosene / ~0.25 t nose module**.
- Normal performance center: **~750 km/h at 6 km**, 6 km **~5.6–6.0 min**, internal radius **~400–500 km**.
- Production cost: **~115–135 k¥, center ~125 k¥** mission-equipped.
- Procurement posture: **96 firm-order class +48 option**; 1940 acceptance **84–108 / center ~96**.
- Pure-J is the normal series backend; JF Single remains engineering-only absent a new requirement.
- The separate visual Draft1 14.2 m² wing proxy is flagged for later correction to the 17–18 m² service envelope when merged.
- No combat clock advanced.

## NAVALJETTORP1

- Technical E5/E6 Navy mission branches remain closed, while NAMEGUARD1 downgrades newly supplied long-form names and `R2As`/`G4As` shorthands to **working aliases**; `R1As` remains an earlier current code referent.
- G4As1 is a high-speed short/medium-range parallel G4 branch, not G4M hardware: one Type91-class torpedo OR ~0.35-0.40 t bomb mission; initial torpedo radius ~300-400 km.
- 1941 Type91 Mod2 retains historical service identity while the worldline normal air-drop qualification becomes **~400-430 km/h**, with selected **~450 km/h** development growth.
- B5N2/D3A1 remain evolutionary; B6N inherits high-speed torpedo release by design origin; B7A later inherits both torpedo and dive-release schools.
- No combat clock advanced.

## B5NAUDIT1

- B5N2 historical/current baseline is now explicit rather than implicit: applicable later EX2/QC lots **~382-384 km/h**, normal mission range **~980-1,020 km class**.
- E5-S-T B5N conversion is **2-4 technical aircraft only**; no serial fleet re-engine program.
- TP screening keeps kerosene/lower-vibration/cleaner-nose benefits but loses medium-altitude performance and useful range; normal/heavy mission screening **~680-780 km**, ferry **~1,350-1,600 km**.
- 1941 Type91 ~400-430 km/h normal release envelope exceeds practical B5N torpedo-attack speed; it improves release margin/repeatability while the airframe becomes the ordinary speed limiter.
- Next conventional naval-aircraft wash: **G3M2 / Type96 land-based attack aircraft**.
- No combat clock advanced.

## G3MAUDIT1

- G3M2 remains the gasoline long-range land-attack baseline; applicable later EX2 aircraft **~377-381 km/h**.
- Ordinary torpedo H->A radius **~650-800 km**; historical ~4,400 km maximum/ferry range is not a torpedo radius.
- E5-S-T direct G3M conversion stays paper-only; E6-S-T does not open a serial G3M branch.
- Mixed avgas/kerosene naval aviation is deliberate because turbine conversion would trade away G3M reach.
- D3A1 wash is now closed by D3AAUDIT1; next wash **G4M1**. No combat clock advanced.

Cryptographic integrity is provided by `FULL-PACKAGE-MANIFEST-SHA256-V10.tsv` / `SHA256SUMS-V10.txt`.

## TORPEDO41CLOSE1 technical revision

- Added 1941 year-end aerial-torpedo effectiveness/employment closeout and ledger.
- Hit semantics: valid release -> water-entry/run reliability -> target geometry; no universal hit-rate scalar.
- Type91 Mod1 remains useful; Mod2 premium capital-ship weapon, ~400-430 km/h normal high-speed qualification.
- Historical calibration anchors: Pearl Harbor ~half of ~40 torpedoes hit restricted targets; Force Z ~8/49 against maneuvering capital ships.
- No combat clock advance.


## D3AAUDIT1

- D3A1 remains the gasoline piston serial carrier-dive-bomber baseline; later EX2/QC aircraft **~391-393 km/h at ~3 km**, mission range **~1,430-1,500 km class**.
- Dive bombing is now layered as target-area arrival -> valid dive/release -> geometry hit. Ordinary maneuvering-large-ship direct-hit band is **~18-28% per valid 250 kg release**, with explicit favorable/disrupted bands.
- Type99 No25 250 kg SAP is guarded as a serious carrier/cruiser weapon but not a guaranteed battleship killer.
- E5-S-T D3A is **2 aircraft + optional third technical article only**; fixed-gear drag and TP cruise economy defeat serial conversion.
- Future D4Y audit should test **~3-6 months earlier effective replacement opportunity**; a 1941H2 D3A production taper is only a gate if D4Y independently passes structural/dive/carrier/engine tests.
- Next conventional naval-aircraft wash: **G4M1**. No combat clock advanced.


## G4MAUDIT1

- G4M1 remains the gasoline very-long-range conventional land-attack main line; applicable early EX2/QC aircraft **~433-436 km/h at ~4.2 km**.
- Ordinary Type91 torpedo radius **~900-1,150 km**, favorable **~1,200-1,300 km** sensitivity only.
- No generic 1941 self-sealing integral wing tank / crew-armor back-port; fuel-system vulnerability remains a real design trade.
- E6-S-T serial conversion rejected; E6-M-T means a new aircraft rather than G4M re-engine.
- Better test/QC allows **~2-4 months earlier effective ramp opportunity**, potentially **~20-50** additional late-1941 acceptances if production rate is otherwise matched; not a pre-recorded inventory.
- Next wash: **B6N requirement/engine**, then D4Y replacement, then B7A composition. No combat clock advanced.

## E7OUTLOOK1

- Restores continuous E-generation timing to future-aircraft planning; project-start engine generation is not a permanent engine lock.
- E7 integrated-core target remains **1940H1 rigs -> 1940H2 gas-generator demonstrator -> 1941H1 full-core ground development -> 1941H2 ground-qualified development core**, with inherited aft-fan limited flight release possible at the latter gate.
- E6 Single selected retrofit outlook: **~785-800 km/h @6 km / ~800-815 @8 km / 6 km ~4.8-5.3 min**, conditional on E7 installed mass/drag closure.
- E6 Twin selected JF retrofit outlook: unchanged-airframe clean speed only **~805-825 km/h** because compressibility dominates; preferred use is heavier fuel/torpedo/protection/equipment, with **~5.4-5.6 t** heavy design target after local gear/wing-root/brake qualification.
- If the E7 program remains healthy, ground research closure before a historical-date late-1941 Pacific-war expansion is plausible; this does **not** pre-record service production, deployment, combat, or the war-start date.
- Earliest E7-dedicated aircraft first-flight target remains **1942Q1-Q2**.
- No combat clock advanced.

## E7TPOUTLOOK1

- Extends E7 outlook to shaft/turboprop products using scale bands rather than freezing future aircraft to E6-S-T.
- E7 small TP outlook: **~1,425–1,500 shp normal / ~1,525–1,575 short**.
- E7 lower-medium (~10–11 kg/s) outlook: **~1,750–1,850 shp normal / ~1,900–2,000 short**, now mandatory B6N-size TP comparator.
- E7 medium central: **~2,250–2,450 shp normal**, with propeller/reducer qualification becoming the main gate above the current ~2,200 hp high-power propeller school.
- E7 large first-aircraft product: **~3,500–4,000 shp flat-rated** pending very-large propeller qualification; thermodynamic core capability remains higher.
- B5N/D3A/G3M/G4M serial E7 retrofits remain rejected; the gain belongs in new-build aircraft.
- AT-3 preferred growth is four E7-M engines (~9,200–9,800 shp aggregate), not an automatic two-large-engine redesign.
- No combat clock advanced.



## B6NAUDIT1

- Dedicated 14-Shi/B6N propulsion outlook now compares piston, E6-S-T test and E7-M lower-flow TP on one carrier-sized airframe.
- Historical B6N geometry remains the carrier constraint; no automatic larger aircraft.
- Piston ~1.75-1.85 khp remains **A- schedule hedge**; E6-S-T 1.3/1.4 khp is **C test/fallback only**.
- E7-M-LF ~1.75-1.85 khp normal / ~1.9-2.0 khp short is **A- conditional main-production candidate**.
- H->A E7 aircraft screen: ~2.80-2.92 t empty, ~520-535 km/h normal max, ~7.5-8.5 min to 5 km, ~650-800 km ordinary torpedo radius.
- Type91 ~400-430 km/h release is design-origin; TP gains are arrival/release opportunity, wave-off and post-drop acceleration rather than a free torpedo hit-rate bonus.
- If E7 reducer/prop/TBO/carrier qualification closes, ~6-12 months earlier effective B5N replacement opportunity versus historical B6N ramp is plausible; no future service date/inventory is pre-recorded.
- Next naval aircraft wash: **D4Y replacement**, then B7A composition.
- No combat clock advanced.

## D4YAUDIT1
D4Y piston/E7-S-T outlook added; no combat clock advance. Final manifest/inventory counts are regenerated below.

## E6BOMBER1

- E5 attack record now explicitly drives a separate dedicated fast-heavy-bomber requirement rather than overloading the common 0.40t E6 mission airframe.
- H->A E6-B center: **~6.7t / 3 crew / 2x E6-M-JF / ~1.0-1.2t internal bombs / ~680-710km/h at 5-7km / ~550-700km standard strike radius**.
- Structural overload target **~1.5t** with reduced fuel; no 2-3t claim on the same E6-M pair.
- Earliest 1940Q2-Q3 first-flight opportunity is a gate only. Prototype posture **2-4**; no future production/deployment/combat is pre-recorded.
- E7 inherited-aft-fan growth: same-airframe ~715-740km/h class or ~7.3-7.6t heavy growth with ~1.3-1.5t standard bomb load after local structural qualification.
- Combat clock unchanged.


## EFAMILY1

- Adds the E5/E6/E7 aircraft-engine family crosswalk without advancing the combat clock.
- Five-axis reading is mandatory: **generation / core scale / backend / airframe family / service fit**.
- Same-engine/multiple-airframe example: **E6-M-JF** powers Army common E6 Twin, Navy R2As/G4As common-family derivatives, and the distinct larger E6-B bomber.
- Same-generation/different-core example: **E7-S-T D4Y / E7-M lower-T B6N / E7-M central-T AT-3 / E7-M J/JF E6 retrofit / E7-L large-aircraft outlook**.
- Conventional gasoline Navy lines remain intentional parallel products; no blanket turbine conversion.
- Combat clock unchanged.


## NAMEGUARD1

- Technical airframe/engine identities are separate from service nomenclature.
- Newly coined 2026-09-07 long-form Army/Navy names and project codes are working aliases unless independently attested earlier.
- Older evaluation/allocation labels are preserved as provenance and may be formally restored without changing hardware lineage.
- No performance, OOB, production, mission, clock or combat result changed.
