# 計算機異聞 refactor v009 — v008実行経路修復・再検証版

v008で確定した1944-04-30T24の世界状態は変更しない。v009は、v008監査で発見した「最新データは保存されているが、event handout generator / relevance profile / validator が旧baselineを参照していた」問題を修理した実行再検証版である。

## 現在の正規入口

1. `00_README/NEXT_SESSION_HANDOFF_REFACTOR_v009.md`
2. `05_WARTIME/CHECKPOINT_INDEX_v008.json`
3. `05_WARTIME/CHECKPOINT_GRAPH_v007.json`
4. `05_WARTIME/CHECKPOINT_1944-04-30T24_v002.json`
5. `02_TECH/TECH_INDEX_v006.json`
6. `00_CONFIG/current_branch_overrides_v003.json`
7. `00_CONFIG/DOMAIN_STATE_MAP_v002.json`
8. `06_RUNTIME/EVENT_RELEVANCE_PROFILES_v003.json`
9. `06_RUNTIME/EVENT_HANDOUT_SCHEMA_v002.json`
10. `06_RUNTIME/RUNTIME_CONTRACT_v002.json`
11. `98_TOOLS/build_event_handout_v005.py`
12. `98_TOOLS/validate_refactor_v007.py`
13. `95_AUDIT/TECH_COVERAGE_AUDIT_v003.json`
14. `95_AUDIT/VALIDATION_RESULT_v009.json`
15. `95_AUDIT/PACKAGE_MANIFEST_v009.json`
16. `06_RUNTIME/MATERIALS_NICKEL_TURBO_JET_1944SPRING_v001.md`
17. `06_RUNTIME/1943_1944Q1_STRATEGIC_SETTLEMENT_v001.md`
18. `06_RUNTIME/WEAPONS_AUDIT_1944-04-30_v001.md`
19. `06_RUNTIME/AIR_COMBAT_RESEARCH_1944SPRING_v001.md`
20. `06_RUNTIME/ASW_TOKAI_MAD_SUBWAR_1944SPRING_v001.md`
21. `06_RUNTIME/I400_SEIRAN_READINESS_GATE_1944_v001.md`
22. `06_RUNTIME/DECISION_RATIONALE_VARIABLE_LEDGER_v001.md`

## v009で修理した内容

- `build_event_handout_v005.py` は指定checkpointを実際に読み、そのcheckpointの `technical_baseline` / `prewar_baseline` / branch override / state sourceを使う。checkpoint引数はラベルではなく実入力になった。
- 現行restartを `CHECKPOINT_1944-04-30T24_v002` とした。世界状態はv001と同一で、TECHをv006、overrideをv003へ進め、欠けていたmaterials/nickel settlementをstate sourceへ追加した同状態execution revalidationである。
- TECH v005追加4件にmachine-readable availability gateを付与し、1943/44技術の1941/42イベントへの逆流を防止した。
- `EVENT_RELEVANCE_PROFILES_v003` と `DOMAIN_STATE_MAP_v002` で AIR_COMBAT / MATERIALS_PROPULSION / SUBMARINE_AVIATION を統合し、`FORAGER_GATE` / `BASE_DEFENSE` / `SPECIAL_STRIKE` / `INDUSTRIAL_AIRCRAFT` profileを追加した。
- state resolutionはcheckpoint-localを優先し、WARSTART ledgerはfallbackとして明示表示する。後世checkpointをopening stateで置換しない。
- branch overrideをv003でschema-normalizeし、base rule 14件すべてとactive overrideをdependency map v002で追跡する。
- current-version registryを拡張し、generator/profile/map/contract/governance/coverage/manifest/validator自体もcurrent familyに含めた。
- validator v007はJSON/source/index/graph/current family/override dependency/profile coverage/generator checkpoint consumption/manifest/checksumを横断検査する。

## v008で正本化した主要事項

