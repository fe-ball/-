# 計算機異聞 refactor v002

## この版で進めたこと

- TECH INDEX を v001 の14項目から **49項目**へ拡張した。速度だけではなく、兵器別航空命中、開戦時主要機、可動・整備、空母任務階級、揚陸、輸送、水雷第二斉射、潜水艦任務実効、ASW、電探、COMINT等を戦史実行用の最小カードへ分離した。
- 数値の確度を accepted / high_confidence_provisional / provisional_center / conditional / gated / diagnostic_only 等へ分け、暫定値を無印で正本化しない。
- `00_CONFIG/adjudication_policy_v001.json` に判断処理を独立させた。ルールが気に入らなければここを修正でき、旧資料・敗者判断は消えない。
- `95_AUDIT/adjudication_cases_v001.json` で主要衝突を突合した。
- legacy `opening_sync_state` の Pearl v002 参照が manifest v004 と不整合だったため、`opening_sync_state_1941-12-07_08_refactor_v002.json` を作り v003 へ正規化した。legacy原文は変更していない。
- 1942高級COMINTについて、70正本＋2026-08-18 handoff と switch_registry の OPEN gate の衝突を明示的に処理した。現行runtimeは70/handoff側を採用し、switch側は削除せず stale gate として監査台帳へ残す。
- PREWAR v002 は TECH の可能性と1941-12時点の実現状態を分離した。
- WARSTART domain audit を追加した。PARTIAL/PROVISIONAL は「史実値へ戻す」の意味ではなく、区間値・状態を保持する。
- event relevance profile と handout builder v002 を追加した。空母戦なら AIR_PLATFORM/AIR_WEAPONS/CARRIER/SENSOR_SEARCH/SIGINT_COMINT を必須解決する。

## 現在の実行上の扱い

通常の大手戻り底は `WARSTART_1941-12-07_08_v002`。開戦後の現行局所停止点は引き続き 1942-05-06 24:00 で、5/7珊瑚海へ進む前に新handoutで5/4-6状態を再監査する。

## 情報保存

`99_LEGACY_UNTOUCHED` はv001から一切変更しない。新しい判断は新層に追加する方式で、旧判断の本文を削除・改変しない。
