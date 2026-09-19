# 浅井1937年：顧客・行政採用・生産需要・満州経済監査 V1

> 状態: WORKING AUDIT / NOT CANON
>
> 現行権威は `ASAI-WORLDLINE-HANDOFF-2026-08-30-FULL-V4/01-CURRENT-BRANCH`。`90-SOURCE-QUARANTINE` と復元V48資料は provenance / restore-candidate の根拠にのみ使用し、旧名称・旧採用史・旧数量を自動復活させない。
>
> 監査時点: 1937-07-27 summer branch.

## 0. 今回の裁定候補

1. **計算機は「200–400フルセット」ではなく、日本+満州で約96–157 FSE、中央約125 FSE**へ下方修正する。
   - FSE = 穿孔・検孔・分類・集計印字を備えた標準一式の年間処理能力換算。
   - 実際の単体機数は約500–900台でも矛盾しない。穿孔機、検孔機、分類機、集計機、印字機が別機だからである。
   - 最新科学計算用の大型リレー計算室は別枠で、日本14–20拠点、満州2–4拠点程度の監査帯。

2. **独立GT 約125コア/年は維持可能**。ただし意味を分ける。
   - 顧客納入・設置: 約70–105コア/年。
   - 工場完成: 約105–135、中央約125コア/年。
   - 差分は社内試験、共同評価、予備、補修交換、完成在庫。
   - よって current Q-007 の「GT125」は `factory completions` と明記すればかなり閉じられる。

3. **排気ターボ 約1300コア/年も維持可能だが、factory completions/run-rate とする**。
   - end-user absorption / installed-disposed: 約1,050–1,220/年、中央約1,135。
   - factory completion: 約1,200–1,350/年、中央約1,300。
   - 軍需は current V4 の325–465/年を保存。残りは商船・沿岸/漁船・大型4-cycle、定置産業diesel、鉱山・発電、鉄道/特殊車、補修交換。
   - 満州に存在する分は全用途込み80–125/年程度、うちcivil/institutionalだけなら概ね60–90/年を監査帯とする。

4. **1937年満州のマクロ純差は、以前の+0.8–1.0%より下げる**。
   - national income 全体: +0.20–0.75%、中央 +0.44%（約1,200万円）。
   - mining + industry + commerce + transport + public の modern sectors: gross +0.87%中央。
   - mining + industry + transport の直接コア: +1.56%中央。
   - 理由は農業が1937年国民所得の約半分で、浅井技術の1937年直接接触が小さいこと、さらに日本系資本への利潤流出があること。

5. **日本本土は1937年GNP水準で +0.22–0.45%、中央 +0.35%程度**を新たな監査帯とする。
   - 名目GNP 228.23億円に対して約0.50–1.03億円、中央約0.80億円相当。
   - 直接の浅井売上ではなく、工具・特殊鋼/QC、過給、計算、在庫・保全、非常電源による downstream value-added / avoided loss の合計。

## 1. 計算部門：何が本当に差分か

史実日本は浅井抜きでもPCSを知っている。1920国勢調査でHollerith、1923に本格Powers一式。1920年代には鉄道省、横浜税関、生命保険、三菱造船、呉工廠などへ広がる。IBM系も1925に日本陶器へ入り、1937に日本法人が成立する。

従って浅井の差は「パンチカードの発明」ではない。以下が差分になる。

- 国産供給で輸入待ち・外貨・部品供給リスクを下げる。
- リースを厚くして初期投資を下げる。
- 返却旧型機を再生し、二次市場へ送る。
- 小顧客は自前一式を買わず service bureau を使える。
- 機械そのものだけでなく、業務分析、カード設計、品目コード、工場番号、材料コード、帳票を売る。
- 軍需・大企業は安全区画へ設備を入れ、汎用計算型と保守だけ浅井から買う。

このモデルでは1937年に約125 FSE相当が妥当。200–400の「一式」は当時の日本市場を考えると過剰だった。

### 行政・公共採用

中央統計は先行済みなので、浅井の追加効果は増設・保守・国内調達。鉄道省は非常に相性が良く、貨物、車両、資材、修繕、給与、運行統計へ横展開できる。軍工廠は給与・在庫・原価から技術計算へ自然に伸びる。

地方庁は全府県が一式を持つ像にはしない。大都市・工業県・公共事業部局の一部が小型設備を持ち、残りはservice bureauで処理する方が1937年らしい。

## 2. 満州の計算：一番効くのは「計算速度」より共通形式

復元資料は満州を明示的に中古再生機の二次市場にしており、品目コード、工場番号、材料分類、在庫帳票、鉄道・鉱山のカード形式の統一を効果の中心に置く。このアイデアは保存価値が高い。

ただし満鉄自体は史実でも巨大な調査・会計・鉄道経営組織であり、浅井が「近代経営を教える」のではない。世界線差は、満鉄・国有鉄道系・鉱山・港・工場・満洲国官庁の間で同じコードや帳票を使う範囲が広く、安くなること。

