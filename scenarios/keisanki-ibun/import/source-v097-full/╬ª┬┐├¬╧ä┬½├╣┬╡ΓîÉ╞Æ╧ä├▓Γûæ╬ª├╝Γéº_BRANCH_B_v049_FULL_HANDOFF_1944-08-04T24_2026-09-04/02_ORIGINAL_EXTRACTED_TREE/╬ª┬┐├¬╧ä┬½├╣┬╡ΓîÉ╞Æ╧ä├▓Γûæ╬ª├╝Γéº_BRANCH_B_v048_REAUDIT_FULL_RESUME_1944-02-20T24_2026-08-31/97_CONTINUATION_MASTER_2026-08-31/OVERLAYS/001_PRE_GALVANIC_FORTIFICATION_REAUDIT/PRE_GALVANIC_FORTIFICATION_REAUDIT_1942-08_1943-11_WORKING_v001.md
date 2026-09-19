# PRE-GALVANIC 要塞化・島嶼防御再監査 — 1942-08〜1943-11-23 WORKING v001

status: WORKING / REOPEN-GATE / NOT CURRENT AUTHORITY
branch: Branch B v048 semantic base
purpose: GALVANIC 再計算に先立ち、これまで固定していた「同じ労働・資材 envelope」という仮定を再監査する。

## 0. 今回の再開理由

v047 の GALVANIC rollback は、Tarawa の戦車物理数・稼働・回収、砲射表、通信、工兵機材などの**陸戦実行層**を再注入した。一方、築城資材・建設機械・基地防護設備が「史実と同じ量だけ島に届く」という上流仮定は実質的に残った。

Branch B では、1942 年末までに前進基地維持へ月 7.5〜9.5 万 t（回復月 9〜12 万 t）級の配送実績があり、輸送効率・月間回転・荷役・修理日数も史実より改善している。Guadalcanal 史実型の大量喪失が無い一方、Midway / Port Moresby / Lunga-Tulagi / Espiritu Santo / New Caledonia の維持費も実際に払っている。

したがって「Guadalcanal で失わなかった船腹・工兵・機材を丸ごと Central Pacific に足す」ことは禁止するが、**重要基地へ実際に届く建設貨物と建設プラントが史実と同量であると固定することも禁止**する。

## 1. GALVANIC 前に既に存在する能力

GALVANIC の戦訓はまだ無い。したがって 1943-11-24 より前に、Tarawa の lagoon-side 弱点を未来知識で完全補修したり、FLINTLOCK 後の縦深防御を先取りしたりしない。

ただし物理的築城能力そのものは別である。現行 land-hardware lineage は、1943H2 の築城標準化・通信機材 serviceability・工兵機材 uptime を FULL WORKING BAND（time / material / terrain gate 付き）としている。

この時点で自然に存在する差は以下。

- 測量、設計表、工事数量表、材料歩留まり、施工順序の標準化。
- 土・木材系掩体、交通壕、revetment、小型防護庫の完成量増加。
- 弾薬・燃料・通信の小分散と blast separation。
- 発電機、ポンプ、トラクター、コンプレッサー等の実働率向上。
- 固定射界での射表、測量、事前登録、観測・通信冗長性。
- 大発等による lagoon / atoll 内の弾薬、水、工兵資材、火砲、予備部隊移動。

これは「賢い GALVANIC 後 doctrine」ではない。**史実型の防御思想を、より完成度高く、より壊れにくく物理化する**差である。

## 2. 輸送差を要塞化へ接続する規約

### 2.1 使ってよい上流差

- 開戦期の実効 cargo/voyage +4〜8% と月間 turnaround +5〜10% は同一物流系の効果として扱い、相互乗算しない。
- 1942 年鋼塊全国差 +2.5〜4.5% は全量を築城へ振らない。
- ship-days、港湾待機、修理、積載適合性を優先し、未監査の総 GRT を使わない。
- Guadalcanal 史実型喪失の回避効果は 1942-08 以降に存在し得るが、Branch の南太平洋前進基地維持費を先に支払う。

