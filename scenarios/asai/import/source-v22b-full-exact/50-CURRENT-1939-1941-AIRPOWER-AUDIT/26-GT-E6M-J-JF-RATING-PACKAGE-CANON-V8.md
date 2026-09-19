# GT E6-M J / JF RATING PACKAGE CANON — V8 AIRPOWER8

> **AIRPOWER8 local backend/rating authority.** Mandatory parents: files 00A, 20, 21, 22 and the v46 E6-M J/JF installed audit. This file does not re-run the cheat multiplier. It closes the higher-rating interpretation that file 20 deliberately left as a shadow.

## 0. What remains fixed

E6-M jet gas path remains:

- 14-stage all-axial, PR7;
- 13.2 kg/s family center, **14.0 kg/s jet/JF high-flow trim**;
- ~13.5 krpm;
- VIGV + two staged bleed bands;
- non-Ni 870 C and selected Ni 920 C gas-generator coordinates already accepted by v46;
- pure-J static product ratings ~850 kgf non-Ni / ~900 kgf selected Ni.

E6-M-JF remains:

`single-spool gas generator -> independent one-stage free LP turbine -> direct-drive aft fan`;

BPR~1.0 / FPR~1.30 / fan ~0.52 m / ~9 krpm / fan shaft ~394 kW.

## 1. E6-M pure-J mass implication

The accepted JF complete dry mass is 610-690 kg, center ~650 kg. The accepted aft-module addition is 100-150 kg, center ~125 kg. Treating correlated rather than worst-case independent extremes gives a current pure-J working closure of:

- **E6-M-J complete dry ~500-555 kg, center ~525 kg**.

This is a derived product ledger coordinate, not a new thermodynamic rating. Aircraft-local inlet, mount and fairing remain separate.

Because the M-core is all-axial, its bare pure-J core is materially slimmer than the aft-fan installation. Working pure-J maximum engine casing/combustor OD is **~0.55-0.62 m**; the accepted JF nacelle/backend envelope is **~0.66-0.72 m**. Therefore, unlike E5, E6-M **does pay a real rear frontal/wetted-area tax when converted to JF**.

## 2. Higher-TIT JF ladder

The unchanged v46 model gives:

| use coordinate | gas-generator TIT | static thrust | static TSFC | main-turbine exit gas | free-turbine exit gas |
|---|---:|---:|---:|---:|---:|
| economy shadow | 820 C | ~964-966 kgf | ~0.646 | ~589 C | ~563 C |
| **long-duration center** | **835 C** | **~984 kgf** | **~0.651** | **~604 C** | **~578 C** |
| **normal military candidate** | **850 C** | **~1,003 kgf** | **~0.656** | **~619 C** | **~593 C** |
| **high-output candidate** | **870 C** | **~1,028 kgf** | **~0.663** | **~639 C** | **~613 C** |
| selected Ni high | 890 C | ~1,052 kgf | ~0.671 | ~659 C | ~633 C |
| **selected Ni upper** | **920 C** | **~1,087-1,088 kgf** | **~0.683** | **~689 C** | **~663 C** |

The free-LP turbine extracts essentially the same ~406 kW across this ladder because fan FPR/BPR and governed fan speed are held near the accepted center. Its temperature drop remains ~26 K.

### Consequence

The higher JF points do **not** expose the free-LP turbine to 850-920 C turbine-inlet gas. It sits downstream of the main turbine and sees roughly 619-689 C inlet gas across the 850-920 C ladder. This lies inside a temperature regime that Asai has already attacked for years in E4/E5 hot-section, free-power-turbine, coating, cooling and life work.

Therefore the backend is **not a new hard thermal ceiling near 1,000 kgf**. The primary extra debts are rear-casing/nozzle temperature, free-spool endurance at the chosen duty, bearing/seal cycles, and product inspection evidence.

## 3. Rating interpretation

AIRPOWER8 closes the engineering ladder but keeps qualification state separate:

- **JF-C / long-duration:** 835 C / ~984 kgf remains the accepted production-center design coordinate.
- **JF-N candidate:** 850 C / ~1,000 kgf class. Natural military normal point once backend endurance is signed.
- **JF-H candidate:** 870 C / ~1,025-1,030 kgf. High-output military point using the same non-Ni main-core thermal coordinate already accepted for pure-J.
- **JF-M/E selected Ni:** 890-920 C / ~1,050-1,090 kgf. Selected short/high-value rating; not a fleet-wide default.

Do not convert these into a universal TBO table. File 21 remains authoritative: TBO/OH is local to material line, starts/cycles, backend duty and installation.

The old branch examples (~450-650 h derated non-Ni JF, ~220-320 h high-temperature Ni jet) remain calibration/provenance, not automatic 1939 fleet claims.

## 4. 1939-04-20 maturity

- E6-M pure-J engine-side rating = accepted development/product coordinate; aircraft flight integration is still on the current May-Jul schedule.
- E6-M-JF 835 C backend = **R3-R4 / engine-side flight-development package**, strongly inherited from E5-JF; aircraft flight remains Aug-Sep target.
- 850 C normal candidate = **R3/R4 qualification branch**; no new architecture is required.
- 870 C high-output and 890-920 C selected Ni = **R3 selected ground/rating-expansion work**, flight/service release not yet claimed.

This is compatible with the current chronology: the rating ladder may be known and exercised on ground hardware before the E6-M-JF aircraft has flown.

## 5. E5 vs E6 J/JF split

Do not transplant the E5 geometry conclusion blindly.

- E5: centrifugal compressor already sets a large maximum OD; aft fan is smaller than that casing, so JF pays mainly mass/length/wetted-area.
- E6-M: all-axial pure-J core is slimmer; the BPR~1 aft-fan/bypass casing expands the rear package to ~0.66-0.72 m. A real high-speed drag tax exists.

Therefore E6-M retains a stronger architectural split:

- pure-J = lighter/slimmer/high-speed research and interceptor direction;
- JF = greater static thrust, acceleration, climb and mission efficiency, with a real rear-area/mass tax.

Exact top-speed difference remains an aircraft H->A measurement, not an engine-side assumption.

## 6. Closed / open

CLOSED:
- E6-M-J derived dry-mass center/band;
- E6-M-JF 835-920 C engineering thrust ladder;
- free-LP turbine thermal-duty interpretation;
- 1,000 kgf is not a hard architecture ceiling;
- E5 and E6 JF frontal-area cases are explicitly distinguished.

OPEN:
- product-specific TBO/OH at 850/870/920 C;
- flight-qualified rating release on E6 aircraft;
- aircraft-local altitude thrust/drag/top-speed map;
- post-1939 procurement and service use.
