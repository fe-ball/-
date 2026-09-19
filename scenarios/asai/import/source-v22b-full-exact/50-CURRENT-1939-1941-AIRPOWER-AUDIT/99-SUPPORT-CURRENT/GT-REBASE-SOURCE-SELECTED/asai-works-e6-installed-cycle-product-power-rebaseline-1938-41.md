# 124 — E6 installed-cycle / product-power rebaseline — v44

> Status: **ACCEPTED v44 semantic rebaseline**. Base checkpoint = v43r1.
> Scope: E6 shaft-product thermodynamics and ratings only. Jet thrust/nozzle H→A and aircraft/ship performance/adoption are not propagated here.
> Compressor authority: v43 (`main/asai-works-e5-e6-compressor-operability-rebaseline-1934-41.md`).

## 0. Question

v43 repaired E6 compressor identity: E6-S is 7.8 kg/s design flow and E6-M is 13.2 kg/s central / 12.5–14.0 kg/s trim. The remaining question is whether the old E6 shaft-product ratings—roughly **1,520 / 1,700 / 2,100 hp**—survive after paying the same installed-cycle debits already imposed on E4/E5.

The old shortcut `gross specific work × airflow = product shaft power` is not permitted. The generation-table values remain gross comparison indices only.

## 1. Installed-cycle accounting

Reference: sea-level 288 K, gamma 1.4, cp=1.005 kJ/(kg K), PR=7, component-efficiency coordinate 0.84.

The v44 model pays, in order:

1. staged vane/rotor/root/seal bleed;
2. combustor total-pressure loss;
3. exhaust/diffuser pressure margin;
4. shaft mechanical and accessory debit;
5. combustion efficiency for fuel-based thermal efficiency;
6. turboprop/free-power output transmission efficiency when reporting propeller-flange power.

Reproducible computation:

- `computation-2026-08-22/e6_installed_cycle_product_power_v44.py`
- `computation-2026-08-22/E6-INSTALLED-CYCLE-PRODUCT-POWER-V44.tsv`
- `computation-2026-08-22/E6-PRODUCT-POWER-V44.tsv`

## 2. Thermodynamic result

| case | gross w | installed shaft w | installed band | fuel-based shaft η | central BSFC |
|---|---:|---:|---:|---:|---:|
| E6 non-Ni, 870°C | 155.3 kJ/kg | **130.5 kJ/kg** | 123.5–135.4 | **22.5%** | **0.372 kg/kWh** |
| E6 Ni, 920°C | 173.3 kJ/kg | **148.7 kJ/kg** | 141.4–153.5 | **23.5%** | **0.356 kg/kWh** |
| E6 non-Ni, 820°C derate | 137.3 kJ/kg | **116.2 kJ/kg** | 109.7–120.5 | **21.6%** | **0.387 kg/kWh** |

The gross-to-installed loss is about 14–16%. Therefore old E6 `26–26.5%` values remain generation/cycle comparison numbers, not product BSFC numbers.

A later Mamba provides a useful non-calendar ceiling check: an early 1946 Mamba delivered roughly 1,010 shp from a compact axial-flow turboprop, while later Mamba versions reached roughly 1,650 shp at PR~6 and airflow~9.8 kg/s. v44 does not import those dates or hardware; it uses them only to show that the resulting E6 shaft-power density is not outside known gas-turbine physics.

## 3. E6-S product verdict

### 3.1 Non-Ni E6-S-T

v43 standard flow = **7.8 kg/s**. With a 97.5% output transmission efficiency:

- central thermodynamic flange capability = **~993 kW / 1,331 hp**;
- uncertainty envelope at the same flow = roughly **1,260–1,381 hp**;
- high-flow 8.2 kg/s trim gives central **~1,400 hp**.

**Verdict:** old **1,520 hp is SUPERSEDED as the standard non-Ni E6-S-T rating**. New standard headline = **1,300 hp**. A **~1,400 hp high-flow/short-rating trim** is physically available after local reducer/prop/life qualification; it is not the common rating.

This is not a compressor failure. It is the installed cooling/pressure/mechanical bill that the old gross-derived product row did not pay.

### 3.2 Ni E6-S-N-T

At 920°C and 7.8 kg/s:

- central flange capability = **~1,517 hp**;
- uncertainty envelope = roughly **1,442–1,566 hp**;
- 8.2 kg/s high-flow trim gives central **~1,595 hp**.

**Verdict:** old **1,700 hp is SUPERSEDED as the standard Ni E6-S-N-T rating**. New standard headline = **1,500 hp**. A **~1,600 hp high-flow/short-rating derivative** is conditional on local gearbox/propeller and hot-section life qualification.

