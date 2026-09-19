# 日本陸上戦闘システム統合再監査 — 2026-08-29 v001

status: WORKING INTEGRATED AUDIT / v047

## 結論

v046の陸上ハードウェア補完は、砲迫・弾薬・築城・通信・工兵機材を回復した一方、戦車・車両を「史実と同じ車体に稼働率+5～10%」へ圧縮しすぎていた。

旧正本と既存のSaipan/中国再監査には、Branch車両の主差分が明確に残っている。装甲や砲威力を別物にするのではなく、履帯、転輪、懸架、変速機、クラッチ、冷却、潤滑、公差、故障統計、予備品、回収・修理によって、同じ車両が短期間に何度戦場へ戻れるかが変わる。

このためv047では車両を独立レイヤーとして復元し、陸上戦を次の七層で統合する。

1. 人員・指揮・予備
2. 火力・観測・弾薬
3. 築城・防護
4. 通信
5. 戦車・車両・機動
6. 工兵・兵站・揚陸
7. 敵の諸兵科制圧

## 車両差分の扱い

### 戦車・豆戦車・装甲車

- Type 95/97等の型式、装甲、主砲級、乗員配置は維持する。
- 47mm砲、無線、増加装甲、新型車を無根拠に追加しない。
- 生産中央値と故障裾、部品互換、整備計画、回収・再投入を差分化する。
- 良好な整備・燃料・回収経路を持つ機動部隊では、72時間内の有効再出現を史実相当の1.3～1.6倍級まで許す。
- ただし環礁では運動空間、砲爆撃、工場喪失、残骸回収が律速するため、局地帯は1.1～1.3倍級に落とす。

### トラック・牽引車・回収車

- 現物数は増やさない。
- 稼働率+5～12%、一般的な修理時間-10～25%を上限帯とする。
- 道路、橋梁、鉄道、燃料、運転手、敵阻止を通過して初めて作戦効果になる。

### 工兵・飛行場車両

- 現存するブルドーザー、トラクター、ポンプ、発電機等のuptimeを+5～12%級とする。
- 資材がある場合の物理工事量は通常+3～8%級。重砲爆撃、燃料切れ、セメント・木材・骨材不足はこれを上回る。

## 年代別成熟

| 時期 | 車両系の状態 | 使用規則 |
|---|---|---|
| 1937～1941開戦 | 早期実在 | 初期故障裾と短期稼働率に差。回収網は不均一 |
| 1942 | 中成熟 | 既存部隊の故障フィードバックと予備品計画が改善 |
| 1943前半 | 中～高成熟 | 整備された戦車連隊・優先基地で上中位帯 |
| 1943後半～1944-02-06 | 作業帯成熟 | 機動部隊では72h再出現を使用可。孤立環礁は下方制限 |

## 二重計上防止

- Branch調整済みserviceable countから開始するイベントに、稼働率をもう一度足さない。
- 再出現を装甲・火力・生産数として数えない。
- 工兵車両uptimeを、すでに完成した築城量と重ねない。
- 揚陸効率を車両生産または殺傷率として再加算しない。
- 撃破、炎上、水没、撤退時放棄、工場喪失車両を修理復帰させない。

## 過去戦闘への反映

GALVANIC Tarawaは、必須考慮メモに車両再出現・大発兵站・固定陣地火力が明記されていたのに、最終因果台帳へ十分入っていなかったため即時差し戻し対象とした。

その他のGALVANIC Makin、Bengal/Arakan、Kwajalein/Roi-Namur初日、1941～43のactive-path地上戦は、個別イベント台帳と死者区分が揃うまで「連合死者出納表」予約を維持する。GALVANICの差分を他戦場へ横流ししない。

## 今後の地上裁定ロード順

1. `JAPANESE_LAND_COMBAT_INTEGRATED_SYNTHESIS...v001`
2. 火器・築城・通信のv046 lineage
3. 車両・装甲のv047 lineage
4. event-local OOB、serviceable、燃料、弾薬、地形、回収
5. 敵航空・艦砲・砲兵・戦車・工兵による制圧
6. 損害分類と24～72時間の修理復帰
7. 人的損害と作戦時刻

## 根拠

内部根拠:

- `SESSION_2026-08-27_GALVANIC_MANDATORY_FACTORS_MEMO_v001.md`
- 旧正本「84_歴史考察_1937-1942_前史・中国・ノモンハン・南方」
- `CHINA_TANK3_REGIMENT_RETRO_AUDIT_1944_v001.md`
- `MARIANAS_SAIPAN_1944-06-11_07-14_SETTLEMENT_v001.md`
- `JAPANESE_LAND_COMBAT_HARDWARE_LINEAGE...v001`

史実境界:

- [U.S. Marine Corps Tank Doctrine, 1920–50](https://www.usmcu.edu/Outreach/Marine-Corps-University-Press/MCH/Marine-Corps-History-Winter-2020/The-US-Marine-Corps-Tank-Doctrine-192050/)
- [Japanese Tanks and Tank Tactics, U.S. War Department Special Series No. 26](https://cgsc.contentdm.oclc.org/digital/collection/p4013coll8/id/2918/)
- [The Battle for Tarawa, Appendix I](https://www.ibiblio.org/hyperwar/USMC/USMC-M-Tarawa/USMC-M-Tarawa-I.html)

