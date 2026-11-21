# Polybrutus 43D — Exact 48-point Euclidean metric and a 37-fold ideal graph mode

**Responsible human scientific author:** Gabriel St-Pierre, independent researcher.  
**Material AI assistance:** OpenAI ChatGPT (Astra) materially assisted exact rational calculations, two separate verification programs, manuscript and controlled publication. AI is not a scientific author.

## Exact unit-radius results

- **48 labelled norm-one points**, **1,128 unordered labelled squared distances**, minimal affine Euclidean realization dimension **43**.
- **1,081/1,081** previous pair labels preserved exactly from [frozen Polybrutus D42 v0.1.0](https://github.com/Topbrutus/polybrutus-d42/tree/v0.1.0), scientific source `cba477c53ccdadaed888730ee0d3d25504eeff10`, [DOI 10.5281/zenodo.24414577](https://doi.org/10.5281/zenodo.24414577).
- A newly appended perpendicular unit point contributes **47** new squared distances, all `2R²`.
- Exact histogram `k=4d²/R²`: `{4:6,7:2,8:1097,9:3,10:10,12:6,13:2,16:2}`. Exact sum of all squared distances at R=1: **9071/4**.
- Exact rational centered Euclidean Gram matrix is PSD of rank **43**.
- For a **separately stipulated ideal complete weighted graph**, unit scalar masses and `w_ij=R²/d_ij²`, the Laplacian eigenvalue **24** has multiplicity **37**, and **47/2** has multiplicity **4**. These are *dimensionless model values*, not measured physical frequencies.
- Two separately implemented exact-rational verifiers independently check all 1,128 labels, all 1,081 original parent pairs, centered Euclidean ranks and selected ideal graph eigenspaces. Four primary adversarial negative controls succeed.

## Reproduce locally

```bash
python -m pip install sympy==1.14.0
python src/verify_d43.py
python tests/independent_d43.py
```

Both scripts print the same deterministic SHA-256 for `results/certificate_d43.json`.

**Complete source lineage:** The exact frozen D42 source tag including all ancestors is in `prior/d42/frozen_scientific_tag_v0.1.0.zip` (SHA-256 `3789f4a185bb50dc0d2aaa157cc370044768598abce2095c3a5e6c80eb8e9f7a`, **28 ZIP entries**). The original parent certificate is copied byte-identically to `prior/d42/results/certificate_d42.json`, and both programs check the archive SHA-256, CRC, embedded entry equality and parent certificate SHA-256. Archive-within-archive packaging avoids the Windows maximum-path problem and retains all old source bytes. No nested Git repositories or submodules.

## Official DOI and verified public release

- **Official DOI:** [10.5281/zenodo.24415111](https://doi.org/10.5281/zenodo.24415111).
- **Public Zenodo record:** https://zenodo.org/records/24415111, all 3 public files checked for exact sizes and MD5 against the original bytes.
- **Frozen science tag:** [v0.1.0](https://github.com/Topbrutus/polybrutus-d43/tree/v0.1.0), source commit `e435e38aed88e8c65d294eeee26bee6b89056fc8`.
- **Tag CI:** [GitHub Actions 44886709829](https://github.com/Topbrutus/polybrutus-d43/actions/runs/44886709829), success.
- **Durable Memoria checkpoint:** https://github.com/Topbrutus/topbrutus_one/blob/main/memoria/checkpoints/POLYBRUTUS_D43_PUBLICATION_2026-11-21.md .
- **Publications registry:** https://github.com/Topbrutus/topbrutus_one/blob/main/memoria/projects/POLYBRUTUS_X72_PUBLICATIONS_INDEX.md .

## Research material

- [Exact mathematical specification](SPECIFICATION_D43.md), [constructive proof and adversarial checks](PREUVE_D43.md), [provenance and limits](PROVENANCE.md), [source lineage archive](prior/d42/ARCHIVE_PROVENANCE.md).
- [Scientific PDF preprint](publication/POLYBRUTUS_43D_NOTE.pdf), [editable preprint](publication/POLYBRUTUS_43D_NOTE.md), [complete certificate](results/certificate_d43.json).

**Scientific limitations:** One reproducible synthetic Euclidean labelled metric and a separately stipulated abstract weighted graph using established perpendicular extensions and graph joins; **no physical extra dimensions, measured resonances, particle discoveries, novel universal theorem or independent human peer review claimed**.

**Licenses:** source code MIT; manuscript CC BY 4.0.
