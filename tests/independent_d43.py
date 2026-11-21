#!/usr/bin/env python3
"""Independent D43 rational-distance verifier, no import of primary Gram generator."""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
from pathlib import Path
import json,hashlib
import sympy as s
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'results'/'certificate_d43.json'
cert=json.loads(p.read_text(encoding='utf-8'))
parent_file=ROOT/'prior'/'d42'/'results'/'certificate_d42.json'
parent=json.loads(parent_file.read_text(encoding='utf-8'))
archive=ROOT/'prior'/'d42'/'frozen_scientific_tag_v0.1.0.zip'
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='3789f4a185bb50dc0d2aaa157cc370044768598abce2095c3a5e6c80eb8e9f7a'
from zipfile import ZipFile
with ZipFile(archive) as archived_parent:
    assert archived_parent.testzip() is None
    assert archived_parent.read('results/certificate_d42.json')==parent_file.read_bytes()
assert hashlib.sha256(parent_file.read_bytes()).hexdigest()=='279a43e425687b0359d61f2b104acaf2df926b04bd822f2934fb2f3016fdda20'
core=[
    (F(0),F(0),F(1)),(F(1,2),F(0),F(1,2)),
    (F(-1,4),F(3,4),F(1,2)),(F(-1,4),F(-3,4),F(1,2)),
    (F(0),F(0),F(-1)),(F(1,2),F(0),F(-1,2)),(F(-1,2),F(0),F(-1,2))
]
def d2(i,j):
    if i==j:return F(0)
    if i<7 and j<7:
        a,b,c=(core[i][k]-core[j][k] for k in range(3))
        return 3*a*a+b*b+c*c
    if 7<=i<12 and 7<=j<12:return F(5,2)
    return F(2)

N=48
pairs=list(combinations(range(N),2))
computed={(i+1,j+1):d2(i,j) for i,j in pairs}
supplied={(int(e['i']),int(e['j'])):F(e['d2']) for e in cert['labelled_squared_distances']}
assert cert['schema']=='POLYBRUTUS-D43-EXACT-CERTIFICATE-v1' and cert['status']=='PASS'
assert len(computed)==len(supplied)==1128 and computed==supplied
old={(int(e['i']),int(e['j'])):F(e['d2']) for e in parent['labelled_squared_distances']}
assert len(old)==1081 and all(computed[k]==v for k,v in old.items())
assert all(d2(i,47)==F(2) for i in range(47))
expected=Counter({F(4):6,F(7):2,F(8):1097,F(9):3,F(10):10,F(12):6,F(13):2,F(16):2})
assert Counter(4*d2(i,j) for i,j in pairs)==expected
assert sum(computed.values(),F(0))==F(9071,4)

D=s.Matrix(N,N,lambda i,j:s.Rational(d2(i,j).numerator,d2(i,j).denominator))
H=s.eye(N)-s.ones(N)/N
assert DomainMatrix.from_Matrix(-H*D*H/2).to_field().rank()==43
oldD=D[:47,:47];Ho=s.eye(47)-s.ones(47)/47
assert DomainMatrix.from_Matrix(-Ho*oldD*Ho/2).to_field().rank()==42

L=s.zeros(N)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
assert DomainMatrix.from_Matrix(L-24*s.eye(N)).to_field().rank()==11
assert DomainMatrix.from_Matrix(L-s.Rational(47,2)*s.eye(N)).to_field().rank()==44
assert cert['affine_rank']==cert['centered_gram_rank']==43
assert cert['parent_distances_preserved']==1081 and cert['new_distances']==47
# Negative tests on labelled metric and histogram-insensitive relabelling.
wrong=computed.copy();wrong[(1,48)]=F(9,4)
assert wrong!=supplied
swap=lambda i:8 if i==1 else 1 if i==8 else i
permuted={tuple(sorted((swap(i),swap(j)))):value for (i,j),value in computed.items()}
assert permuted!=computed and Counter(permuted.values())==Counter(computed.values())

print('INDEPENDENT D43 PASS: 1128/1128 rational pairs, 1081/1081 parent pairs, Gram rank 43')
print('INDEPENDENT IDEAL GRAPH PASS: eigenvalue 24 x37, eigenvalue 47/2 x4')
print('CERTIFICATE_SHA256='+hashlib.sha256(p.read_bytes()).hexdigest())
