# 計算機異聞 refactor v042 — Branch B dawn carrier exchange WORKING

CURRENT authority remains **1944-01-01**. WORKING Central-Pacific discussion clock advances to **1944-02-03 15:30 Marshall local**.

This revision first repairs three v041 second-cycle center-field transcription errors without changing the adjudicated event. It then closes the 2-Feb night/pre-dawn track, opens the 3-Feb Shokaku/Zuikaku/Hiryu GO gate, resolves one Japanese dawn strike and one US counterstrike, and stops after both carrier forces break contact.

Centered 3-Feb carrier result:
- Japan launch ~121: 42 fighters (20 Kinsei centered), 45 D4Y, 34 B6N.
- Cabot: 1 torpedo, campaign-out pending repair audit.
- Intrepid: 1 bomb, temporary flight-deck interruption.
- US counterstrike ~140; Hiryu: 1 bomb + damaging near miss, flight operations suspended but withdrawal speed retained.
- 3-Feb carrier-air irrecoverable centers: Japan ~73 / US ~46. No carrier sunk centered.
- Japan withdraws with Shokaku/Zuikaku operational and Hiryu mobile but flight-limited.
- Marshall local air at 15:30: ~47 serviceable / 21 fighters / 4 Raiden / 9 unique water-air / 9 attack.

Load first:
1. `00_README/CURRENT_DISCUSSION_FRONTIER_v011.json`
2. `06_RUNTIME/PARALLEL_THEATER_STATE_1944-02-03T1530_WORKING_v001.json`
3. `06_RUNTIME/US_COUNTERSTRIKE_JAPAN_CARRIER_FORCE_1944-02-03_WORKING_v001.json`
4. `06_RUNTIME/JAPAN_CARRIER_DAWN_STRIKE_1944-02-03_WORKING_v001.json`
5. `06_RUNTIME/MARSHALL_NIGHT_DAWN_CONTACT_CHAIN_1944-02-02_03_WORKING_v001.json`
6. `06_RUNTIME/JAPAN_FIRST_LINE_CARRIER_BATTLE_STATE_1944-02-03T1530_WORKING_v001.json`

Next exact action: close Cabot/Intrepid/Hiryu repair clocks, then decide the amphibious D-Day (5 vs 6 Feb centered) and continue submarine/Marshall pressure on assault/support echelons.
