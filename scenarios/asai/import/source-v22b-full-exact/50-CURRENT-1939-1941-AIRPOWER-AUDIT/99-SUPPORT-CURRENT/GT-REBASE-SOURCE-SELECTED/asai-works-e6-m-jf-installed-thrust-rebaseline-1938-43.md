# E6-M-J / JF installed-thrust rebaseline — 1938–43

> **v46 current authority.** This file closes the E6-M pure-jet and aft-fan engine-side installed-thrust audit. It does **not** propagate the new thrust into aircraft speed/range/climb; those remain H→A gates.

## 1. Upstream identities held fixed

- Compressor authority: v43 E6-M = **PR7, 14-stage all-axial, 13.2 kg/s central / 12.5–14.0 kg/s full-speed trim**.
- Jet/JF product uses the **14.0 kg/s high-flow trim**.
- Shaft-cycle authority: v44. Gross Brayton work is not converted directly into thrust.
- Sea-level audit coordinate: 288 K / 101.325 kPa; inlet recovery 0.99; compressor η≈0.84; combustor ΔPt≈3%; main turbine η≈0.84; nozzle η≈0.94.
- Fuel accounting follows v44: staged bleed, combustor efficiency and accessory/mechanical debit are paid before product figures are quoted.

Reproducible model:

- `computation-2026-08-22/e6_m_jf_installed_thrust_v46.py`
- `computation-2026-08-22/E6-M-J-JF-INSTALLED-THRUST-V46.tsv`
- `computation-2026-08-22/E6-M-JF-FAN-SIZE-V46.tsv`

## 2. Pure turbojet result

The main turbine first pays the E6 compressor and accessory bill. Only the resulting turbine-exit total state is expanded through the propulsive nozzle.

| product point | TIT / bleed | calculated static thrust | calculated TSFC | v46 product headline |
|---|---:|---:|---:|---:|
| E6-M-J long-life comparison | 835°C / 5.25% | ~814 kgf | ~0.785 kg/(kgf h) | comparison only |
| **E6-M-J non-Ni** | **870°C / 5.0%** | **~854 kgf** | **~0.797** | **~850 kgf/engine** |
| **E6-M-N-J Ni** | **920°C / 4.5%** | **~907 kgf** | **~0.817** | **~900 kgf/engine** |

The old E6-M-J / E6-M-N-J **~500 kgf** product anchor is therefore **SUPERSEDED**. It was a deliberately conservative empirical placeholder left after gross-work-to-thrust was prohibited; v46 now supplies the missing installed nozzle work balance.

The higher-TIT Ni engine gains thrust and hot/high margin, but its static TSFC does not automatically improve because more fuel is being burned at the product point. Ni remains principally a temperature/life/altitude capability, not a free fuel-economy multiplier.

## 3. E6-M-JF aft-fan architecture

The production JF is not a single-spool turbojet with a passive fan. Its correct architecture is:

> **single-spool E6-M gas generator → separate one-stage free LP turbine → direct-drive single-stage aft fan + stator → separate core and bypass exhausts**

Thus the gas-generator compressor remains single-spool, but JF adds an **independent free-LP-turbine/fan spool**. Old wording `二軸化せず尻に足す` is acceptable only if it means “do not redesign the gas-generator compressor as a two-spool compressor”; it is not acceptable if it denies the added rotating spool.

### Standard v46 JF point

- core inlet flow: **14.0 kg/s**
- non-Ni long-life TIT: **~835°C** (about 35°C below the 870°C pure-jet point)
- cooling/bleed: **~5.25%**
- bypass ratio: **~1.0**
- fan pressure ratio: **~1.30**
- fan efficiency: **~0.80**
- fan-drive efficiency: **~0.97**
- free turbine efficiency: **~0.82**
- bypass duct pressure recovery: **~0.96**

At this point:

- fan shaft demand = **~394 kW**;
- free-LP-turbine extraction = **~406 kW**;
- free-LP-turbine temperature drop = **~26 K**;
- core stream thrust after the free turbine = **~717 kgf**;
- bypass/fan stream thrust = **~267 kgf**;
- total static thrust = **~984 kgf**;
- TSFC = **~0.649 kg/(kgf h)**.

Against the **same 835°C** pure-jet comparison (~814 kgf / ~0.785 TSFC), the aft fan gives approximately:

- **+20.9% static thrust**;
- **−17.3% TSFC**.

Therefore the old blanket **+30–40% thrust / −20–30% fuel** rule is superseded for E6-M. The v46 product headline is **~950–1,000 kgf/engine**, with **~1,000 kgf class** used for catalog-level discussion.

## 4. Fan-pressure and bypass sensitivity

At BPR=1.0:

