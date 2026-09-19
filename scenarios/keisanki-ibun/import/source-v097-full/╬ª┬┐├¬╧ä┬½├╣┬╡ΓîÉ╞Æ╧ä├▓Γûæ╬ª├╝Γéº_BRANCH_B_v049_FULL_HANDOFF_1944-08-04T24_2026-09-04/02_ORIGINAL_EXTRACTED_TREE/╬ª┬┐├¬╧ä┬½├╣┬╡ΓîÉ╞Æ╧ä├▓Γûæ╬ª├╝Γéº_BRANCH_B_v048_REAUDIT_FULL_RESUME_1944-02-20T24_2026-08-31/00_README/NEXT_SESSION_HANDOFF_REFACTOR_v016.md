# 次回引継ぎ — refactor v016

## CURRENT

- 時点: `1944-04-25T00:00`（v015から時計は進めていない）
- CATCHPOLE / Eniwetok closeout済み
- 一号相当は未発起・未規模確定

## 最初に読む

1. `06_RUNTIME/CURRENT_BRANCH_STATE_v001.json`
2. `06_RUNTIME/PRE_ICHIGO_LAND_AIRFIELD_OOB_SHIPPING_NANJING_AUDIT_1944-04-25_v001.md`
3. `06_RUNTIME/SESSION_2026-08-24_ROLLBACK_PACIFIC_CHINA_SETTLEMENT_v001.md`
4. `06_RUNTIME/CHINA_FIVEGO_POLITICAL_IMPLEMENTATION_1942Q4_v001.md`
5. `06_RUNTIME/1942H2_STRATEGIC_SETTLEMENT_v001.md`

## 先に閉じるデータ

- Burma OOB: 第2師団を史実OOBから除外し、U-Go NO-GOによる15/31/33師団のfreshnessと両立させる。
- China/Burma land and airfield ledger: 実効支配node、飛行場serviceability、補給接続を固定。
- China Expeditionary Army: fixed vs mobile divisions/brigades and support arms.
- shipping: 1944 sea-lift burdenを更新し、China inland rail/road/river bottleneckと分離。
- Nanjing: 総人数よりJapanese rear/security workload releaseを測る。

これらを閉じた後に一号相当の目的・師団数・発起日を決める。旧7–9個師団、旧~14個師団はいずれも自動継承しない。
