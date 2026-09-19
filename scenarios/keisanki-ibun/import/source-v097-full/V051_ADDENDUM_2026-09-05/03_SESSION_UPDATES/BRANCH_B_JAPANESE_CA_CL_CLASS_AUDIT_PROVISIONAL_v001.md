# BRANCH B — 日本巡洋艦 CA/CL 艦級性能監査・暫定正本 overlay v001

- date: 2026-09-05
- authority: **canonical-provisional-overlay**
- canonical frontier: **1944-08-04T24:00**（時計は進めない）
- scope: 日本海軍の重巡・軽巡について、詳細監査が未了の艦級に既存正本の計算援用原則を粗く適用する。
- use: 個艦監査がない場合の既定値。個艦の改装日、損傷、修理、電探搭載、乗員、配置が常に優先。

## 0. 権限と非重複

このoverlayは、既存の詳細正本を置換しない。

- **最上型**：既存 `11_水上艦_最上型・変則艦・生残旧艦` の詳細監査が優先。
- **北上 / 大井**：既存正本の「北上のみ40門級実証、大井は通常軽巡」が優先。
- **高雄型**：本セッションで閉じた1938基準 split を、ここから現行の暫定正本とする。
- それ以外：本書の艦級profileを、個艦詳細監査が成立するまで使用する。

**絶対にしないこと**：速度・燃費・DC・I/Oの改善を一つの「戦闘力倍率」に潰すこと。既存の砲術技術、九三式魚雷改善、電探技術と二重加算すること。

## 1. 全艦級棚卸し

| 区分 | 艦級 | 対象 | 監査状態 | 暫定Branch差 |
|---|---|---|---|---|
| CA | Furutaka | Furutaka / Kako | PROVISIONAL_OVERLAY | refit_engineering: mature post-accident analysis; engineering/rework burden ~15–25% lower where yard bottleneck does not dominate; speed: do not increase headline rating; healthy practical sustained performance centered about historical 33 kt, with ~0.1–0.3 kt-equivalent retention benefit; cruise_fuel: ~3–5% better sensitivity |
| CA | Aoba | Aoba / Kinugasa | PROVISIONAL_OVERLAY | refit_engineering: mature case ~20–30% shorter engineering loop where docks/materials do not dominate; speed: headline near historical; ~0.1–0.3 kt-equivalent better practical retention; cruise_fuel: ~4–6% better sensitivity |
| CA | Myoko | Myoko / Nachi / Haguro / Ashigara | PROVISIONAL_OVERLAY | speed: healthy practical band ~33.4–33.7 kt equivalent; emphasis on repeatability, not a new top-speed rating; cruise_fuel: ~4–6% better sensitivity; post_refit_faults: ~15–25% lower unplanned correction/yard tail |
| CA | Takao | Takao / Atago / Maya / Chokai | CURRENT_PROVISIONAL_AUTHORITY | 高雄/愛宕=T-38A完全改装、摩耶/鳥海=T-38B限定。1942-11雷装は16/16/8/8射線。 |
| CA | Mogami | Mogami / Mikuma / Suzuya / Kumano | DETAILED_CANONICAL_INHERITED | 既存詳細監査を優先。本overlayでは変更しない。 |
| CA | Tone | Tone / Chikuma | PROVISIONAL_OVERLAY | speed: planned 35 kt realized more consistently; good-condition practical/trial sensitivity ~35.1–35.4 rather than a new official rating; cruise_fuel: ~4–7% better sensitivity; initial_fault_tail: ~15–25% lower |
| CA | Ibuki | Ibuki / planned sister as applicable to Branch construction policy | PROVISIONAL_FUTURE | engineering: use mature Mogami/Tone lessons; lower rework/fault tail; performance: no additional guns/armor/speed beyond separately authorized design changes |
| CL | Tenryu | Tenryu / Tatsuta | PROVISIONAL_OVERLAY | speed: no headline increase; only small practical retention (~0.1–0.2 kt-equivalent sensitivity); fuel_maintenance: ~2–4% better process sensitivity; dc_io: modest only |
| CL | Kuma-conventional | Kuma / Tama / Kiso / Oi | PROVISIONAL_OVERLAY_WITH_INHERITED_EXCEPTION | speed: healthy practical ~32.2–32.5 kt-equivalent band; cruise_fuel: ~3–5% better sensitivity; maintenance: modest fault-tail reduction |
| CL | Kitakami-special | Kitakami | DETAILED_CANONICAL_INHERITED | 既存「北上一隻のみ40門実証」を優先。 |
| CL | Nagara | Nagara / Isuzu / Natori / Yura / Kinu / Abukuma | PROVISIONAL_OVERLAY | speed: healthy practical ~32.2–32.5 kt-equivalent band; cruise_fuel: ~3–5% better sensitivity; fire_control_io: modest calibration/communications improvement |
| CL | Sendai | Sendai / Jintsu / Naka | PROVISIONAL_OVERLAY | speed: healthy practical ~32.2–32.5 kt-equivalent band; cruise_fuel: ~3–5% better sensitivity; destroyer_leader_io: moderate improvement in plotting, torpedo-salvo calibration, communications and second-salvo control |
| CL | Yubari | Yubari | PROVISIONAL_OVERLAY | speed: historical physical performance; no meaningful headline uplift; trim_maintenance: ~5–10% process/availability benefit sensitivity; dc_io: modest; tight volume limits remain |
| training_CL | Katori | Katori / Kashima / Kashii | WATCHLIST_ONLY | value: training, calibration, communications and staff-work platform rather than frontline combat uplift |
| CL | Agano | Agano / Noshiro / Yahagi / Sakawa | PROVISIONAL_OVERLAY | speed: good-condition practical/trial sensitivity ~35.2–35.5 kt without changing official design rating; cruise_fuel: ~5–8% better sensitivity; initial_fault_tail: ~15–25% lower |
| CL | Oyodo | Oyodo | PROVISIONAL_FUTURE | speed: historical ~35.3 kt trial neighborhood; Branch good-condition sensitivity ~35.4–35.6; cruise_fuel: ~4–7% better sensitivity; command_plotting_io: ~10–15% process improvement in plotting/report handoff/space-power integration |

