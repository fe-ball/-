# 計算機異聞 refactor v012 — 1944夏セッション状態・Saipan確定・次期戦力回復台帳

v012はv011の実行層を保持したまま、1944-05-01以後に会話で確定・先行裁定した内容をruntime settlementとして保存するセッション状態更新である。

重要: canonical restart checkpoint は引き続き `CHECKPOINT_1944-04-30T24_v004`（1944-05-01 00:00）。v012は完全な新global checkpointを作っていない。理由は、Chinaだけ8/6まで先行裁定した一方、Pacific/Europe/production等を同時に8/6まで閉じていないため。

現在の全世界analysis frontierは **1944-07-14 24:00**。Saipan organized defense終了までをPacificで確定し、以後は日米の1944夏force-regeneration月次台帳を閉じるまでGuam/Tinianへ進まない。

## 現在の正規入口

1. `00_README/NEXT_SESSION_HANDOFF_REFACTOR_v012.md`
2. `06_RUNTIME/CURRENT_ANALYSIS_FRONTIER_1944SUMMER_v001.json`
3. `06_RUNTIME/MARIANAS_SAIPAN_1944-06-11_07-14_SETTLEMENT_v001.md`
4. `06_RUNTIME/1944SUMMER_JAPAN_US_FORCE_REGENERATION_WORKING_LEDGER_v001.md`
5. `06_RUNTIME/CBI_AIR_LOGISTICS_TAX_1944-04_06_WORKING_SETTLEMENT_v001.md`
6. `06_RUNTIME/CHINA_ICHIGO_ANALOG_1944-05-27_08-06_FORWARD_ADJUDICATION_v001.md`
7. `05_WARTIME/CHECKPOINT_1944-04-30T24_v004.json`
8. checkpoint `combat_resolution_support` pointers
9. `06_RUNTIME/WEAPONS_AUDIT_1944-04-30_v001.md`
10. `06_RUNTIME/AIR_COMBAT_RESEARCH_1944SPRING_v001.md`
11. `06_RUNTIME/PACIFIC_CENTRAL_1943_1944Q1_SETTLEMENT_v001.md`
12. `06_RUNTIME/CHINA_BURMA_CBI_1943_1944Q1_SETTLEMENT_v001.md`
13. `98_TOOLS/validate_refactor_v010.py`
14. `95_AUDIT/VALIDATION_RESULT_v012.json`

## v012で固定したもの

### Saipan / Marianas

Saipan main campaign is authoritative through **1944-07-14 24:00**. 米軍はSaipanを確保するが、史実のPhilippine Sea型carrier-air annihilationは起きない。日本main carriers 5 hullsと相当量のcarrier aviation、水上主力が残る。US fast-BB layerは7→4 immediate effectiveまで低下した時点があり、TF58/CVE/DD/engineers/ground troopsも有限疲労を負う。

日本主力艦隊は6/18 PMにSaipan救援のmain fleet battleを打ち切り、6/19以後はsubmarine/logistics harassmentへ移る。Saipan地上戦はAslito優先・Nafutan extraction・water-lift・tank reliability改善を含み、7/14 organized defense end、US combat casualties center ~20.3k。

Guam/Tinianは未確定。史実7/21・7/24を自動採用しない。

### CBI航空物流税

成都/重慶航空圧迫は、直接aircraft/personnel exchangeだけなら日本側不利だが、Hump high-value cargo、transport flight-hours、replacement ferry、special tooling、B-29 stockpile、配置拘束まで含めると1944春CBIのimmediate marginal resource exchangeはnear-even～Japan-favorableになり得る。ただしlong-run US industrial/personnel advantageは維持する。

### China 一号相当

Changsha→Hengyangまでの詳細は保存したが、**1944-08-06 Hengyang fallはChina-only forward adjudication**。global clockを8/6へ進めない。Changsha/Hengyangの交通・行政価値、Nanjing regimeの国家化メンタリティ、Chinese transport networkがmeshからfew corridorsへ圧縮される構造を保存する。

### 1944夏force regeneration

日本は輸送崩壊回避、1944 crude steel center8.7Mt、kaibokan/ASW lineとfleet-DD lineの並立、既存Solomons損耗低下により、1944夏～秋にrepair + new construction + air-group rebuildが同時進行する。

ただし preliminary ledger はまだ **WORKING_NOT_CLOSED**。Unryu/Amagi/Katsuragi、Ibuki、Yamato/Musashi/Nagato/Kongo repairs、Yūgumo/Akizuki/kaibokan、airframes、carrier aircrew、trucks/AFV、US parallel recoveryを月次で閉じてからGuam/Tinianを判定する。

## 判定上の強制注意

- 米軍だから万能、を禁止。Radar detection ≠ instant classification/fire solution。CIC/CAP/AA/search/refuel/repair/sortie cycleは有限。
- 日本側も同じ。Improved doctrine/logisticsはmagic speed/hit rate/AA immunityではなく、failure reduction、I-O、reacquisition、package integrity、regenerationに現れる。
- completion / existence / acceptance / work-up / readiness / allocation / mission effectivenessを分離する。
- lower casualtiesを選ぶなら、通常はgeography / tempo / objective / simultaneous-task coverageのどこかを支払う。
- local forward adjudicationをglobal timeへ昇格させる前に、10～14日ごとに他戦域・生産・人員を同期確認する。

## Legacy

`99_LEGACY_UNTOUCHED` は変更しない。v011までのexecution-layer repairも保持する。

## v011実行互換の明示

戦闘判定では `WEAPON_PLATFORM_CAPABILITY_INDEX_v001.json` を維持し、潜水艦・水上戦闘艦・空母・航空機のmandatory platform reviewを行う。handout生成は `98_TOOLS/build_event_handout_v007.py` を継続使用する。
