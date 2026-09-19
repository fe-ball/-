# HOMARE DEVELOPMENT / SERVICE-PERFORMANCE AUDIT — V8

## Status
This file supplements `01-ENGINE-REQUIREMENT-TEAM-RELEASE-CANON-V8.md`.
The **development mechanism and broad schedule are authoritative**. Exact boost-duration tables and aircraft performance consequences remain working values until later aircraft/war-production closure.

**AIRPOWER3 note:** quarter-level timing, fuel/lubricant qualification sequencing, availability grades and the 1943Q1 technical-maturity boundary are superseded by `11-HOMARE-QUARTERLY-DEVELOPMENT-QUALIFICATION-CANON-V8.md`.

## 1. Historical starting point — CLOSED INTERPRETATION
Do not caricature early Homare as a fundamentally non-running engine.
Historical Nakajima development was already fast and technically competent:

- formal design around 1940;
- multiple parallel specialist teams for cooling/combustion, main-rod bearing, supercharger/carburetion, ignition, steel crankcase, lubrication and fuel-system work;
- first running in 1941;
- first 300-hour endurance program completed in 1941;
- 1,800 hp class followed rapidly by 2,000 hp class development.

Therefore V8 does **not** gain a one-year prototype miracle. The largest divergence appears after prototype success: fuel/lubricant changes, aircraft integration, manufacturing replication and frontline realization.

## 2. V8 schedule — CLOSED
- 1939Q3-Q4: concept study may be earlier/deeper from Sakae team release and available technology shelf.
- 1940Q1: formal design.
- 1940H2: full-size rigs / production preparation / comparison tests.
- 1941Q1: first running only modestly earlier than history at most.
- 1941Q2: 300-hour class endurance closure; timing advantage is weeks to perhaps 1-2 months, not a year.
- 1941H2: aircraft integration and alternate fuel/lubricant qualification deepen.
- 1942: initial production remains the main window.
- 1943Q1: a technically mature/reproducible good-engine Homare 20/21 specification exists in V8; fleet-wide maturity after this point remains war/production-branch dependent.

## 3. What is already on the domestic technology shelf in 1940 — CLOSED
Nakajima does not receive a complete Homare design from Asai. It can draw from:

- high-load multilayer bearing/surface options;
- crankpin grinding, roundness/roughness and gauge standards;
- dynamic balancing and torsional-vibration measurement methods;
- oil pump/suction/aeration/high-altitude test methods;
- corrected centrifugal-compressor maps;
- gasoline knock maps versus boost, intake temperature, mixture and ignition;
- 100/standard/emergency fuel-map methodology;
- ADI rig/flight-test experience and boost interlock concepts;
- low-pressure metering/injection experiments;
- cylinder-by-cylinder thermal measurement culture;
- lot traceability, master gauges and process-control methods.

## 4. What remains Homare-specific — CLOSED
The following cannot be pre-solved by a 180–200 hp research engine or generic turbo program:

- 18-cylinder intake distribution;
- front/rear-row cooling interaction;
- master rod and articulated-rod geometry/load;
- full crankshaft deflection and torsional modes;
- 2,000 hp reduction-gear behavior;
- steel crankcase large-forging/process development;
- complete 18-cylinder ignition and accessory layout;
- whole-engine thermal distortion and sealing;
- aircraft cowl/oil-cooler/propeller integration.

Failures in these areas are allowed and expected. V8 primarily shortens diagnosis loops and improves final replication.

## 5. Limiting-factor model — CLOSED METHOD
At any operating point use:

`P_service(h) = min(P_design, P_knock, P_thermal, P_lubrication, P_mechanical, P_supercharger)`

Production quality is then applied as a **distribution / realization problem**, not a stack of bonus percentages.

Do not add separate +% bonuses for compressor efficiency, mixture distribution, cooling and ADI if they merely raise the same knock/thermal limit to the next constraint.

## 6. Bearings / lubrication — CLOSED INTERPRETATION
Asai's early multilayer-bearing, surface, grinding and clearance technology substantially reduces the amount of basic bearing-material exploration Nakajima must do.

