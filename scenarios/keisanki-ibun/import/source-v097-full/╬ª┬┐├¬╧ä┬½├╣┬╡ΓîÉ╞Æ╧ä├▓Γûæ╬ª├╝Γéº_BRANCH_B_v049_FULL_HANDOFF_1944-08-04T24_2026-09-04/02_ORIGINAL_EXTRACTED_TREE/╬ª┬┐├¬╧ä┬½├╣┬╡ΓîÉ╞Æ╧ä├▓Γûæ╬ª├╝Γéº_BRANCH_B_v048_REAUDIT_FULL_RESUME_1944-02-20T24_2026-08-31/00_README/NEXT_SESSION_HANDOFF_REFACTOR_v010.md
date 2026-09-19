# 次回引継ぎ — refactor v010

## 現在時刻

1944-05-01 00:00。現行restartは `CHECKPOINT_1944-04-30T24_v003`。世界状態はv009/v002と同一。

## 開始時に必ずロード

1. `05_WARTIME/CHECKPOINT_1944-04-30T24_v003.json`
2. checkpointの `combat_resolution_support` にある `COMBAT_ADJUDICATION_CONTEXT_v001.md`
3. `COMBAT_CAPABILITY_FACTOR_INDEX_v001.json`
4. `COMBAT_EVENT_FACTOR_MATRIX_v001.json`
5. TECH/profile/domain mapは従来どおりcheckpoint/current registryから解決する。

戦闘・邀撃・空襲・船団・上陸・基地防空・特殊攻撃・大作戦Gateでは、TECH domainだけで判定を完了しない。profileのmandatory combat factorを全件評価し、未入力を暗黙の0/中立にしない。

## 実行

- 通常handout: `python 98_TOOLS/build_event_handout_v006.py FORAGER_GATE --date 1944-05-01`
- compact chat/context: `python 98_TOOLS/build_combat_context_v001.py FORAGER_GATE --date 1944-05-01`
- event-local入力を与える場合: `--combat-input <json>`。形式は `COMBAT_EVENT_INPUT_SCHEMA_v001.json`。
- `execution_blocked=false` はbaseline/state整合のみを意味する。最終戦闘結果にはさらに `combat_resolution_ready=true` が必要。

## 最初のGate

1944-05-01 Pacific/FORAGER Gateから開始。実参加兵力、情報鮮度、疲労/整備、燃料弾薬、索敵/C2、距離/任務幾何、天候、集中状態、敵対抗策、発動/撤退閾値を明示してから配分と出撃可否を確定する。

その後の世界状態・兵器監査・中国/Burma/Europe/Eastern Frontの既存引継ぎ内容はv009 `NEXT_SESSION_HANDOFF_REFACTOR_v009.md` を状態資料として参照してよい。ただし実行入口はこのv010を正とする。
