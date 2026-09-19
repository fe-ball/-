# Carrier propulsion decision pass 1 — 2026-08-27

Status: working decision layer on top of the historical crosswalk and large-core audit. The comparison table is `19-CARRIER-BOOST-COMPARISON-V1.csv`.

## Method

Historical steam shaft horsepower and speed are retained as the baseline. Candidate E6 additions use **propeller-shaft hp after the explicit 0.975 marine reduction path** from `13-MARINE-LARGE-SCALE-AUDIT-V1.tsv`. Speed is only a cube-law first comparison; no claim is made that the historical propellers, shafts, gear rooms or hull resistance curve can accept the additional power unchanged.

Two candidate blocks are compared:

- 4 × E6-large-A/甲: the earlier large E6 band; derived marine gate 1939–40 conditional.
- 2 × E6-large-B/乙: fewer units but later, larger scale; derived marine gate 1940–41 conditional.

The result is a *benefit screen*, not an installation design.

## Kaga

Historical post-refit machinery is about 127,400 shp / 28.34 kt. Her 1934–35 reconstruction actually replaced the power plant, which makes it mechanically tempting as an alternate-history insertion point, but it occurs before E5 large marine productization and years before E6 large.

Even if a later E6-A package is applied counterfactually, 4 × E6-A adds roughly 16.2–20.3 kshp and gives only about **29.50–29.77 kt** on the cube-law screen, a gain of ~1.2–1.4 kt. The chronology is the decisive blocker.

**Decision: mature GT co-main conversion = NO for the historical 1934–35 refit.** Instrumentation, arrangement studies and auxiliary experiments remain possible.

Historical machinery source: https://rikukaigun.org/Nishida/e/stc0203.html

## Akagi

Akagi's 1935–38 reconstruction overlaps E5 completion, but her machinery was largely retained while boilers/ventilation were modernized; the historical power level after modernization was about 133,000 shp / 31.2 kt. A full GT combining train would therefore be a new propulsion redesign, not a simple by-product of the historical refit.

Four E6-A units would screen at roughly **32.42–32.71 kt**, only ~1.2–1.5 kt above baseline, and E6-A itself does not reach the derived marine gate until 1939–40.

**Decision: full GT co-main Akagi = NO as central.** Keep only limited test/auxiliary insertion if a separate experimental branch needs it.

Historical chronology source: https://www.combinedfleet.com/Akagi.htm

## Soryu / Hiryu

Soryu (~152,000 shp / 34 kt) and Hiryu (~153,000 shp / 34.3 kt) already sit in a high-power, high-speed cruiser-derived steam regime. Their build/design windows are too early for E6 large, and even a hypothetical four-E6-A addition buys only roughly **+1.2 to +1.5 kt** on the first-order screen.

That is a poor trade against extra intakes/exhausts, gear trains, shaft transients, fuel system, volume, top-side routing and a second high-power propulsion technology.

**Decision: historical steam architecture = CLOSED CENTRAL.** GT influence may exist in auxiliary power, test instrumentation or future design studies, not as a co-main propulsion branch on these ships.

Historical machinery sources:
- Soryu: https://rikukaigun.org/JeffD/_warships1.html
- Hiryu: https://www.navypedia.org/ships/japan/jap_cv_hiryu.htm

## Taiyo / Kasuga Maru

Taiyo is the outlier because the baseline is only about **25,200 shp / 21 kt on two shafts**. Here the same E6-A package is not a marginal increment:

- 4 × E6-A @780 C: total ~41.4 kshp, cube-law ~**24.79 kt**.
- 4 × E6-A @870 C: total ~45.5 kshp, cube-law ~**25.57 kt**.
- 2 × E6-B is mechanically tidier as one large GT path per shaft, but is later and less mature; it screens at roughly 24.4–25.1 kt.

So Taiyo is the only examined carrier where GT boost has a large *relative* speed effect. However, the historical conversion window is only May–September 1941 and the previous `existing main gear + added pinion` shortcut is retired. A real 60–80% shaft-power increase requires new combining/reduction/shafting, intake/exhaust and machinery-space work. E6-B is only reaching its derived marine gate in 1940–41, and four E6-A units multiply installation complexity.

The unresolved aviation/WOD speed threshold must not be used to force the answer.

**Decision: four-E6-A / two-E6-B co-main conversion = technically interesting but NOT CENTRAL under the historical 1941 conversion schedule.** Retain the revised calculation as a design study. If a faster escort carrier is desired, it needs either an earlier purpose-designed conversion program or a different hull rather than a short-notice machinery graft.

Historical conversion anchor: https://www.niehorster.org/014_japan/navy-commanders/cv.html

## Unryu

Unryu is the first strong new-build carrier decision point because the 1941 urgent program comes after E6-A can plausibly have marine qualification and while E6-B is entering it. But the historical design already uses ~152,000 shp / 34 kt steam machinery. Adding 4 × E6-A screens at only **35.17–35.45 kt**; 2 × E6-B gives about **35.04–35.29 kt**.

Replacing the whole 152,000-shp steam plant with the current E6 large classes would require a many-engine installation and far more product/gear/fuel maturity than has been closed. A boost-only system gives modest speed gain while penalizing urgent standardization. The historical wartime program explicitly rewards rapid, standardized construction; later ships even accepted lower-power substitute steam machinery when shortages appeared.

**Decision: Unryu historical-type steam plant = CENTRAL. E6 large co-main/boost = NOT ADOPTED in the 1941 urgent central design.** Retain E6 only as a research branch for future purpose-designed high-speed or damage-tolerant propulsion after the prewar boundary.

Historical program/machinery source: https://www.usni.org/magazines/proceedings/1955/september/japans-wartime-carrier-construction-and-pictorial-section

## Carrier branch closures from this pass

- Kaga mature GT conversion: **CLOSED NO**.
- Akagi full co-main GT: **CLOSED NO as central**; experimental insertion only.
- Soryu/Hiryu GT main/co-main: **CLOSED NO as central**.
- Taiyo E6 co-main: **OPEN-CALC retained / adoption CLOSED NO under historical short conversion window**.
- Unryu 1941 urgent design: **steam CENTRAL; E6 co-main CLOSED NO for central design**.
- `25.5 kt carrier WOD threshold`: **still OPEN and no longer needed to decide these propulsion chronology questions**.