## 2. 艦級別の暫定値

### 2.1 古鷹型
史実の1936–39大改装を物理的骨格として維持する。主砲・装甲・雷装を架空に増やさない。Branch差は、友鶴・第四艦隊事件後に成熟した重量/KG/縦強度計算、機関較正、配管・配電の再整理に置く。

- 改装設計・再作業負担：造船所そのものが律速でない部分で **約15–25%低下**。
- 速力：公称値を引き上げず、健全艦の実用速度保持で **0.1–0.3kt相当**の感度。
- 巡航燃費：**3–5%改善感度**。
- 機関/軸系の悪いtail：**10–20%低下感度**。
- DC/I-O：中程度。装甲倍率なし。

### 2.2 青葉型
古鷹型より遅い時期に成熟改装を受けるため、計算援用の適用度を一段高く置く。

- engineering loop：dock/material制約を除き **20–30%圧縮感度**。
- 実用速力保持：**0.1–0.3kt相当**。
- 巡航燃費：**4–6%改善感度**。
- 不意の再入渠・補正工事tail：**15–25%低下感度**。
- DC/I-O：中～高。ただし旧船体の容積・防御限界は残る。

### 2.3 妙高型
完成時の物理性能は計算機導入以前なので史実近傍。差は1939–41大改装の出来に出す。史実近傍の **20.3cm×10、61cm四連装×4＋次発8、改装後約33.3kt** を基礎とする。

- 健全艦の実用速度：**33.4–33.7kt相当の良好帯**。公式最高速の上書きではない。
- 巡航燃費：**4–6%改善感度**。
- 改装後の機関・軸系・配管不具合tail：**15–25%低下感度**。
- DC/I-O：中～高。
- 九三式魚雷の搭載・次発危険は残す。安全艦にはしない。

### 2.4 高雄型 — 1938基準を現行化
**高雄・愛宕 = T-38A 完全改装**、**摩耶・鳥海 = T-38B 限定改装**。

