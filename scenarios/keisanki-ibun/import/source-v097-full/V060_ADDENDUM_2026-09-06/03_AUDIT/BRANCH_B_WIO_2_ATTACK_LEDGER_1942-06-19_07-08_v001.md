# Branch B — WIO-2 Attack Ledger v001

Period: 1942-06-19 through 1942-07-08 (working local/event clocks)

## 1. Center loss ledger

| Attack date | Boat | Target | Normalized GRT | Historical mechanism | Branch B center ruling |
|---|---|---|---:|---|---|
| 28 Jun | I-10 | Queen Victoria | 4,937 | torpedo; sunk | RETAIN |
| 29 Jun | I-20 | Goviken | 4,854 | torpedo; sunk | RETAIN |
| 30 Jun | I-20 | Steaua Romana | 5,311 | gunfire, first torpedo premature, second torpedo sinks | RETAIN; no extra kill; inventory/exposure ticket |
| 30 Jun | I-10 | Express | 6,736 | two torpedo hits; sunk | RETAIN |
| 1 Jul | I-18 | De Weert | 1,805 | heavily damaged by submarine attack; sank 3 Jul | RETAIN; loss charged to this block |
| 1 Jul | I-16 | Eknaren | 5,243 | torpedo; sunk | RETAIN |
| 6 Jul | I-18 | Mundra | 7,341 | torpedo + gunfire; sunk | RETAIN |
| 6 Jul | I-10 | Nymphe | 4,504 | torpedo; sunk | RETAIN |
| 8 Jul | I-10 | Hartismere | 5,498 | torpedo hit then gunfire; sunk | RETAIN |
| 8 Jul | I-10 | Alchiba | 4,427 | torpedo hit then gunfire; sunk | RETAIN; 8 Jul working date |
|  |  | **WIO-2 total** | **50,656** | **10 ships** | **CLOSED_CENTER** |

Inherited WIO-1C regular-submarine total through 18 Jun: 12 ships / 52,840 GRT.

Cumulative through 8 Jul: **22 regular-submarine sinkings / 103,496 GRT**.

Surface-raider ELYSIA and midget-submarine BRITISH LOYALTY effects remain separately accounted and are not folded into the 103,496-GRT regular-submarine figure.

## 2. Failed/survived attacks — the proper Stage 3A sensitivity set

The Royal Navy 6 Jul situation report lists four ships unsuccessfully attacked since the late-June recrudescence: ROOKLEY, DALLINGTON COURT, PHEMIUS and AGAPENOR.

| Date | Target | Observed outcome | Defect linkage | Branch center | Sensitivity treatment |
|---|---|---|---|---|---|
| 30 Jun | Rookley | shelled but not sunk | none established; deck-gun event | SURVIVES | Stage 3A torpedo reliability does not auto-convert a gun attack |
| 30 Jun | Dallington Court | torpedo attack failed | exact failure mechanism not securely recovered | SURVIVES | OPEN defect-sensitive tail only; no mechanical reset probability assigned until failure class is proven |
| 2 Jul | Phemius | I-18 torpedoes exploded prematurely | direct Stage 3A running/fuze-fault relevance | SURVIVES | strongest tail case; mechanical gate may reopen, but geometry/hit/damage gates remain |
| 6 Jul | Agapenor | unsuccessful attack | exact boat/mechanism unresolved in current source set | SURVIVES | no center conversion; source/mechanism ticket OPEN |

### Phemius conditional mechanical-reset band
Stage 3A reduces the relevant torpedo running/fuze-fault event rate by 15–25% relative.

Do **not** interpret that as a 15–25% sinking probability.

If the plural-source report corresponds to exactly two independently defecting torpedoes, the conditional probability that the uplift removes at least one of the two mechanical failures is:

`1 - (1-r)^2`, for `r = 0.15..0.25` -> **27.75%..43.75%**.

This is only a mechanical-reset probability. A reset shot must still pass:

`correct run -> geometry/intercept -> hit -> damage -> loss`

Therefore PHEMIUS remains a survivor at center. Exact salvo count is not promoted from inference to fact.

## 3. Already-successful attacks are not multiplied

The WIO-2 sinkings occurred while the historical British evasive-routing and high-value-ship protection regime was already in force. Reapplying those same historical measures as a Branch-only rescue would double-count the defense.

Likewise, Stage 3A improvements are not applied to an already-successful attack as an extra merchant kill. The clearest example is STEAUA ROMANA: I-20's first torpedo exploded prematurely, but a second torpedo sank the tanker. The Branch benefit can be an unfired/saved torpedo, shorter exposure, or a later sortie-clock advantage; it is not a second ship sunk at the same event.

## 4. Center closure

**WIO-2 CLOSED_CENTER: 10 ships / 50,656 GRT, Branch center delta +0 / +0 GRT.**

Open sensitivity is retained for later tail/Monte-Carlo or event-tree work, especially PHEMIUS, but does not alter the center ledger before the remaining hit/damage gates are resolved.
