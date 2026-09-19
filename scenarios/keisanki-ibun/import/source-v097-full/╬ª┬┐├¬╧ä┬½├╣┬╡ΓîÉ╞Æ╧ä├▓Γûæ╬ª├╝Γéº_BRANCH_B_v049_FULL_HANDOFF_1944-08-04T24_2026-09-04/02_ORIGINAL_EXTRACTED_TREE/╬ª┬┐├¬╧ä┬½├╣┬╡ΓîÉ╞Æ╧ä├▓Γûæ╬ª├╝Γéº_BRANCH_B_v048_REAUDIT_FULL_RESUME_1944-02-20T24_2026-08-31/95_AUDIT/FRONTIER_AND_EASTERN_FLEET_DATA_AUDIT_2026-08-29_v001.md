# Frontier/index + Eastern Fleet data audit v001 — 2026-08-29

status: WORKING_AUDIT / NO CURRENT AUTHORITY PROMOTION

## What was mechanically repaired

- `current_version_families_v019.json` conflated execution authority with package/navigation recency. It correctly preserved v030 execution authority, but therefore pointed README/HANDOFF/PACKAGE_MANIFEST/VALIDATION_RESULT at v030 even though v031 discussion work existed.
- v020 keeps the legacy `current` key for compatibility, adds `latest_present`, `runtime_role`, and explicit registry semantics. Navigation/package families now point at v032; execution-authority families remain on the v030-derived current state/checkpoint/overrides.
- `JAPAN_HULL_RECONCILIATION...v003` still listed origin/route as open after the route audit had already closed it. v004 removes that stale open item without deleting v003.
- A dedicated `CURRENT_DISCUSSION_FRONTIER_v001.json` now separates authoritative restart state from unpromoted discussion frontier and provides a mandatory load order.
- Validator v019 checks both authority invariants and frontier/index consistency.

## Historical Eastern Fleet chronology now dated

Primary working source: Vice Admiral Eastern Fleet War Diary, 15 Dec 1943–31 Jan 1944, transcribed at:
https://www.naval-history.net/xDKWD-EF1943Dec-Apr1944.htm

Key chronology used:
- 30 Dec 1943: Renown / Queen Elizabeth / Valiant sail Scapa; Illustrious / Unicorn leave Clyde that night.
- 5–6 Jan 1944: Gibraltar / Straits passage under explicit secrecy precautions.
- 10 Jan: diary says force was probably sighted by enemy aircraft.
- 11 Jan 16:40: diary records German aircraft sighting — first robust source-grounded Axis visual gate.
- 12–13 Jan: Port Said / Suez.
- 19–21 Jan: Aden fueling.
- 27–28 Jan: Colombo / Trincomalee arrival.
- After arrival: QE/Valiant boiler cleaning and normal defect work estimated through 11 Feb; squadron training intended 14 Feb. Arrival therefore must not be collapsed into immediate battle-ready sortie.

Official RN January diary provides corroborating station-planning context:
https://sccd.royalnavy.mod.uk/-/media/rnweb/locations-and-operations/navy-historical-branch/pdfs/1944/war_diary_naval_1944_01.pdf

## Andaman–Arakan observation-network data decision

The previous request for an "exact station count" was not a compare-like quantity. It mixed radar sites, DF/ESM/COMINT, air-reconnaissance detachments, visual coastwatch/reporting and plot cells. Under `R-SCIENCE-COMPARE-LIKE`, a single point count would be false precision.

The working replacement is a functional-node model:
- forward: Akyab; Port Blair; Mergui/Victoria Point sector; Chittagong/Patenga;
- rear support: Sabang/Padang sea-search; Penang/Singapore reporting/Axis liaison.

Physical Jan-1944 radar-site count remains UNKNOWN. Later evidence establishes that Port Blair had multiple radar installations by mid-1944, but that is not back-dated into an exact 1 Jan count. Useful corroboration:
- Benbow, RN carrier study: June 1944 Port Blair strike included two radar stations: https://kclpure.kcl.ac.uk/portal/files/65358706/Contribution_of_RN_aircraft_carriers_BENBOW_Accepted3March2017_GREEN_AAM.pdf
- Electronic-warfare historical summary notes Australian/British ferret aircraft from India plotted Japanese radars on the Andamans: https://www.govinfo.gov/content/pkg/GPO-CRECB-1967-pt22/pdf/GPO-CRECB-1967-pt22-10-2.pdf
- Secondary operational synthesis reports 331 Air Group detachments at Mergui/Port Blair and 705 Air Group sea-search from Padang/Sabang: https://rldunn.com/japanese-air-raid-on-calcutta/

No radar/DF node is allowed to generate a weapon-quality solution by itself. Cue -> track -> fresh recontact remains mandatory.

## What remains genuinely open

The first substantive Branch-1944 decision is no longer "find the timeline". It is: adjudicate whether and how quickly the 11 Jan German sighting is passed into Japanese operational intelligence. Only then may the Truk group receive an actual GO/withhold decision, with Central-Pacific opportunity-cost debit. Historical hindsight alone does not realize the order.
