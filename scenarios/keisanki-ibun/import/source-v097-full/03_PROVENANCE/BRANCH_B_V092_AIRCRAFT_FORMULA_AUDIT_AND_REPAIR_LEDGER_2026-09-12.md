# Aircraft Formula Audit & Repair Ledger — 2026-09-12

## Why this addendum exists
During a broad aircraft audit, several cards were initially tightened using historical performance anchors plus power/drag scaling. A later consistency check against the canonical calculation method found that this shortcut was acceptable for a first max-speed sanity check but insufficient for HARD closure of climb, range, carrier handling, dive envelopes and one-engine-out performance.

## Canonical method restored

Horizontal flight:
- q = 0.5 rho V^2
- CL = 2W/(rho V^2 S)
- CD = CD0 + k CL^2 + cooling/stores increments
- D = q S CD
- eta_p P_shaft = D V

Climb:
- ROC = (P_available - P_required)/W
- integrate dh/ROC across altitude bands.

Range:
- use propulsive efficiency, SFC, L/D and log weight ratio as a calibration form;
- convert to mission radius only through an explicit fuel budget for takeoff, assembly, climb, cruise, target work, attack, escape, return, recovery and reserve.

Carrier approach:
- Vs = sqrt(2W/(rho S CLmax)); approach normally uses a safety multiplier.

Takeoff:
- integrate m dV/dt = T - D - rolling resistance term, using deck wind and changing lift.

Dive:
- use q = 0.5 rho V^2, brake drag, structural speed, and n = 1 + V^2/(gR) as pull-out checks.

Twin-engine failure:
- split feathered / windmilling prop states and include asymmetric trim drag.

## Status changes made in session

- D4Y: repaired under formal method; old 7-minute 5km climb retired.
- Ki-67: repaired; prior 1.5t loaded weight and climb were too optimistic.
- B7A2: repaired; earlier climb slightly optimistic, torpedo/landing states now separated.
- P1Y, D3A2, G4M2, Ki-48-II, Ki-49-II: downgraded from near-close to runtime-close pending formal repair.

## Important non-performance conclusions that remain valid
- D4Y liquid-cooled Atsuta line remains the contemporary rational choice; no hindsight air-cooling.
- D4Y reconnaissance precedes dive-bomber certification.
- B7A is a deliberate 16-Shi unified torpedo/dive-bomber airframe; crew qualifications remain mission-specific.
- Ki-67 requirement arises from the real 1941–42 gap between Ki-48/Ki-21/Ki-49 mission classes.
- computation mainly narrows distributions, accelerates test feedback, and improves availability/reproducibility; it does not create free horsepower or structure.
