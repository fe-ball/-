# GT LIFE / RATING SEMANTICS CANON — V8 GTCORE1

> **AIRPOWER5 / GTCORE1 semantic authority.** This file closes the meaning of life/rating terminology for Asai gas turbines without blanket numerical down-rating. It preserves accepted v39 E4/E5 life coordinates and prevents qualification hours, core life and product overhaul intervals from being collapsed into one historical-comparison number.
>
> Mandatory parent: `00A-MANDATORY-CHEAT-CAPABILITY-PREFLIGHT-CANON-V8.md`.

## 0. Central verdict

The previous conversational proposal to replace early Asai aviation-GT life with generic ~40-250 h bands based mainly on W1/Jumo/Welland comparison is **REJECTED** as a blanket re-rating. Those historical figures remain useful semantic/mechanism anchors, but v39 had already paid the Asai-specific materials, cooling, long-clock, QC and service-history assumptions and produced its own life coordinates.

The correct repair is semantic separation, not historical down-rating.

## 1. Mandatory vocabulary

### `L_mat` — material / component baseline life

Comparative life of a material/process/component class at a defined metal temperature, stress, environment and geometry. It is not an engine TBO.

### `L_core` — representative rated core hot-section engineering life

Expected/qualified life band of the established core at a stated rating before limiting hot-section removal/major inspection. This is the appropriate upstream coordinate when an E-generation table needs one life value.

### `H_qual` — cumulative qualification/endurance hours

Hours accumulated across rigs, components and one or more engines to pass a gate. `H_qual = 300 h` does not imply one engine has a 300 h TBO.

### `TBO_prod` / `OH_prod` — product-specific overhaul/inspection interval

What the operator sees after installation, rating, mission duty, starts/cycles, environment, intake, gearbox/accessories, maintenance doctrine and material line are included.

### cycle / emergency ledger

Hours are not enough. Track at least:

- starts/hot starts;
- thermal cycles;
- time in temperature bands;
- overspeed/overtemperature events;
- emergency/sprint minutes;
- salt/dust ingestion exposure;
- inspection findings and replaced modules.

## 2. Accepted v39 E4/E5 upstream coordinates — RETAIN

These are already rebaselined Asai-worldline values, not raw historical-jet guesses:

| core/material-rating coordinate | representative rated `L_core` | current reading |
|---|---:|---|
| **E4 mature representative** | **250-450 h** | full/normal-rating core hot-section engineering band |
| **E5 Ni @800 C high-end** | **400-700 h** | high-end material line; may spend margin on higher rating in a local product |
| **E5 non-Ni @800 C full** | **150-300 h** | sprint/experimental/high-value full-rating line |
| **E5 non-Ni @760-770 C quantity** | **350-600 h** | production/workhorse coordinate |

Do not reinterpret a stationary/intermittent E4 product claim of several-hundred to ~1000 h as E4 full-rating `L_core = 1000 h`; product duty/derating and replaceable liners may legitimately make `TBO_prod` longer than the representative full-rating core coordinate.

## 3. Why historical early-jet numbers do not overwrite these values

W1, Jumo 004 and Welland histories show that qualification hours, material scarcity, production quality and product TBO can differ radically. They calibrate failure modes and semantics. They do not establish a universal calendar-derived ceiling for Asai because the Asai line has already paid, in-world:

- early creep/oxidation/thermal-cycle clocks;
- hollow/air-cooled hot-section work;
- Ni/non-Ni material branches;
- precision machining/balancing;
- NDT and process control;
- modular service/overhaul practice;
- years of stationary/marine/aviation GT feedback.

Any future down-rating must identify a new unpaid component/duty gate, not merely cite a later historical engine with a shorter life.

## 4. E6 life — what is and is not current

A single universal E6 TBO is **NOT CLOSED** by GTCORE1.

The old pre-v48 aviation branch contained product examples such as:

- Ni high-temperature jet product: factory OH roughly 220-320 h;
- derated non-Ni JF long-life product: roughly 450-650 h.

Those figures remain useful **provenance/calibration examples of what the established life model can produce**, but the associated old aircraft adoption/service history is archived. They must not be silently promoted to every current E6 product or fleet.

What is current:

- E6-M-J 870 C and Ni 920 C installed thrust are accepted engine-side rating coordinates;
- E6-M-JF 835 C is explicitly a long-life production-center thermal point;
- local product TBO/OH must be generated from the chosen material line, TIT, starts/cycles, backend duty and installation.

Therefore a fighter may rationally spend life margin on higher TIT, while transport/fixed/marine products may spend the same capability on longer interval. Neither choice is the universal "Asai philosophy".

## 5. Rating ladder rule

Every mature GT product should identify its own rating ladder rather than one generation-wide temperature.

Suggested semantic labels:

- **C / continuous** — long-duration product rating;
- **N / normal** — normal military/operational rating;
- **M / maximum** — time-limited high output, generating inspection/life debt;
- **E / emergency** — short cumulative-minute budget with mandatory log/inspection consequences.

The exact TIT/thrust at C/N/M/E is a **local product audit**. Do not automatically assign the same ladder to pure-J, JF, shaft, marine and stationary products.

## 6. E6-M-JF specific guard

The v46 835 C / ~984 kgf coordinate is a selected long-life production center. Higher-TIT capability shadows in file 20 do not become free product ratings.

For any higher JF rating, close separately:

- gas-generator limiting component life;
- free-LP-turbine material/cooling/endurance;
- fan/shaft/bearing overspeed and cycle debt;
- duct/nozzle thermal duty;
- inspection interval and accumulated high-rating minutes.

This is a **rating/life qualification problem**, not a reason to cap the architecture at 1,000 kgf and not a reason to invent a new E-generation.

## 7. E7-E9 life rule

New generation does not imply automatically longer or shorter TBO.

- a new higher-TIT/PR architecture may temporarily shorten product interval while component and manufacturing maturity catch up;
- inherited cooling/material/NDT/service infrastructure prevents a full reset to a first-ever historical jet baseline;
- new alloy, new cooling passage, new two-spool bearing/seal arrangement, new fan or new duty cycle receives a **partial local clock reset** only for the genuinely new elements.

For E8/E9, exact product TBO remains local/conditional until the installed product and endurance/yield gates are closed.

## 8. Machine-reading rules

When a document states an hour figure, tag it as one of:

`L_mat / L_core / H_qual / TBO_prod / emergency-minute-budget / unknown`.

If it is `unknown`, do not use it to change another life coordinate until the semantic class is resolved.

When comparing two products, always include:

`{material line, rating/TIT, backend, duty, L_core, H_qual if relevant, TBO/OH, cycles, environment}`.

## 9. Supersession guard

GTCORE1 supersedes the conversational blanket assumptions that:

- early Asai aviation GTs must have sub-100 h TBO because early historical jets often did;
- all combat E6 products should be forced into ~150-250 h without a local life audit;
- the v39 E4/E5 several-hundred-hour coordinates were inherently overoptimistic merely because the calendar is early.

It does **not** guarantee a several-hundred-hour TBO for every new aircraft engine. It requires that the result be derived from the already-paid Asai life system and the actual product duty rather than from a calendar analogy.
