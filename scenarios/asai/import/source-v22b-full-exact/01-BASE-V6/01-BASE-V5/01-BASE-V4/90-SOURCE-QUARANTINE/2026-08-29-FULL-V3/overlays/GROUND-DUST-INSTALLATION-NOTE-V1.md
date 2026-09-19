# Ground dust / Manchuria installation closure — 2026-08-29

This is a topic-local delta, not a full handoff package.

## Locked design
- Dirty side: raised/down-facing intake head -> centrifugal/inertial precleaner with external dust cup.
- Final cleaner: oil bath plus oil-washed metal element.
- Clean side: fully sealed duct; never draw combustion air from the engine cooling compartment.
- Cleaner cell families: AC-150 and AC-315. D-A uses 1x AC-150; D-B uses 1x AC-315; D-C/D-D use 2x AC-315 in parallel.
- Clean restriction target: ~1.6-2.0 kPa (D-C ~1.2-1.6 due to deliberate oversizing); service limit 3.0 kPa.
- D-D ordinary 1937 comparison uses 220-235 hp continuous. 245-260 hp remains a higher Normal/test-duty branch.

## Installation
- D-A/B: cleaner at cowl/hood side, bowl removable downward/outward; intake above wheel dust plume.
- D-C/D-D: external precleaners above track dust plume; oil-bath cells inside protected service wells, with dirty/clean sides physically separated. D-D uses one bank per side.
- D-C/D-D cleaners are deliberately modular; one cell is not a full-load operating mode.
- Low point before the clean plenum gets a water trap/drain. A bolt-on riser preserves the same intake area for wading; allowable water depth remains vehicle-specific because vents/electrics/transmission breathers also govern it.

## Service doctrine
- Working precleaner credit for sizing: 75% of incoming dust mass, primarily coarse fraction.
- Oil-bath retained-dust capacity is conservatively derated from later 315-cfm test anchors: AC-150 0.45 kg; AC-315 1.0 kg per cell.
- At 0.5 g/m3 severe convoy dust, calculated oil-bath service intervals are roughly 17-25 h; doctrine rounds this down to daily/shift service.
- At 1.5 g/m3 extreme dust, calculated interval is roughly 6-8 h; empty precleaner cups every ~2 h and service the oil bath each shift.
- At 0.1 g/m3 dusty-road conditions, calculated holding time is many tens of hours; still inspect cups daily.

## Winter
- Warm season: seasonal non-detergent engine oil.
- 0 to -20 C: light winter oil.
- -20 to -40 C: low-viscosity hydraulic/spindle-type oil; keep cleaner inside the warming envelope of the engine bay where possible.
- Below ~-40 C: dry operation is emergency-only; restore oil when temperature/maintenance permits. No fine external mesh at the intake head; it becomes an icing surface.

## E5-VR disposition
- Raw E5-VR airflow: 7.6 kg/s = 15050 cfm at the working density.
- At ~87% loading of a 315-cfm oil-bath cell this corresponds to ~55 cells, about 842 kg and 1600 L installed as a sensitivity estimate.
- Equal D-D shaft power while preserving E5 specific airflow still requires ~19 cells, about 291 kg and 553 L.
- Therefore E5-VR remains a vehicle mule/special low-dust application, not the ordinary Manchuria tank powerplant. Compressor dust-TBO remains OPEN-TEST.

## Source anchors
- 1942 TM 9-1750G: GM 6-71 tank powerplant used oil-bath cleaners with oil-washed metal wool; six cleaner assemblies; cleaner oil and service instructions. https://www.scribd.com/document/139026938/TM-9-1750G-General-Motors-Twin-Diesel-6-71-Power-Plant-for-Medium-Tanks-M3A3-M3A5-And-M4A2-1942
- 1944 Army Motors cold-weather guidance: low-vis hydraulic oil in air cleaners below 0 F, dry operation only at about -40 F and below. https://www.scribd.com/document/716389847/Army-Motors-V4-N10-February-1944
- US2304778A: centrifugal cleaner ahead of oil-bath cleaner as a known tandem arrangement; reduces dirt load on oil cleaner. https://patents.google.com/patent/US2304778A/en
- NBS Donaldson A10574 test: 315 cfm, 27 lb including 3.5 qt oil, 7.9 in H2O clean restriction, 1380 g dust loading; used only as a later scaling anchor and conservatively derated here. https://www.govinfo.gov/content/pkg/GOVPUB-C13-48ef4410fd2130000d06100885d3c650/pdf/GOVPUB-C13-48ef4410fd2130000d06100885d3c650.pdf
