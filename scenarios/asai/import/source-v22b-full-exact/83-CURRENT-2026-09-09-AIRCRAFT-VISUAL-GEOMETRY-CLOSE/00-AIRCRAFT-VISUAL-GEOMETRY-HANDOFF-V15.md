# AIRCRAFT VISUAL GEOMETRY / CG HANDOFF — V15

Status: **VISUAL GEOMETRY CLOSED THROUGH 1941 FOR CURRENT FICTIONAL PHYSICAL AIRFRAMES; PAPER-ONLY PROGRAMS REMAIN INTENTIONALLY UNFROZEN.**

## 1. Authority boundary

This directory is the highest authority for **outer-mold-line / CG reference geometry only**. It does not replace performance, procurement, naming, OOB, or measured-flight authorities in V12/V13/V14.

The point of this closeout is to make a reusable three-view and 3D model deterministic. Where an older CURRENT file explicitly refused to invent a production drawing (notably Ki-42 and E6 Single/Twin), this V15 layer does **not** claim that a lost manufacturer drawing was recovered. Instead it creates a new, explicit `CG-OML reference closure` whose dimensions are the canonical visual representation of the worldline airframe.

Priority for visual conflicts:

`83 VISUAL-GEOMETRY V15` > older visual proxies / descriptive geometry.  
Priority for performance/history conflicts remains the older subject-specific CURRENT authority.

## 2. What is locked

For P1, P2, Material No.1/2, E5 future-form, Ki-42, HS-2, E5 Twin, E6 Single, E6 Twin, E6-B, X-TP reference configuration, A7M Gaifu, A8N Sakufu, Ki-40, H1 and H2:

- overall OML length/span/rotor diameter/height;
- wing planform reference, thickness ratio, dihedral/sweep/washout;
- fuselage station envelope sufficient for lofting;
- tail volumes as visible geometry;
- cockpit/cabin location and glazing language;
- gear type, track, wheelbase and wheel-size class;
- nacelle/inlet/nozzle or propeller envelope;
- principal high-lift/control-surface segmentation;
- carrier fold/hook geometry where applicable;
- visible bomb/mission bay and research-access logic;
- rotor head/blade/tail-boom visual architecture for H1/H2.

Material No.3 / AT-3 receives a **1941 formal-design OML freeze**, not a flown-aircraft claim.

## 3. What is deliberately not locked

- exact rivet pitch and every inspection screw;
- factory drawing tolerances below the CG/modeling scale;
- serial-specific antenna masts, gun marks, cameras, radios and local test probes;
- exact prototype paint batch or individual tactical code;
- service-local gun model where performance canon intentionally kept only a mass/recoil envelope;
- J2N Hekireki final OML, H3 final OML, HS-3 final OML, E7 clean-sheet aircraft: these remain requirement/paper/future programs and must not acquire a fake definitive shape.

## 4. Required modeling convention

Use `x=0` at the forwardmost fixed OML point (spinner excluded only when explicitly called a separate feature), +x aft; +y starboard; +z up. `02-FUSELAGE-STATION-OML` widths/heights are main body envelope only, excluding canopy, nacelles, inlets, landing gear and local fairings.

Wing reference area uses the full aerodynamic planform including the center section. Rounded tips/fillets may locally change mesh silhouette while preserving the master reference area within ~0.5%.

## 5. Family visual language

- **Asai research jets:** compact, functional, forward cockpit, short straight/tapered wings, conspicuous test access, cheek inlets where rear-engine architecture is used. No science-fiction area ruling or swept-wing aesthetic is backdated.
- **Mitsubishi Gaifu/Ki-40:** smoother oval fuselage, tighter fillets, conservative Japanese all-metal construction language, compact framed canopy, cleaner panelization.
- **Nakajima Sakufu:** wider shoulder, strong nacelle/wing integration, large practical fold geometry and visibly mechanical powered-lift cascade.
- **Kawasaki E6-B:** long low-drag fuselage with purposeful crew glazing, large internal-bay belly, no decorative heavy turret farm.
- **P1/P2:** practical rough-field utility appearance, fixed gear and strut-braced high wing; P2 is visibly more STOL-specialized than P1.
- **H1/H2:** H1 visibly experimental/tube-and-fairing; H2 is the first compact enclosed practical helicopter, but remains 1940 technology—no modern composite fairing language or electronic-sensor bulges.

## 6. Historical-reference aircraft

Ki-76 is not re-invented here. Its historical outer geometry remains the visual reference for the worldline military-STOL branch; worldline changes affect chronology/acceptance and Asai-derived high-lift know-how, not a fictional new shell.

## 7. Three-view readiness verdict

After this closure, all listed physical/current fictional aircraft can be modeled from one deterministic reference geometry without using a generic AI-image guess for wing shape, landing gear, intake, fold, rotor architecture or cabin proportions.
