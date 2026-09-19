# コア再基底化の経緯——v38からv48まで、何が変わり何が壊れたか

> **v48 provenance authority.** 本稿は数値の正本ではなく、旧航空史をアーカイブするに至った理由と、発動機コアの正本がどの監査を経て変わったかを追うための履歴である。現行数値は `asai-works-engine-capability-core-e1-e9.md` を使う。

## 1. 問題の発端

旧航空史は、E世代を「年代ごとの代表エンジン」に近く扱い、特にjet側で保守的な経験則を長く引き継いでいた。このため、

- E5 jet ≈300 kgf
- E6 pure jet ≈500 kgf
- E6 aft-fan ≈650–700 kgf

といった値が航空機設計・採用史の上流錨になった。

v38以後、転生知識・計算・組織を**物理性能の無料ボーナスではなく、現地で製造可能な設計へ収斂する能力**として再定義し、同時に世代・規模・installed productを分離したことで、この旧錨が順次崩れた。

## 2. v38——能力収斂の方法を先に固定

- 100% benchmark = 未来工場ではなく、**その年の材料・工作・試験条件で作れる最良設計**。
- O/Gは性能倍率でなく、設計・開発・品質の改善余地をどれだけ回収できるかの監査座標。
- 史実年は比較錨であって能力上限ではない。
- 長期材料試験、試験データ、計算型、組織学習を別時計として払う。

この方法変更により、「歴史上1939だからjetはまだ弱い」のような逆算を禁止した。

## 3. v39——熱部寿命を意味別に分解

E4/E5の寿命を、core能力、part duty、qualification、product TBOの混同から分離。

- E4大型/長寿命用途：250–450 h級の座標。
- E5 Ni：400–700 h級。
- E5 nonNi 800℃全開：150–300 h級。
- E5 nonNi 760–770℃量産：350–600 h級。

これにより「温度が出る＝同じ寿命で商品化できる」の短絡を切った。

## 4. v40–v42——E4/E5をgross比仕事からinstalled productへ

v40でE4/E5を実サイクル・bleed・mechanical loss込みへ移した。

- E4 6.7 kg/s simple：約507 kW中央能力。
- E5 7.6 kg/s：Ni/非Niの材料・定格別に約950–1060 hp級。

v41でpower turbine、reducer、accessories、airflow、径、質量を商品側へ配り、旧「同じ比仕事なら自由に出力を増やせる」を禁止。

v42でE4回生を据付込みにし、「効率上昇には大きな質量・容積税がある」ことを固定。

## 5. v43——E5/E6圧縮機と規模帯

- E5 small：7.6 kg/s、PR6、5 axial + 1 centrifugal。
- E6 small：7.8 kg/s、PR7、7 axial + 1 centrifugal。
- E6 medium：14-stage all-axial、13.2 kg/s中央、12.5–14 trim。

旧E6 medium 10 kg/s exact coreはsuperseded。ここで**世代とmass flowを別軸にする必要性**が決定的になった。

## 6. v44——E6軸商品を閉じる

- E6 small nonNi：1,300 hp standard。
- E6 small Ni：1,500 hp standard。
- E6 medium：2,100 hp qualified flat-rated、installed capability中央約2,253 hp。

旧generic 1,500/1,700 hp smallという書き方を材料・定格別へ修正した。一方、medium shaftは旧2,100 hpがほぼ正しかった。

## 7. v46——E6 jet/fanの旧錨が崩壊

E6 mediumのinstalled pure-jet / aft-fanをサイクルから閉じると、

- nonNi pure jet：product約850 kgf。
- Ni pure jet：product約900 kgf。
- aft-fan：product約950–1,000 kgf、中央約984 kgf。
- same-TIT pure jet比でaft-fanはstatic thrust +20.9%、TSFC −17.3%。

となり、旧500 kgf / 650–700 kgfは大幅な過小評価と判明した。

この時点で旧航空機性能へ単純伝播すると、旧直線翼戦闘機がいきなりM0.8近辺へ入り、**航空史そのものの前提が壊れる**ことが見えた。v47で霹靂へ伝播を試みたが、これは「古い機体史を守ったまま新推力を入れる」過渡計算であり、v48では航空採用史とともにアーカイブする。

## 8. post-v46——E1–E9能力包絡を再整理

追加比較で分かったのは、後期ほど世代上昇そのものより、

- core scale
- fan / multi-spool
- reheat
- prop absorption / contra / split-power

の**architecture選択**が出力包絡を広げること。

したがってE7–E9は「代表推力一個」では表せない。小型・中型・大型コアと、軸・純jet・fan・再燃焼を組み合わせた能力包絡として扱う。E8大型上端ですでに4 t級wetが候補となり、E9の価値は単純な最大推力だけでなく小型化・SFC・高度・surge marginへ移る。

## 9. E4/E5 jetを再び開く理由

E6のinstalled監査を後方外挿すると、旧E5 300 kgf錨も保守的すぎる兆候が出た。

- E4 6.7 kg/s：pure jet約300 kgf級のpre-audit影。
- E5 high-flow 8.4 kg/s：430–455 kgf級、浅井直接調整なら445–470 kgf級のpre-audit影。

この値が閉じれば、E4で飛行実証、E5で高速軍用機が成立し得る。さらにE5はfree-power-turbine地力を持つため、**後置fanをrig-onlyとする旧順序も再監査対象**になった。

したがって航空史は旧「E5で飛べる、E6で兵器になる」という一列を守れない。

## 10. v48の裁定

- **発動機上流能力は閉じる**：E1–E9、規模帯、後端方式、組織/浅井差。
- **旧航空採用史は閉じない**：旧機体名・制式年・主力構成はアーカイブ。
- **E4/E5 jetとE5 fanはlocal installed auditを再開**。
- **ターボプロップは旧航空機値を再利用せず、最新shaft/product/prop吸収で再監査**。
- **ピストンも計算・統合・過給の更新済み能力で同一任務比較へ参加**。

新航空史は「jetを主役にする」のではなく、同じ年代の piston / turboprop / pure jet / fan を、同じ組織能力と任務要求で比較して初めて採用を決める。

## 11. 参照

- 現行コア：`asai-works-engine-capability-core-e1-e9.md`
- 構造模型：`asai-works-core-hierarchy.md`
- 方法：`asai-works-capability-convergence-framework-1903-45.md`
- v39–v46各installed親：E4/E5 life, installed, sizing, regen, compressor, E6 shaft, E6 J/JF各正本。
- 航空リセット：`asai-works-aviation-reconstruction-framework-v48.md`
- v47霹靂伝播：`archive/aviation-pre-v48/v47-working/`（provenance only）
