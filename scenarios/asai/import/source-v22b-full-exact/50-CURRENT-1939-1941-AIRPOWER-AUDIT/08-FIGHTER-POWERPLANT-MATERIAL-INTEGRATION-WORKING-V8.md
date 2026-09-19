# FIGHTER POWERPLANT / MATERIAL INTEGRATION — WORKING AUDIT V8

## Status
**WORKING, NOT FINAL CANON.**
This file records the current quantitative envelope so later chats do not silently revert to older support values.
Exact speeds, weights, climb times, ranges and procurement outcomes remain open to airframe, production and war-history closure.

**AIRPOWER4 NOTE:** file 15 is now the canon authority for high-power propeller/cooling technology availability and `PA/CI` state semantics; file 16 is the canon authority for branch-neutral 1940-1943Q1 aircraft-integration chronology. Numerical performance envelopes in this file remain WORKING.

## 1. Corrected engine anchors
Use approximately the following historical/reference points as current working anchors:

- Sakae 21: ~1,130 hp takeoff; ~1,070 hp @ 2.85 km; ~940 hp @ 6 km.
- Kinsei 54: ~1,300 hp takeoff; ~1,200 hp @ 3 km; ~1,100 hp @ 6.2 km.
- Kinsei 62: ~1,560 hp takeoff; ~1,340 hp @ 2.1 km; ~1,190 hp @ 5.8 km.
- Homare 12: ~1,825 hp takeoff; ~1,560 hp class near 6.5 km.
- Homare 21/22: historical/reference ~1,990–2,000 hp takeoff and ~1,625 hp near 6.1 km; V8 1943Q1 good-engine realization broad ~1,600–1,680 hp near ~6.1 km, center ~1,640–1,650.
- Ha-43-11: ~2,200 hp takeoff; ~2,050 hp @ 1 km; ~1,820 hp @ 6.6 km.

Old working use of Sakae 21 at ~980 hp/6 km should be treated as superseded by the ~940 hp anchor.

## 2. Material technology use — WORKING RULE
V8 material gains are applied part-by-part, not as generic Cd0 or total-airframe percentage bonuses.

Current material picture:
- paper honeycomb / bonded sandwich: mature enough by the late 1930s for large secondary/semi-structural flight applications;
- plant-fiber FRP/epoxy: useful for fairings, ducts, covers and selected structures;
- bonded metal: important in smooth secondary skins/panels and part-count reduction;
- GFRP: selective early-1940s structural/secondary use, not a universal primary structure;
- CFRP: experimental/small local reinforcement only, not a mass-production fighter primary structure.

Primary spar caps, landing gear, engine mount, firewall and other concentrated-load parts remain metal unless separately proven.

### Current net mass-reduction centers
After reinserting inserts, sealing, minimum thickness, repair margin, carrier local reinforcement, etc.:

- existing A6M minor retrofit: ~15–30 kg;
- redesigned later A6M: ~25–45 kg;
- N1K1-J: ~25–55 kg;
- N1K2-J redesign-origin: ~40–70/75 kg;
- Reppu design-origin 3–8 t class: ~45–80 kg, center ~60–70 kg.

Do not turn these directly into speed bonuses.

## 3. Propeller / reduction / cooling logic — SUPERSEDED CHRONOLOGY
The old short chronology in this section is superseded by:
- `15-HIGH-POWER-PROPELLER-COOLING-INTEGRATION-CANON-V8.md`;
- `16-PREBRANCH-HOMARE-HA43-AIRFRAME-INTEGRATION-CANON-V8.md`;
- `17-PREBRANCH-AIRFRAME-INTEGRATION-STATE-LEDGER-V8.tsv`.

Retain only these numerical installation anchors here for performance work:

### Historical Reppu Homare reference (historical A7M; worldline designation A9M)
- roughly 3.6 m four-blade propeller class;
- Homare special reduction ratio around 0.422 remains a meaningful system choice;
- at 3,000 rpm this gives ~1,266 prop rpm;
- AIRPOWER4 first-order guard: at ~620 km/h around 6 km, 3.6 m / 1,266 rpm gives helical tip speed roughly Mach 0.93.

### Historical Reppu Ha-43 reference (historical A7M; worldline designation A9M)
- approximately the same 3.6 m diameter class is plausible;
- Ha-43 reduction around 0.472 and ~2,800 rpm gives ~1,322 prop rpm;
- AIRPOWER4 first-order guard: at ~630 km/h around 6 km, 3.6 m / 1,322 rpm gives helical tip speed roughly Mach 0.96.

These are compressibility/integration guards, not final propeller-efficiency calculations. Homare and Ha-43 variants still require separate cowl/cooling/propeller qualification; engine hp cannot be swapped with no installation penalty.

## 4. Historical Reppu / worldline A9M mass audit — CURRENT WORKING ENVELOPE
Historical anchors:
- **historical A7M1 Reppu (worldline A9M anchor):** empty ~3,110 kg; loaded ~4,410 kg class.
- **historical A7M2 Reppu (worldline A9M anchor):** empty ~3,226 kg; loaded ~4,720 kg class.

V8 material/application effects are now treated separately from mission load.

### Homare Reppu equivalent
- empty: ~3.03–3.07 t working;
- normal combat/internal-fuel state: ~4.05–4.15 t working;
- heavy/long-range/historical-loaded-equivalent: ~4.33–4.37 t working.

### Ha-43 Reppu equivalent
- empty: ~3.14–3.19 t working;
- normal combat/internal-fuel state: ~4.20–4.32 t working;
- heavy/long-range/historical-loaded-equivalent: ~4.63–4.68 t working.