| FPR | static thrust | TSFC | free-turbine power |
|---:|---:|---:|---:|
| 1.25 | ~973 kgf | ~0.657 | ~344 kW |
| **1.30** | **~984 kgf** | **~0.649** | **~406 kW** |
| 1.35 | ~994 kgf | ~0.643 | ~468 kW |
| 1.40 | ~1,002 kgf | ~0.638 | ~527 kW |

At FPR=1.30, varying BPR from 0.85 to 1.15 gives roughly **959–1,010 kgf**. The gain above FPR~1.30 is modest while turbine work, blade speed, duct area and weight continue to rise. Therefore **FPR≈1.30 / BPR≈1.0** is the production center rather than chasing the maximum static-thrust corner.

## 5. Fan geometry and rotational speed

For a 14 kg/s bypass stream at sea-level static conditions, an annulus with axial velocity about 105–120 m/s and hub/tip ratio 0.70–0.74 requires a fan tip diameter of roughly **0.49–0.55 m**. The v46 central geometry is:

- bypass axial velocity: **~110 m/s**;
- hub/tip ratio: **~0.72**;
- fan tip diameter: **~0.52 m**;
- fan hub diameter: **~0.38 m**;
- stage loading coefficient ψ: **~0.46**;
- tip speed: **~247 m/s**;
- direct fan/free-turbine speed: **~9,000 rpm**;
- combined axial/tangential tip-relative Mach: **~0.80**.

Release band: **fan tip 0.50–0.55 m, ~8.5–9.5 krpm**, with local blade-count/solidity/stator tuning. The central point does not require a highly loaded or transonic fan.

## 6. Package size and mass

The aft module is treated as a real engine module, not a weightless “cold part”. A v46 engineering ledger is:

| item | working mass |
|---|---:|
| fan rotor + stator + local casing | 35–50 kg |
| one-stage free LP turbine + nozzle row | 25–35 kg |
| shaft, bearings, seals, support frame | 15–25 kg |
| bypass duct / rear casing / reinforcement | 20–30 kg |
| controls, actuation, oil and local accessories | 5–10 kg |
| **aft-module addition** | **~100–150 kg; central ~125 kg** |

This closes the long-standing aircraft mass anchor rather than replacing it: **E6-M-JF dry mass ~610–690 kg/engine, central ~650 kg**, so a twin installation remains approximately **1.30 t engine dry mass** before airframe-specific intake/pylon/nacelle structure.

Working package envelope:

- aft-module added length: **~0.60–0.75 m**;
- fan tip: **~0.52 m** central;
- nacelle maximum OD: **~0.66–0.72 m** after casing, bypass duct and clearance.

The larger rear frontal/wetted area is an aircraft drag/CG/structure debit and is **not** converted here into a new top speed.

## 7. Historical calibration, not calendar import

Two later/parallel anchors show the architecture is physically real without being copied wholesale into the worldline:

- Metropolitan-Vickers F.3 used an F.2 gas generator with a turbine-driven aft-mounted ducted fan; testing began in 1943 and contemporary reporting credited a much larger thrust gain than v46, but with a significant weight increase.
- GE CJ805-23 later used a single-stage aft fan and a one-stage free turbine; its published takeoff-thrust gain and SFC reduction likewise demonstrate the aft-fan/free-turbine trade, but at different pressure ratio, scale and maturity.

v46 intentionally sits below those more aggressive thrust-gain ratios because E6 uses **BPR≈1 / FPR≈1.30** and preserves a long-life non-Ni thermal point.

## 8. Canonical verdict

### Current engine authority

- **E6-M-J non-Ni:** ~**850 kgf/engine** static product rating.
- **E6-M-N-J Ni:** ~**900 kgf/engine** static product rating.
- **E6-M-JF production:** **~950–1,000 kgf/engine**, central installed calculation ~984 kgf at 835°C.
- JF fan: **BPR~1.0, FPR~1.30, ~0.52 m tip, ~9 krpm**.
- JF free turbine: **one stage, ~0.41 MW extraction**.
- JF aft-module mass: **~100–150 kg**, total engine dry **~610–690 kg**, central ~650 kg.

### Superseded

- E6-M-J / E6-M-N-J = ~500 kgf as current product thrust.
- E6-M-JF = 650–700 kgf as current product thrust.
- blanket JF `+30–40% static thrust / −20–30% SFC` for E6-M.
- any interpretation of `二軸化せず` that removes the free-LP-turbine/fan spool.

### Still gated — do not auto-propagate

The following existing aircraft values become **A_old / conditional until dedicated H→A**:

- Hekireki 11/21 speed, climb, takeoff and range;
- Sakufu prototype / 11 / 21 carrier takeoff and speed;
- CFRP aircraft using twin E6-M-JF;
- jet trainer and cheap single-engine E6-M-J derivatives;
- any twin-engine thrust-weight ratio based on 1,000 or 1,300–1,400 kgf total.

The engine thrust increase is real, but higher nacelle diameter, rear wetted area, mass distribution, inlet/nozzle matching and fuel flow must be paid at aircraft level.