- 現在時刻を1944-04-30T24（1944-05-01 00:00）へ進める。
- 旧LEGACYの1943/44戦果は自動継承せず、会話中に再計算した現行枝のみを正とする。
- 第二次Midwayは1943年9月に米軍勝利。日本四空母核心（翔鶴・瑞鶴・飛龍・蒼龍）は生存。
- Tarawa/Makin、Kwajalein/Roi、Eniwetokは米軍が攻略。Wakeは1943年10月時点で日本保持。Trukは艦隊本拠から索敵/潜水艦/局地航空ノードへ格下げ。
- Palau/Trukへの高速空母空襲に対し、日本は主力艦を泊地へ集めず高価値移動資産を保存。基地防空は効果を示すが米高速空母群を撃退できない。
- 史実4/22 Hollandiaは現行枝では発生しない。Port Moresby/Lunga/Santo/New Caledonia喪失により史実SWPA基地連鎖が成立しないため。米戦略重心は史実以上にCentral Pacificへ寄る。
- FORAGERは6/15中心を維持。浮いた4月高速空母時間は日程前倒しより整備・訓練・再抑圧へ使われ、米側がやや健康な状態で来る方向。
- 五号作戦は1943年3月開始、5月宝鶏、7月漢中。第三期四川突入はHOLD。1944年春は成都B-29基地を航空圧迫しつつ、華中華南の一号相当作戦を5月下旬発起予定として準備。
- Burmaは1942末～44春を連続した物流圧迫戦として扱う。1944年春の深いImphal/Kohima突入はGateでNO-GO。日本軍壊滅を避ける代わり、連合軍も北Burmaへ余力を戻せる。
- Eastern Fleetの史実4/19 Sabang空襲はSaratoga不在、Formidable/Indomitable喪失によりNO-GO。
- ItalyはTunisia終結を史実より約1～2週遅延、HUSKY 7/10中心維持、Salernoは高損害。SHINGLE/Anzioは中止中心。Romeは6月中～下旬予測。ANVILは史実より生存。
- OVERLORDは6/6・五海岸・史実級第一波を維持。戦略物流bufferは薄いがSHINGLE中止でLST等assault liftは回復。弱点はD+8～30の再生・港湾/鉄道/荷役buffer。
- 東部戦線は1941～44春の差分を累積計算。1944-04-07までの中心でソ連追加不可逆約7.5万人、追加負傷約15.2万人、戦車/SPG追加全損約940、航空機約305。ドイツ側の現存保存人員差は約2.9万人中心。
- 赤軍は頭数を前倒し補充で埋めるため、実人数差より質・第二梯団・再建予備の低下が大きい。1944-04-07時点の補充/再建用人的予備は史実=100に対し85～92中心。
- New Caledoniaニッケル増加は量産全体の魔法の性能加算ではなく、高温部品・ターボ・ジェットの試験回数、材料選択、破断統計へ優先的に効かせる。
- 1944年春戦闘機研究を高度帯/任務/敵機別に閉じる。機体スペックだけで撃墜比を決めず、先見・位置エネルギー・任務拘束・離脱能力・管制を上位変数とする。
- 東海/MAD対潜は「撃沈数」より先に発見→datum維持→weapon deliveryを増やす。重点覆域で投弾/爆雷投射到達回数は史実相当の約2.5～3倍中心。
- 伊400は単艦三機攻撃が1944年3～4月に技術的可能。合理的最早初陣は伊401合同の5月末～6月前半。奇襲価値を三機小戦果に浪費しない。

## 判断原則（v008で強化）

1. 国籍・年式ラベルで戦力を決めない。実在兵器、即応数、搭乗員/乗員中央値、情報ループ、整備再生、敵対抗技術から判定する。
2. existence / availability / readiness / mission set / mission effectiveness / allocation を必ず分離する。
3. 遠隔世界イベントは史実骨格を参照できるが、直接/間接接続がある場合は日程・損耗・配分を再計算する。
4. 技術進歩は単一倍率ではなく、因果段階（発見、接触維持、投射、命中、損傷、再生等）へ置く。
5. 大作戦は発起前に他戦域の割り込みを確認する。10日～2週間進めるたび世界チェックを行う。
6. 「浮いた兵力」は最適用途へ自動転送しない。輸送、政治、敵意図不確実性、再編時計、指揮系統を通す。
7. 判断記録には理由、注意点、見逃しやすい変数、再判定Gateを併記する。

## 重要な未固定

- 1944年日本商船総GRTの単一値。物理船腹は史実より健全だが、統計母集団未統一のため引き続き固定しない。
- 金星零戦改の1944年全国月産/累計単一値。4月末配分可能即応80～110機帯を暫定使用。
- 通常巡潜の1944年4月末総隻数。個別損失台帳未統合のため、任務日/重点線効果を優先。
- 伊400初陣の目標・日付。5月末～6月前半に米FORAGER集積を見てGate判定。
- 一号相当作戦の最終航空・工兵配分。5月1 Pacific Gateで確定。
- BAGRATION結果。4月末までの赤軍質/予備低下を初期条件に持ち込むが、6月戦果は未計算。

## Legacy扱い

`99_LEGACY_UNTOUCHED` は証拠・比較・技術詳細の参照層。旧87/88/89等の戦史結果は現行枝へ自動継承しない。v009でもlegacy subtreeのファイル内容は変更しない。
