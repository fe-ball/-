# 浅井世界線：単発中央後部GT機 一次サイジング V11

## Status
- Purpose: E5/E6 central-rear single-engine architecture sizing before adoption chronology.
- Classification: engine parent values = FIXED-UPSTREAM; airframe dimensions/mass/drag/range = DERIVED/SENSITIVITY; adoption = OPEN.
- Not a canonical aircraft type.

## 1. Engine parent
- E5 pure jet: 430–470 kgf pre-audit shadow; installed product audit remains open.
- E6-M pure jet: 850 kgf non-Ni / 900 kgf Ni engine-side product rating.
- E6-M aft-fan: 950–1,000 kgf; complete dry 610–690 kg, central 650 kg; BPR ~1, FPR ~1.30.

## 2. E6 working airframes

| item | E6 pure rear-engine | E6 aft-fan rear-engine |
|---|---:|---:|
| static thrust | 850–900 kgf | 950–1,000 kgf |
| propulsion dry sizing allowance | 480–540 kg (working inference, not parent spec) | 610–690 kg (parent) |
| normal loaded mass | 2.75–2.90 t | 3.05–3.25 t |
| wing area | 17–18 m² | 18–19.5 m² |
| wing loading | ~155–170 kg/m² | ~160–180 kg/m² |
| static T/W | ~0.30–0.33 | ~0.30–0.33 |
| internal fuel target | 850–950 L (~680–760 kg) | 950–1,050 L (~760–840 kg) |
| nose equipment design allowance | 220–280 kg | 220–300 kg |

Representative calculation points used below: pure 2,850 kg / 17.5 m² / 900 kgf / 730 kg fuel; fan 3,150 kg / 18.5 m² / 984 kgf / 800 kg fuel.

## 3. Intake sizing
First-order static capture sizing at sea-level density 1.225 kg/m³, nominal capture velocity 70–80 m/s, +20% margin:

- E6 core 13.2 kg/s: total capture area ~0.16–0.19 m². Twin side intakes: ~0.08–0.095 m² each, equivalent round diameter ~0.32–0.34 m.
- BPR~1 aft-fan if all air is taken through common forward intakes: total ~0.32–0.37 m². Twin common intakes become ~0.45–0.49 m equivalent diameter each: bulky.
- Preferred early aft-fan packaging for a free nose: core side intakes forward + separate aft/shoulder fan scoops, rather than one enormous common duct.

Arrangement ranking for armed/recon nose:
1. twin side/cheek or wing-root intake — default;
2. ventral intake — feasible but conflicts with centerline drop tank and FOD clearance;
3. dorsal intake — preserves belly but incurs high-angle/distortion risk;
4. nose intake — aerodynamically simple research configuration, but sacrifices the major nose-volume advantage.

## 4. Nose bay
Working geometry: ~1.8–2.2 m nose structural length ahead of cockpit, tapered section; after nose-gear bay, structure and sighting space, usable equipment volume ~0.45–0.60 m³.

Design the equipment/recoil frame for ~250 kg normal modular payload, ~300 kg growth allowance. The aft engine makes forward equipment useful for CG rather than merely tolerated.

Period/growth packages:
- early/light: rifle-calibre guns + camera/test equipment;
- 1940-era Navy-class fit: twin 20 mm Oerlikon/Type-99-class installation plus ammunition fits comfortably;
- 1941 Army-class fit: four 12.7 mm-class guns with belt ammunition is roughly a 200+ kg installed package and fits the design allowance;
- later growth: one 37 mm-class gun or later twin 20/30 mm-class packages are geometrically plausible if the 2.1–2.2 m structural gun bay and recoil path are provided from the start; actual weapon chronology remains military-side.
- recon: ~100–150 kg camera/film/heater/control package leaves margin for small gun/radio equipment.
- radar: nose volume is a future structural option only; radar program chronology is not auto-advanced.

## 5. Fuel and CG
Recommended internal distribution rather than a giant nose tank:

Pure ~900 L example:
- wing-root tanks 2 x 220–240 L = 440–480 L;
- fuselage/keel/saddle near CG 280–320 L;
- forward trim/service tank 120–160 L.

Fan ~1,000 L example:
- wing-root 480–520 L;
- central near-CG 320–360 L;
- forward trim 120–160 L.

Illustrative longitudinal mass model gives fuel-burn CG migration only ~0.05–0.09 m if most fuel is kept near the aerodynamic CG and the forward tank is scheduled as trim fuel. Do not make the forward nose tank the main tank.

