# GT E6-S / JF / E7-E9 REBASE CANON — V8 GTCORE1

> **AIRPOWER5 / GTCORE1 current propulsion authority.** This file is a rebase/guard layer over the existing E6/E7 production canon. It does not lower any v38-v46 accepted installed value. It re-promotes the E1-E9 continuous-front semantics, closes one E6-S pure-jet pre-audit shadow, clarifies the E6-M-JF rating ceiling issue, and separates advanced-technology start clocks from integrated E-generation product clocks.
>
> Mandatory parent: `00A-MANDATORY-CHEAT-CAPABILITY-PREFLIGHT-CANON-V8.md`. Advanced-branch 1939 readiness child: `22-GT-ADVANCED-BRANCH-1939-STATE-CANON-V8.md`.

## 0. Central verdict

1. **E6-M installed values remain accepted.** No blanket re-rating is authorized:
   - E6-M-J non-Ni ~850 kgf;
   - E6-M-N-J Ni ~900 kgf;
   - E6-M-JF v46 long-life production center ~950-1,000 kgf, central ~984 kgf at 835 C.
2. Those values were produced by the v38-v46 cheat/computation/organization rebaseline. Historical early-jet examples are comparison anchors only and do not justify a second downward correction.
3. **E6-S-J standard-flow shadow is lower than the earlier conversation estimate** because the v46 E6-M jet product uses the 14.0 kg/s high-flow trim, not the 13.2 kg/s family center. At E6-S standard 7.8 kg/s, same-cycle/nozzle scaling gives ~476 kgf non-Ni / ~505 kgf Ni. The ~500/~530 figures belong to the 8.2 kg/s high-flow short trim.
4. **E6-M-JF 835 C is a selected long-life production point, not a hard thrust ceiling.** The unchanged v46 model gives >1,000 kgf when the same architecture is operated at higher TIT. Those higher points are capability shadows until hot-section/free-turbine/fan/product qualification is separately closed.
5. E7, E8 and E9 are continuous technology-front coordinates. The existing E7 1939-42 schedule is an **integrated E7-core/product schedule**, not the invention date of VSV, multi-spool, reheat, fan, advanced cooling or high-PR component ideas.
6. Old E8/E9 upstream capability is re-promoted as a technical parent. The old calendar labels are maturity coordinates, not hard R&D-start dates and not guaranteed procurement dates.

## 1. E6-S-J local installed pre-audit

### 1.1 Parent identities

From the accepted compressor/shaft rebaseline:

- E6-S = PR7;
- 7-stage axial booster + 1 centrifugal HP stage;
- design corrected flow **7.8 kg/s**;
- working trim **7.6-8.2 kg/s**;
- VIGV + stage-4 bleed;
- E6 family thermal coordinates retain non-Ni 870 C and Ni 920 C high-end points unless a local product deliberately selects a lower rating.

The v46 E6-M pure-jet audit uses **14.0 kg/s high-flow trim**. At fixed PR/TIT/component efficiencies/nozzle assumptions, static thrust and fuel flow scale almost linearly with gas-path flow. A local S-core audit still owes exact small-core exhaust geometry, accessory package, mass and flight-installation qualification; this section therefore closes only a **PRE-AUDIT capability shadow**, not a product rating.

### 1.2 Result

| E6-S-J point | flow | v46-method static thrust shadow | status |
|---|---:|---:|---|
| non-Ni 870 C standard | 7.8 kg/s | **~476 kgf** | PRE-AUDIT |
| Ni 920 C standard | 7.8 kg/s | **~505 kgf** | PRE-AUDIT |
| non-Ni 870 C high-flow short trim | 8.2 kg/s | **~500 kgf** | PRE-AUDIT / short trim |
| Ni 920 C high-flow short trim | 8.2 kg/s | **~531 kgf** | PRE-AUDIT / short trim |

Support calculation: `99-SUPPORT-CURRENT/GT-REBASE-SOURCE-SELECTED/E6-S-J-PREAUDIT-SHADOW-V8.tsv`.

### 1.3 Consequence for high-speed research

A dedicated light research aircraft may legitimately use the E6-S-J family without inventing a new core. For planning, distinguish:

- ~475-505 kgf **standard-flow** engine-side shadow;
- ~500-530 kgf **8.2 kg/s short/high-flow trim**.

Do not silently call the latter the standard E6-S-J rating.

## 2. E6-M-JF rating interpretation

### 2.1 What v46 actually closed

The accepted architecture is:

`E6-M single-spool gas generator -> separate one-stage free LP turbine -> direct-drive aft fan`

with BPR~1.0, FPR~1.30 and central ~984 kgf at **835 C**, explicitly selected as a non-Ni long-life production coordinate.

The v46 headline `950-1,000 kgf` is therefore a **production-center band**, not proof that the architecture cannot exceed 1,000 kgf.

### 2.2 Same-model TIT sensitivity — capability shadow only

Keeping the same fan/free-turbine geometry and v46 accounting, representative shadows are:

| TIT | static thrust | interpretation |
|---:|---:|---|
| 820 C | ~966 kgf | economy/continuous shadow |
| **835 C** | **~984 kgf** | **v46 accepted long-life production center** |
| 850 C | ~1,003 kgf | higher normal-rating shadow |
| 870 C | ~1,028 kgf | high-output shadow |
| 890 C | ~1,053 kgf | Ni high shadow |
| 920 C | ~1,088 kgf | Ni upper shadow |

