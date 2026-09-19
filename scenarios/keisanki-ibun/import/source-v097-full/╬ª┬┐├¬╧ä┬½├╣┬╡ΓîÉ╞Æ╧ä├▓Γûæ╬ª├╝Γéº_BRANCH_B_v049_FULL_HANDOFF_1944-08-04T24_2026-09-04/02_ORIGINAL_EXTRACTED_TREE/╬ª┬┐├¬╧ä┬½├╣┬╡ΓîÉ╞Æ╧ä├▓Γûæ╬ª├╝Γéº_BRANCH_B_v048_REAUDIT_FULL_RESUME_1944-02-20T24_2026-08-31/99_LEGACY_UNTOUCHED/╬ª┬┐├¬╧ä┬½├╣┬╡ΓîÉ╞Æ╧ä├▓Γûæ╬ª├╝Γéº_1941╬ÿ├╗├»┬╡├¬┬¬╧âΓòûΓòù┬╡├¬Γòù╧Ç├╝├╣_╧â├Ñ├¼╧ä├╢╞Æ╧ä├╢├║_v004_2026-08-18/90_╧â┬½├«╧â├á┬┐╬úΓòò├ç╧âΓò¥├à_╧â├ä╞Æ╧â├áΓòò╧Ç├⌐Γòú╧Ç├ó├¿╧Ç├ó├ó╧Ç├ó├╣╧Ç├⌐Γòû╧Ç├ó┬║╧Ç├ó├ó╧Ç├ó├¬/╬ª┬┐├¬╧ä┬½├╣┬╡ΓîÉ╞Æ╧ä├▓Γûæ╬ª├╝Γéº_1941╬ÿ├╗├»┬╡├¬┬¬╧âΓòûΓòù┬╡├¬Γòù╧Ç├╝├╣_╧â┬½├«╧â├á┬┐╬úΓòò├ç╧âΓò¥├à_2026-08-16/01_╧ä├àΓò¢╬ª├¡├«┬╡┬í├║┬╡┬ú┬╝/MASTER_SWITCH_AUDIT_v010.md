# 後続スイッチ総監査 v0.10

## 結論

後続正本の「途中からONになったもの」を、制度名ではなく因果上の扱いで正規化した。現行登録は **46項目**。

|群|意味|件数|開戦再走査での扱い|
|---|---|---:|---|
|`A_RETROACTIVE_METHOD`|後から発見した評価/状態追跡規約|11|開戦前集中/開戦初日から適用|
|`B_PHYSICAL_CLOCK`|戦前からの物理技術時計|5|物理存在は保持。運用量・配備量は状態から計算|
|`B_OPENING_CAPABILITY`|開戦時に既に部分存在する能力|4|物理存在は保持。運用量・配備量は状態から計算|
|`B_OPENING_DOCTRINE`|開戦時の任務配分教義|2|物理存在は保持。運用量・配備量は状態から計算|
|`C_RECALCULATE_TRIGGER`|実戦観測で成熟日を再決定する制度/政策|20|旧日付を使わず、観測・需要・能力・時間から遷移|
|`D_RECOMPUTE_OUTCOME`|旧枝の歴史出力|4|入力禁止。該当作戦で再計算|

## 開戦状態の重要訂正

- `A-NATURAL-RETURN` は制度ではなく状態遷移。1941年11月の集中段階から生残者・負傷者・転属・補充を追う。
- `IJA-AIR-BASE-MOBILITY` は開戦時から `OPERATIONAL_PARTIAL`。陸軍航空には既に航空地区部隊・飛行場大隊・修理補給・輸送・通信等がある。
- `IJN-AIR-GROUND-SEPARATION` は `LATENT`。陸軍の機能分離を海軍へコピーしない。
- `A-NO-TOPDOWN-OUTPUT-MULTIPLIER = ON`。旧 +15–25% / +20–35% を直接掛けない。
- 潜水艦・水上艦は名簿ではなく個艦Availabilityを経て任務へ入れる。
- 1942–44の「安全線」、旧MI/Guadalcanal枝に依存した建造・人事・配置の日付は解除済み。

## 45→46項目で追加した洗浄規約

`A-NO-TOPDOWN-OUTPUT-MULTIPLIER` を追加した。旧正本に残る「第一線実効作戦出力 +15–25%」「反復陸上基地戦 +20–35%」は、性能・整備・航法・人員を通した後の**診断帯**であり、作戦入力ではない。

## 全項目