Do not use one "loaded weight" for every maneuver/range calculation.

## 5. Reppu wing loading — WORKING
With ~30.86 m² wing area:

### Homare
- normal combat ~4.10 t -> ~133 kg/m²;
- heavy ~4.35 t -> ~141 kg/m².

### Ha-43
- normal combat ~4.26 t -> ~138 kg/m²;
- heavy ~4.65 t -> ~151 kg/m².

This is a major guardrail: Reppu is a large aircraft but not automatically a high-wing-loading heavy fighter. The historical requirement lineage retained Zero-like maneuvering emphasis.

## 6. Reppu performance envelope — WORKING
Historical A7M1 Reppu underperformance (used only as an H-anchor for worldline A9M, **not worldline A7M Gaifu**) should **not** be copied directly into V8 because its Homare high-altitude realized power was far below the intended design point.

Current V8 working ranges:

### Homare Reppu
- 6 km service power: ~1,630–1,680 hp for a mature good installation, center ~1,650; upper end requires a favorable engine/induction/cooling realization;
- maximum speed: broad audit ~610–624 km/h; center ~615–620;
- 6 km climb, normal combat: ~5:35–5:55;
- 6 km climb, heavy state: ~5:55–6:15.

### Ha-43 Reppu
- 6 km service power: ~1,800 hp class;
- maximum speed: ~625–632 km/h working;
- 6 km climb, normal combat: ~5:20–5:45;
- heavy-state climb remains materially better than a similarly loaded Homare variant.

These are not canon test results.

## 7. Reppu engine-selection interpretation — CURRENT WORKING CONCLUSION
V8 no longer supports the simplistic history-derived chain:

`Homare Reppu = failed prototype -> Ha-43 = rescue`.

Current rational program shape is:

- **Homare 21/22 Reppu = earlier/light carrier-fighter branch**, with meaningful service value if Homare realizes design output;
- **Ha-43 Reppu = growth / heavy-armament / protection / fuel / altitude-margin branch**.

Parallel engine installation design is rational because:
- Homare is earlier in production and lighter/smaller;
- Ha-43 provides greater absolute power and long-term growth;
- by the 1942 requirement window neither choice is so dominant that the other should be discarded without flight/production evidence.

Exact designation/numbering is NOT reclosed; use "Reppu equivalent" where support naming conflicts exist.

## 8. Reppu armament / protection — WORKING
Do not buy V8 performance by deleting historical protection.
Historical Reppu design already moved toward self-sealing tanks, armor and armored windscreen.

A four-20 mm main armament is a plausible 1943-class V8 target. The gun-body mass increase over a mixed 13.2 mm + 20 mm battery is only tens of kilograms once ammunition is included, not hundreds.

Material savings are better spent maintaining protection and armament/fuel than creating a paper-light unprotected aircraft.

## 9. A6M / Kinsei bridge — WORKING
Earlier V8 discussion that treated a late fully equipped A6M8 as a ~2.86 t aircraft was too light.

Use:
- lightweight early-to-mid-war Kinsei conversion concept: ~2.85–3.0 t depending on protection/fuel/armament;
- maximum-speed central band: ~585–598 km/h;
- >600 km/h is possible only for an unusually clean/light/high-quality configuration, not the default.

The Kinsei Zero's main value is:
- strong power-to-weight and climb/reacceleration;
- existing carrier footprint / production familiarity;
- bridge timing before a large new carrier fighter matures.

Its costs remain:
- larger nose/propeller/cooling installation;
- fuel/range penalty versus Sakae Zero;
- limited growth margin around the small A6M airframe.

## 10. N1K1 / N1K2 — WORKING
Better Homare does not erase N1K1-J's mid-wing / long-complex-gear / installation problems.

### N1K1-J V8
- still a short-lived bridge/test/service aircraft;
- speed center roughly high-580s/low-590s, not the paper ~649 km/h goal;
- V8 Homare benefits climb, reacceleration, repeatability and sortie reliability more than headline speed.

### N1K2-J V8
- low-wing/short-gear/fuselage redesign remains strongly motivated;
- V8 material saving ~40–70/75 kg can be additional to the historical structural cleanup, but must not double-count the historical ~250 kg redesign saving;
- working speed ~598–607 km/h;
- 6 km climb ~6 minutes class rather than historical ~7+ minutes if Homare service realization is strong.

Automatic combat flap remains primarily a transient/high-lift combat aid, not a conversion into A6M-like sustained turn performance.

## 11. High-altitude split — WORKING
Single-stage/two-speed Sakae/Kinsei/Homare/Ha-43 fighters all begin to lose relative position above their full-throttle heights.

Demand generation above roughly 8 km naturally creates separate branches:
- higher-stage mechanical supercharging;
- Homare turbo variants;
- three-speed/high-altitude Ha-43;
- Ha-43 turbo dedicated interceptor.

Do not make turbo standard on the ordinary carrier fighter solely because the technology exists.

## 12. Current comparison shorthand — WORKING ONLY
For future discussions use these centers rather than older unsupported values:

- A6M Kinsei bridge: ~2.9 t, ~590 km/h class;
- N1K2 V8: ~3.8–4.0 t normal combat, ~600 km/h class, ~6 km / ~6 min class;
- Homare Reppu: ~4.1 t normal combat, ~615–620 km/h center;
- Ha-43 Reppu: ~4.25 t normal combat, ~628 km/h center.

Procurement demand, production quantity and final service dates remain dependent on the war-history branch and R0–R6 requirement revalidation.