### 2.2 島へ送るべきもの

増援歩兵だけを最適解としない。基地価値と地形が許す場合、以下を一つの construction / defense package として扱う。

- bulk: cement, reinforcing steel / structural steel, timber, wire, pipe, sandbags, explosives, mines, fuel/water containers
- plant: mixer, compressor, rock drill, pump, generator, tractor, truck, winch, welding / cutting equipment, small machine tools
- combat support: ammunition, spare barrels, optics, telephone cable, batteries, test gear, medical/water stores
- coastal / lagoon denial: existing coast guns and ammunition, mines/obstacles, Daihatsu and service craft; midget submarines / MTBs only when a dated allocation and suitable harbor/lagoon exist

大型固定砲は「沈没艦の余剰砲塔」を自動生成しない。Branch B は艦艇喪失が薄いため、むしろ salvage gun source は史実より細い可能性がある。追加砲は旧式沿岸砲・旧式艦砲・目的生産簡易砲架など、出所を別途 trace する。

## 3. 1943-11-23 時点の防御投資優先度（暫定）

これは兵員数の新規作成表ではなく、**追加の建設・防護資源をどこへ置く合理性が高いか**の working ranking。

### Tier A — 高優先

**Tarawa / Betio**
- forward airfield / Gilbert gate として高価値。
- ただし極小 atoll なので縦深 ceiling が強い。
- extra material は完成度・生残率を上げるが、配置思想（south/west 優先、lagoon north の相対低優先）は GALVANIC 前には大きく変えない。

**Nauru**
- 有用な航空基地。
- 港湾・荷役条件は悪いが、raised island / rugged interior / existing excavations のため、資材を防護へ変換する適地は Betio より大きい。
- runway suppression と基地機能消滅を同義にしない。revetment、分散燃料、修理、通信、防空を独立破壊対象とする。

**Mili / Maloelap (Taroa) / Wotje**
- outer Marshall airfield nodes。史実でも優先築城対象。
- Branch では land-air、水上航空、search network の生残基盤としてさらに価値が高い。

**Kwajalein / Roi-Namur**
- lagoon / logistics / air / submarine / command hub として高価値。
- ただし GALVANIC 前は beach-defense doctrine の優先方向がまだ後知恵化していないため、「拠点 hardening」と「全周対上陸要塞化」は分ける。

**Jaluit**
- lagoon / seaplane / logistics node。水上航空の ramp, fuel, tender/support craft, crane, dispersal を別 layer とする。

### Tier B — 中優先

**Makin**
- seaplane/base function はあるが trained first-line garrison が小さく、追加工事だけでは Tarawa 化しない。
- combat manpower が律速。建設労務を infantry に変換しない。

**Ocean / Banaba**
- raised phosphate island で natural shelter potential はあるが、航空・港湾・作戦位置の価値を Nauru と同一視しない。

**Eniwetok**
- 1943-11 時点では後の FLINTLOCK 直前ほど最優先ではない。改善は存在しても集中度は抑える。

## 4. 島別 working hardening band

以下は「戦闘 multiplier」ではない。史実相当の建設計画を baseline とし、Branch の有用 delivered material、工程効率、plant uptime を重複させずに**完成物・生残機能へ変換した暫定帯**。

| 地区 | useful construction delivery | 完成する earth/timber/protected works | concrete-heavy works | 主要な質的差 | 地形 ceiling |
|---|---:|---:|---:|---|---|
| Tarawa | +5〜15% | +15〜30% | +5〜15% | 分散庫、通信、revetment、障害完成度、既存砲の防護 | 非常に強い |
| Makin | +5〜10% | +10〜20% | 0〜+10% | seaplane/base防護、障害、小火点 | 非常に強い |
| Nauru | +10〜20% | +15〜30% | +5〜15% | 航空機掩体、燃料/修理分散、自然地形 shelter 活用 | 中程度 |
| Mili/Maloelap/Wotje | +5〜15% | +10〜25% | +5〜15% | airfield revetment、stores、C2、水上航空支援 | atoll依存 |
| Jaluit | +5〜15% | +10〜20% | +0〜10% | lagoon/water-air support hardening | 強い |
| Kwajalein/Roi | +5〜15% | +10〜20% | +5〜15% | logistics/air/sub-base hardening | atoll強、ただし面積大 |
| Eniwetok | 0〜+10% | +5〜15% | 0〜+5% | 初期 hardening | 強い |

