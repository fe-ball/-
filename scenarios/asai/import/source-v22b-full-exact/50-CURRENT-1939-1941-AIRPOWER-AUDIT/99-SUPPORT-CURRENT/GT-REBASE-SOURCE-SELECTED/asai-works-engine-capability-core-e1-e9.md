# 発動機能力コア正本——E1–E9・規模帯・後端方式（v48再配置）

> **v48 canonical authority.** E世代は一個のエンジン型式ではなく、各年代に支払済みの圧力比・入口温度・要素効率・材料・計算/試験能力が作る**技術前線**である。実際の馬力・推力は、世代能力 × コア規模 × 後端方式 × 据付・定格を支払って初めて決まる。
>
> 本稿はv38以後の再基底化をまとめ直し、旧航空史に埋もれていたE世代表を発動機上流の親へ戻す。個別航空機の速度・航続・採用年は本稿から自動生成しない。

## 1. 読み方

### 1.1 E世代 = 技術前線

- E1–E9は「この世代なら必ずこの出力」というレールではない。
- 世代は主として **圧力比(PR)、タービン入口温度(TIT)、圧縮機/タービン効率、熱部材料・冷却、計算・試験・制御の成熟**を表す。
- 史実年次は較正錨であって上限ではない。現地で製造・試験・整備でき、必要な実時間を払えていれば前倒しできる。

### 1.2 規模帯は独立

- **小型コア：約5–8 kg/s**
- **中型コア：約10–15 kg/s**
- **大型コア：約20–40 kg/s**

規模帯を跨ぐと新しいコア設計が必要。比仕事だけを保った自由拡大は禁止する。大型化は圧縮機径、軸・ディスク、ケーシング、燃焼器均一性、始動、振動、加工・試験設備を別に払う。

### 1.3 コアと商品を分ける

**商品 = コア + 後端 + 補機/減速/ノズル/吸気 + 定格 + 据付**。

後端の代表は、

- 軸出力（ターボプロップ／ターボシャフト／舶用・発電）
- 純ジェット
- 後置ファン／低バイパスfan
- 前置fan／多軸fan
- 再燃焼
- 二重反転プロペラ／分割動力

である。同じコアでも目的関数で商品は変わる。

## 2. E1–E9 技術前線

| 世代 | 主年代帯 | PR | TIT | 圧縮機効率の代表 | 単純熱効率の座標 | gross比仕事の座標 | 能力の読み |
|---|---:|---:|---:|---:|---:|---:|---|
| **E1** | ～1921 | 2.5 | 540℃ | 0.77 | 約8% | 約32 kJ/kg | 正味出力成立そのものが課題 |
| **E2** | ～1925 | 3.0 | 620℃ | 0.79 | 約12% | 約56 | 改良実証、過給機へ技術転用 |
| **E3** | 1928–29 | 3.5 | 690℃ | 0.80 | 約15% | 約77 | 将来性実証、商品構成の入口 |
| **E4** | 1931–33 | 4.5 | 710℃ | 0.82 | 約18% | 約93 | 最初の売れる独立GT |
| **E5** | 1934–37 | 6 | 800℃級 | 0.83 | 約22.5% | 約126 | 材料・定格を分けた限定実用、多用途化 |
| **E6** | 1938–41 | 7 | 870℃級 | 0.84 | 約26% | 約155 | 軸・純ジェット・fanを実用品として主力化可能 |
| **E7** | 1942–44 | 8 | 900℃級 | 0.85 | 約28% | 約173 | 前世代方式を組織が吸収し、fan/reheat/大型枝を拡張 |
| **E8** | 1945–46 | 9–10 | 940℃級 | 0.86 | 約31% | 約194 | 冷却込み高端実用、薄翼高速機へ十分な能力 |
| **E9** | 1945–47 technical front | 11–12 | 約1000℃ | 0.86–0.87 | — | — | component/rig current。全方式の長寿命量産は別資格 |

E8の冷却込みinstalled-core座標は比仕事約181–183 kJ/kg、熱効率約30.4–30.5%を高端実用の目安とする。E9は技術前線であり、全型式が同時に量産可能という意味ではない。

## 3. E4–E6：据付監査済みの基準点

### 3.1 E4

- simple core：**6.7 kg/s**。
- 中央能力：約**507 kW**、航空軸商品の旧見出しは約630 hp、浅井直接調整のusableは概ね680–700 hp級まで候補。
- dry core：約0.80–0.90 t、simple shaft SFC座標約0.557 kg/kWh。
- 回生型6.7 kg/s：shaft約467.7 kW、熱効率19.34%、SFC約0.433 kg/kWh。回生器＋headerは0.6–1.1 t級で、重量・容積を払う。
- **純ジェット化は物理的にE5まで禁止しない。** 現在のE6 installed方法を後方外挿したpre-audit shadowでは、標準6.7 kg/sで約300 kgf級、高流量枝7.2 kg/sで約330 kgf級が見える。これは**専用E4 jet product audit前の能力影**であり、商品定格ではない。