## 6. Drop tanks
Kerosene-type fuel density assumed ~0.80 kg/L.

- standard operational external tank: 300–400 L centerline if side/cheek intakes are used. Fuel mass +240–320 kg.
- alternative for ventral intake: 2 x 200 L wing tanks.
- 500–600 L centerline is structurally possible as ferry-only, but adds ~400–480 kg fuel before tank/pylon mass, pushing the small interceptor into ~3.3–3.6 t territory and eroding takeoff/acceleration. Not preferred as normal combat fit.
- tank is jettisoned before maximum-speed interception; clean-aircraft performance should not be quoted with the tank retained.

## 7. Aerodynamic sensitivity
Simple drag polar used for sizing only:
- pure: representative Cd0=0.024, induced factor k=0.07, S=17.5 m²;
- fan: Cd0=0.029, k=0.07, S=18.5 m²;
- explicit compressibility drag rise begins around M0.60–0.70; no claim of a finished swept-wing design.
- thrust lapse used only as a sensitivity: 0.78 static at 6 km, 0.70 at 8 km, 0.62 at 10 km.

Representative level-speed solutions:
- E6 pure 900 kgf: ~660 km/h SL, ~765 km/h at 6 km, ~785 km/h at 8 km, ~795 km/h at 10 km.
- E6 pure 850 kgf: ~640 / 750 / 770 / 785 km/h.
- E6 aft-fan 984 kgf: ~610 km/h SL, ~720 km/h at 6 km, ~745 km/h at 8 km, ~765 km/h at 10 km.

Treat these as SENSITIVITY, not canonical performance. Intake recovery, installed mass, exact altitude thrust map, wing thickness/sweep and compressibility testing remain local aircraft gates.

## 8. Low-speed / takeoff
With CLmax ~1.6–1.8 and the working wing loadings:
- stall ~140–150 km/h;
- liftoff target ~165–180 km/h;
- first-order ground-roll estimate ~0.45–0.65 km for clean normal-load E6 variants; practical requirement should carry margin for spool response, runway condition and installation loss.

Aft-fan gains most clearly in takeoff/initial acceleration/loiter rather than an enormous small-airframe radius increase.

## 9. Range sensitivity
At ~6 km, simplified cruise calculations use:
- pure cruise TSFC working ~0.82 kg/(kgf h);
- aft-fan ~0.68 kg/(kgf h), consistent with the parent ~17% TSFC improvement over pure reference;
- 30% of internal fuel held for climb/combat/reserve rather than cruise.

Internal fuel only, representative 450–550 km/h cruise:
- pure: cruise-equivalent distance ~0.9–1.0 thousand km; practical round-trip combat radius order ~0.4–0.5 thousand km.
- aft-fan: ~1.0–1.1 thousand km; practical radius ~0.45–0.55 thousand km.

With +400 L (~320 kg) external fuel, before external-tank drag corrections:
- cruise-equivalent distance grows to roughly 1.3–1.4 thousand km;
- useful combat/ferry radius gain order ~150–220 km after climb/reserve and jettison assumptions.

A 600 L tank only adds another ~0.15–0.2 thousand km in this first-order model while imposing much worse takeoff/gear/handling burden; hence 300–400 L is the better standard scale.

## 10. E5 predecessor
For an E5 pure-jet rear-engine demonstrator at ~2.1–2.3 t and 430–470 kgf:
- static T/W ~0.19–0.22;
- simple sensitivity gives roughly ~550–600 km/h at 6–8 km;
- useful for intake/CG/control/high-speed/rear-engine architecture evidence, but not compelling enough to make the single-engine interceptor the first military GT adoption.

E5 aft-fan remains an installed-audit OPEN. Do not assign a product thrust here.

## 11. Working conclusion
The single central-rear architecture should not be restored as the first small GT fighter. It is better classified as:
- E5: full-scale future-form demonstrator;
- E6: credible operational interceptor/recon/fighter candidate;
- pure rear-engine branch: speed, thin-wing/compressibility and later reheat/swept-wing parent;
- aft-fan rear-engine branch: a slightly larger, lower-speed but more usable single-engine fighter architecture.

The nose should be designed from the outset as a modular ~250 kg mission bay and as a CG tool. Standard internal fuel around 0.9–1.0 m³ plus a 0.3–0.4 m³ jettisonable tank is the best first closure; a 0.6 m³ drop tank is ferry-special rather than standard combat equipment.
