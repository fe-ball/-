# Branch B — Zero-family and water-fighter root gate
## 1942-07-23

Status: **OPEN ROOT GATE / CURRENT CONSTRAINTS CLOSED**

## 1. The important correction

The Branch's `Zero` is not simply the historical A6M2/A6M3 family copied into a different war.

Canonical aircraft-development material in the inherited archive explicitly sets the main early Zero line to:

**Zuisei 13改 -> Zuisei 15 -> Zuisei 21 lineage**

and says adoption / unit service comes several months earlier than history.

The same canon also explicitly warns that the detailed Zuisei submodel performance numbers were not fully audited and must not be promoted into final combat performance without a dedicated integration audit.

Therefore v091 does **not** hard-code a new July-1942 speed/climb/radius. It closes the rule that the historical A6M2 performance card is no longer valid authority.

## 2. July-1942 questions that must be answered before the Santo air battle

For each relevant unit, settle:
- exact Branch Zero submodel / engine;
- physical aircraft count;
- serviceable and MR count;
- propeller / supercharger / cooling / exhaust state actually standardized by that date;
- carrier suitability and launch/recovery weight limits;
- trained pilot and maintenance crew state;
- spare engines / propellers / 20-mm ammunition / drop-tank availability;
- whether replacement aircraft come from a carrier replacement pool, Midway garrison pool, Southeast Area pool or home production.

## 3. 6th Air Group / Midway garrison gate

Historical baseline:
- 33 Zeros prepared for Midway garrison duty by late May 1942;
- pre-MI distribution: 6 Akagi / 9 Kaga / 3 Hiryu / 3 Soryu / 12 Junyo.

Branch facts:
- Midway is actually captured;
- Akagi/Kaga are lost in Modified MI;
- Soryu/Hiryu survive damaged;
- Junyo survives and had a separate Aleutian/MI-area mission history.

Therefore the 33-aircraft pool cannot be treated as either:
- all destroyed with the lost carriers; or
- all saved and available for Rabaul/Santo; or
- automatically following the historical post-Midway 6th Air Group path.

Required hull-by-hull settlement:
1. Which 6th-AG aircraft were cargo/stowed versus combat-launched?
2. What was aboard Akagi/Kaga at their loss and is unrecoverably lost?
3. What survives aboard / via diversion from Soryu/Hiryu?
4. What remains with Junyo?
5. What quantity is actually landed at Midway, on what date, and with what support echelon?
6. Does the occupied Midway base retain most surviving 6th-AG aircraft through July, or is any detachment legitimately released?

Until this is closed, do not use 6th-AG aircraft as free replacement Zeros for Shokaku/Zuikaku, Rabaul or Santo.

## 4. A6M2-N-equivalent branch

Current v053 canon remains authoritative for the accelerated float-fighter production line through 1942-03/04.

Implication for July:
- historical `9 at Tulagi` proves a real mission concept and local support geometry;
- Branch national availability is likely substantially larger than history because the line started earlier;
- exact Santo-area allocation must nevertheless pay competing demand from Midway/Wake, Aleutians, base defense, training and tender-supported detachments.

The correct task is a national July allocation ledger, not a multiplication factor on the historical Tulagi nine.

## 5. Performance discipline

Do not double-count Branch improvement.

If a Zero variant's speed/climb/reliability is already derived from the Zuisei development canon, do not add a separate generic `Branch aircraft performance bonus` in combat.

Likewise, water-fighter improvements already embedded in the v053 center (including 444~452 km/h max working range and production acceleration) are not to receive an additional fixed percentage improvement merely because the project uses better calculation/quality control.

## 6. Immediate Santo consequence

Before the Zero root is closed, the following old outcomes have no current authority:
- exact CAP numbers that depend on historical A6M performance assumptions;
- F4F vs Zero loss ratios;
- Ryujo fighter-cycle timing if climb/range/turnaround inputs change materially;
- land/water-fighter interception of PBY/B-17 trackers;
- old D-day VMF-212 pulse loss exchange.

Physical carrier decks and broad air-group headcounts remain useful inputs; their aircraft combat model does not.