### 3.2 E5 小型コア

- standard small core：**7.6 kg/s、PR6、軸流5段＋遠心1段、約17.5 krpm**。
- Ni高温型中央能力：約**1,063 hp**。
- 非Ni 800℃中央能力：約**1,014 hp**。
- 非Ni量産760–770℃中央能力：約**952 hp**。
- headline 1,000 hp級は成立。ただし完全installed TP（power turbine/reducer/accessories）の質量・径・プロペラ吸収を別に払う。
- high-flow 8.08 kg/sで旧1,130 hp級の派生が成立する。旧marine 1,300 hp at standard flowは不整合で、約9.29 kg/s級を要する。
- E5 pure jet high-flow 8.4 kg/sは、v46式を後方適用したpre-audit shadowで**非Ni量産765℃約430 kgf、800℃高端約455 kgf、浅井直接調整約445–470 kgf**。旧300 kgf固定錨は保守的すぎる可能性が高く、専用installed auditで閉じる。
- **E5 fanは「rig止まり」を正準としない。** free-power-turbine/turboprop地力が既にあるため、後置fanの地上・飛行試験、限定実用の可否をv48 OPENとして再監査する。

### 3.3 E6 小型／中型

**小型コア**：7.8 kg/s、PR7、軸流7段＋遠心1段、約18 krpm。

- 非Ni shaft product：**1,300 hp standard**。
- Ni高温型：**1,500 hp standard**。

**中型コア**：14段all-axial、PR7、**13.2 kg/s中央（12.5–14.0 trim）**、約13.5 krpm。旧10 kg/s exact full-PR7 coreはsuperseded。

- 非Ni shaft：**2,100 hp qualified flat-rated**。installed capability中央約2,253 hp。
- long-life/transport derate：約1,870 hp。
- marine short：約2,300 hp候補、通常continuousは2,000–2,100 hp級。installation gateは残る。

**純ジェット**：

- nonNi long-life 835℃：約814 kgf、static TSFC約0.785。
- nonNi 870℃：計算約854 kgf → product **約850 kgf**。
- Ni 920℃：計算約907 kgf → product **約900 kgf**。

**後置fan**：single-spool gas generator + separate one-stage free-LP turbine + direct-drive aft fan。

- BPR約1.0、FPR約1.30。
- 中央static：約**984 kgf**、product **950–1,000 kgf**。
- 同835℃pure jet比：static thrust **+20.9%**、TSFC **−17.3%**。
- complete dry：約610–690 kg/基（中央650）、nacelle OD約0.66–0.72 m。

## 4. E7–E9 能力包絡

ここからは「一機種の定格」より、規模帯と後端方式が作る設計空間を正本化する。**航空機への搭載値ではない。**

### 4.1 E7

中型戦闘機向け代表：

- pure jet 組織設計値：約**970 kgf**。浅井直接調整：約980–1,000。
- 継承後置fan 組織設計値：約1,100–1,150。
- 浅井新方式・前置低バイパスfan dry：約1,150–1,200。
- pure-jet再燃焼：wet約1,180–1,220。
- fan＋再燃焼の集中枝：wet約1,350–1,450。

大型コア中央（約24 kg/s）：

- shaft capability 組織約4,650 hp、浅井約4,780。
- practical prop absorption：組織約3,600–4,100 hp、浅井約4,400–4,750。
- pure jet約1,550 kgf、low-BPR約1,900–2,000、浅井fan dry約2,000–2,250、wet約2,300–2,600。

大型上端約36 kg/sは、shaft capability約6,980 hp、pure jet約2,320 kgf、fan約2,850–3,390 kgf、wet約3,400–3,900 kgf級の**特殊大型枝**。標準戦闘機の値ではない。

### 4.2 E8

中型戦闘機向け：

- small shaft：約1,890 hp組織／約1,935浅井。
- medium shaft capability：約3,400 hp組織／約3,480–3,500浅井。
- pure jet：約1,100組織／約1,110–1,150浅井。
- front low-BPR 組織dry：約1,250–1,400。
- pure-J + reheat 組織wet：約1,350–1,450。
- 浅井true/near-true two-spool low-BPR fighter：約1,400–1,550 dry。
- medium-BPR 2–3 transport/patrol：約1,600–1,850 dry。
- integrated low-BPR + reheat interceptor：約1,700–1,850 wet。