|ID|class|開戦状態|監査群|扱い|
|---|---|---|---|---|
|`A-NATURAL-RETURN`|METHOD|ON|A_RETROACTIVE_METHOD|1941-11-15/12-07から常時適用|
|`IJA-AIR-BASE-MOBILITY`|SERVICE_CAPABILITY|OPERATIONAL_PARTIAL|B_OPENING_CAPABILITY|開戦時能力として存在、制約付き|
|`IJN-AIR-GROUND-SEPARATION`|SOFT_TRIGGER|LATENT|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`JOINT-BASE-STANDARDIZATION`|SOFT_TRIGGER|LATENT|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`A-SKILL-LEVELING`|SOFT_TRIGGER|LATENT|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`A-DELIBERATE-VETERAN-NUCLEUS-REALLOCATION`|SOFT_TRIGGER|LATENT|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`A-DEDICATED-FERRY`|SOFT_TRIGGER|LATENT|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`A-CARRIER-TACTICAL-RETRAINING`|SOFT_TRIGGER|LATENT|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`C-POST-BATTLE-CARRIER-BUILD`|POLICY|OPEN|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`C-EMERGENCY-CONVERSIONS`|POLICY|OPEN|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`C-UNRYU-DAMAGE-CONTROL-LESSONS`|SOFT_TRIGGER|LATENT|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`SF-WARTIME-DD`|POLICY|OPEN|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`SS-SENTAKA-LOT3`|SOFT_TRIGGER|LATENT|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`SS-GUADALCANAL-TRANSPORT-BIND`|POLICY|OPEN|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`ASW-LOCAL-COMMAND`|SOFT_TRIGGER|LATENT|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`ASW-NATIONAL-COMMAND`|SOFT_TRIGGER|LATENT|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`TECH-RADAR-FLEET-TRIAL`|HARD_CLOCK|PRECURSOR|B_PHYSICAL_CLOCK|物理研究・試験時計を保持|
|`TECH-THRUST-EXHAUST`|HARD_CLOCK|TEST|B_PHYSICAL_CLOCK|物理研究・試験時計を保持|
|`TECH-TOKAI`|HARD_CLOCK|PRELIMINARY_REQUIREMENT|B_PHYSICAL_CLOCK|物理研究・試験時計を保持|
|`ENEMY-MARK14-FIX`|SOFT_TRIGGER|HISTORICAL_BASELINE_PROCESS|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`A-PRECOMBAT-CONCENTRATION-STATE`|METHOD|METHOD_ON|A_RETROACTIVE_METHOD|1941-11-15/12-07から常時適用|
|`A-REPLACEMENT-QUALITY-TRACKING`|METHOD|ON|A_RETROACTIVE_METHOD|1941-11-15/12-07から常時適用|
|`IJA-AIR-GROUND-LIAISON`|SERVICE_CAPABILITY|PRESENT_LIMITED|B_OPENING_CAPABILITY|開戦時能力として存在、制約付き|
|`IJA-AIR-MISSION-PRIORITY`|OPERATIONAL_DOCTRINE|COUNTERAIR_FIRST|B_OPENING_DOCTRINE|開戦時教義/任務集合として保持|
|`LOG-WARTIME-STANDARD-SHIP-I`|HARD_CLOCK|DESIGN_FROZEN_PRODUCTION_TRANSITION|B_PHYSICAL_CLOCK|物理研究・試験時計を保持|
|`LOG-WARTIME-STANDARD-SHIP-II`|POLICY|OPEN|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`COMSEC-CENTRAL-STATISTICAL-AUDIT`|SERVICE_CAPABILITY|OPERATIONAL_PARTIAL|B_OPENING_CAPABILITY|開戦時能力として存在、制約付き|
|`COMSEC-1942-HIGH-GRADE-OUTCOME`|OUTCOME_GATE|OPEN|D_RECOMPUTE_OUTCOME|旧枝の結果を入力禁止|
|`ASW-ESCORT-STAFF`|SERVICE_CAPABILITY|PRESENT_LIMITED|B_OPENING_CAPABILITY|開戦時能力として存在、制約付き|
|`TECH-TYPE2-DEPTH-CHARGE`|HARD_CLOCK|PRE_ADOPTION|B_PHYSICAL_CLOCK|物理研究・試験時計を保持|
|`ASW-DEDICATED-ESCORT-PRIORITY`|POLICY|OPEN|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`SUB-GERMANY-LIAISON-VOYAGE-OUTCOME`|OUTCOME_GATE|OPEN|D_RECOMPUTE_OUTCOME|旧枝の結果を入力禁止|
|`RERUN-START-STATE`|METHOD|METHOD_ON|A_RETROACTIVE_METHOD|1941-11-15/12-07から常時適用|
|`A-SOFT-HUMAN-STATE-DIVERGENCE`|METHOD|ON|A_RETROACTIVE_METHOD|1941-11-15/12-07から常時適用|
|`A-POSTOPENING-FIELDING-QUANTITY`|METHOD|ON|A_RETROACTIVE_METHOD|1941-11-15/12-07から常時適用|
|`SUB-OPENING-MISSION-ALLOCATION`|OPERATIONAL_DOCTRINE|MULTI_MISSION|B_OPENING_DOCTRINE|開戦時教義/任務集合として保持|
|`SUB-INDIVIDUAL-AVAILABILITY`|METHOD|ON|A_RETROACTIVE_METHOD|1941-11-15/12-07から常時適用|
|`SURFACE-INDIVIDUAL-AVAILABILITY`|METHOD|ON|A_RETROACTIVE_METHOD|1941-11-15/12-07から常時適用|
|`SUB-COMMERCE-RAID-ALLOCATION`|POLICY|OPEN|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`MARITIME-REPAIR-CARRYFORWARD`|METHOD|ON|A_RETROACTIVE_METHOD|1941-11-15/12-07から常時適用|
|`RERUN-1942-44-SAFE-LINE`|OUTCOME_GATE|OPEN|D_RECOMPUTE_OUTCOME|旧枝の結果を入力禁止|
|`SF-1942-43-BUILD-POLICY`|POLICY|OPEN|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`SF-SURVIVING-OLD-HULL-CONVERSION`|POLICY|OPEN|C_RECALCULATE_TRIGGER|旧カレンダー日付を解除|
|`SF-MUTSU-ACCIDENT`|OUTCOME_GATE|HISTORICAL_SHOCK_WITH_SENSITIVITY|D_RECOMPUTE_OUTCOME|旧枝の結果を入力禁止|
|`FLEET-ROSTER-SNAPSHOT-PROVENANCE`|METHOD|ON|A_RETROACTIVE_METHOD|1941-11-15/12-07から常時適用|
|`A-NO-TOPDOWN-OUTPUT-MULTIPLIER`|METHOD|ON|A_RETROACTIVE_METHOD|1941-11-15/12-07から常時適用|

