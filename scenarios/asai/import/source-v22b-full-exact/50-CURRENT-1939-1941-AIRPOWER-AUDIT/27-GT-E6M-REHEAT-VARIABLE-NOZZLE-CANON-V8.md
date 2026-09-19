# GT E6-M REHEAT / VARIABLE-NOZZLE CANON — V8 AIRPOWER8

> **AIRPOWER8 research-backend authority.** This file closes the physical installed envelope of the already-current R2 reheat/variable-nozzle branch. It does not claim a 1939 flight-qualified or operational afterburning engine.

## 0. Parent

Baseline engine is the accepted E6-M-J non-Ni high-flow pure jet:

- 14.0 kg/s;
- PR7;
- TIT 870 C;
- dry static thrust ~850-854 kgf;
- dry full-static fuel ~682 kg/h;
- dry effective choked-nozzle throat ~0.0513 m2.

The reincarnator/advanced-branch authority already places tailpipe burner/flameholder/fuel-distribution and two-position/variable-area nozzle work at **R2 active by 1939-04-20**. The issue here is installed magnitude, not invention date.

## 1. Architecture

`E6-M gas generator -> main turbine -> short mixing/straightening section -> spray bars + flameholder -> cooled/double-wall reheat liner -> mechanically enlarged/variable convergent nozzle`

No downstream turbine is exposed to reheat gas. Therefore reheat outlet temperature is a tailpipe/liner/nozzle problem rather than an E6 turbine-blade TIT problem.

## 2. Installed static envelope

A 5% lit tailpipe total-pressure loss and ~95% reheat combustion efficiency give the following engineering map:

| reheat outlet gas | static thrust | gain vs ~853.5 dry | total fuel | TSFC | required throat | dry/wet area ratio |
|---|---:|---:|---:|---:|---:|---:|
| 900 C | ~943 kgf | +10.5% | ~1,041 kg/h | ~1.10 | 0.0616 m2 | 1.20 |
| **1000 C** | **~985 kgf** | **+15.4%** | ~1,178 kg/h | ~1.20 | **0.0644 m2** | **1.26** |
| 1050 C | ~1,005 kgf | +17.8% | ~1,247 kg/h | ~1.24 | 0.0657 | 1.28 |
| **1100 C** | **~1,025 kgf** | **+20.1%** | ~1,316 kg/h | ~1.28 | **0.0670** | **1.31** |
| 1150 C | ~1,045 kgf | +22.5% | ~1,385 kg/h | ~1.32 | 0.0683 | 1.33 |
| **1200 C** | **~1,065 kgf** | **+24.8%** | ~1,453 kg/h | ~1.36 | **0.0696** | **1.36** |
| 1300 C rig ceiling | ~1,103 kgf | +29.3% | ~1,591 kg/h | ~1.44 | 0.0721 | 1.41 |

This explains the old roadmap expectation that an early reheat backend should buy roughly the low-20-percent thrust class rather than a free doubling.

## 3. Practical 1939-41 development ladder

### 1939 R2 current rig

The current test branch can reasonably occupy roughly **900-1000 C reheat outlet**, demonstrating flameholding, pressure loss, fuel distribution and nozzle-area scheduling. This is about +10-15% static thrust in the installed model.

### 1940 first flight-development target

Once hot-duct/nozzle endurance and relight/stability pass, a **1050-1150 C** outlet band gives about **1.00-1.05 tf**, roughly +18-22% over the 870 C dry E6-M-J.

### mature research target

**~1200 C / ~1.065 tf** is a natural next research coordinate. It is not a continuous service rating. The selected ~1300 C / ~1.10 tf point is retained as a demanding rig/short-test ceiling until liner/nozzle evidence earns more.

The exact cumulative wet-minute budget remains OPEN and must come from teardown evidence; initial use is explicitly short-duration research duty.

## 4. Variable nozzle

A fixed dry nozzle cannot serve the useful reheat range efficiently. The required effective throat grows from ~0.0513 m2 dry to roughly:

- 0.0644 m2 at 1000 C;
- 0.0670 m2 at 1100 C;
- 0.0696 m2 at 1200 C.

Thus the useful wet range requires approximately **+25 to +36% throat area**. A mechanically scheduled two-position nozzle is sufficient for early dry/wet testing; a continuously scheduled mechanism is a later refinement, not a prerequisite for first reheat flight.

Equivalent circular wet throat is roughly 0.286-0.298 m across the 1000-1200 C band.

## 5. Package mass / length

The reheat backend is materially lighter than the E6-M JF free-turbine/fan module because it has no additional high-power rotating spool.

Working installed addition:

- spray bars / manifolds / flameholder: ~8-14 kg;
- double-wall liner / local cooling / outer tailpipe: ~15-25 kg;
- enlarged/variable nozzle petals or plug/ring mechanism + actuation: ~18-28 kg;
- fuel control/lines/ignition/local structure: ~8-14 kg;
- **total addition ~55-85 kg, center ~70 kg**;
- added package length **~0.45-0.65 m**.

Therefore an E6-M-JR research engine is roughly **~570-625 kg dry**, center around **~595 kg**, before aircraft-specific intake/mount/fairing.

## 6. 1939-04-20 state

- flameholder/spray/fuel-distribution hardware: R1-R2 paid;
- short static reheat rear-end rig: **R2 active**;
- two-position / variable-nozzle rig: R1-R2 active;
- complete flight-qualified E6-M-JR: **not yet R4**;
- installed target for HS-3 may be defined now without waiting for E7, but first-flight release remains a 1940-41 local gate.

## 7. Consequence for high-speed research

HS-3 should not wait for E7. Its natural sequence is:

1. E6-M-J dry, ~850-900 kgf class, to map M0.8-0.95;
2. same E6-M gas generator + research reheat backend, initially ~1.0 tf and later ~1.05-1.10 tf, to control acceleration through the drag-rise region and approach the M1 research gate;
3. E7 may later replace the gas generator, but that is a separate experimental variable.

## 8. Closed / open

CLOSED:
- E6-M reheat architecture;
- static thrust/fuel/nozzle-area response through the useful early research range;
- early two-position nozzle area requirement;
- package mass/length working envelope;
- 1939 R2 and 1940-41 flight-development relationship.

OPEN:
- exact wet endurance/minute budget;
- flight relight/blowout/envelope;
- measured altitude/Mach augmentation;
- operational military afterburner adoption;
- higher-temperature service package.