高雄・愛宕：
- 大型バルジ・機関大整備・四連装発射管化を維持。
- 1942-11中心：**61cm四連装×4**、次発8。
- 史実改装後約34.3ktを基礎。良好条件のBranch感度は **34.4–34.6kt程度**だが、主利得は反復性・燃費・不具合低下。
- 巡航燃費：**3–5%改善感度**。
- DC/I-O：中～高。
- 1942-11は八九式12.7cm連装4基を持つ側として扱う。

摩耶・鳥海：
- 同一時期に完全改装を魔法のように追加しない。yard capacity制約を残す。
- 1942-11中心：**61cm連装×4**。
- 大型バルジ/四連装化は未実施。
- DC/I-O・機関較正・配電準備は改善するが、高雄/愛宕ほど重量余裕は増えない。
- 1942-11の高角砲は旧12cm系を基本とし、後世の摩耶大防空改装を先取りしない。

**1942-11の4隻合計瞬間雷撃射線は 16+16+8+8 = 48。64ではない。**

1942年夏以降の21号系電探搭載は個艦日付で扱う。本Branchの差は、1938改装時からの電源・配線・plotting/I-O余裕によって後付け装備を使いやすいことであり、電探自体の探知性能を米SG相当にしない。

### 2.5 最上型
**既存詳細正本を変更しない。**
既存の教師群（最上・三隈）／成熟群（鈴谷・熊野）の差、損傷後機能保持、昼間砲戦の既存帯をそのまま使う。

また、史実の最上航空巡洋艦化はBranch MIの損傷因果が違うため**自動発生しない**。必要なら別gateで監査する。

### 2.6 利根型
第四艦隊事件後の知見を設計段階から多く取り込める新造艦なので、旧重巡の改装より「初期不具合tailの減少」を大きく見る。

- 物理骨格：20.3cm×8、61cm三連装×4、偵察水上機群、約35ktは史実近傍。
- 速度：35kt計画値を安定して実現。良好条件で **35.1–35.4kt相当**の感度。
- 巡航燃費：**4–7%改善感度**。
- 初期機関・艤装不具合tail：**15–25%低下感度**。
- 水偵の発進・回収・報告cycle：**5–10%改善感度**。索敵半径そのものは増やさない。
- DC/I-O：同時期日本重巡として高め。

### 2.7 伊吹型（建造中）
既存Branchの建造時計・「重巡として継続」の方針を優先。本overlayは完成時の粗い工学profileだけを置く。

- 最上/利根で得た建造・艤装残差還流を適用。
- 兵装・装甲・速度を勝手に増やさない。
- 史実の空母転換は自動ではない。

## 3. 軽巡

### 3.1 天龍型
旧式・容積余裕小。計算援用で別物にはならない。

- headline speed変更なし。
- 実用速力保持：**0.1–0.2kt相当**の小さい感度。
- 燃費/整備：**2–4%改善感度**。
- DC/I-O：小～中。
- 史実で検討されただけの大規模AA化を自動実施しない。

### 3.2 球磨型通常艦（球磨・多摩・木曾・大井）
安定性工事・油専焼化後の約32kt級を基礎。古い「36kt軽巡」として扱わない。

- 健全時実用：**32.2–32.5kt相当**。
- 巡航燃費：**3–5%改善感度**。
- 整備/DC/I-O：小～中。
- **大井は通常軽巡**。40門重雷装へ戻さない。

### 3.3 北上
既存正本どおり、**40門級重雷装の一隻実証艦**。
系列化なし。後の高速輸送化・回天化は戦況依存の別gate。

### 3.4 長良型
約32kt級の旧5500t軽巡として扱う。個艦改装差を消さない。

- 健全時実用：**32.2–32.5kt相当**。
- 巡航燃費：**3–5%改善感度**。
- 射撃/雷撃I-O、通信、DC：小～中。
- 阿武隈などの個艦雷装を全艦へコピーしない。
- 後世の五十鈴AA/護衛艦化は別gate。

