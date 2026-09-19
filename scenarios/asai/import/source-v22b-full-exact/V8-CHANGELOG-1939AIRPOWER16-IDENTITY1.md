# V8 CHANGELOG — 1939AIRPOWER16 IDENTITY1

- Adds `50-HISTORICAL-DESIGNATION-NOT-IDENTICAL-HARDWARE-GUARD-V8.md` and `50A-HISTORICAL-DESIGNATION-DIFFERENCE-LEDGER-V8.tsv`.
- Makes explicit the package-wide rule: **historical designation != identical worldline hardware**. Historical names are preserved for lineage/readability, so configuration, lot, QC, serviceability and historical-anchor inclusion must be checked separately.
- Integrates the guard into `47/47A`, `TERMINOLOGY-AND-SUPERSESSION-GUARD-V8.tsv`, `PRECEDENCE`, `PACKAGE-STATE` and a new `CURRENT-MASTER-FILE-INDEX-V8.tsv`.
- Adds cross-service ID0/ID1/ID2/ID3/ID4/ID5/IDH semantics and a machine-readable caution ledger covering Army, Navy, engines, ground vehicles and special ammunition/retrofits.
- Closes a Navy designation ambiguity: **worldline A7M=Gaifu; historical A7M Reppu is a worldline A9M H-anchor**. Current V8 Reppu comparison files are relabeled accordingly.
- Reasserts `A8N=Sakufu`, `J2N=Hekireki`, `B6N=Tenzan` historical Nakajima lineage, `B7A=Ryusei` independent design; old B6A-Aichi Tenzan remains superseded.
- Reasserts current `Ki-64` as Kawasaki tandem-Ha-40 experimental lineage; old fictional single-engine turbo production concept remains superseded.
- OOB processing is explicitly split: historical inventory count -> worldline lot/config mix -> serviceable -> forward deployed -> combat used.
- EXHAUST1 remains current and is nested under the new identity guard; no combat clock advance.
