# V8 CHANGELOG — STATEFIX1 — 2026-09-03

This patch corrects handoff/state-machine semantics only. It does **not** change worldline events, equipment performance values, production quantities, or combat outcomes.

Changes:
- distinguishes the old furthest-explored **1939-09-01 post-Nomonhan V6 state** from the current revalidated **1939-04-20** combat checkpoint;
- records the rollback cause as aviation-history inconsistency/rebase;
- marks combat replay as **HOLD_FOR_AVIATION_AUDIT**;
- records the active technical workfront as **PISTON_AVIATION** rather than implying that the next action must be combat replay;
- weakens the 1942 carrier-fighter portfolio from a mandatory immediate next step to a high-value next audit cluster inside the broader piston-aviation closure;
- reclassifies the legacy 1937 retreat/interdiction `HARD OPEN` as an unresolved **retroactive, nonblocking** audit item under current V8 workflow;
- adds `50-CURRENT-1939-1941-AIRPOWER-AUDIT/10-HANDOFF-STATE-MACHINE-CANON-V8.md` as the explicit authority for these semantics.
