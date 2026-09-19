# 計算機異聞 refactor v007 — 1942年後半実装・年末restart版

v006の1942-06-16 MI直後restartから、限定FS、Santo、New Caledonia、英米物流/戦闘艦、欧州枢軸波及、中国五号準備を再監査し、1942-12-31T24まで現行枝を正式に進めた。

## 現在の正規入口

1. `00_README/NEXT_SESSION_HANDOFF_REFACTOR_v007.md`
2. `05_WARTIME/CHECKPOINT_INDEX_v006.json`
3. `05_WARTIME/CHECKPOINT_1942-12-31T24_v001.json`
4. `06_RUNTIME/1942H2_STRATEGIC_SETTLEMENT_v001.md`
5. `06_RUNTIME/SANTO_1942-08_TECH_STACK_REAUDIT_v001.md`
6. `06_RUNTIME/NEW_CALEDONIA_1942-10_SETTLEMENT_v001.md`
7. `06_RUNTIME/ALLIED_LOGISTICS_FLEET_AXIS_EFFECTS_1942H2_v001.md`
8. `06_RUNTIME/CHINA_FIVEGO_POLITICAL_IMPLEMENTATION_1942Q4_v001.md`

## v007で正本化したこと

- 7--8月は基地建設、索敵/妨害、空母修理/訓練を優先。正規空母を「余剰」として印度洋へ回さない。
- Santo攻略を技術スタック付きで再監査。旧暫定損害値を置換。
- New Caledonia守備をAmerical非転用等から46--52千総人員級へ上方修正し、10月の二個師団級攻略を確定。
- WaspはNew Caledonia戦で中破生存。Washington夜戦でHaruna中--大破。米水上艦隊のレーダー夜戦優位を維持。
- 11月20までに限定FSを終了。Fiji/Samoaは期限未定延期。
- New CaledoniaはVichy名義主権/民政＋日本軍事管理。ニッケル/クロム等を契約購入し、復路有価貨物として船腹効率へ反映。
- PM喪失の豪州物流効果を「輸送減」ではなく豪州北岸へ後退/積替え/沿岸船/鉄道負担増として修正。
- 印度洋の枝固有直接追加撃沈は2--4万GRT級。主効果は護衛、船日、空母ローテーション拘束。
- 米国は補給可能だが1942年末は空母/揚陸艦不足で敵前上陸への変換が弱い。Guadalcanal非発生により水上戦闘艦は史実より強い。
- Royal NavyはIndomitable/Formidable喪失で予備弾力性が低下。Victorious米貸与はFormidable不在を理由に2--3か月遅延方向を中心線。
- 欧州枢軸への効果はEl Alamein/TORCH/Stalingrad逆転ではなく、RN予備・護衛・Tirpitz抑止・U-boat環境への間接配当。
- 五号は年末に春1943実施方針を正式承認。北10＋宜昌6個師団級を維持し、四川盆地突入は漢中後再審査。

## 重要な変更理由

1. Santo旧値: 守備数と兵の質を混同していたため再監査。
2. New Caledonia旧25--35千: AmericalのGuadalcanal転用を暗黙継承していたため破棄。
3. South Pacific追加船腹旧90--140船月: 史実Guadalcanal補給が消える相殺を過小評価していたため破棄。
4. 米水上艦隊: Guadalcanal非発生で史実損失/損傷を継承できないため上方修正。
5. Victorious: 史実貸与後のFormidable backfillがこの枝では存在しないため貸与時計を再評価。
6. New Caledonia船腹: 復路を空荷扱いしていたためニッケル/クロム購入を追加。ただし南行き維持需要は減らさない。

## 未固定

- 1942年末日本商船総GRTの単一値。v006で隔離した630--638万GRT級は引き続き非canonical。
- 1943年Victoriousの最終出航日、NC鉱業の月次実績、U-boat追加撃沈GRT等は今後のイベントで確定。

## 包装

v006 ZIP内部の日本語パスがCP437誤解釈された状態だったため、本v007では意図されたUTF-8日本語名へ正規化した。`99_LEGACY_UNTOUCHED` のファイル内容は全件SHA-256でv006と同一確認する。
