# 次回引継ぎ — refactor v011

## 現在時刻

1944-05-01 00:00。現行restartは `CHECKPOINT_1944-04-30T24_v004`。世界状態はv009/v010と同一で、v011は判定入口の再検証。

## 開始時に必ずロード

1. `05_WARTIME/CHECKPOINT_1944-04-30T24_v004.json`
2. checkpoint `combat_resolution_support` の全ポインタ
3. とくに `COMBAT_ADJUDICATION_CONTEXT_v002.md`
4. `COMBAT_CAPABILITY_FACTOR_INDEX_v001.json` / `COMBAT_EVENT_FACTOR_MATRIX_v001.json`
5. `WEAPON_PLATFORM_CAPABILITY_INDEX_v001.json` / `COMBAT_PLATFORM_MATRIX_v001.json`
6. `NOVEL_WEAPON_ADJUDICATION_POLICY_v001.json`
7. TECH/profile/domain mapはcheckpoint/current registryから解決する。

戦闘・邀撃・空襲・船団・上陸・基地防空・特殊攻撃・大作戦Gateでは、20要素チェックに加えてmandatory platform classを全件レビューする。platform indexは通常のevent TECH tagとは独立経路なので、艦種を「profileに書いていなかったから無視」してはならない。

### 潜水艦

撃沈数だけで弱い/強いを決めない。実働艇数、哨戒艦日、接触情報のage、潜高の水中位置修正、雷撃機会、生残再出撃、敵護衛/航路拘束を統合する。潜高は通常潜水艦の史実戦績へ丸めない。

### 水上艦

公称砲力だけで決めない。実用速力・航続・稼働率・損害制御・索敵/追尾・砲雷撃・第二斉射・隊形・再突入を確認する。日本駆逐艦/巡洋艦の次発魚雷を「搭載しているが戦闘火力にならない」と自動処理しない。

### 史実外/分岐兵器

新登場した兵器・variantは `weapon_systems` に登録する。史実にない、時期が違う、同じ名前でも仕様が違う場合は、工学能力・成熟・availability/readiness・provenanceを記録する。史実類似兵器は部品単位のbounded priorにのみ使い、史実の戦果・評判を結果として移植しない。

## 実行

- handout: `python 98_TOOLS/build_event_handout_v007.py FORAGER_GATE --date 1944-05-01`
- compact context: `python 98_TOOLS/build_combat_context_v002.py FORAGER_GATE --date 1944-05-01`
- event-local入力: `--combat-input <json>`、schemaは `COMBAT_EVENT_INPUT_SCHEMA_v002.json`

FORAGER Gateでは `CARRIER / AIRCRAFT / SURFACE_COMBATANT / SUBMARINE` がmandatory platform review。したがって空母航空戦中心の局面でも水上艦・潜水艦の能力候補がhandoutへ残る。

最終戦果は `execution_blocked=false` に加え `combat_resolution_ready=true` を要求する。
