# HANDOFF STATE MACHINE — CANON — V8 1939REPLAY2 NANCHANG-A2

Purpose: prevent chronological exploration history, current canonical replay position, and technical-audit workfront from being conflated. This file changes **handoff/workflow semantics only**; it does not introduce a new worldline event.

## 1. Progression lineage
1. The older V6 line progressed through the 1939 Nomonhan sequence and reached **1939-09-01 00:00**.
2. Aviation/aircraft history was then found to contain inconsistencies serious enough to require rollback/rebase rather than continuing from the post-Nomonhan state.
3. The combat-history replay was rebuilt forward through **1939-04-20 24:00**.
4. Combat progression was then deliberately held for the broad aviation/company audit. AIRPOWER14 released that hold, and REPLAY1 advanced through the opening Nanchang counteroffensive to 1939-04-26, and REPLAY2 closes the Nanchang counteroffensive and concurrent due flight-test events through **1939-05-10 24:00**.

## 2. Machine-readable conceptual fields
- `furthest_prior_explored_clock = 1939-09-01 00:00`
- `furthest_prior_explored_branch = V6 / post-Nomonhan`
- `current_revalidated_combat_checkpoint = 1939-05-10 24:00`
- `combat_replay_status = ACTIVE_COMBAT_REPLAY`
- `active_technical_domain = ON_DEMAND_ONLY`
- `next_chronological_combat_gate_if_resumed = 1939-05-11 Nomonhan opening clash / border incident sequence`

## 3. Authority rule for later-dated preserved material
Chronologically later files under preserved V6/V7 trees do not regain CURRENT status merely because their date is later than 1939-04-20. Treat post-1939-04-20 older-branch results as **reference/comparator/provenance** until the current replay or a current aviation overlay explicitly revalidates them.

This is especially important for post-Nomonhan aviation conclusions: they are useful evidence of prior reasoning, but they cannot silently override the current aviation rebase.

## 4. Present technical workfront
AIRPOWER13 completed the broad Apr20 technical/company reconstruction and AIRPOWER14 releases the workflow hold. Broad technical work is now **ON_DEMAND_ONLY** during event replay.

AIRPOWER3/AIRPOWER4 have already carried the branch-neutral piston-engine, high-power propeller/cooling and J2M/B7A/N1K/Reppu-prestudy integration audit forward to the **1943Q1 technical boundary**. That closure is retained.

The active workfront is now the broader **AVIATION TECHNOLOGY AUDIT**, with the current subaudit on:
- Asai GT/jet capability semantics and v38-v48 rebaseline inheritance;
- preventing historical-calendar double-downrating after a cheat/computation-aware installed audit;
- E6-S / E6-M-JF rating interpretation and life/TBO semantics;
- E7-E9 continuous technology-front logic, including technology-start clocks versus integrated-core/product clocks;
- adjacent high-speed/transonic and CFRP-merge work, without advancing combat history.

The piston-side **1942 requirement/procurement replay gate** remains a separate hard boundary for formal Reppu/Ki-84-equivalent requirements, engine allocation, production quantities and post-1943 service dates. GT/jet/high-speed technical capability does not auto-resolve that procurement branch.

## 5. 1937 retreat/interdiction research status
`40-RESEARCH-AND-OPEN-ISSUES/00-HARD-OPEN-RETREAT-AIR-INTERDICTION-V7.md` remains unresolved as a historical research question. Its old `HARD OPEN / MUST CARRY` workflow label belonged to the V7 pre-replay state.

Current classification: **UNRESOLVED RETROACTIVE AUDIT; NONBLOCKING BY DEFAULT.**

If later evidence indicates a material change to late-1937 carryover, reopen it explicitly, calculate the delta, and propagate the delta through affected 1938-39 gates. Do not silently invalidate the present checkpoint merely because the legacy filename contains `HARD-OPEN`.


## 6. AIRPOWER14 replay release
The prior `HOLD_FOR_AVIATION_AUDIT` workflow state and the intermediate `READY_TO_RESUME_COMBAT_REPLAY` state are superseded. File 48 remains the Apr20 launch/carry-in authority; REPLAY1 has now advanced through the 21-26 April opening phase. Current workflow state is **ACTIVE_COMBAT_REPLAY**.


## 7. REPLAY1 / REPLAY2 advancement
On explicit user instruction, REPLAY1 advanced through the opening Chinese Nanchang counteroffensive to 1939-04-26. REPLAY2 then advances through the Japanese counterstroke, renewed Chinese assault and Chinese withdrawal, closing Nanchang through **1939-05-09 24:00** and using **1939-05-10 24:00** as the quiet administrative checkpoint. Authority: `60-CURRENT-1939-COMBAT-REPLAY/02-1939-04-27-05-09-NANCHANG-CLOSEOUT-GATE-V8.md`.

Because the chronological clock moved, REPLAY2 also resolves test events already physically due from the Apr20 roster: **E6 Twin No.1 first airframe flight on 29 Apr** and **HS-2 first flight on 4 May**. E6 Single remains unflown. Authority: `60-CURRENT-1939-COMBAT-REPLAY/03-1939-04-27-05-10-CONCURRENT-AVIATION-EVENTS-GATE-V8.md`.

The next chronological gate is **1939-05-11 Nomonhan opening clash / border incident sequence**. No later Nomonhan result or field-validation label is current until replayed.