1937年の満鉄管理鉄道網は平均営業線約9,814km級まで拡張している。ネットワークが巨大なので、単独事務所の集計時短より、車両・資材・貨物・保全データを跨拠点で合わせられる価値が大きい。

1937年4月には満洲産業開発五ヶ年計画が実施され、7月1日に実業部を改編した産業部が発足。現在時点7月27日には新組織はまだ約4週である。よって「産業部が浅井機を入れたから1937年GDPが大幅増」は置かない。1937年の水準差は主として1930–36の満鉄・企業・鉱山・工場への累積浸透で説明し、新五ヶ年計画への計算・標準化効果は1938年以降へ送る。

## 3. 満州のdiesel / turbo

満州は浅井過給が効きやすいが、幹線鉄道を一気にdiesel化する場所ではない。石炭が豊富で液体燃料は制約なので、蒸機の大宗を残しつつ、以下へdieselを寄せる。

- 鉱山・工事・重貨物の特殊車両。
- 発電機・ポンプ・定置機。
- 小編成・高頻度・特定用途の気動車。
- 軍用砲牽引・重6x4・装甲車など。
- 高地、高温、粉塵、長距離で自然吸気の出力低下が問題になる用途。

史実でも1935年に一社だけで満州向けを含む132台のdiesel大量受注例があり、50PS船用105台、150PS船用7台、150PS発電用18台、340PS発電用2台を3年で納めている。このことは「満州・周辺で中小dieselを数十台/年単位で吸収する市場」が存在したことを示す。一方、日本の鉄道dieselは1928初採用後も維持技術に苦労し、国鉄が1935以降に標準級dieselを競作させる段階である。ゆえに浅井差は全鉄道diesel化でなく、限定用途の信頼性・過給・潤滑・保守の改善に置く。

## 4. GT125 / turbo1300 の需要監査

### independent GT

current V4軍需30–60コア/年を基底とし、civil/publicを積む。

- 治水・排水: 8–15。
- 鉄道・港湾・utility非常電源: 8–15。
- 工業standby/peak: 15–25。
- 商用/実証/貸与: 5–10。

単純和は重複するため、顧客納入を70–105に丸める。これに試験、共同評価、予備、在庫20–45程度を加えれば factory completion 105–135、中央125となる。

したがって `GT actual 125/year` は「actual customer demand」ではなく **工場完成コア数**と定義するのが最も安定する。

### exhaust turbo

current V4軍需325–465を基底に以下を置く。

- merchant/coastal/fishing/large 4-cycle marine: 260–380。
- stationary industrial/mining/genset/pump: 160–240。
- railway/civil heavy-special vehicle: 50–90。
- replacement/service/export/training: 120–180。

全レンジを機械的に足すと915–1,355だがカテゴリ間の重複と時期ずれがある。顧客側で1,050–1,220、factory completions 1,200–1,350、中央1,300という二段に置く。

「1,300売れた」ではなく「1,300完成した。その一部は補修在庫・翌期据付・試験・輸出待ち」である。

## 5. 満州1937マクロ監査

史実の1937年満洲国国民所得（物的方法）は以下の百万圓換算。

- agriculture 1,312.319
- fisheries 6.159
- mining 65.279
- industry 259.506
- commerce 765.925
- transport 300.272
- public/liberal/domestic 125.013
- international investment/business profit difference -131.268
- total 2,703.204

浅井の主な接触先は mining / industry / transport と、その周辺のcommerce/adminである。農業には機械修理、輸送、肥料・加工等の二次波及しかまだ入らない。

中央ケースのレベル差仮定：agri +0.08%, fisheries +0.25%, mining +1.5%, industry +2.0%, commerce +0.4%, transport +1.2%, public +0.25%。これで域内gross upliftは約1,421万円。

さらに資本集約部門の利潤の一部が日本側へ帰属することを表す粗いoutflow offsetを約220万円置き、満洲国national incomeの純増を約1,201万円、**+0.444%**とする。

この数字は「満州の現場が0.44%しか変わらない」という意味ではない。mining+industry+transportだけでは中央 +1.56%、modern sectors全体ではgross +0.87%。農業の大きさと域外利潤帰属が国全体の比率を薄める。

### 五ヶ年計画への将来効果

原計画約26億円規模のうち、浅井の計算・帳票・保全・コード統一が本当に触れる投資を45–60%、その部分の資材待ち・重複・在庫滞留・発注誤差等を1.5–3.0%改善すると置く。

有効資本の前倒し/節約相当は約1,750万～4,650万円、中央約3,050万円。これはGDPへ一括加算してはいけない。工場完成時期や設備稼働率に変換されて1938–40へ分散する。

