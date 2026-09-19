# Europe casualty-delta ledger to OVERLORD — Axis submarine-exchange effects v001

status: LIGHTWEIGHT_RUNNING_LEDGER
cutoff: 1944-06-06

This ledger records only Branch **differences** attributable to Japan<->Germany submarine exchange, not historical Axis capability already realized.

| Driver | Status | Pre-OVERLORD treatment |
|---|---|---|
| I-30 outbound Type 91 aerial-torpedo material | historical receipt already occurs; Branch can improve data quality | `OPEN_EVENT_DELTA`: from 1943H1, allow small reliability/drop-envelope/test-cycle improvement in applicable German/Axis aerial-torpedo events. Do not book fixed deaths now. |
| I-30 return survival | Japan-side effect | German receipt delta = zero; outbound already succeeded historically. |
| I-8 outbound / Type 95 data | historical receipt | Branch death delta near zero by default; partial technical reference only unless a specific German torpedo event shows a causal link. |
| 1943 historical W/Sn/rubber successful cargo | mostly historical | No Branch delta unless package-specific success/quantity differs. Macro German production bonus prohibited. |
| I-34 extra westbound leg | unresolved as of 1944-01-01 | `PENDING`; if Europe arrival occurs, book actual W/Sn/rubber/etc then trace allocation -> production -> combat. |
| Japanese general computing/process methods | restricted sharing + absorption lag | no default pre-OVERLORD combat delta. |

## Casualty accounting rule
Never write `X tons W = Y Allied deaths`. Book only casualties that arise when a re-adjudicated concrete air/sea/ground event changes. Small technical changes have a fat right tail: often zero effect; occasionally an extra hit on a destroyer, tanker or troop transport creates a large discrete casualty difference.
