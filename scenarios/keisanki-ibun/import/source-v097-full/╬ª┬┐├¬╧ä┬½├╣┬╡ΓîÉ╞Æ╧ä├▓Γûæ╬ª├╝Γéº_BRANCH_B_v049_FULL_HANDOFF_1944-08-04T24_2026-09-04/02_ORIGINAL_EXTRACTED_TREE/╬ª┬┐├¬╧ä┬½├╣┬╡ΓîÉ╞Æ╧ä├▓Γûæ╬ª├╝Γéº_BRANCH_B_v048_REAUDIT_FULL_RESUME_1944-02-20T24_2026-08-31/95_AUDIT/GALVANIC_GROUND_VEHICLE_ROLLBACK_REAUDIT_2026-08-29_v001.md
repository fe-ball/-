# GALVANIC地上車両・陸上統合差し戻し再監査 — 2026-08-29 v001

status: AUTHORITATIVE SCOPED ROLLBACK AUDIT

## 差し戻し判断

Tarawa地上戦を1943-11-24上陸前まで戻す。

理由は、`SESSION_2026-08-27_GALVANIC_MANDATORY_FACTORS_MEMO_v001` が次を必須としていたにもかかわらず、最終v003 settlementと旧negative-delta表が十分な入力台帳を持たなかったためである。

- 車両の物理数と稼働数
- 72時間再出現サイクル
- 大発・環礁内兵站
- 砲射表、測量、登録射撃、弾薬lot/QC
- 工兵車両、築城、通信機材の物理稼働

旧negative-delta表のTarawa行は、Kinsei/F6F再計算に対する独立性しか確認していない。今回の陸上入力に対する閉鎖証明にはならない。

## 史実側の固定点

米海兵隊公式史系のTarawa兵器表は、BetioにType 95車載37mmを14門記録する。米側はM4A2を14両投入した。史実20-Novでは低潮と礁・砲弾孔のため初日稼働車が激減したが、本Branchは24-Novの高水位・測定航路計画を維持している。

したがって、次の両方を同時に表現する必要がある。

1. 日本の14両を「夜襲3～4両だけ」に縮めない。
2. 米軍の14両を史実同様ほぼ礁上で失う扱いへ戻さない。

参照:

- [Tarawa Appendix I: actual enemy weapon emplacements](https://www.ibiblio.org/hyperwar/USMC/USMC-M-Tarawa/USMC-M-Tarawa-I.html)
- [U.S. Marine Corps Tank Doctrine, Tarawa section](https://www.usmcu.edu/Outreach/Marine-Corps-University-Press/MCH/Marine-Corps-History-Winter-2020/The-US-Marine-Corps-Tank-Doctrine-192050/)
- [Littoral Obstacles during Operation Galvanic](https://www.usmcu.edu/Outreach/Marine-Corps-University-Press/MCH/Marine-Corps-History-Summer-2024/Finding-the-Gaps/)

## 再構成した車両状態

### 日本

- Type 95 physical: 14
- pre-bombardment serviceable: 12～14
- bombardment後のcontact-capable/mobileまたは短距離移動火点: 6～9
- 第一夜の組織反撃: 4～5
- 11/25～26の追加mobile-firepoint/reposition pool: 2～4

14両すべてが自由に運動するわけではない。破壊・埋没・履帯切断・乗員損耗・燃料/弾薬断・回収不能を支払う。Branchの車両差は、6～9両のうち何両が数時間後・翌日に別火点へ現れるかへ効く。

### 米国

- M4A2 physical: 14
- 11/24高水位・測定航路により第一夜までに上陸: 8～11
- 第一夜に稼働: 6～8

これは史実の初日3両稼働をコピーしない一方、全14両無傷上陸にもならない。75mm/37mm、砲弾孔、海岸壁通路、単独行動による損害を残す。

## 地上戦再裁定

第一夜反撃は350～450名+3～4両から、**380～480名+4～5両**へ上方修正する。Red 2/3接続部を数時間混乱させるが、6～8両のM4A2、砲兵、照明、機関銃、駆逐艦砲撃を越えて海岸堡を破壊できない。

11/25以後、日本戦車2～4両が短距離移動火点として再出現する。登録射撃、弾薬QC、通信、工兵機材と結びつき、米軍のtank+engineer+75mm+destroyer reduction cycleを遅らせる。ただし島が小さく、米諸兵科制圧が強いため、1.3～1.6倍の機動部隊帯は使用せず、1.1～1.3倍の環礁帯に制限する。

## 修正結果

| 項目 | v003 | v047再裁定 |
|---|---:|---:|
| 米KIA/MIA | 550～700 | **620～770** |
| 米WIA | 1,350～1,650 | **1,530～1,780** |
| 米総死傷 | 1,900～2,300 | **2,150～2,550** |
| 総死傷中心 | 約2,100 | **約2,350** |
| 中心差分 | — | **+250** |
| 組織抵抗終結 | 11/28昼 | **11/28夜～11/29昼、中心11/29朝** |

米軍によるTarawa/Makin攻略、11/26空母戦、Independence/Lexington/Soryu等の損傷、Franks/Pierceの結果は維持する。

## 下流依存性

### 変更する

- GALVANIC final outcome ledger
- GALVANIC settlement
- 1943H2 year-end settlement内のTarawa損害・終結日
- 連合死者出納表予約のGALVANIC項目
- discussion frontierとload order

### 変更しない

- 11/23 Independence被雷
- 11/26空母戦と航空機損失帯
- 11/26-27 Franks沈没
- 11/27 Pierce被雷
- 日本空母・米空母の修理時計
- Gilbertsの最終領有
- 1944-01-01の艦隊OOB

地上戦の約半日～一日延長は、これらの海空イベントの発生時刻・接触幾何を反転させない。米CVE/艦砲支援をわずかに長く拘束するが、1944年1月の作戦可能艦数を変える修理損傷は生じない。