It does not make lubrication irrelevant.
Remaining failure channels include:

- crankpin deflection / edge loading;
- insufficient oil flow or excessive flow causing suction-side problems;
- aeration/cavitation at altitude;
- oil-temperature excursions;
- contamination and filtration;
- poor lubricant chemistry;
- incorrect production clearance or surface finish.

The V8 advantage is earlier misalignment/edge-load testing, better surface control, better failure classification and faster correction.

## 7. Lubricant qualification — CLOSED METHOD / WORKING CLASSES
Use three operational classes rather than one generic "good/bad oil" multiplier:

- **L-P Premium**: imported first-class or genuinely equivalent domestic certified oil;
- **L-Q Qualified Domestic**: realistic domestic mass-service aviation oil meeting V8 acceptance limits;
- **L-E Emergency**: lower/unstable quality, substitutes or doubtful lots.

Lubricant quality primarily controls **duration, life and the permitted high-output envelope**, not instant horsepower.

Bad oil may force command/maintenance to restrict boost; it does not automatically subtract a fixed percentage from a dynamometer reading.

## 8. Fuel / anti-knock qualification — CLOSED METHOD
Asai/Nakajima should not be written as discovering in 1942 that low-octane fuel is difficult. From formal design in 1940 the test program distinguishes:

- premium fuel design point;
- ~92-class standard-service + ADI branch;
- ~88–90-class emergency low-grade + ADI branch;
- low-grade/no-ADI survival map with substantial boost restriction.

The engine-side objective is low **fuel-quality sensitivity**, not fuel-quality independence.

ADI, mixture distribution, charge temperature, ignition and boost limits are treated as one anti-knock system.

## 9. Working Homare 21 fuel/boost envelope — NOT YET FINAL CANON
Representative Homare 21 anchors remain approximately:

- takeoff/emergency: ~1,990–2,000 hp class;
- low-altitude rated: ~1,850–1,900 hp class;
- ~6.1–6.5 km rated: ~1,625–1,700 hp class.

Working operational interpretation for V8 maturity:

### Premium fuel
- rated +300/+350 mmHg-class operation is comparatively easy;
- +500 mmHg-class operation with ADI is the takeoff/emergency branch;
- premium fuel buys margin: less ADI dependency, better ignition/mixture freedom and more tolerance to hot/uneven cylinders.

### ~92-class fuel + ADI
- intended to retain most or nearly all standard rated performance after engine-side optimization;
- +300/+350-class rated operation is the main V8 target;
- +500-class emergency operation may be certified for short duration once the specific engine/airframe cooling system passes.

### ~88–90-class fuel + ADI
- deliberate derating is normal;
- approximately 15–25% below the best premium-fuel emergency output is a reasonable working envelope depending on altitude and oil/cooling condition;
- the goal is a healthy known-output engine, not an unknown nominal 2,000 hp engine.

### Low-grade fuel without ADI
- substantial boost restriction;
- training/return/emergency-survival use, not normal maximum combat setting.

## 10. Working lubricant × fuel service matrix — NOT FINAL CANON
For a mature 1943 Homare 21 installation:

- premium or ~92 fuel + ADI + L-P/L-Q-good: rated output is broadly usable;
- +500-class emergency boost begins as a ~3-minute certified setting and may reach ~5 minutes on airframes with adequate cooling/oil systems;
- L-Q lower-bound oil can shorten high-output duration and overhaul intervals even if instantaneous output is available;
- L-E oil normally blocks the high-emergency setting and forces a lower boost map.

Do not assume one duration for every Homare aircraft. Engine certification and airframe installation certification are separate.

## 11. Cooling / mixture distribution — CLOSED INTERPRETATION
V8 uses cylinder-by-cylinder thermal limits:

`T_limit = max(T_cyl_1 ... T_cyl_18)`

not average CHT.

Mixture-distribution improvement and cooling improvement are not separate horsepower bonuses if both merely lower the same worst-cylinder temperature. They raise the thermal/knock ceiling until another limit controls.

