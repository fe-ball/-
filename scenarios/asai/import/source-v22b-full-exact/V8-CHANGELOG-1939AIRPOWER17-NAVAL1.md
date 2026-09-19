# V8 CHANGELOG — 1939AIRPOWER17 NAVAL1

- Retains REPLAY2, EXHAUST1 and IDENTITY1; combat clock remains **1939-05-10 24:00**.
- Expands `50` Section 7 and `50A` from a generic naval-ship fallback into an explicit Navy ship/carrier caution system.
- Separates carrier headline chain: hull/deck geometry -> installed/serviceable shaft power -> speed -> WOD -> aircraft launch/recovery envelope -> elevator/hangar/deck cycle -> deck-ready aircraft -> sortie generation. No stage automatically grants the next.
- Adds specific cautions for Akagi/Kaga, Soryu/Hiryu, Shokaku class, Hosho/Ryujo/small carriers, low-speed merchant/converted carriers, carrier main steam plant, carrier GT boost, emergency GT power, carrier air-group capacity, aircraft compatibility, WOD, sortie generation, aviation-fuel/fire/damage control, shipboard AA/director/radar, Yamato/A-140 propulsion, destroyer/cruiser GT, and hull-count/commissioning schedule.
- Reasserts current marine-GT state: Apr20 1939 has shore qualification capability but **no automatic large-surface-ship GT installation**.
- Explicitly forbids the old shortcut `~21 kt converted carrier + GT = fleet carrier`. GT boost may only be a conditional short-duration WOD aid after installed integration gates.
- Explicitly forbids generic knot/range/shp bonuses from Asai machinery/QC, and forbids converting aircraft serviceability gains into physical carrier capacity or sortie-rate gains.
- Carrier-aircraft compatibility must close actual worldline aircraft weight/size/prop/landing-speed against elevator, hangar, deck, arresting and WOD limits.
- Adds no ship procurement, refit, OOB, launch, commissioning or combat result.