注: delivery と construction efficiency を単純に掛けない。帯は両方を統合した working output である。

## 5. GALVANIC に入る前に固定する「過去の陸戦ミス」チェック

1. physical OOB と serviceable/crewed を分ける。
2. bombardment 後の contact-capable と、完全な mobile-ready を分ける。
3. mission kill / recoverable / catastrophic / drowned / abandoned を分類し、repair/reappearance はその後に行う。
4. construction/support personnel を first-line infantry にしない。
5. gun count だけでなく crew, observation, registration, ammunition survival, communications を追う。
6. better firing tables / QC を一律命中率 multiplier にしない。prepared lane でのみ効かせる。
7. fortification は warning time × labor × material × plant × terrain で閉じる。深い tunnel / concrete bunker を願望だけで増やさない。
8. ammo/water/medical/telephone line の分散が bombardment 後の組織抵抗へどう残るかを追う。
9. tanks は gun/armor が勝手に強くならない。Branch 差は running gear, transmission/clutch, cooling/lubrication, spares, recovery/reappearance。
10. atoll の vehicle reappearance は mobile formation band を使わず、workshop access / tiny maneuver space / naval fire で強く cap する。
11. Daihatsu / lagoon logistics は D-Day 前の ammo, guns, water, engineers, reserves の位置を変え得る。
12. runway suppression と water-air suppression を分ける。ramps, fuel, tenders, cranes, anchorages を別 target set とする。
13. aircraft existence / local allocation / serviceable / sortie-ready を分ける。
14. 沿岸砲、甲標的、魚雷艇を「能力があるから各島にいる」としない。dated allocation + suitable geography が必要。
15. GALVANIC 前には GALVANIC の戦訓を入れない。強化された誤った配置は、誤ったまま強くなることがある。

## 6. GALVANIC への propagation gate

現 authoritative `GALVANIC_BRANCH_B_1943-11_SETTLEMENT_v004` は、Tarawa ground vehicle/hardware node を再開・再閉鎖したが、pre-battle construction/logistics material envelope を再開していない。

したがって次を WORKING_REOPEN とする。

- 11/23 Nauru suppression sortie wallet / residual runway and support function
- Marshall/Gilbert land-air ground-loss and repair persistence
- water-air ramps / fuel / support craft suppression burden
- Tarawa pre-invasion fortress survival, beach-fire synchronization, ammo/comms survival
- Makin fortification/base survival
- Tarawa vehicle bombardment-survival state（physical count は変更しない）

当面維持するもの:

- GALVANIC D-Day = 1943-11-24
- historical/Branch tide-lane logic
- Tarawa total/first-line personnel accounting unless separate troop-allocation ledger reopens it
- Type 95 physical 14 / US M4A2 physical 14 unless new OOB evidence
- no automatic extra coast gun / tank / infantry count
- no pre-GALVANIC lagoon-defense hindsight

## 7. 次の adjudication sequence

1. 1943-11-10〜23 US mobilization signature と日本 alert を固定。
2. Tarawa/Makin/Nauru/Marshall の 11/23 physical fortification & base-function ledger を固定。
3. Nauru suppression を再実行。
4. Marshall air / water-air suppression と sortie persistence を再実行。
5. Tarawa prelanding naval/air bombardmentで、砲・観測・通信・弾薬・戦車・掩体の surviving state を出す。
6. 11/24 D-Day を、前回の tank/ground correction を保持したまま再計算。
7. Makin を同じ精度で再監査。
8. ground closeout が 11/26 carrier battle geometry へ届くほど変わった場合だけ海空 node を再開する。

この v001 は戦果を変更しない。次の GALVANIC 再計算用の上流入力ゲートだけを開く。
