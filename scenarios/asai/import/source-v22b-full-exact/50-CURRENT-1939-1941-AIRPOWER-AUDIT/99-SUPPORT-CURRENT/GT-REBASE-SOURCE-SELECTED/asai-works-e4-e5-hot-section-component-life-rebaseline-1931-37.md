# E4/E5 hot-section component / life 再基線化 1931–37 — v39

> **v39 authority.** 本稿はE4/E5のhot-section寿命を、TIT一語ではなく blade / vane / disk-root / liner / bearing-seal / cooling-process に分解して再基線化する。E4/E5のPR・TIT・部品効率・gross比仕事は本稿では変更しない。installed cooling debit、製品出力、航空・舶用性能、採用・戦史への伝播は後続監査へ送る。

## 1. 中央裁定

- E4：PR4.5 / TIT710℃は維持。圧縮機出口は一次近似で約204℃。単純な中空空冷を払えばrotor blade metalは概ね **543–613℃ local/hot-spot envelope**に置ける。1931年に成熟Ni基超合金を要求する座標ではない。
- E5：PR6 / TIT800℃は維持。圧縮機出口は約247℃。rotor local/hot-spotは概ね **587–668℃**。ここでNi-rich / precipitation-strengthened高端線の価値が大きくなる。
- engine lifeはTITから一発で決めず、関連series componentの最小帯で `L_core` を閉じる。replaceable liner等は `L_core` より短い交換間隔を許す。

## 2. 二つのclock

1921–24のlong-duration clockを後年の全合金へそのまま相続させない。

1. **generic clock**：定荷重炉、温度/応力/時間記録、酸化/thermal-cycle観察、破面/NDT、統計整理、station capacity。1921–24から蓄積し、後続材料へ強く継承する。
2. **family/process clock**：実際の合金family、heat treatment、鍛造/鋳造/溶接・ろう付け、中空通路、section size。新family/process導入時に部分resetする。

v39監査帯：

| 系統 | rating時点のspecific clockの読み | 意味 |
|---|---:|---|
| E4耐熱austenitic / Cr-rich鋼family | 約4–8年以上 | 特殊鋼＋1923–25過給機serviceを含む。材料allowableは統計化できる |
| E4 fabricated hollow route | 約2–5年 | weld/braze/passage geometryは若く、lower-tail failureを残す |
| E5非Ni quantity line | 約5–10年以上の継承 | E4 routeの連続性がyieldとderating予測を強くする |
| E5 Ni high-end | exact alloy/heat/processは約2–5年として扱う | 1921から同一合金を試したことにはしない。成熟test systemだけを相続 |

この区別により、浅井のチートは「未来合金を15年熟成済みにする」のではなく、**新材料を外れlot・加工・温度・応力に分解して短期間で正しく評価できる組織を先に作る**こととして回収する。

## 3. cooling / metal-temperature audit

一次監査では cooling effectiveness `epsilon_c=(T_gas-T_metal)/(T_gas-T_coolant)` を用いる。これは現代CFDを導入したという意味ではなく、浅井が有用な無次元整理を知り、local burner/rigで係数を同定する監査座標である。

| 部品 | E4 nominal metal | E4 local/hot spot | E5 nominal metal | E5 local/hot spot |
|---|---:|---:|---:|---:|
| rotor blade | 約523–573℃ | **約543–613℃** | 約562–623℃ | **約587–668℃** |
| first vane/nozzle | 約497–558℃ | **約527–608℃** | 約535–601℃ | **約565–651℃** |

したがって `TIT = blade metal temperature` として寿命を判定してはならない。

## 4. rotor blade / root / process

E4中央routeを成熟した中空investment castingへ依存させない。**simple fabricated hollow airfoil（sheet/shell成形＋controlled seam weld/braze）＋replaceable root**を量産中央候補とし、proof-flow、wall thickness、mass/balance、NDTを全数ledger化する。investment castingはR&D/limited routeとして並走可。

