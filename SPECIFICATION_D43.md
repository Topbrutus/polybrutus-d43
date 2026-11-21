# Polybrutus 43D — Exact rational labelled Euclidean squared-distance specification

## Parent and complete immutable lineage

Frozen scientific parent: `Topbrutus/polybrutus-d42@v0.1.0`, scientific commit `cba477c53ccdadaed888730ee0d3d25504eeff10`, DOI `10.5281/zenodo.24414577`, parent certificate SHA-256 `279a43e425687b0359d61f2b104acaf2df926b04bd822f2934fb2f3016fdda20`. It consists of 47 norm-one vertices and 1,081 labelled unordered squared pair distances.

The **full frozen original tag, including all ancestors**, is retained byte-for-byte as `prior/d42/frozen_scientific_tag_v0.1.0.zip`, SHA-256 `3789f4a185bb50dc0d2aaa157cc370044768598abce2095c3a5e6c80eb8e9f7a`, 28 archive entries, CRC `PASS`. The parent certificate copy at `prior/d42/results/certificate_d42.json` is verified byte-identical to its ZIP entry by both checking programs.

## Exact perpendicular Euclidean construction

For old norm-one vertices `p_i`, `i=1,...,47`, embed `q_i=(p_i,0)`. Adjoin new unit vertex `q48=e44`, orthogonal to every preceding point. Original squared distances remain unchanged by label, and every new squared distance satisfies `||q48-q_i||²=1+1-2<q48,q_i>=2`, so `C(48,2)=1128=1081+47` labelled unordered squared pairs result.

Seven original canonical norm-one points form a rational rank-three Gram block with inner products `3*x_i*x_j+y_i*y_j+z_i*z_j`. Five centred regular-simplex unit points form an independent rank-four block with diagonal 1 and off-diagonal `-1/4`. Thirty-six further perpendicular unit-coordinate axes are mutually orthogonal and orthogonal to both blocks. Full rational Gram `G` has diagonal 1, is PSD by explicit Gram representation and exact rank `3+4+36=43`.

Let full squared-distance matrix `D_ii=0`, `D_ij=2-2G_ij` and projector `H=I-11ᵀ/48`. The unique centered Euclidean Gram is `B=-(1/2)HDH=HGH`, of exact rational rank **43**. The original antipodal canonical pair places the origin in the affine hull. Thus the **minimum affine Euclidean dimension** for this complete labelled metric is exactly 43 (ambient storage 44 coordinates).

## Exact invariants at R=1

```text
Labelled norm-one vertices                   48
Unordered labelled squared-distance pairs  1128
Inherited D42 labels unchanged              1081/1081
New squared-distance pairs                  47 × 2
Histogram k=4*d²/R²                         4:6 7:2 8:1097 9:3 10:10 12:6 13:2 16:2
Sum of all squared distances                9071/4
Minimum affine/centered Gram rank           43
Ambient coordinate storage                  44
```

## Separately stipulated ideal weighted complete graph

Independently select scalar unit masses and symmetric edges `w_ij=R²/d_ij²`. The new point joins all 47 earlier vertices at edge weight 1/2, giving block Laplacian

```text
L43 = [ L42+I47/2       -1_47/2 ]
      [ -1_47ᵀ/2            47/2 ].
```

Uniform-join recurrence: `chi48(z)=z(z-24)chi47(z-1/2)/(z-1/2)`. With inherited original canonical seven-point nonzero graph factor `f6(z)=chi_P7(z)/z`, closed expression: `chi48(z)=z(z-24)^37(z-47/2)^4*f6(z-41/2)`. Independent exact matrix-rank calculations verify `nullity(L43-24I)=37` and `nullity(L43-(47/2)I)=4`.

These eigenspaces describe **dimensionless chosen-model modes**, not measured acoustic/physical frequencies.
