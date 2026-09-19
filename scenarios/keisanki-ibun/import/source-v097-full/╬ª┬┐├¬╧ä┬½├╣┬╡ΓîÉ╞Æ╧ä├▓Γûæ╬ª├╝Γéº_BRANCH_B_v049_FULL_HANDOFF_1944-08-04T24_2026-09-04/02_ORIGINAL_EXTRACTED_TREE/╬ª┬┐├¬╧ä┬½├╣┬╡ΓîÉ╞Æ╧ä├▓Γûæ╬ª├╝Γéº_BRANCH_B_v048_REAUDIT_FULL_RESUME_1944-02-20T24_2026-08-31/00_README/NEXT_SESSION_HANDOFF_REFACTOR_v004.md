# NEXT SESSION HANDOFF — refactor v004

## 現在地

リファクタリング工程は終了。次は資料構造の議論ではなく歴史再走査へ移る。

正式restart：`05_WARTIME/CHECKPOINT_1942-05-06T24_v001.json`

1942-05-07珊瑚海戦闘は未実行。まずcheckpoint内 `mandatory_reaudit_before_5_7_execution` を閉じる。

## 最初に読むもの

- `05_WARTIME/CHECKPOINT_1942-05-06T24_v001.json`
- `04_WARSTART/WARSTART_STATE_LEDGER_v002.json`
- `02_TECH/TECH_INDEX_v003.json`
- `00_CONFIG/current_branch_overrides_v001.json`
- `06_RUNTIME/EVENT_RELEVANCE_PROFILES_v002.json`

必要なら `python 98_TOOLS/build_event_handout_v004.py CARRIER_BATTLE --date 1942-05-07` でイベントカードを生成する。

## 絶対に旧枝から暗黙継承しないもの

- 80/85の珊瑚海勝敗・損傷・祥鳳結果
- 85以降のMI/AL/FS等の戦果
- 史実JN-25級のMO事前情報

旧枝は削除されておらず、比較・証拠としてのみ残る。

## COMINT

現行branchでは70と2026-08-18 handoffの条件を採用する。日本高級海軍暗号本文は1942年に米側の短期戦略入力として通常利用不能。ただし低級通信、平文、traffic analysis、DF、偵察、潜水艦、地理・兵站推定は残る。

## ルールを変える場合

旧本文を書き換えず `00_CONFIG/current_branch_overrides_v001.json` の次revisionを作り、依存checkpointだけ無効化する。
