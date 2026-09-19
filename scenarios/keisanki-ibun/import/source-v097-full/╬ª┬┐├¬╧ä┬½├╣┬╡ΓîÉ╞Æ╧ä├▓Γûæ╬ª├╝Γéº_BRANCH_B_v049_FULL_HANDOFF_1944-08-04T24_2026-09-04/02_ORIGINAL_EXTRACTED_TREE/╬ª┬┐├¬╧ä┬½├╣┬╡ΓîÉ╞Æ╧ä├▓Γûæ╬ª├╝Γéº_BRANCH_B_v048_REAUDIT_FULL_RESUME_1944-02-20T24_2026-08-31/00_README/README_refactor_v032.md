# 計算機異聞 refactor v032 — Branch B Indian Ocean frontier/index repair working full package

v032 preserves the v030-derived CURRENT authority and repairs the discussion-frontier/index layer that v031 left implicit.

Authoritative restart is unchanged:
- `05_WARTIME/CHECKPOINT_1943-12-31T24_BRANCH_B_v004.json`
- `06_RUNTIME/CURRENT_BRANCH_STATE_v012.json`
- `00_CONFIG/current_branch_overrides_v012.json`

Start navigation from:
- `00_README/CURRENT_DISCUSSION_FRONTIER_v001.json`

Working changes in v032, **not promoted into CURRENT**:
- stale origin/route open item removed in `JAPAN_HULL_RECONCILIATION...v004`;
- reinforcement screen advanced to v005 with dated trigger evidence but no realized order;
- Eastern Fleet historical movement dated: 30 Dec departure, 5–6 Jan Gibraltar, 10 Jan probable enemy sighting, 11 Jan German visual sighting, 12–13 Jan Port Said/Suez, 19–21 Jan Aden, 27–28 Jan Ceylon;
- post-arrival boiler-cleaning/readiness gate retained, so arrival is not treated as an immediate combat sortie;
- Andaman–Arakan sensor question normalized from an invalid single "station count" into four forward functional reporting nodes plus two rear support nodes; exact Jan radar-site count remains unknown rather than fabricated;
- `current_version_families_v020.json` now distinguishes package/navigation recency from runtime authority using `latest_present` and `runtime_role` while retaining `current` for compatibility;
- validator v019 checks authority invariants plus discussion-frontier/index consistency.

No 1944 movement order has been realized. The first substantive decision now is whether/when the 11 Jan German visual report reaches Japanese operational intelligence; only then is the first Truk-group GO/withhold decision made with Pacific opportunity-cost debit.
