# V8 CHANGELOG — 1939AIRPOWER15 EXHAUST1

- Adds current canon `49-PISTON-EXHAUST-ENERGY-RECOVERY-CANON-V8.md` and machine ledger `49A-PISTON-EXHAUST-APPLICATION-LEDGER-V8.tsv`.
- Introduces EX0 collector / EX1 individual-nonintegrated / EX2 thrust-individual / EX3 integrated exhaust-energy-recovery states.
- Replaces binary “individual exhaust exists -> Asai delta zero” logic with residual-improvement accounting while retaining strict no-double-count rules.
- Supersedes the older B5N2 `historical individual exhaust -> E1=0` closure; B5N2 is now treated as historical collector-ring EX0 for current calculations unless stronger primary hardware evidence overturns it.
- Restores Ki-27 late-production thrust-exhaust adoption path; exact 1939-05-10 24th Sentai fit remains OPEN.
- Reattributes late-war J2M/N1K/Ki-84/A6M5 differences: historical EX2 already consumes the collector-to-stack large card; Asai retains EX2->EX3 residual plus engine/cooling/QC benefits.
- Separates D4Y/Ki-61 exhaust residual from liquid-cooling radiator/heat-recovery credit.
- Combat clock remains 1939-05-10 24:00; Nomonhan opening remains next chronological gate.