## 残るOPEN

- `IJN-AIR-GROUND-SEPARATION` — LATENT。base_transfer_delay, support_transport_mass, tool_parts_mismatch, unit_immobilization
- `JOINT-BASE-STANDARDIZATION` — LATENT。cross_unit_tool_mismatch, fuel_ammo_incompatibility, repair_handoff_delay, receiving_base_activation_time
- `A-SKILL-LEVELING` — LATENT。unit_skill_variance, formation_failure_by_unit, available_veteran_nuclei, replacement_low_skill_share
- `A-DELIBERATE-VETERAN-NUCLEUS-REALLOCATION` — LATENT。new_unit_failure_rate, leader_navigation_gap, veteran_surplus_in_transfer_pool, frontline_availability
- `A-DEDICATED-FERRY` — LATENT。combat_pilot_ferry_hours, ferry_accidents, delivery_delay, base_mobility_maturity
- `A-CARRIER-TACTICAL-RETRAINING` — LATENT。carrier_battle_lessons, surviving_staff, training_fuel, weeks_available_before_next_operation
- `C-POST-BATTLE-CARRIER-BUILD` — OPEN。after first major carrier-loss event
- `C-EMERGENCY-CONVERSIONS` — OPEN。carrier_shortage review
- `C-UNRYU-DAMAGE-CONTROL-LESSONS` — LATENT。carrier_fire_events, fuel_system_cascade_events, hangar_ordnance_events, test_program_results
- `SF-WARTIME-DD` — OPEN。destroyer/escort pressure review
- `SS-SENTAKA-LOT3` — LATENT。first_boat_launch, land_electrical_endurance, construction_defect_rate, submarine_demand
- `SS-GUADALCANAL-TRANSPORT-BIND` — OPEN。if isolated garrison supply crisis develops
- `ASW-LOCAL-COMMAND` — LATENT。submarine_contacts, shipping_losses, escort_reallocation_cost, route_density
- `ASW-NATIONAL-COMMAND` — LATENT。multi_theater_shipping_loss, command_conflict, escort_shortage, national_shipping_pressure
- `LOG-WARTIME-STANDARD-SHIP-II` — OPEN。after first-generation operating data and wartime shipping/repair pressure are observed
- `COMSEC-1942-HIGH-GRADE-OUTCOME` — OPEN。evaluate continuously by cipher system and operation; especially before MO/MI and shipping/submarine operations
- `ASW-DEDICATED-ESCORT-PRIORITY` — OPEN。review when submarine pressure and fleet-destroyer escort bind become observable
- `SUB-GERMANY-LIAISON-VOYAGE-OUTCOME` — OPEN。evaluate each voyage at its historical/alternate departure time
- `SUB-COMMERCE-RAID-ALLOCATION` — OPEN。commerce raiding is an available opening mission but its fraction of submarine effort is recalculated from observed fleet targets, shipping opportunities, intelligence and command 
- `RERUN-1942-44-SAFE-LINE` — OPEN。withdraw former assumption that 1942-43 rerun remains fixed and 1944-06-10 is a safe continuation point; recompute sequentially from opening
- `SF-1942-43-BUILD-POLICY` — OPEN。destroyer/carrier/cruiser build and conversion decisions formerly conditioned on no Guadalcanal-style losses are reopened and triggered by actual rerun losses, escort burden, air-g
- `SF-SURVIVING-OLD-HULL-CONVERSION` — OPEN。do not auto-apply historical or former-branch conversions to surviving old hulls; compare active, minor refit, mission conversion, reserve, training/test and retirement