Support calculation: `99-SUPPORT-CURRENT/GT-REBASE-SOURCE-SELECTED/E6-M-JF-TIT-RATING-SHADOW-V8.tsv`.

These rows **do not automatically become product ratings**. Higher-TIT JF operation must separately receive:

- main hot-section life at the chosen material line;
- free-LP-turbine metal-temperature/cooling/endurance;
- fan/free-turbine overspeed and vibration margin;
- nozzle/duct temperature and pressure compatibility;
- product TBO / inspection / emergency-minute accounting.

### 2.3 Current rule

- retain **950-1,000 kgf** as the current long-life/production-center E6-M-JF headline;
- do not treat 1,000 kgf as a hard upper capability ceiling;
- fighter/high-output JF ratings may be opened by a local rating/life qualification audit rather than by inventing a new generation.

## 3. E7 schedule — what it means and what it does not mean

Existing V8 target schedule remains usable for the **integrated E7 core**:

- 1939: E7 component/rig program;
- 1940H1: full compressor/hot-section rigs;
- 1940H2: integrated gas-generator demonstrator;
- 1941H1: full-core ground development;
- 1941H2: ground-qualified development core / inherited aft-fan advanced ground or limited flight candidate;
- earliest E7-dedicated aircraft: 1942Q1-Q2 target.

GTCORE1 clarifies that the phrase "1939 component/rig" does **not** mean all E7/E8/E9-enabling technologies begin in 1939.

### Paid/inherited before or by E6

- multi-stage axial-compressor design method;
- VIGV and staged bleed scheduling;
- hollow/air-cooled hot-section concept and fabrication path;
- coatings and Ni/non-Ni material strategy;
- precision balancing, rotordynamics/Campbell methods, NDT and statistical QC;
- free-power-turbine experience;
- separate free-LP-turbine/aft-fan architecture;
- computation/data methods for map, transient, thermal and rotor work.

### Parallel advanced branches that must have their own clock

The reincarnator rule permits the following branches to be known and investigated before the generation in which they become a standard product:

- multi-row VSV;
- true multi-spool compressor architecture;
- front low-BPR fan;
- reheat / variable-area nozzle;
- more aggressive staged cooling;
- higher-PR compressor components.

Their **exact 1939 hardware maturity remains OPEN unless an earlier rig/test ledger closes it**. Do not set them to zero merely because E7 full core is later; do not promote them to qualified hardware merely because the concept is known.

## 4. E8/E9 re-promotion

The v48 upstream parent remains technically valid and is re-promoted into the current audit semantics.

### E8 mature technical coordinate

- PR **9-10**;
- TIT **~940 C**;
- component eta **~0.86**;
- high-end practical / qualifiable technical coordinate;
- 15-16 stage single-spool + VSV/bleed remains a central possible architecture;
- true two-spool is an alternative that buys off-design/start/surge margin while paying shaft/bearing/seal/control/assembly tax.

The old `1945-46` label is a **mature-coordinate / qualification-window label in the previous technical ledger**, not a prohibition on earlier E8-directed component work.

### E9 later technical front

- PR **11-12**;
- TIT **~1000 C**;
- component eta **~0.86-0.87**;
- design/component/rig technical front;
- flight/series remains conditional on multi-spool rotordynamics/bearings/control, staged cooling debit, full-core maps, start/acceleration/surge, endurance and manufacturing yield.

The old `1945-47` label likewise does not mean the ideas are invented then. It identifies the later integrated technical front. **GTCORE1 does not claim PR11-12 / 1000 C E9 hardware already exists in 1939.** The actual 1939 component state must be reconstructed from paid facilities, rig programs and long-clock evidence.

## 5. What is now CLOSED vs OPEN

### CLOSED / retained

- v38-v46 non-double-counting rule;
- E-generation = continuous technology front, not model number;
- core scale and backend are independent axes;
- E6-M J/JF accepted engine-side installed values;
- E6-S-J standard/high-flow pre-audit shadow distinction;
- E6-M-JF 835 C = selected long-life production center, not a hard capability ceiling;
- E8/E9 technical-front semantics and old mature coordinates remain valid upstream parents.

### OPEN / next local audit

- E6-S-J local installed package is **CLOSED in file 25/25A** at development-product level; R5 service qualification/TBO and measured altitude map remain open;
- E6-M-JF higher-TIT engineering rating ladder is **CLOSED in file 26/26A**; exact product TBO/OH and flight/service release remain local OPEN;
- 1939 readiness class for multi-row VSV, true two-spool compressor, reheat/variable nozzle and front-fan branches is closed at subsystem level by file 22; exact serial/product dates remain local;
- E7/E8/E9 product-specific installed thrust/weight/TSFC maps;
- E8/E9 actual military procurement, production and post-1943 deployment.

## 6. Supersession guard

This file supersedes any conversational or working claim that:

- standard-flow E6-S-J is automatically ~500/~530 kgf;
- E6-M-JF cannot exceed ~1,000 kgf in the same architecture;
- E8/E9 disappeared from the worldline because V8 only displayed E7;
- E8/E9 technologies must wait until the printed E8/E9 mature-year labels before R&D can start;
- historical introduction dates alone justify lowering a v38-v46 accepted Asai capability.
