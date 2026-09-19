# 計算機異聞 refactor v010 — 戦闘能力判定の網羅性レイヤ追加

v009で修復した実行経路と1944-04-30T24世界状態は変更しない。v010は、戦闘能力に関わる要素が個別判定から漏れる問題に対して、戦闘専用の強制チェック層を開始checkpointへ組み込んだ同状態execution revalidationである。

## 現在の正規入口

1. `00_README/NEXT_SESSION_HANDOFF_REFACTOR_v010.md`
2. `05_WARTIME/CHECKPOINT_INDEX_v009.json`
3. `05_WARTIME/CHECKPOINT_GRAPH_v008.json`
4. `05_WARTIME/CHECKPOINT_1944-04-30T24_v003.json`
5. `06_RUNTIME/COMBAT_ADJUDICATION_CONTEXT_v001.md`
6. `06_RUNTIME/COMBAT_CAPABILITY_FACTOR_INDEX_v001.json`
7. `06_RUNTIME/COMBAT_EVENT_FACTOR_MATRIX_v001.json`
8. `06_RUNTIME/COMBAT_EVENT_INPUT_SCHEMA_v001.json`
9. `02_TECH/TECH_INDEX_v006.json`
10. `06_RUNTIME/EVENT_RELEVANCE_PROFILES_v003.json`
11. `00_CONFIG/DOMAIN_STATE_MAP_v002.json`
12. `06_RUNTIME/EVENT_HANDOUT_SCHEMA_v003.json`
13. `06_RUNTIME/RUNTIME_CONTRACT_v003.json`
14. `98_TOOLS/build_event_handout_v006.py`
15. `98_TOOLS/build_combat_context_v001.py`
16. `98_TOOLS/validate_refactor_v008.py`
17. `95_AUDIT/COMBAT_CAPABILITY_COVERAGE_AUDIT_v001.json`
18. `95_AUDIT/VALIDATION_RESULT_v010.json`
19. `95_AUDIT/PACKAGE_MANIFEST_v010.json`

## v010の追加

- 戦闘能力を20要素へ分解し、兵力・練度・疲労・補充・機体/艦性能・兵器適合・損傷・整備・索敵/射撃管制・情報/奇襲・C2・教義・燃料弾薬・sortie cycle・航続/搭載/距離・天候/視界/海象・地形/基地・集中/相互支援・敵対抗策・目的/撤退/再生を必ず候補に上げる。
- `EVENT_RELEVANCE_PROFILES` はTECH選択、`COMBAT_EVENT_FACTOR_MATRIX` は判定漏れ防止を担当する。片方で代用しない。
- current checkpoint v003が `combat_resolution_support` を明示参照するため、次回開始時に索引を読み忘れない。
- generator v006は各要素を `CHECKPOINT_EVIDENCE / TECH_EVIDENCE / MIXED_EVIDENCE / RUNTIME_INPUT / RUNTIME_AND_ARCHIVE_EVIDENCE / RUNTIME_INPUT_REQUIRED / UNKNOWN / NOT_APPLICABLE` のいずれかで出力する。
- 天候、視界、実参加兵力、疲労、直前損傷、contact age、sortie cycle、距離/高度/搭載、隊形、撤退閾値等はイベント固有なので、未入力時にゼロ補正せず `RUNTIME_INPUT_REQUIRED` とする。
- `execution_blocked` はbaseline/state構造の異常、`combat_resolution_ready` は戦闘ローカル入力の完全性として分離した。handout生成は可能でも `combat_resolution_ready=false` のまま最終戦果を確定してはならない。

## 世界状態

`CHECKPOINT_1944-04-30T24_v003` はv002と同一の世界状態であり、戦果・配備・技術成熟値そのものを変更していない。変更は実行支援依存関係のみ。

## Legacy

`99_LEGACY_UNTOUCHED` は引き続き証拠・比較層で、内容を変更しない。
