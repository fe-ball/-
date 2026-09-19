# 計算機異聞 refactor v005 — 1942Q2再監査反映版

v004のリファクタ骨格を保持したまま、会話上で確定したOperation C、Doolittle、MO/Coral Sea、Port Moresby、修正MI、Midway攻略とその決算を現行実行枝へ反映した。

## 現在の正規入口

1. `00_README/NEXT_SESSION_HANDOFF_REFACTOR_v005.md`
2. `05_WARTIME/CHECKPOINT_INDEX_v004.json`
3. `05_WARTIME/CHECKPOINT_1942-06-15T24_v001.json`
4. `06_RUNTIME/1942Q2_OPERATION_C_MO_MI_REAUDIT_SETTLEMENT_v001.md`
5. `06_RUNTIME/MIDWAY_1942-06-10_15_SETTLEMENT_v001.json`

## v005で変わったこと

- 1942-04-05 Operation CでForce Aを捕捉し、Indomitable/Formidableを喪失させる質的枝を正式化。
- Doolittleの早期警報/限定迎撃、TF16生存を反映。
- Coral Seaを全面再走査。Yorktown/Lexington喪失、Shokaku大破、Zuikaku/Shoho生存、Port Moresby陥落へ更新。
- 修正MIを5正規空母+独立第二航空梯団+近接高速水上追撃+前進山本主力+19隻級潜水艦で正式化。ALは分離。
- Tone索敵遅延は固定せず、天候は歴史再現ではなく確率条件。日本の改善は広域気象情報の作戦利用に限定。
- MI決算：米Enterprise/Hornet/Saratoga喪失。日本Akagi/Kaga喪失、Soryu/Hiryu大破生還、Zuikaku健在。6月15日Midway陥落。
- Midway基地方針、連合軍潜水艦/航空妨害、日米艦政・航空隊再建の再計算ゲートを新設。

## 旧枝の扱い

`99_LEGACY_UNTOUCHED` は無変更。旧80/81/82/85/86+は比較・証拠としてのみ用い、現行戦果を暗黙継承しない。旧 `CHECKPOINT_1942-05-06T24_v001` も保存するが、現行restartではない。
