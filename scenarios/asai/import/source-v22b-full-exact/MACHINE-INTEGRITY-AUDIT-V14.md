# MACHINE INTEGRITY AUDIT — V14

Status: **PASS**.

- Expected total files after V14 audit/inventory/manifest/checksum creation: **939**
- Expected SHA-256 manifest entries: **937**
- Expected package-inventory entries: **936**
- Manifest exclusions: exactly `FULL-PACKAGE-MANIFEST-SHA256-V14.tsv` and `SHA256SUMS-V14.txt`
- Inventory exclusions: itself plus the V14 manifest/checksum pair
- New V14 ground current files: **8**
- New V14 naval current files: **11**
- New V14 ground-quarantine files: **10**
- New V14 naval-session provenance files: **3**
- Combat clock advanced: **NO**

Structural checks:
- V12 fixed-wing and V13 helicopter current trees are retained.
- `81-CURRENT-2026-09-09-GROUND-VEHICLE-CLOSE/` is highest ground-vehicle authority through 1941.
- Chi-Ha-family 1941 new-hull accounting is 500 total; derivative SPG/ARV hulls are inside that total.
- Amphibious Chi-Ha and deep-wading Chi-Ha remain zero.
- `82-CURRENT-2026-09-09-NAVAL-MARINE-CLOSE/` is highest naval/marine authority through the prewar boundary.
- Surface combatants remain primarily steam through 1941; Yamato remains all-steam.
- No selected carrier/cruiser/destroyer GT propulsion/boost installation before 1941-12-08.
- The Yokosuka propulsion-test-ship program is active, while the working public number 4017 is explicitly not locked.
- E6 marine qualification is explicitly below M3 primary-propulsion qualification.
- GT high-speed craft option value is separated from actual prewar series inventory/OOB.
- Low-speed powered-lift/STOL carrier force remains a 1942+ qualification/policy option; 1941 operational OOB is zero.
- Asai naval/ground role is explicitly ripple/collaboration, not service-policy domination.
- Ground and naval provenance/quarantine directories are non-current.

Pre-manifest semantic/TSV/pointer checks: **PASS**.
Final verification: **PASS**. Independent archive extraction showed **939 total files**, **937 manifest entries**, **0 missing files**, **0 size mismatches**, and **0 SHA-256 mismatches**. The final archive is regenerated after this audit update and re-verified against the refreshed manifest.