大型コア中央（約28 kg/s）：shaft capability約6,150 hp組織／6,300浅井、practical prop約5,200–5,700／6,000–6,300、pure jet約1,920 kgf、low-BPR約2,400–2,600、medium-BPR約3,000–3,300、wet約3,500–3,750。

大型上端40 kg/sでは、shaft capability約8,780 hp、pure jet約2,740、low-BPR約3,500–3,700、medium-BPR約4,300–4,650、wet約4,300–5,300 kgf級。したがって**4 t級wet thrustをE9専売にしない**。

### 4.3 E9

E9は「さらに大推力」だけでなく、同程度の推力を**小型・軽量・低SFC・高高度・大surge margin**で得る方向へ価値が移る。

規模帯のshaft capability目安：

- 小型上限8 kg/s：約1,940 hp組織／1,980–2,000浅井。
- 中型上限15 kg/s：約3,630／3,720 hp。
- 大型25 kg/s：約6,050／6,200 hp。
- 大型30 kg/s浅井集中：約7,260–7,440 hp capability。

中型推進：pure jet約1,100 kgf組織／1,120–1,160浅井、low-BPR dry約1,450–1,600／1,550–1,700、medium-BPR dry約1,700–1,900／1,850–2,050、fan+reheat wet約1,900–2,200／2,200–2,400。

大型25 kg/s：pure jet約1,800–1,900、low-BPR dry約2,400–2,600、medium-BPR dry約2,800–3,100、fan+reheat wet約3,300–3,700。浅井側はそれぞれ約1,900、2,600–2,800、3,000–3,300、3,600–4,000 kgf級。

大型30 kg/s集中上端では、fan約3.5–4.0 t dry、4.2–4.6 t wet級が候補。

## 5. 組織設計値／浅井直接調整値／浅井新方式値

- **組織設計値**：浅井がそれ以前に発明・制度化した方法を組織が継承し、当代に新発明なしで仕上げる値。
- **浅井直接調整値**：同じコア・同じ方式で本人がmatching、loss、inlet、combustor、control、gear、nozzle、packagingを詰める。成熟世代では通常数%～十数%であり、魔法の倍増ではない。
- **浅井新方式値**：その年代に製造・試験・整備できる新architectureを導入する値。
- **浅井集中上端値**：規模・寿命・コスト・用途を一方向へ集中した特殊枝。通常量産商品ではない。

一度浅井が発明し、生産・教育・試験標準まで制度化した方式は**次世代の組織設計値へ相続**する。これが後期に本人のsame-form差が縮み、architecture差が大きくなる理由。

## 6. v48で閉じるもの／まだ閉じないもの

**CLOSED / upstream**

- E1–E9の技術前線。
- 小型／中型／大型コア規模帯の分離。
- shaft / pure jet / fan / augmentationを別後端として扱うこと。
- 組織設計値と浅井介入の継承規則。
- E4–E6の主要installed engine authority（v39–v46）。
- E7–E9の能力包絡と「大型化は別コア」規則。

**OPEN / local product**

- E4 pure jetの専用installed product audit。
- E5 pure jetの専用installed product audit（現pre-audit約430–470 kgf）。
- **E5後置fanのinstalled auditと飛行可能時期**。
- 各E7–E9製品の乾燥重量・径・TSFC・高度map・TBO。
- ターボプロップの最新installed mass/prop absorption/altitude/part-load再監査。
- 個別航空機のH→A、速度、航続、離着陸、採用史。

## 7. 正本接続

- 構造規則：`asai-works-core-hierarchy.md`
- 更新経緯：`asai-works-core-rebaseline-history-v38-v48.md`
- E4/E5 installed：`asai-works-e4-e5-installed-cycle-rebaseline-1931-37.md`
- E4/E5 product sizing：`asai-works-e4-e5-product-massflow-size-rebaseline-1931-37.md`
- E4 regeneration：`asai-works-e4-regeneration-installed-rebaseline-1931-33.md`
- E5/E6 compressor：`asai-works-e5-e6-compressor-operability-rebaseline-1934-41.md`
- E6 shaft：`asai-works-e6-installed-cycle-product-power-rebaseline-1938-41.md`
- E6 J/JF：`asai-works-e6-m-jf-installed-thrust-rebaseline-1938-43.md`
- E8/E9 earlier rebaseline：`asai-works-e8-e9-later-war-propulsion-rebaseline-1942-47.md`（v48能力包絡が上位）
- 航空への伝播：`asai-works-aviation-reconstruction-framework-v48.md`
