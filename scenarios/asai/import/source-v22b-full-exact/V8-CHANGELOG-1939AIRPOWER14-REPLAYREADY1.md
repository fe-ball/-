# V8 CHANGELOG — 1939AIRPOWER14 REPLAYREADY1

## Purpose

Close the final workflow/precedence preparation needed to resume the 1939 chronology without advancing the clock in the package itself.

## Added

- `47-1939-04-20-HISTORICAL-VEHICLE-DELTA-CANON-V8.md` and ledger:
  - compact replay-facing list of representative historical Japanese vehicles already altered by Asai capability;
  - resolves Type 97 Chi-Ha ordinary-production power at **200 hp continuous / 220 hp short** from the later v27 tank parent;
  - explicitly supersedes older 180/200 wording for new 1939 calculations while keeping allocation/combat separate.
- `48-1939-04-20-COMBAT-REPLAY-LAUNCH-CARD-V8.md` and queue:
  - changes workflow status to `READY_TO_RESUME_COMBAT_REPLAY` at the unchanged 1939-04-20 24:00 checkpoint;
  - fixes the next gate at 1939-04-21 Nanchang counteroffensive;
  - records carry-in, no-back-propagation rules and local stop conditions.

## Updated

- handoff state machine and Apr20 restart baseline: aviation audit no longer blocks replay by default;
- `PACKAGE-STATE-V8.tsv`: current package/workflow identity repaired through AIRPOWER14;
- Start Here / precedence: replay launch card and historical-vehicle delta promoted to mandatory top-level reading;
- integrity metadata rebuilt for AIRPOWER14.

## State-machine ruling

- combat clock remains **1939-04-20 24:00**;
- status is **READY_TO_RESUME_COMBAT_REPLAY**;
- technical work is **ON_DEMAND_ONLY** unless a concrete event dependency appears;
- old post-Nomonhan V6 results remain comparator/provenance only.
