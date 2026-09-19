# 計算機異聞 — Branch B バージョン系譜整理（2026-08-30）

## 結論

運用上の正本は **v048 base + continuation overlay を統合した 1944-06-15T24 FULL RESUME** とする。

ただし、元の `FULL_RESUME_THRU_1944-06-15T24` は manifest に `99_LEGACY_UNTOUCHED` を保存すると記載している一方、実ZIPには当該188ファイルが入っていなかった。本 canonical package では v048 Bengal base からその188ファイルを復元した。

これは **v049への昇格ではない**。基底の意味版は v048 のまま、継続フロンティアを `1944-06-15T24` として別軸管理する。

## 実際の系譜

1. `v046 2026-08-29 LAND_HARDWARE_RETRO_RESERVATION`  
   land-combat hardware retro reservation を導入した基底。
2. `v047 2026-08-29 LAND_VEHICLE_GALVANIC_GROUND_REAUDIT`  
   v046の非legacy coreを全て継承し、24ファイルを追加。GALVANIC/vehicle層を更新。
3. `v048 2026-08-29 BENGAL_LAND_VEHICLE_ROLLBACK`  
   v047から21ファイルを追加し、同名2ファイルの参照を `JAPANESE_LAND_COMBAT_INTEGRATED_SYNTHESIS ... v001` から `v002` に更新。これは意図したsupersessionで、v047側を復活させない。
4. `v048 2026-08-30 CONTINUATION_FULL_WORKING`  
   v048 Bengalの非legacy core 746ファイルをハッシュ一致で保持し、`96_SESSION_WORKING_2026-08-30` 52ファイルを追加。`99_LEGACY_UNTOUCHED` はこの中間パッケージでは省略された。
5. `v048 2026-08-30 FULL_RESUME_THRU_1944-06-15T24`  
   CONTINUATIONの798ファイルを **100%同一ハッシュ** で包含し、`97_CONTINUATION_MASTER_2026-08-30` 232ファイルを追加。28 overlayをロードして global frontier を `1944-06-15T24` に進める。
6. **本 canonical reconciliation package**  
   上記FULL RESUMEの1030ファイルを変更せず収録し、v048 Bengalからlegacy 188ファイルを復元。さらに系譜・canonical manifest・checksumを追加する。legacyのファイル内容は変更せず、ZIP経路のCP437誤読による文字化けだけをUTF-8日本語名に正規化した。

## ロード規則

- 現行 authority baseline は v048 Bengal の `00_CONFIG / 00_README / 01_CORE / 02_TECH / 03_PREWAR / 04_WARSTART / 05_WARTIME / 06_RUNTIME / 90_REFERENCE / 95_AUDIT / 98_TOOLS`。
- `96_SESSION_WORKING_2026-08-30` は未promoteの作業履歴・監査・gateとして保存する。現行状態へ無差別に上書きしない。
- 実際の継続は `97_CONTINUATION_MASTER_2026-08-30/MANIFEST/MASTER_LOAD_ORDER_v001.json` の順序を厳守する。後段のcorrection/re-audit overlayが矛盾する前段working propositionをsupersedeする。
- `99_LEGACY_UNTOUCHED` は provenance/archive 専用であり、現行状態へロードしない。

## 旧ZIPの扱い

- v046: **ARCHIVE / superseded**
- v047: **ARCHIVE / superseded**
- v048 Bengal: **BASE AUTHORITY SNAPSHOT / 保管必須**
- v048 CONTINUATION: **INTERIM SESSION PACKAGE / superseded by FULL RESUME**
- v048 FULL RESUME: **直前の運用正本 / 本canonical packageのデータ本体**
- 本canonical package: **以後の再開点**

今後は「最新版 = v番号最大」ではなく、`semantic base revision` と `simulation frontier` を分けて扱う。authorityの意味変更がない限り v048 を維持し、再開点は `R19440615T24` のようなfrontier tagで識別する。authority自体を次に昇格させた時だけ v049 を使う。

## 入力ZIP SHA-256

- v046: `a3a6c10f4417e8098c112a39f42f2b7eca9a2b7bed9b7f79e40ac7babdeb5d9d`
- v047: `6807e92081040ecbb42b433c664e38542bbb3eeebafbc0b94fe53ce700e455cf`
- v048 Bengal: `fcce8a708a2efd56fb8e5e71de7382c1fc3a8f6b1286287faef2b43d5cacc448`
- v048 Continuation: `ff3dd4452ee5cd4160ca4c3389ab3fc67116d6fcb78b27deeb348f12d12a284f`
- v048 Full Resume: `0278f2cab9f1b46411b44a51e20a5fba52b07dc4f61f85de2110ee718c7e6456`

## 監査上の要点

- 5本すべてZIP CRC正常、重複entryなし。
- JSON parse error: 0。
- v046/v047/v048 Bengalの`99_LEGACY_UNTOUCHED`は、経路文字列の文字化け差を無視して内容ハッシュmultisetが188/188一致: `true`。
- FULL RESUMEの`PACKAGE_COUNTS_AND_ID_AUDIT_v001.json`: JSON 693、parse error 0、duplicate ID 0、source overlay 28。
