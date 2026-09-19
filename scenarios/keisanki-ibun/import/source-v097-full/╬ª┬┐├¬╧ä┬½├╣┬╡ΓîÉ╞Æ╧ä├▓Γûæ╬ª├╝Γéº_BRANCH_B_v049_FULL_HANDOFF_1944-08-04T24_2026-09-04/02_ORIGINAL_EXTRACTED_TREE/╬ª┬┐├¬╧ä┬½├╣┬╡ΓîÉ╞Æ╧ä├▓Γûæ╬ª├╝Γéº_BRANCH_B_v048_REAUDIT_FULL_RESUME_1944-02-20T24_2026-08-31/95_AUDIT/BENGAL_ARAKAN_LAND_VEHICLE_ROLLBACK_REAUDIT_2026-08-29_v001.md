# Bengal / Arakan 陸上・車両差し戻し再監査 — 2026-08-29 v001

status: AUTHORITATIVE CAMPAIGN ROLLBACK AUDIT / v048

## 判断

`BENGAL_ARAKAN_CHITTAGONG_1943-10_12_SETTLEMENT_v001` は、車両損失を80～150両とだけ置き、車種、物理数、稼働数、損傷区分、回収経路、24～72時間の修理復帰を持っていなかった。

これはv047統合陸上規則の必須入力を満たさない。しかもBengal/Arakanは、環礁と違って7週間にわたり道路、河川、沿岸舟艇、砲兵、工兵、後方修理を繰り返す。欠落の影響はTarawaより長く累積する。

よって作戦を**1943年10月28日のNaf渡河前まで差し戻し**、独立したイベント台帳を作って再決算する。

## GALVANICとの関係

GALVANICで増えた米軍死傷者やM4A2損失をBengalへ移すものではない。両作戦間に米地上部隊・車両の直接移動はなく、Bengalの中心線は第一線・第二線空母投入0のままである。

差し戻し理由は、両作戦が共通して参照すべき日本陸上ハードウェア層が、Bengal決算でも未入力だったことにある。Tarawaの補正率や+250人を転用していない。

## 史実境界とOOB

米陸軍の日本軍便覧は、標準歩兵師団に輸送連隊を置き、標準的な自動車大隊を2～3個トラック中隊、各中隊約50両と推定している。また日本歩兵師団全体の車両は約500両級だが、米師団よりはるかに低いモータリゼーションであった。

第55師団のArakan所在とBurma Area Army直轄は維持する。第54師団は1943年11月時点で第55師団へ合流途上だったため、早期戦闘に丸ごと追加しない。

このため作戦用の陸上モータープールを、55師団の有機車両と明示的な工兵・通信・軍直轄道路輸送を合わせて物理430～560両、開始時稼働355～465両と置く。これは厳密な車番台帳ではなく、史実編制上限、既往損耗、混成輸送体系、付加部隊を同時に満たす作戦帯である。

独立戦車連隊は0、中心的な戦車戦力も0とする。未確認の豆戦車・装甲車0～4両を後方警備感度として残すが、戦闘効果は与えない。今回の主差分は「強い戦車」ではなく、トラック、牽引車、軽トラクター、工兵機材、修理工場である。

史実境界:

- [Handbook on Japanese Military Forces — infantry division and transport organization](https://www.ibiblio.org/hyperwar/Japan/IJA/HB/HB-3.html)
- [US Army official history — Japanese division motorization was roughly 500 vehicles and far below a US division](https://www.ibiblio.org/hyperwar/USA/USA-P-Triumph/USA-P-Triumph-5.html)
- [Stilwell's Mission to China — Burma Area Army retained 55th Division in Arakan](https://www.ibiblio.org/hyperwar/USA/USA-CBI-Mission/USA-CBI-Mission-9.html)
- [Stilwell's Command Problems — 54th Division moving to join 55th in late 1943](https://www.ibiblio.org/hyperwar/USA/USA-CBI-Command/USA-CBI-Command-2.html)
- [RAF official history — Arakan terrain, roads, air power and supply constraints](https://www.ibiblio.org/hyperwar/UN/UK/UK-RAF-III/UK-RAF-III-15.html)

## 車両・工兵の適用

- 開始時稼働数にBranchの+5～12% dispatchabilityを含める。もう一度加算しない。
- Cox's–Chakaria–Chiringa道路軸では、到達可能な一般故障に24～72時間の1.20～1.40倍級再出現を認める。
- Naf、Sangu、Karnaphuli渡河、泥濘、橋梁破壊、英空軍阻止では上限を下げる。1.6倍は使用しない。
- 永久損失と一時的mission-killを分離する。沈没、焼失、敵手への放棄、河川喪失は復帰不可。
- 改善は沿岸LOCの150～220t/dayを増やさない。最終配分の途切れを減らし、砲弾、工兵資材、通信班、負傷者後送を同じ作戦テンポに乗せる。

旧80～150両の一括working lossは、永久喪失55～95両、一時mission-kill 45～80両へ分解する。一時損失のうち25～50両は24～72時間で復帰し、年末時点の長期修理・部品取りは15～30両とする。

## 再裁定

| 項目 | v001 | v048再裁定 |
|---|---:|---:|
| 日本軍総戦闘損害 | 5,800～8,300、中心6,900 | **5,300～7,600、中心6,300** |
| 日本KIA/MIA | 1,700～2,400 | **1,550～2,150** |
| 英印軍総戦闘損害 | 7,200～10,500、中心8,700 | **7,700～11,100、中心9,300** |
| 英印軍KIA | 1,500～2,100 | **1,700～2,350** |
| 日本車両 | working loss 80～150 | **永久55～95、一時45～80、うち24～72h復帰25～50** |
| 英印軍車両損失 | 350～600 | **390～660** |
| Chittagong進入 | 12月15日午後～夜 | **12月14日夜～15日朝、中心14日夜** |

日本側の人的中心差は約-600、英印側は約+600である。Tarawaほど一方向に殺傷率が動かないのは、前進戦闘では観測、準備陣地、補給、視界が頻繁に切れ、改善した火器・車両を常時使えないためである。

第7インド師団はなお主力人員を脱出させるが、保存帯を約8,000～9,500から7,700～9,100へ下げる。橋梁・港湾爆破は間に合い、Chittagongを無傷で奪取する結果にはしない。

## 下流

年末の第55師団は依然として疲弊している。ただし旧決算より実効人員が約300～600、dispatchable車両が約20～45多い。Chittagongの12月末処理能力は300～500t/dayから320～520t/dayへ小幅上方修正する。

これは1月の陣地化・警戒・限定偵察を少し早めるが、Feni/Comilla攻勢を解禁しない。海上LOC、破壊されたKalurghat橋、英空軍、Feni–Comilla防衛弧が律速するため、1944年1月末～2月6日の「硬化する膠着」は維持する。

GALVANICの海空・地上結果、第二線空母のPacific優先、Indian Ocean第二水上増援HOLD、U-Go NO-GOは変更しない。
