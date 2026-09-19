# V8 CHANGELOG — 1939AIRPOWER3 HOMARE1 — 2026-09-03

This overlay advances **technical audit only**. Combat history remains at the revalidated 1939-04-20 24:00 checkpoint.

## Added
- `11-HOMARE-QUARTERLY-DEVELOPMENT-QUALIFICATION-CANON-V8.md`
  - closes Homare branch-neutral development/qualification through 1943Q1;
  - separates `EA-D` development-flight, `EA-Q` service-qualified and `EA-S` series-repeatable availability;
  - makes 100-class / ~92-class+ADI / low-grade emergency maps part of the 1940 design architecture;
  - details bearing, lubrication, induction, vibration and production-QC convergence by quarter;
  - defines 1943Q1 as technical-maturity, not fleet-maturity.
- `12-HOMARE-QUARTERLY-STATE-LEDGER-V8.tsv`
  - machine-readable quarter/state summary.
- `13-HA43-PREBRANCH-DEVELOPMENT-AUDIT-V8.md`
  - closes the branch-neutral Ha-43 path through 1943Q1;
  - separates base mechanically supercharged Ha-43 from remote-turbo/Ru development;
  - preserves procurement priority after 1942Q3 as a branch variable.
- `14-PISTON-ENGINE-PREBRANCH-ROLLUP-V8.md`
  - short engine-availability bridge for subsequent aircraft analysis.

## Refined
- file 07 now points to file 11 for quarter-level Homare authority and no longer describes 1943 fleet maturity as branch-independent;
- Homare 21 near-6-km V8 good-engine center is pulled to ~1,640–1,650 hp, broad ~1,600–1,680; ~1,700 becomes an upper favorable case rather than the default center;
- file 08 Homare/Reppu working engine input is adjusted consistently, without canonizing aircraft performance;
- package state and precedence are updated for the new technical authority.

## Major guard
The engine audit may proceed beyond the combat clock where its causal dependencies are branch-neutral. It must stop before fixing 1943+ quantities, theater fuel/oil reality, fleet TBO/reliability or procurement outcomes that depend on NC/war play.
