# Carrier GT working calculations — NOT adoption canon

## A. General carrier conclusion from this conversation

Old concept: `steam main propulsion + GT boost for 30–60 min`.

New result after E6 scale study:

- E6 large GT blocks can often produce the **entire cruising power**, not merely a 1–2 kt boost.
- Therefore the architecture can invert to `GT cruise / steam high-power / both at maximum`.
- On new-builds, GT may become a co-equal second main plant and allow a smaller steam plant.
- On conversions, the main difficulty is often **shaft/reduction-gear reconstruction and airflow routing**, not GT core mass.

No specific carrier adoption is closed here.

## B. Taiyo-class style worked example used in discussion

Old baseline from the earlier carrier worksheet:

- steam: ~25,200 shp
- baseline speed: ~21 kt
- old target: ~25.5 kt
- cube-law required total power ~45,100 shp -> ~19,900 shp added GT

### New E6-甲 ×4 working arrangement

Use four analysis-class E6 甲 machines, two per shaft.

| GT rating | per engine | four engines | GT-only cube-law speed | steam+GT cube-law speed |
|---|---:|---:|---:|---:|
| 780C long-life | ~4,110 hp | ~16,440 | ~18.21 kt | ~24.83 kt |
| 800C continuous | ~4,340 | ~17,360 | ~18.55 | ~25.01 |
| 820C normal | ~4,570 | ~18,280 | ~18.87 | ~25.19 |
| 870C maximum | ~5,140 | ~20,560 | ~19.62 | ~25.62 |

### Part-engine GT-only cube-law points at 780C

- 1 engine: ~11.5 kt
- 2 engines: ~14.5 kt
- 3 engines: ~16.5 kt
- 4 engines: ~18.2 kt

Interpretation: the four GTs are a credible **cruise propulsion system**, not a boost-only package.

### Working fuel numbers

- four E6-甲 at 780C: ~4.95 t/h near full long-life point
- exact 18 kt required output ~15,870 shp -> ~97% of the 4-engine long-life total
- working 18 kt fuel ~4.78 t/h
- 6,500 nmi / 18 kt = ~361 h
- pure propulsion fuel ~1,726 t
- with reserve/operational margin: ~1,850–1,950 t GT distillate design band

Fuel identity used: clean broad-range marine turbine distillate, roughly kerosene-tail through gas-oil range, LHV ~42 MJ/kg.

### Shaft/reduction redesign

Two shafts. Per shaft:

- existing steam ~12,600 shp
- + two E6-甲 long-life ~8,220 -> ~20,820 shp
- + two E6-甲 max ~10,280 -> ~22,880 shp

Therefore the old idea `add a GT pinion to the existing gear` is retired.

Working design requirement:

- rebuild each shaft train for ~23,000 shp
- new combined steam/GT reduction arrangement
- shaft diameter ~18–22% higher than the old same-material torque basis (cube-root torque scaling)
- new propeller around ~5.1–5.3 m, ~220–240 rpm working study band
- exact hull clearance/cavitation requires model-basin calculation

### Intake/exhaust

Four E6-甲 total intake mass flow:

- 29.7 × 4 = **118.8 kg/s**
- sea-level volume ~97 m3/s working estimate
- practical intake opening total ~7–8 m2 after separator/screen allowance

Hot exhaust total working volume can be ~240 m3/s around ~450C order of magnitude.

- exhaust effective area ~8–10 m2 working band
- combined intake/exhaust trunk floor footprint with structure/insulation/access ~20–25 m2 order of magnitude

Working conclusion: hanger loss is not automatically catastrophic; routing geometry matters more than raw area. Expect local unusable parking/handling zones rather than simply subtracting 10 m of hangar length.

### Working installed-weight increment

Net increment versus the old ship machinery, not a closed detailed weight estimate:

- four E6-甲 + foundations/accessories: +25–35 t
- stronger combined reduction gear: +30–50 t
- stronger shaft line: +15–25 t
- new propellers: +5–10 t
- intake/exhaust/separators/insulation/dampers: +30–45 t
- lube/start/fire/piping: +10–20 t
- total **~115–185 t**
- with meaningful exhaust-heat recovery: **~150–240 t**

These numbers are deliberately broad and should be recalculated against actual ship arrangement drawings before closure.

## C. Carrier architecture ladder to compare later

For any actual carrier/refit window, compare at least:

A. 1–2 large GTs as literal boost auxiliaries
B. 2 large GTs as cruise/emergency propulsion
C. 4 GT blocks as an independent second main plant
D. new-build reduced steam plant + GT co-main propulsion

For 4-shaft carriers, E6-乙×4 may integrate more cleanly than E6-丙×2 because `one GT per shaft` can avoid large cross-connecting gear. E6-丙 becomes stronger when the shaft system is designed around it from the beginning.

## D. Carrier items explicitly left OPEN

- Kaga conversion machinery implementation
- Akagi conversion machinery implementation
- Soryu/Hiryu design consequences
- Taiyo-class actual adoption
- Junyo/Hiyo consequences
- Unryu-class / 雲龍系 consequences
- exact WOD threshold after aviation reset
- exact hangar/duct arrangements
- exact exhaust-boiler mass/benefit

Do not propagate the Taiyo worked example to all carriers automatically.