現時点でturbine diameter/rpmを一点固定しないため、監査用のlocal design stress bandはE4約120–230 MPa、E5約140–280 MPaとする。これはallowableではなく、short-time tensileだけでなくstress-rupture clockが必要になる応力帯を示すsensitivity envelopeである。

成熟blade-system帯：

- E4：**350–600 h**（established lower 250–350 h）。
- E5 Ni high-end @800℃：**500–900 h**（established lower 350–500 h）。
- E5 non-Ni @800℃ full rating：**150–300 h**級が中央。量産workhorseには自然でない。
- E5 non-Ni @760–770℃ quantity rating：**350–650 h**級のblade lifeを見込む。普遍的な「15℃低下=寿命2倍」則では決めず、材料/応力/冷却ごとのledgerで閉じる。

## 5. vane / disk-root / liner / bearing-seal

| subsystem | E4 mature engineering band | E5 mature engineering band |
|---|---:|---:|
| vane/nozzle | 400–800 h | 500–900 h |
| disk/root（rim target達成時） | 600–1200 h | 800–1500 h |
| liner scheduled inspection/replacement | 150–300 h | 200–400 h |
| liner well-developed potential | 250–450 h | 300–600 h |
| bearing/seal stationary | 400–800 h | 500–900 h |
| bearing/seal aviation | 250–500 h | 350–700 h |

DiskはTITではなくrim/attachment temperatureとthermal gradientでgateする。design targetはE4 rim bulk約300–380℃、attachment hot region約380–470℃、E5は約330–410℃ / 410–500℃。これを外す場合、disk/rootは即cliff gateへ戻す。

Combustor linerは平均TITよりlocal flame attachment / dilution pattern / thermal gradient / punched-louver defectが支配する。can/linerをreplaceable moduleとし、交換間隔をengine deathと同義にしない。

Bearing/seal/oilは別熱系。directed oil jet、scavenge、heat shield、shutdown soak-back、cleanliness/filter、balance/critical-speed ledgerを要求する。

## 6. v39 representative `L_core`

| E coordinate / material-rating | representative rated `L_core` | 読み |
|---|---:|---|
| **E4 normal/full rating** | **250–450 h** | 旧「百数十〜数百h」を狭める。初期/new-processはこれ未満可 |
| **E5 Ni high-end @800℃** | **400–700 h** | headline high-end line |
| **E5 non-Ni @800℃ full** | **150–300 h** | sprint/experimental/high-value short duty寄り |
| **E5 non-Ni @760–770℃ quantity rating** | **350–600 h** | supply/yield/lifeを買う量の線 |

`gt-shogouki`の定置・間欠/減格 `TBO_prod=数百〜千h級` は保持する。これはliner交換・hot-section inspection・低full-power dutyを許す製品間隔であり、E4 full-rating `L_core=1000 h`を意味しない。

## 7. 旧temperature-life shortcutの扱い

`core-elements`の「翼金属温度約−15℃で寿命約2倍」は**方向を見るrough sensitivity anchor**へ降格する。Larson-Miller型の温度感度は強いが、倍率はalloy、stress、metal temperature、environment、processで変わる。さらに `ΔTIT != ΔTmetal` である。以後の寿命ratingはmaterial/component ledgerで閉じる。

## 8. 次のgate

本稿から性能へ直接ボーナスを出さない。次に閉じるのは **E4/E5 cooling bleed / pressure-loss installed-cycle debit**。

- coolant pickoff station / mass fraction
- combustor main-flow reduction
- turbine work and cooling-air mixing
- cooling passage pressure margin
- vane/blade cooling split
- seal/cavity flow
- installed shaft work / efficiency

を閉じてから500 kW、126 kJ/kg、turbojet/turboprop出力へ伝播する。

## 9. 履歴境界

本稿はtechnical capability/lifeの監査であり、航空機・艦船の性能、調達、採用、OOB、1941-12-08以後の実戦史を変更しない。下流の判断影響はinstalled-cycle監査後に別H→Aで行う。
