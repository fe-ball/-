# 1939-04-20 HISTORICAL VEHICLE DELTA — CANON — V8 AIRPOWER14

> Purpose: compact replay-facing authority for **historically existing Japanese vehicles/aircraft that are already altered by Asai capability by 1939-04-20**. This is not a catalogue of Asai-original research vehicles.
>
> **IDENTITY1 integration:** before copying a historical datasheet for a same-named item, consult `50-HISTORICAL-DESIGNATION-NOT-IDENTICAL-HARDWARE-GUARD-V8.md` / `50A`. Exhaust-specific state is controlled by `49/49A`; fire-control/sighting/bombing realization is controlled by `51/51A`. A historical designation is not proof of identical worldline hardware or identical combat fire effect.

## 1. General rule

Asai effects on historical vehicles divide into three layers:

1. **visible configuration change** — the design window was still open and Asai hardware/methods entered the vehicle itself;
2. **installed-system / production change** — external shape is near historical, but engine/propeller/boost/cooling/transmission/QC differs;
3. **readiness/support change** — headline specification remains near history while reproducibility, maintenance, mission preparation and field support improve.

Do not convert layer 2/3 effects into invented headline speed, armor or armament gains without a local calculation/test.

## 2. Representative aircraft already affected

### A6M1 / 12-Shi carrier fighter
- current V7 first-flight window: **1939-03-24 to 26**;
- Z-900N ~900 hp working engine state;
- **three-blade constant-speed propeller from first flight**;
- thrust-exhaust integration is design-origin rather than a late retrofit;
- Asai effect also enters governor, vibration/cooling instrumentation and production-test method.

This is a visible configuration difference. It does **not** auto-select the later production engine: 1940 production main engine remains Sakae 12 unless a later replay gate changes that decision.

### Ki-43 prototypes
- initial prototype clock remains close to history;
- the main delta is a stronger 2-/3-blade, pitch/governor, cooling, CG, handling and pilot-evaluation loop;
- no 1939 mass-service result is imported.

### Ki-27, G3M, Ki-15, Ki-21, Ki-30, B5N/H6K-class historical aircraft
- basic airframe/mission architecture remains broadly historical at this checkpoint;
- Asai effects concentrate in engine/propeller matching, bearings, cooling, vibration, gauges/QC, maintenance, photographic/bombing workflow and serviceability;
- **Ki-27 and several Navy/Army types also have lot-/variant-dependent exhaust deltas closed in `49/49A`;** this does not authorize a generic speed bonus for every airframe;
- **B5N2 old `historical individual exhaust -> E1=0` is superseded** by `49/49A`; current working historical state is EX0 collector-ring and later worldline lots may differ;
- replay should prefer local type/lot audit plus higher reproducibility/readiness rather than invented blanket headline-performance deltas.

## 3. Type 97 Chi-Ha power closure

The earlier branch value **180 PS continuous / 200 PS maximum** is superseded for new 1939 calculations.

The later v27 tank parent closes the 1938 mass-production center at:

- Mitsubishi V12 diesel + Asai low-pressure turbo/intake integration;
- **200 hp continuous**;
- **220 hp short-duration**;
- 220-240 hp remains reinforced-chassis/test territory rather than ordinary production rating.

This value changes mobility/power margin and heat/cooling load. It does not change the low-velocity 57 mm gun into an anti-tank gun and does not create a different armor doctrine.

For the **South Nanchang operation/current center branch**, Chi-Ha still does **not** participate in combat; existing Type 89/94 armored assets remain the trained/logistical choice. Power closure and theater allocation are separate ledgers.

## 4. Type 95 Ha-Go

- ordinary mass-production line remains approximately the historical 120 hp naturally aspirated class;
- Asai turbo is reserved for high-altitude/hot-weather/special comparison branches where maintaining roughly 120-125 hp with altitude matters;
- 140-145 hp class remains limited test territory at this checkpoint.

Do not turn all Ha-Go into boosted high-output vehicles merely because the turbo capability exists.

## 5. Heavy trucks / artillery tractors / workshop-recovery vehicles

This is one of the largest existing ground-vehicle changes:

- low-pressure turbo-diesel is concentrated where towing, altitude and heavy auxiliary loads justify it;
- filters, injection control, cooling, gearbox/bearing/heat-treatment and standardized service packages improve;
- mobile generators, winches, machine-tool/workshop and recovery packages are a system effect, not merely a higher engine rating.

Ordinary light vehicles and tankettes remain much closer to historical configuration.

## 6. Replay use

For a historical vehicle appearing after Apr20:

0. **resolve designation identity in `50/50A` first** — especially Navy `A7M` (worldline Gaifu) versus historical Reppu (worldline `A9M`);
1. check whether its design freeze allowed Asai hardware to enter;
2. check lot/variant state and whether the chosen historical performance anchor already contains the improvement;
3. if yes, apply only the remaining installed-system delta already closed here/upstream;
4. if no, apply production/QC/service effects only;
5. use `49/49A` for piston-exhaust state-differential accounting;
6. use `51/51A` before copying historical hit-rate / bombing-dispersion / sighting-effect assumptions;
7. keep procurement, allocation, named-unit fit and combat result event-dependent.

This file supersedes `180/200 hp` Chi-Ha wording for current 1939 replay calculations while preserving older files as provenance.


## Naval ship / carrier guard

Historical ship names/classes are not covered by aircraft headline-delta shortcuts. Use `50` Section 7 / `50A` for same-name ship cautions, `42-MARINE-GT-1939-04-20-STATE-CANON-V8.md` for Apr20 marine-GT state, and the selected large-marine rebaseline for propulsion integration. In particular, carrier speed, WOD, aircraft capacity, aircraft compatibility and sortie generation are separate gates.


## NOMONHAN-A2 mobility routing
For Chi-Ha battlefield mobility/trajectory replay, use `52-RELATIVE-MOBILITY-GEOMETRY-TIMING-CANON-V8.md`. Current working combat-mass band is 15.3-15.6 t; 200/220 hp does not authorize a top-speed multiplier or copying historical individual vehicle geometry.
