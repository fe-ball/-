# Branch B — Japanese aviation wallet root reopen
## Santo cut: 1942-07-23 00:00

Status: **ROOT REOPEN — old D-4 aviation type/count close superseded**

## 1. Trigger

The running Santo model mixed three incompatible baselines:
- historical 1942 aircraft labels;
- Branch-specific aircraft-development canon;
- an event-local working OOB that compressed forward water/flying-boat aviation.

That produced a precise-looking but internally inconsistent wallet.

## 2. Old values that may not be reused as authority

From the old D-4 snapshot, do not carry forward without re-audit:
- `66 A6M` as if all were historical A6M2-equivalent performance;
- `3 D4Y1-C MR` on Shokaku/Zuikaku;
- `H6K/H8K-family 6 MR` as the whole FS flying-boat pool;
- `Tulagi/Gavutu 3 A6M2-N MR` as the Branch float-fighter allocation.

The physical existence of Shokaku/Zuikaku/Ryujo and the broad carrier-air-group size remains usable, but aircraft variants, mission performance, reconnaissance capacity and replacement source must be re-materialized.

## 3. Historical theater anchors

Use historical data as lower-bound / feasibility anchors, not Branch caps:
- on 7 Aug 1942, U.S. Navy postwar analysis gives Tulagi **7 Type-97 flying boats and 9 seaplane fighters usable**;
- Halavo received a **9-aircraft A6M2-N detachment on 5 Jul 1942**;
- Rabaul also carried a material land-attack/fighter/flying-boat pool;
- two Type-2 large flying boats were listed in the broader Rabaul/Tulagi usable-air picture on 7 Aug.

These anchors show that the previous July snapshot was too thin in forward water/flying-boat aviation even before Branch-specific acceleration is applied.

## 4. Branch-specific root canon that must be honored

### Carrier / land Zero lineage

The canonical Branch fighter-development line chooses **Zuisei** for the early Zero family and advances service maturity by several months.

Do not infer the July 1942 fighter's exact:
- engine submodel;
- maximum speed;
- climb;
- radius;
- weight;
- carrier handling;

from the historical A6M2 label.

The root aircraft canon itself warns that the Zuisei 13/15/21 detailed performance figures were not fully audited and must not be promoted to final combat values without the missing integration work.

### Float-fighter lineage

Existing current canon is much firmer:
- A6M2-N-equivalent prototype: 1941-05~07;
- enlarged/unit testing: summer–autumn 1941;
- pilot production: 1941-09~11;
- completed by 1941-12: 30~50;
- combat-usable at opening: 18~35;
- cumulative completed by 1942-03~04: 90~130;
- usable at that point: 60~90 / roughly 6~9 detachments;
- existing v053 performance center remains 444~452 km/h maximum, front-line median 438~447 km/h, subject to float/seakeeping penalties.

Therefore the July Santo theater may contain materially more than the historical 9-aircraft Tulagi detachment, but the exact theater allocation is still OPEN because Midway, Aleutians, home defense, training and other dispersed-base tasks consume aircraft.

## 5. D4Y reconnaissance gate

The old three-aircraft D4Y1-C ready pool is reopened.

Required audit:
1. Branch D4Y development clock before June 1942.
2. Exact Modified-MI embarked experimental/early-production inventory.
3. Soryu/Hiryu damage and aircraft survival/recovery.
4. Post-MI transfer decisions to Shokaku/Zuikaku or land bases.
5. maintenance/spares/trained reconnaissance crews.

Until then:
- do not assume 3 fast-recon D4Y;
- do not assume zero D4Y either;
- use no exact D4Y-dependent contact time as current authority.

## 6. H6K / H8K gate

Rebuild by named unit/node rather than a single family number:
- Tulagi/Gavutu/Halavo;
- Rabaul/Kavieng;
- other tasking such as Australia reconnaissance/raids;
- maintenance and sea-state limits;
- tender/mooring/fuel support;
- losses already paid before 23 Jul.

A large flying boat can search far, but it is not a free persistent shadower. Turnaround, weather, crew fatigue, radio reporting and enemy fighter interception remain real.

## 7. J1N / C5M / other reconnaissance

Do not hide land reconnaissance aircraft inside G3M/G4M counts if they are physically present in the Southeast Area. Conversely, do not teleport New Guinea/Coral Sea reconnaissance assets into a Santo tactical sector without range and base-tasking logic.

## 8. A6M3 historical clock is not a Branch answer

Historical early Model-32 Zeros reaching Rabaul around 29 Jul are useful for industrial/logistical plausibility only.

Branch has a different Zero engine/development lineage. Therefore:
- do not add historical A6M3 Model 32 to the 26-Jul Santo OOB by date-copy;
- do not assume the Branch lacks an equivalent late-Zero improvement just because the historical A6M3 shipment is not yet at Rabaul;
- first reconcile the Branch fighter development and production clock.

## 9. Runtime consequence

The correction may simultaneously:
- increase broad-area search density through more flying boats/water aviation;
- increase protection of search/shadow aircraft through a larger water-fighter layer;
- alter carrier CAP/escort combat performance because Branch Zero performance is not historical A6M2 by default;
- decrease or change fast carrier-recon precision if the old D4Y count cannot be materialized.

This means the old search/contact sequence cannot be repaired by simply adding aircraft to the previous outcome. It must be rerun from D-4.
