# BRANCH B v052 — Authority / Supersession Map (2026-09-05)

## Inherited authorities
All v051 and v050 authority ordering remains active, including cruiser overlays and the Santo→New Caledonia chain.

## New v052 authorities
- `BRANCH_B_YAMATO_MUTSU_1942-11_REAUDIT_v001.*`
  - status: **canonical-provisional-overlay** for Yamato/Mutsu as of 1942-11-09.
  - overrides any generic assumption that both ships have identical radar/I-O, speed, or modernization realization.

- `BRANCH_B_HEAVY_GUN_PROJECTILE_MATERIALIZATION_1934_1942_v001.*`
  - status: **canonical-provisional-overlay** for Japanese 36/41/46 cm heavy-gun physical realization when no more specific weapon audit exists.
  - supersedes only the prior shorthand that “gun/projectile body itself does not change.”

## Precedence
1. Date/hull-specific battle damage and repair state.
2. v052 Yamato/Mutsu individual audit.
3. Detailed existing weapon/fire-control canonical documents.
4. v052 heavy-gun/projectile physical-realization layer.
5. v051 cruiser overlay / generic technology rules as applicable.
6. Historical baseline.

## Nominal-physics guard
v052 does **not** authorize free redesign.
Unless explicitly reopened, retain:
- caliber and barrel length;
- service projectile mass and overall ballistic family;
- standard service muzzle velocity;
- service charge weight;
- armor thickness;
- fundamental Type 91/Type 1 underwater-trajectory doctrine and long-delay fuze concept.

What may change is the **distribution around those nominal values**: metallurgy/heat treatment, dimensional tolerance, lot spread, driving-band concentricity, cap fit, charge consistency, barrel/chamber realization, proof/rejection control and failure tails.

## Non-stacking guard
- Do not convert body-quality improvement into a generic “penetration +X%.”
- Do not add ammunition consistency separately on top of an already-adjudicated intrinsic-dispersion improvement if both represent the same causal term.
- Existing `TECH-GUNFIRE-SURFACE-1942-001` and electronic ballistic-aid effects remain separate from physical ammunition/gun realization.
