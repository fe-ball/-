# V17 branch guard and clocks

## Current clocks

- China / main replay: **1940-07-31 24:00**.
- Nomonhan: 1939-08-31 24:00 CLOSED.
- V17 technical/naval discussion does not advance the combat clock.

## Precedence

1. V17 files in `85-CURRENT-2026-09-12-NAVAL-CRP-CONSOLIDATION-V17/` override older files only where explicit.
2. V16 remains the highest replay/China-state authority.
3. V14 remains the general naval/marine architecture authority where V17 is silent.
4. V10/V9/V8 technical files remain active where not explicitly superseded.
5. Quarantined/source/working branches never override current files automatically.

## Explicit V17 supersessions/reopens

- Reopen V8 one-way assumption that E15K CRP difficulty necessarily biases N1K toward a normal propeller.
- Preserve V14 rejection of prewar carrier GT up-power and automatic extra combat-hull count.
- Preserve V14 Yamato steam plant decision.
- Preserve V10 Type91 aerial-torpedo service/qualification bands.
- Preserve historical headline Type93/95 body performance unless explicitly changed later.

## Counting guards

- `exists` != `accepted` != `service-released` != `assigned` != `ready` != `combat-present`.
- Workbands and engineering indices are not direct combat multipliers.
- Repair/logistics percentage bands are component-scoped unless explicitly stated end-to-end; do not stack correlated gains.
- Later historical refit configurations must not be copied into the 1940-07-31 OOB without ship-specific date verification.
