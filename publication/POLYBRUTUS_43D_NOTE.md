# Polybrutus 43D: Exact 48-point Euclidean distance geometry and a thirty-sevenfold ideal graph mode

**Gabriel St-Pierre** — Independent researcher  
**21 November 2026**  
**Exact mathematical case study / scientific preprint**  
**Material AI assistance:** OpenAI ChatGPT (Astra) assisted rational calculations, two separately implemented exact verifiers, scientific writing and controlled publication. AI is not a scientific author.

## Abstract

We construct an exact Euclidean labelled squared-distance metric on 48 norm-one points by conservatively adjoining a perpendicular unit point to the frozen Polybrutus 42D scientific source. All 1,081 predecessor labelled squared distances are preserved. One new perpendicular unit point adds 47 squared distances equal to 2 at unit radius, giving 1,128 unordered labelled pairs. The exact rational centered Euclidean Gram is positive semidefinite of rank 43, proving minimum affine realization dimension 43 for this particular labelled metric. For a separately stipulated ideal unit-mass complete weighted graph with weights w_ij=1/d_ij², Laplacian eigenvalue 24 has multiplicity 37 and eigenvalue 47/2 multiplicity 4. Two separately implemented exact-rational programs verify every pair label, parent conservation, Euclidean ranks and selected graph eigenspaces. The dimensionless graph eigenvalues are not measured physical resonances, and the construction does not establish physical extra spacetime dimensions.

## 1. Immutable parent and complete compressed scientific lineage

The frozen scientific parent is Topbrutus/polybrutus-d42 at tag v0.1.0, commit cba477c53ccdadaed888730ee0d3d25504eeff10, DOI 10.5281/zenodo.24414577. Its exact certificate lists 47 norm-one vertices and 1,081 labelled unordered squared distances, SHA-256 279a43e425687b0359d61f2b104acaf2df926b04bd822f2934fb2f3016fdda20.

The entire unchanged D42 source including previous ancestral archives is retained at prior/d42/frozen_scientific_tag_v0.1.0.zip (1,944,221 bytes, 28 entries, valid CRC, SHA-256 3789f4a185bb50dc0d2aaa157cc370044768598abce2095c3a5e6c80eb8e9f7a). Both independently implemented verification programs read the original certificate entry from the archive and check it byte-identical to the extracted copy prior/d42/results/certificate_d42.json. Archive nesting preserves original source while avoiding recursively expanded Windows paths exceeding the filesystem limit. All older scientific Git tags and DOI remain unchanged.

Embed the 47 prior norm-one vectors p_i as q_i=(p_i,0) with one additional coordinate, and append new perpendicular unit vertex q48=e44. The inner products and pair distances of all old points are unchanged. Each new squared distance is ||q48-q_i||²=1+1-2<q48,q_i>=2. Hence there are C(48,2)=1128=1081+47 exact unordered labelled squared pairs.

## 2. Exact rational Gram and minimum Euclidean affine realization

Seven original canonical norm-one vertices form a rational rank-three Gram block with inner products 3*x_i*x_j+y_i*y_j+z_i*z_j. Five centered regular-simplex unit points form an independent rank-four block, unit diagonal and off-diagonal products -1/4. Thirty-six further independent mutually perpendicular unit coordinate vectors are orthogonal to both blocks. Thus full 48-by-48 rational Gram G is PSD by construction, has unit diagonal and rank 3+4+36=43.

Let complete squared-distance matrix D satisfy D_ii=0 and D_ij=2-2G_ij for distinct pairs. Define centering H=I-(1/48)11^T. Its unique centered Euclidean Gram B=-(1/2)HDH=HGH has exact rational rank 43. Two original canonical points are antipodal, so the origin is within their affine span. Every realization of the same complete labelled metric has the same centered Gram rank; therefore minimum Euclidean affine dimension is exactly 43.

## 3. Exact arithmetic of 1,128 labelled squared distances

At unit radius let normalized class index k=4d²/R². Exactly eight classes occur: k=4 on six pairs; k=7 on two; k=8 on 1,097; k=9 on three; k=10 on ten; k=12 on six; k=13 on two; and k=16 on two. The counts total 1,128. The exact sum of all squared pair distances is 9071/4.

Every one of the 1,081 predecessor pair labels is checked against the frozen source certificate, not only against its histogram. A histogram-preserving permutation of labels changes the labelled metric and is detected by adversarial controls.

## 4. Separately stipulated ideal complete weighted graph

Independently choose a complete graph with scalar unit masses and symmetric edge weights w_ij=1/d_ij². The new perpendicular point joins each of 47 predecessor vertices at uniform weight 1/2, giving the block Laplacian

L43 = [ L42+(1/2)I47          -(1/2)1_47 ]
      [ -(1/2)1_47^T                  47/2 ].

The exact uniform-join characteristic polynomial recurrence is chi48(z)=z(z-24)chi47(z-1/2)/(z-1/2). Writing f6(z)=chi_P7(z)/z for the original seven-point nonzero model graph factor gives chi48(z)=z(z-24)^37(z-47/2)^4*f6(z-41/2).

Two distinct exact rational nullity calculations establish nullity(L43-24I)=37 and nullity(L43-(47/2)I)=4. These are dimensionless spectral properties of a stipulated mathematical graph, not physical sound frequencies, resonances, particles or new physical spacetime dimensions.

## 5. Two exact-rational verifiers and falsification controls

The primary program src/verify_d43.py explicitly builds the rational Gram and all 1,128 labelled squared distances, verifies the frozen parent source archive and exact parent certificate SHA, checks each 1,081 old labelled pair, and validates centered Euclidean and model eigenspace ranks. Four adversarial negative controls reject corrupted squared distances, a duplicated point, a nonorthogonal tilt and a histogram-preserving label swap.

Separately tests/independent_d43.py constructs every labelled squared distance using Python fractions.Fraction structural rules, without importing the primary Gram generator. It independently authenticates the original source archive, its CRC and parent certificate, all 1,081 old labels, all 1,128 present labels and exact ranks. Both programs emit identical SHA-256 for results/certificate_d43.json; GitHub CI reruns them and enforces certificate byte determinism.

Reproduction: Python and sympy==1.14.0; run python src/verify_d43.py and python tests/independent_d43.py. The entire frozen parent and older ancestors are kept in prior/d42/frozen_scientific_tag_v0.1.0.zip.

## 6. Scientific boundaries and references

Orthogonal Euclidean extensions and uniform joining of weighted graphs are established mathematical techniques. These are verifiable results for one synthetic metric and one freely stipulated ideal model, not a novel universal theorem or experimental discovery of 43 physical dimensions. No measured particle frequencies, observed resonances or independent human peer review is claimed.

References: Gabriel St-Pierre, Polybrutus 42D (2026), DOI 10.5281/zenodo.24414577; frozen source github.com/Topbrutus/polybrutus-d42 v0.1.0; original seven-point configuration github.com/Topbrutus/polybrutus.
