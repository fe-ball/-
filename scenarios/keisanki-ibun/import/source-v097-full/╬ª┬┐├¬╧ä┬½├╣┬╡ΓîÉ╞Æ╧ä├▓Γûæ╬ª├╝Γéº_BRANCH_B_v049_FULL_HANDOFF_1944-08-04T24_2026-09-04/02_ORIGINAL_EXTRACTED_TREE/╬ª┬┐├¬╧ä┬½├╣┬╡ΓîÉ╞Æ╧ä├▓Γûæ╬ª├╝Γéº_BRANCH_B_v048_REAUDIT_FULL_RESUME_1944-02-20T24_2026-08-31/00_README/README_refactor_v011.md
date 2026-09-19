# 計算機異聞 refactor v011 — 兵器・プラットフォーム能力／史実外新兵器レイヤ

v010の戦闘20要素チェックに加えて、兵器・艦種そのものの能力が史実イメージや通常TECHタグの外へ落ちる問題を修正した。同じ1944-05-01世界状態を維持したexecution revalidationであり、戦果・配備・既存技術成熟値そのものは変更しない。

## 現在の正規入口

1. `00_README/NEXT_SESSION_HANDOFF_REFACTOR_v011.md`
2. `05_WARTIME/CHECKPOINT_INDEX_v010.json`
3. `05_WARTIME/CHECKPOINT_GRAPH_v009.json`
4. `05_WARTIME/CHECKPOINT_1944-04-30T24_v004.json`
5. `06_RUNTIME/COMBAT_ADJUDICATION_CONTEXT_v002.md`
6. `06_RUNTIME/COMBAT_CAPABILITY_FACTOR_INDEX_v001.json`
7. `06_RUNTIME/COMBAT_EVENT_FACTOR_MATRIX_v001.json`
8. `06_RUNTIME/WEAPON_PLATFORM_CAPABILITY_INDEX_v001.json`
9. `06_RUNTIME/COMBAT_PLATFORM_MATRIX_v001.json`
10. `06_RUNTIME/NOVEL_WEAPON_ADJUDICATION_POLICY_v001.json`
11. `06_RUNTIME/COMBAT_EVENT_INPUT_SCHEMA_v002.json`
12. `02_TECH/TECH_INDEX_v006.json`
13. `06_RUNTIME/EVENT_RELEVANCE_PROFILES_v003.json`
14. `06_RUNTIME/EVENT_HANDOUT_SCHEMA_v004.json`
15. `06_RUNTIME/RUNTIME_CONTRACT_v004.json`
16. `98_TOOLS/build_event_handout_v007.py`
17. `98_TOOLS/build_combat_context_v002.py`
18. `98_TOOLS/validate_refactor_v009.py`
19. `95_AUDIT/WEAPON_PLATFORM_COVERAGE_AUDIT_v001.json`
20. `95_AUDIT/VALIDATION_RESULT_v011.json`

## v011で追加した判定層

`WEAPON_PLATFORM_CAPABILITY_INDEX` は、潜水艦・水上戦闘艦・空母・航空機・ASW・陸戦システム・特殊/史実外システムを、個々の戦闘能力軸へ分解する。通常のEVENT_RELEVANCE profileとは別経路で引くため、profile tagに無い艦種でも大作戦Gateで必要なら消えない。

潜水艦は撃沈数や魚雷命中率だけで評価しない。出撃成立、到着、on-station、情報鮮度、水中機動による射点変換、攻撃、生残、再出撃、敵護衛・航路変更の拘束までを見る。既存正本の潜高第一世代18.5–19.0kt級水中最大速力は、連続静粛追跡ではなく「古くなった接触情報から射点へ間に合わせる」閾値能力として扱う。

水上戦闘艦は砲口径・公称速力・第一斉射だけで評価しない。実用満載速力、航続、機関信頼性、損害制御、sensor/optical tracking、砲射撃、水雷射撃、再装填・再接触・第二斉射、隊形支援、離脱再突入までを見る。陽炎型等の改善と12–20分級の第二有効魚雷斉射サイクルは、該当艦・条件を確認した上で候補能力として必ず提示する。

## 史実にない／史実と違う兵器

`NOVEL_WEAPON_ADJUDICATION_POLICY` により、`DIVERGENT_VARIANT / AHISTORICAL_TIMING / AHISTORICAL_NEW / UNKNOWN` を明示する。新兵器は「最も近い史実兵器の戦績」へ丸めない一方、「新しいから強い」とも扱わない。工学能力、成熟段階、生産数、即応数、乗員/搭乗員、統合、任務包絡、故障様式、敵の認知/対抗を分ける。

現在索引には、瑞星系零戦/B5N分岐、潜高第一世代、潜高改の存在候補、水上魚雷第二斉射システム、計算援用朝潮/陽炎運用profile、I-400/晴嵐統合、東海/MAD統合を登録している。索引にない今後の新兵器は `COMBAT_EVENT_INPUT_SCHEMA_v002` の `weapon_systems` へ追加できる。未登録の史実外兵器は capability record・availability/readiness・provenance が揃うまで最終戦果を確定しない。

## readiness

`execution_blocked` はcheckpoint/baseline/stateの構造異常。`weapon_capability_ready` は兵器・platform層の完全性。`combat_resolution_ready` は従来の20要素と兵器・platform層の両方が揃った場合のみtrueになる。

## 世界状態 / Legacy

`CHECKPOINT_1944-04-30T24_v004` はv003と同一世界状態。`99_LEGACY_UNTOUCHED` は引き続き変更しない。