1938–40の exposed sectors の成長率を年+0.1～0.25ポイント程度押す余地はあるが、日中戦争による計画改訂、資材統制、輸送競合が同時に発生するため forward OPEN とする。

## 6. 日本本土1937マクロ監査

1937名目GNPは約228.23億円。1934–36平均の国民所得構成では一次産業約20%、二次産業約31%、三次産業約49%である。

浅井効果を二次産業へ最も厚く置き、一次へごく薄く、三次へ計算・鉄道・電力・商務・行政分だけ置くと、1937のGNP水準差は **+0.22～0.45%、中央+0.35%程度**が妥当。

金額は約0.50～1.03億円、中央約0.80億円/年相当。

ここで重要なのは売上高との区別。浅井自体の付加価値ではなく、利用側で発生する切削時間短縮、工具交換減少、不良低下、設計反復減少、在庫滞留減少、車両/機関停止時間減少、停電損失回避を含む。

+1%以上を1937に置くのはまだ早い。農業、零細小売、一般建設、軽工業など国民経済の大部分へ浅井技術が深く浸透していないためである。

## 7. 行政効果をGDPへ足し過ぎない規則

行政計算機は「役人が同じ人数で帳票を二倍作る」なら測定上の産出が増え得るが、現実には人手・残業・誤記・再集計を減らす。この場合、政府部門の測定国民所得はむしろ直接には増えないこともある。

従って行政機械化の主要マクロ効果は、

- 予算/資材配賦の遅延減少
- 在庫・貨車・設備の所在精度
- 工事順序と発注の整合
- 税関・輸送・統計の再集計速度
- 企業・官庁間のコード互換

として民間/公企業側の資本稼働率へ流す。満州中央ケースでpublic sector自体の upliftを+0.25%に抑えたのはこのため。

## 8. Current branchへの推奨変更

### Q-007

`1937 GT125 / turbo1300年産の実需根拠` は以下へ再定義すれば CLOSE-CANDIDATE。

- GT: customer deliveries 70–105; factory completions ≈125 central.
- turbo: end-user absorption 1,050–1,220; factory completions ≈1,300 central.

この二層化を `production_or_adoption` と `factory_completion` の別フィールドで持つ。

### computation adoption gate

新規に1本作る価値がある。

- Japan+Manchuria 1937 FSE: 96–157, central ≈125.
- exact named customer/site count remains OPEN where V4 lacks closure.
- high-end scientific rooms: Japan 14–20 sites, Manchuria 2–4.
- Mitsubishi/Nakajima U4 remains current CLOSED; U4を他社へ自動伝播しない。

### Manchuria macro gate

- 1937 national income level delta: +0.20–0.75%, central +0.44%.
- modern-sector gross delta central: +0.87%.
- direct mining/industry/transport core central: +1.56%.
- Five-Year Plan capital-efficiency effect: forward OPEN for 1938–40.

## 9. 監査に使った主な内部資料

Current V4:
- `05-CURRENT-CLOSED-PRODUCT-WEAPON-LEDGER.tsv`
- `06-CONFLICT-AND-REVIEW-QUEUE.tsv`
- `08-MILITARY-DELIVERY-LEDGER-1937-SUMMER.md`
- `04-CURRENT-BRANCH-HISTORY-1903-1937-SUMMER.md`
- `99-NEXT-CHAT-HANDOFF.md`

Quarantine/restored provenance:
- `main/asai-works-computation-origin-business.md`
- `computation-2026-08-22/prior-v2/05_civil_computation.md`
- `provisional-2026-08-20/07-asai-works-computation-commercial-diffusion-provisional.md`
- `main/asai-works-gt-first-customers.md`
- `main/asai-works-military-diesel-vehicles.md`
- `main/asai-works-company-structure.md`

External calibration used in the audit:
- Statistics Bureau of Japan: PCS introduced for 1920 census; full Powers system imported 1923.
- IBM Japan history: first IBM Hollerith installation at Nippon Toki 1925; Japan Watson Statistical Accounting Machinery established 1937.
- Historical computing chronology: Railways, customs, insurers, Mitsubishi yards, Kure Arsenal were real prewar PCS users.
- South Manchuria Railway accounting-history study: 1937 managed/open railway length ≈9,814.4 km; Five-Year Plan ≈2.6bn yen, ≈1.4bn for minerals/industry.
- Manchukuo national-income study: 1937 official income table used above.
- JACAR: Manchukuo Industrial Affairs Department effective 1937-07-01, responding to Five-Year Plan active since April.
- Akasaka diesel history: 1935 order of 132 diesel engines linked to the Chinese Eastern Railway sale / Manchukuo settlement, delivered over three years.
- Railway Technical Research Institute: first Japanese diesel rail vehicle 1928; JNR diesel-engine competition from 1935.
- Long-Term Economic Statistics / historical GNP table: Japan 1937 nominal GNP 22,823 million yen.

