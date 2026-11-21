# Polybrutus D43 — Constructive exact proof and independent checks

**Scientific parent:** `Topbrutus/polybrutus-d42@v0.1.0`, scientific commit `cba477c53ccdadaed888730ee0d3d25504eeff10`, DOI `10.5281/zenodo.24414577`, certificate SHA-256 `279a43e425687b0359d61f2b104acaf2df926b04bd822f2934fb2f3016fdda20`.

**Integrity of complete source and all ancestors.** Exact D42 Git-tag source including inherited ancestors lives in `prior/d42/frozen_scientific_tag_v0.1.0.zip`, SHA-256 `3789f4a185bb50dc0d2aaa157cc370044768598abce2095c3a5e6c80eb8e9f7a`. The archive has 28 entries and passes ZIP CRC. Both verification programs compare the original `results/certificate_d42.json` ZIP entry byte-for-byte against the extracted local parent certificate and verify SHA-256. This compressed archival lineage avoids Windows path length exhaustion.

**Exact labelled pair preservation.** Zero-extend all 47 parent unit points. Adjoin one perpendicular norm-one point. All **1081/1081** predecessor pair values and their labels are preserved. Every new squared distance equals `2R²`, yielding 47 new pairs and **1128=C(48,2)** unordered labelled pairs.

**PSD and minimal affine rank.** The complete exact rational Gram consists of an original canonical rank-three block, centred simplex rank-four block and 36 perpendicular unit axes: `rank(G)=3+4+36=43`. It is PSD with unit diagonal. The uniquely constructed centered Gram `B=-(1/2)HDH=HGH` has exact rank **43**. The inherited antipodal canonical pair places the origin in the affine hull, proving minimum Euclidean affine dimension **43** for this specific complete labelled metric.

**Exhaustive rational arithmetic.** Histogram of `k=4d²/R²`: `{4:6,7:2,8:1097,9:3,10:10,12:6,13:2,16:2}` with total 1128. Exact sum of all squared distances at R=1 is `9071/4`. Pairwise predecessor conservation is checked by label, not only by histogram.

**Separately stipulated abstract graph.** With scalar unit masses and `w_ij=1/d_ij²`, exact Laplacian matrix ranks establish eigenvalue **24** of multiplicity **37**, and **47/2** of multiplicity **4**. These are dimensionless ideal graph eigenmodes, not measured hertz.

**Independent implementations.** Primary `src/verify_d43.py` constructs exact Gram entries, checks all 1128 pairs, all 1081 original parent labels against the exact hash-authenticated archive/certificate and verifies centered Euclidean and graph ranks. Four adversarial controls detect a corrupted pair distance, duplicated point, nonorthogonal tilt and histogram-preserving label permutation. Independent `tests/independent_d43.py` derives all labelled distances using Python `fractions.Fraction` structural rules, **without importing the primary Gram generator**, and checks all 1081 predecessor labels, 1128 present labels, frozen archive, certificate and exact ranks. Both print identical SHA-256 for deterministic `results/certificate_d43.json`.

**Scientific limits.** Established Euclidean perpendicular extension and uniform graph joining yield one synthetic reproducible metric and one selected graph, not a novel universal theorem, observed extra physical spacetime dimensions, particles, measured resonances or independent human peer review.
