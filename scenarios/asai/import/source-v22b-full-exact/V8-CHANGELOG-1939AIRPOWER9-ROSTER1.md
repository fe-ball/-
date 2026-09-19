# V8 CHANGELOG — AIRPOWER9 ROSTER1

Closes the physical/product/research aircraft roster at the current **1939-04-20 24:00** checkpoint without advancing the combat clock. Restores the P2 practical-STOL line to an Apr20 pilot-product quantity, closes Material No.2 build/q-release semantics, closes E6 Twin/Single build state, and closes the small-helicopter physical count while keeping rotor topology open.

New current files under `50-CURRENT-1939-1941-AIRPOWER-AUDIT/`:

- 29 / 29A — Apr20 Asai aircraft/product/experimental roster + ledger;
- 30 / 30A — P2 STOL product closure + ledger;
- 31 / 31A — Material No.2 build/q-release closure + ledger;
- 32 — E6 Twin/Single Apr20 build state;
- 33 — small helicopter Apr20 state.

Key guards:

- old Sep1939 P1/P2 16-22 aircraft bands are not back-propagated to Apr20;
- HS-1 is the converted E4 Single No.2 and is not double-counted;
- no E6/HS-2/Material No.2 future first flight is promoted into Apr20;
- customer/procurement outcomes remain separate from technical/product capability.
