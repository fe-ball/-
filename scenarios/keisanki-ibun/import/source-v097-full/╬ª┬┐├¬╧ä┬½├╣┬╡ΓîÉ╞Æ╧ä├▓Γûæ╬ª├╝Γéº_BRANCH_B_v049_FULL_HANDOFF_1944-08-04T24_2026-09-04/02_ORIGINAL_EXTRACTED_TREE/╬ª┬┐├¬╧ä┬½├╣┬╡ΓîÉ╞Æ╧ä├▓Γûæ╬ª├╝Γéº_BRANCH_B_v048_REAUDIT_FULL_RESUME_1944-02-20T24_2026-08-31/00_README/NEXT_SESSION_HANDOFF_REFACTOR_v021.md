# 次回引継ぎ — refactor v021

## CURRENT

- 再監査開始点: **1943-03-26T00:00**
- モード: `PACIFIC_1943_SPRING_COUPLED_REAUDIT`
- 理由: 1943年5月Efate再監査でAleutians同時進行を未統合だったことが判明。Efate戦結果を押し進めず、北太平洋の艦艇・輸送・情報判断を先に閉じる。
- 1943-05-24～26の旧Efate戦シミュレーションは **scenario probe / provisional**。Wasp mission-kill等を現行史実として継承しない。

## 最初に読む

1. `06_RUNTIME/CURRENT_BRANCH_STATE_v003.json`
2. `06_RUNTIME/SESSION_2026-08-26_ALEUTIANS_EFATE_COUPLED_REAUDIT_HANDOFF_v001.md`
3. `06_RUNTIME/1942H2_STRATEGIC_SETTLEMENT_v001.md`
4. `06_RUNTIME/ALLIED_LOGISTICS_FLEET_AXIS_EFFECTS_1942H2_v001.md`
5. `06_RUNTIME/1942Q2_OPERATION_C_MO_MI_REAUDIT_SETTLEMENT_v001.md`
6. `06_RUNTIME/NEW_CALEDONIA_1942-10_SETTLEMENT_v001.md`
7. `06_RUNTIME/SANTO_1942-08_TECH_STACK_REAUDIT_v001.md`

## 次回の処理順

1. **1943-03-26 Komandorski** の正確なOOB/艦状態を枝台帳から再構成。
2. 海戦結果を再裁定。ただし目的は撃沈数より **Attu輸送船団が任務を継続できるか**。
3. 日本側の耐候航法・機関信頼性・船団維持・fast transport/鼠輸送能力をイベント確率へ変換。
4. Attuへ実際に届く兵員・弾薬・食料・工兵資材・医療・通信・対空資材を算定。
5. 米側がその補給をどこまで認識できるかを別判定。
6. 米側のAttu/Kiska発起判断を再構成。Efate防衛と同一の艦艇/船腹財布から支払う。
7. 日本側のAleutians上陸警戒・救援/放棄判断を再構成。Attu/Kiska/date/OOBを事前知識にしない。
8. LANDCRAB相当の日付・戦力・結果を閉じる。
9. その結果から **1943年5月Efate OOBを再構築**し、限定攻撃の発起日・Wasp/CVE/BB/CA/DD配置を再裁定。
10. その後にだけIndian Ocean案を再開。

## 最重要論点

### 日本の輸送能力

史実Tokyo Expressをそのままコピーしない。台帳上の改良はAleutiansでは平均性能より、

- 悪天候で予定速度を維持できるか
- 霧中の集結/到着誤差
- 機関故障で一航海が潰れる確率
- 荷役時間
- fast transportの積載内容
- 護衛要求
- 一つの天候窓を使い切れる確率

へ質的に効く可能性が高い。

またSolomons消耗の減少と設計変更により、輸送艦/駆逐艦/補助艦の **数も史実と違う**。北方投入=南方から同数減、とは自動的にしない。

### 米国のトレードオフ

EfateはSantoとNew Caledoniaの間で敵前増強中。したがって米軍が北へ行く場合、

- fast CV/fast BB
- old BB/CVE
- CA/CL/DD
- APA/AKA/LST等
- AO/tender
- engineers/air defense

を分離して、どれなら北へ出してもEfateを危険なほど薄くしないかを見る。

### 情報認識

双方とも「何か来る/何か守っている」ことは察知できても、相手の正確な目標・日付・OOB・補給量は知らない。

- 日本: Adak/Amchitka、空襲テンポ、船舶通信、Komandorskiから春の上陸可能性を評価。
- 米国: 日本のAttu補給が成功したか、守備隊が何人/何日分の物資を持つかを必ず不確実情報として扱う。

## 継承してよい大枠

- Port Moresby: 日本保持。
- Lunga/Tulagi: 日本保持。
- Santo: 日本保持。
- New Caledonia: 現行settlementに従い日本軍事優位＋仏行政継続。
- 日本四正規空母核心: 翔鶴・瑞鶴・飛龍・蒼龍。
- 米1942空母大損失、Wasp生存・修理復帰。
- 五号: 1943-03-25開始の現行線。
- Limited FS: 1942-11-20終了。Fiji/Samoa自動継続禁止。

## 継承禁止

- 5/24 Efate D-day固定。
- Efateの旧仮置き航空機数/OOB。
- Efate旧式BB4隻同時配置。
- Denver被雷、Wasp mission-kill等のシミュレーション結果。
- 史実5/11 LANDCRABの日付/OOB/損害の自動コピー。
- Attu守備2.5～2.7千等の先取り。

まずKomandorskiとAttu補給から始める。
