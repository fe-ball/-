# BUILD RECIPE / PROVENANCE

Base archive SHA256: `7beb3a2bd35453cf24c640d29c32d3861d146b76b3f5b31a0762fcb69fa8562f`  
Base archive: `計算機異聞_BRANCH_B_v048_CANONICAL_RESUME_1944-06-15T24_2026-08-30.zip`

The full package was created by byte-preserving extraction of the base archive, addition of the 2026-08-31 continuation master, extraction of each listed source overlay under a unique sequence directory, and preservation of each source overlay ZIP under `SOURCE_ZIPS`.

`MASTER_LOAD_ORDER_v002.json` defines semantic precedence.  Files are not made authoritative merely by physical presence in this full archive.

The package validation stage parses every JSON file, audits top-level `id` values in the active 2026-08-31 runtime overlays, creates a full-file SHA256 manifest (excluding the manifest itself), and performs ZIP CRC testing.
