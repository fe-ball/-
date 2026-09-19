# 56 — 1937-10-10 REBASE / CONSISTENCY AUDIT V1

Status: AUDIT-CLOSED for bookkeeping corrections; tactical numeric deltas remain WORKING unless explicitly marked CLOSED-DIRECTION.

## Purpose
Audit the continuation from current-branch file 35 through the 10 October 1937 position before further progression. Checks: chronology, supersession, double counting, strength labels, casualty anchors, and attrition/readiness handling.

## 1. Canonical gate numbering
The supplied FULL-V4 current branch ends at file 35 (26–27 July Guang'anmen convoy-delay gate). Therefore continuation files 36 onward are the canonical sequential gate IDs. Earlier conversational labels such as “Q-035 / Q-036” were informal and occasionally off by one. From this audit onward use the filename integer as the gate ID.

- 36: 27–28 Jul final ultimatum / offensive opening
- 37: 28 Jul Nanyuan / Peiping withdrawal
- 38: 28–29 Jul Tientsin / Tongzhou / Peiping transition
- 39: 29–31 Jul Tientsin/Tangku/Tongzhou closeout
- 40: 31 Jul–2 Aug occupation / wider-war transition
- 41–55: subsequent chronological continuation through 10 Oct

File 43 V2 supersedes the earlier non-V2 file 43. The non-V2 file is retained only as provenance.

## 2. Production terminology correction
FULL-V4 contains two different kinds of 1937 production numbers which must not be conflated:

A. Actual/factory-completion run-rate (working, subsequently audited):
- independent GT: ~125 completed cores/year, ~70–105 customer deliveries/year (center ~88)
- exhaust turbo: ~1,300 completions/year, ~1,050–1,220 end-user absorption/year (center ~1,135)

B. Gross installed-equipment / machine-hour capacity in FULL-V4 session delta:
- one-shift theoretical GT 270–320 cores/year; turbo 2,000–2,200/year
- mixed two-shift theoretical GT 350–400 + turbo 1,700–1,900/year

These are NOT sustainable 1937 sellable throughput without labor, alloy, bearings, inspection, balancing, supplier and competing-product allocation. For autumn 1937 military planning, use audited sustainable throughput, not the gross machine-hour ceiling. This also supports the October ruling that Asai cannot credibly promise immediate mass aviation-GT output while existing turbo/power/tool demand is consuming the same skilled bottlenecks.

## 3. Asai effect channels retained
CLOSED-DIRECTION channels:
- selected heavy diesel trucks / artillery tractors / recovery and support vehicles: low-pressure turbo and QC improve loaded/hot/high-altitude performance and readiness;
- artillery computation, survey reduction, firing tables, metrology/QC: somewhat faster/more repeatable preparation/correction where units actually absorbed the methods;
- Mitsubishi/Nakajima engine-development diffusion: small aircraft-engine reliability/serviceability advantage, not higher historical aircraft counts by fiat;
- naval fire control: computation/synchro/switching/metrology improve information transfer and adjustment on influenced ships; no universal retrofit;
- tools, gauges, heat treatment, parts repeatability and failure diagnosis: modest maintenance-turnaround and maintenance-debt advantage.

Prohibitions retained:
- no universal turbo truck fleet;
- no mass motorization;
- no bridge/landing-craft/rail-capacity creation;
- no dense portable-radio network;
- no universal naval fire-control retrofit;
- no aviation GT/jet mass combat use in 1937;
- no additive stacking of every micro-delta into a huge combat multiplier.

## 4. Quantitative micro-deltas: normalize status
Use the following only as WORKING sensitivities, not universal canon multipliers:
- Asai-exposed heavy-vehicle ready fraction: roughly +3 to +6 percentage points for the exposed subset, NOT the whole vehicle park.
- Japanese aircraft mission-capable/serviceability margin: typically +2 to +5 percentage points depending unit and maintenance exposure; center about +3 points. Do not translate automatically into the same percentage increase in sorties.
- registered/fixed or semi-fixed shore/land fire mission cycle on influenced fire-control chains: approximately 5–10% shorter in favorable conditions. This is NOT +5–10% accuracy and not fleetwide.
- aggregate casualty effect must be calculated at the event level. Do not sum vehicle + air + artillery + naval percentages.

## 5. Combat-balance audit corrections
### 29 Aug Shanghai
The FRUS anchor of roughly 30,000 Japanese vs 100,000 Chinese in the field is retained as HIGH historical anchor.
Other figures (guns, vehicles, AFV, logistics indices) remain WORKING-AUDIT and may not be quoted as historical returns.

### 4–10 Oct Shanghai
The previous TSV label `effective_personnel` was too strong. Interpret its 80–95k Japanese and 175–220k Chinese bands as broad THEATER/FIELDED manpower estimates, not immediately combat-effective bayonet strength. Combat-usable manpower is lower because of casualties, integration, rear services and fatigue.

### North China
The late-August / early-October artillery, AFV and vehicle counts are order-of-magnitude modeling bands only. Operational conclusions should be driven by historically attested bottlenecks (rail/bridge repair, mud, river crossing, horse losses, artillery delay), not the exact modeled counts.

## 6. Casualty audit correction
Strong Japanese anchor: NIDS study gives approximately 8,600 Japanese casualties in North China and 12,300 on the Shanghai front as of 29 September; Shanghai casualties rose to approximately 40,700 by 8 November. Treat these as casualties/戦闘損害, NOT killed-only figures.

Chinese absolute casualty totals before October are much less secure. Previous conversational estimates such as a precise cumulative China:Japan exchange ratio (~5.3:1 to ~5.6:1) are WITHDRAWN from canon. They may be used only as discarded sensitivity examples.

Counterfactual use from now on:
- maintain a RELATIVE delta against historical-equivalent Japanese losses rather than inventing exact Chinese cumulative totals;
- through ~10 Oct, cumulative Japanese personnel-loss reduction remains roughly low-single-digit: Shanghai ~4–6% working band, North China ~2–4% working band;
- local artillery/mechanized actions may temporarily reach larger reductions, but these do not become theaterwide fixed multipliers;
- Chinese losses are normally same-order, with at most small local increases from more consistent Japanese fire support. No cumulative percentage is closed without a specific battle calculation.

## 7. Attrition/readiness model introduced
A single A/B/C grade hides too much. From 10 Oct onward track four dimensions on a 0–100 index, where 100 approximates a fresh, properly supplied formation for its historical equipment/training level:
- P = personnel/cohesion (losses, junior leaders, fatigue, replacements)
- F = fire-support readiness (organic artillery and access to higher fire support)
- M = mobility (horses, vehicles, tractors, engineers/road movement)
- S = sustainment (ammunition, spares, maintenance debt, supply flow)

Asai directly affects F/M/S only in exposed Japanese units and indirectly preserves P by reducing some losses. To avoid double counting, the P preservation already includes the casualty benefit of better support; do not add a second casualty multiplier afterward.

Mission classification:
- A: sustained offensive feasible
- B: offensive feasible but limited / needs pauses or rotation
- C: primarily defensive/local action; major attack requires relief/reconstitution
- D: organizational reconstitution required

The four-index vector, not the letter, is canonical working state.

## 8. Overall ruling
No major historical date through 10 Oct needs reopening. Hour-scale Asai margins at Paoting/Chengting/Liuhang remain plausible but WORKING. The strategic calendar remains historical through Shihchiachuang.

The main correction is methodological: future divergence should appear when unit readiness crosses a threshold (e.g., a formation remains B instead of falling to C, or reaches loading/attack readiness earlier), not by mechanically applying a fixed “Asai speed bonus.”