### 3.5 川内型
長良型と同じく約32kt級。水雷戦隊旗艦としてI/O改善の価値をやや高めに置く。

- 健全時実用：**32.2–32.5kt相当**。
- 巡航燃費：**3–5%改善感度**。
- 雷撃扇面作図、次発射管理、通信・plottingの再現性：中程度改善。
- 川内・神通・那珂の個艦雷装差は維持。

### 3.6 夕張
実験的な小型高密度設計で、重量/容積marginが厳しい。

- 速度・兵装を増やさない。
- trim/整備/availabilityのprocess benefit：**5–10%感度**。
- DC/I-O：小～中。
- 1944型大改装は自動ではない。

### 3.7 香取型
戦闘用の高速軽巡とは別枠。

- 物理性能は史実近傍。
- Branch価値は教育、射撃/通信較正、司令部訓練、要員養成。
- frontline CL walletへ自動算入しない。

### 3.8 阿賀野型
計算援用が設計・建造・艤装へ最初からかなり入る新造軽巡。
既存正本の竣工時計を優先し、ここでは性能profileだけを置く。

- 兵装は既存weapon/hull ledgerを優先。**本overlayで砲種・門数を上書きしない**。
- 約35kt級を基礎。良好条件の実用/公試感度：**35.2–35.5kt**。
- 巡航燃費：**5–8%改善感度**。
- 初期不具合・再入渠tail：**15–25%低下感度**。
- DC/I-O、通信・plotting：日本軽巡として高め。

### 3.9 大淀
偵察・司令部機能を重視する新造艦。既存正本の1943年2月竣工時計を変更しない。

- 史実35.3kt級を基礎。良好条件で **35.4–35.6kt相当**の感度。
- 巡航燃費：**4–7%改善感度**。
- command/plotting/report I-O：**10–15%のprocess改善感度**。
- 水偵handling：**5–10%改善感度**。
- ただしE15K等、航空機そのものの不具合・性能限界は別。後世の連合艦隊旗艦化も別gate。

## 4. 1942-11 New Caledonia 第一夜への即時適用

現在の前衛 `Hiei / Kirishima + Atago / Takao / Maya / Chokai + Sendai + DD8` では、本overlayを即時使用する。

- Atago/Takao：完全改装側。各16射線。
- Maya/Chokai：限定改装側。各8射線。
- CruDiv 4の最大同時発射管：**48**。
- 高雄/愛宕のAAは摩耶/鳥海より一段良い。
- 4艦の電探は個艦搭載日を満たす場合に使用。ただし水上砲戦の主解は依然として光学＋既存射撃盤。SGレーダー優位を打ち消さない。
- Branch砲術改善は既存 `TECH-GUNFIRE-SURFACE-1942-001` を一度だけ適用する。高雄型profileをさらに命中率ボーナスとして加算しない。

## 5. 外部史実アンカー（粗いcross-check）

本overlayの物理骨格は既存正本を優先し、外部資料は数値の逸脱防止にだけ使用した。

- Furutaka modernization: Navypedia `jap_cr_furutaka.htm`
- Myoko modernization: Navypedia `jap_cr_nachi.htm`
- Takao modernization: Navypedia `jap_cr_takao.htm`
- Tone baseline: Navypedia `jap_cr_tone.htm`
- Kuma/Nagara/Sendai old-CL stability speed: Navypedia class pages
- Agano baseline: Navypedia `jap_cr_agano.htm`
- Oyodo: historical completion/trial baseline only; existing Branch completion clock wins

## 6. 後日精査の優先順

1. **高雄型**：T-38A/T-38Bを重量表・GM/KG・DC系統・電探I/Oまで個艦化。
2. **妙高型**：1939–41改装の個艦差と1942電探/AA搭載日。
3. **利根型**：水偵運用cycle、航空燃料・弾薬区画、損傷時偵察能力。
4. **古鷹/青葉型**：旧船体のDCと構造余裕。
5. **5500t軽巡群**：個艦ごとの雷装/AA/電探/機関状態。
6. **阿賀野/大淀**：竣工後公試実測をBranch設計残差へ還流。