Low-pressure fuel injection may mature earlier as a comparison branch, but early Homare production need not wait for it if pressure-carburetion/intake distribution can meet the requirement.

## 12. Supercharger / ignition / control — CLOSED INTERPRETATION
The near-term Homare remains a mechanical-supercharger engine. V8 gains are:

- closer realization of designed compressor efficiency;
- lower charge-temperature scatter;
- more accurate two-speed operation;
- better ignition-timing uniformity;
- more precise mixture/metring/governor hardware.

A mechanical fuel-grade/boost-stop and ADI-flow interlock is plausible before electronic control:

- no adequate ADI flow -> emergency boost stop remains engaged;
- fuel-grade selector or maintenance setting changes permitted boost range.

## 13. Vibration — CLOSED INTERPRETATION
Asai measurement culture reduces blind trial-and-error but does not know Homare natural frequencies in advance.

Prototype/rig work must still map RPM/load/propeller-inertia dependent torsional modes. V8 gains faster identification of dangerous bands and more precise corrective work, not zero vibration.

## 14. Production replication — PRIMARY V8 DIVERGENCE
This remains the most important Homare advantage.

Use:
- port/profile master gauges;
- casting-core dimensional/process checks;
- sample flow testing;
- crank/bearing/gear acceptance gauges;
- dynamic-balance acceptance;
- hardness/case-depth checks;
- engine dynamometer corrected maps;
- lot/plant traceability;
- field-failure return linked to component lot.

Thus V8 shifts from "prototype engine achieved the number" toward "series engines cluster near the number".

The main service divergence is reduced mean loss **and reduced variance**.

## 15. V8 service-performance centers — WORKING
### 1941 prototype
- roughly historical design power; do not inflate headline hp;
- development advantage is test coverage and diagnosis.

### 1942 initial Homare 12 production
- good certified fuel/oil: ~1,780–1,825 hp takeoff-class good-lot realization;
- ~6 km: ~1,500–1,560 hp-class good-lot realization;
- standard fuel + ADI can support a strong but still conservatively certified combat envelope.

### late 1942 Homare 20/21 qualification
- takeoff/emergency working realization: ~1,900–2,000 hp depending on fuel/oil/installation;
- near ~6 km: ~1,580–1,650 hp during transition toward the 21-series service configuration.

### 1943Q1 branch-neutral technical-maturity checkpoint
- good qualified engine: ~1,950–2,000 hp takeoff-class;
- near ~6.1 km: broad good-engine band ~1,600–1,680 hp, center ~1,640–1,650 hp;
- ~1,700 hp at ~6 km is an upper favorable case, not the default center;
- this closes existence of a mature/reproducible specification, **not** fleet-wide production quality, TBO or theater reliability after 1943Q1.

## 16. Homare turbo branch — OPEN PERFORMANCE / CLOSED CAUSALITY
Historical turbo-supercharged Homare variants existed. V8 therefore does not invent the concept.

Asai makes earlier integration plausible because turbo hardware/control/high-altitude oil-system knowledge already exists before Homare.

Working development path:
- 1941H2: Homare + Asai turbo bench integration can begin;
- 1942H1: exhaust collection, wastegate, fuel/boost coordination, intercooler/heat-management and altitude-cell work;
- 1942H2: complete engine-package / aircraft integration trials are plausible;
- 1943: high-altitude reconnaissance/interceptor flight-test and limited mission-specific service candidate.

Turbo is **not** standard on ordinary A6M/Ki-43/J2M/N1K carrier/base fighters. Installation mass, ducting, intercooling, heat, fire protection and maintenance remain real costs.

## 17. Main conclusion — CLOSED
V8 Homare is not primarily "an earlier Homare" or "a higher-rated Homare".

It is:

> **a Homare that reaches roughly the historical design schedule and design output, but suffers a much smaller prototype -> production -> frontline performance cliff.**

This is the basis for later N1K/Reppu/Ki-84 performance work.