Ni therefore buys roughly +14% specific shaft work at the E6 coordinate, plus altitude/life margin; it does not buy a free 1,700 hp from the standard 7.8 kg/s gas path.

### 3.3 E6-S-S turboshaft

Using the non-Ni 870°C core and a 0.99 engine-output coupling factor gives **~1,352 shp** central at 7.8 kg/s.

**Verdict:** use **~1,350 shp core/product capability** as the standard shaft derivative. The older `~1,500 shp` is retained only as a short development ceiling/high-flow target, not a continuous standard value. The already-rebased first medium rotorcraft rating of 900 shp continuous / 1,000 shp short remains unaffected.

## 4. E6-M product verdict

v43 repaired the M-family flow from the old exact 10 kg/s coordinate to **13.2 kg/s central / 12.5–14.0 trim**. This materially changes the result.

At 13.2 kg/s, non-Ni 870°C:

- central flange capability = **~1,680 kW / 2,253 hp**;
- uncertainty envelope = roughly **2,132–2,336 hp**.

**Verdict:** old **2,100 hp E6-M-T headline is RETAINED**, but its proof changes completely. It is no longer `10 kg/s × 155 kJ/kg`; it is a **flat-rated product point below a ~2,250 hp central installed capability** on the corrected 13.2 kg/s M-family gas path.

This ~150 hp thermal/rating reserve is useful for gearbox life, propeller absorption, hot-day/altitude margin, deterioration and production scatter.

### 4.1 Marine short/sprint point

At **13.5 kg/s**, the same cycle gives central **~2,304 hp** at the output flange.

Therefore the existing marine design convention—**~2,300 hp short/sprint, ~2,000–2,100 hp continuous**—is thermodynamically consistent with v44. Local salt/FOD/reducer/shaft/prop qualification remains a marine H→A gate.

### 4.2 Long-life transport rating

At 820°C (~50°C thermal derate), 13.2 kg/s central capability is still **~2,006 hp**. A product headline of **~1,870 hp** is therefore retained as a deliberately flat-rated long-life point with additional thermal/gear/deterioration margin.

The old statement `~25% product thermal efficiency` is superseded. The central 820°C installed fuel-based shaft efficiency is **~21.6%** before mission-specific inlet/propulsive effects. Water/methanol remains a short augmentation tool and is not counted in the continuous 1,870 hp rating.

## 5. What changes and what does not

### Canonical now

- E6-S non-Ni standard: **1,300 hp** at 7.8 kg/s; ~1,400 hp high-flow short trim.
- E6-S-N standard: **1,500 hp** at 7.8 kg/s; ~1,600 hp high-flow short trim conditional.
- E6-S-S standard shaft capability: **~1,350 shp**; ~1,500 remains development ceiling only.
- E6-M-T standard aircraft rating: **2,100 hp retained** at 13.2 kg/s, flat-rated below ~2,250 hp central capability.
- E6-M marine: **~2,300 hp short / ~2,000–2,100 hp continuous** is cycle-consistent.
- E6-M-T long-life: **~1,870 hp retained**, now explicitly flat-rated below ~2,000 hp capability at 820°C.

### Still gated

- exact E6 aircraft speed/range/climb changes from the S-rating reduction;
- E6 aircraft intake/duct/engine-mass installation with the corrected flows;
- E6-M marine hull/shaft/prop H→A;
- all E6 turbojet/turbofan thrust: nozzle/inlet/cooling/mass-flow accounting is a separate installed-thrust audit;
- post-1941 actual production/deployment/combat remains HISTORY/FROZEN.

## 6. H→A consequence map

The most important downstream split is asymmetric:

1. **E6-S aircraft using 1,520/1,700 hp must be recomputed.** Tenzan, Ki-40 development and S-core fighter rows cannot keep their old performance simply by relabeling the engine.
2. **E6-M 2,100 hp aircraft need no headline-power downgrade**, but their airflow/intake and installation geometry must inherit the 13.2 kg/s core identity.
3. **Marine E6 2,300 hp short rating survives thermodynamics**, so the next marine gate is installation, not cycle power.
4. **Jet products are untouched by this shaft audit.** Do not infer thrust from the 130.5/148.7 kJ/kg values.

## 7. Next local P1

Proceed with **E6 shaft-product downstream H→A** in this order:

1. E6-S-T Tenzan / S-core fighter and reconnaissance power-performance repair;
2. E6-S-N-T Ki-40 high-altitude repair;
3. E6-M aircraft intake/installation audit while retaining 2,100 hp headline;
4. E6 marine 2,300/2,100 hp installation reconciliation;
5. separate E6 installed turbojet/JF thrust audit.
