# Independent review: scalar row reduction, first layer

Reviewer: `/root/independent_math_review`. Date: **2026-11-09 UTC**.
Review type: **independent internal AI review**, not human peer review.
I did not author the proposed A/tri construction, edit its packet, or create
repository acceptance-register or App records. This review covers only the
first layer of the proposed sequence.

**Decision: accept the conditional local rational input-projection equivalence,
the specified 379-variable/425-digit construction, and its declared v1.2
handoff scope at commit `ce15e8ece219a2bb000075a5a79f6ffd9bea6dfd`.**
No material local objection remains. No author correction was required during
this review. Acceptance is conditional on the same inherited arithmetic inputs
as the parent; it does not accept a new global theorem, current-manuscript
incorporation, optimality, public readback or designated App authorization.

## Frozen sources

The worktree was `/tmp/codex-glazer389-review-3j08z564/row379`. The parent is
the previously reviewed mixed-normalization layer at
`eb00b7c9c5be2e8666c0403c750c6c780cf78563`. The new packet is
`research/scalar-row-reduction/`.

| Artifact | SHA-256 |
| --- | --- |
| `PROOF.md` | `b64c429a02bdb083182ede492cfb67f902e487585f5eca4eeb28dd353ffc320e` |
| `APPLICATION_CONTRACT.json` | `b6bc8327a0b30c275b9204f34966ef3ee9b8541abf91ad4d033930e664d63997` |
| `SOURCE_BINDINGS.json` | `18a701c1d456e6aa9893b6d26be3f30ef12264f267b26de457ffb4bbac7edc7a` |
| `DIAGONAL_WEIGHTS.json` | `c42701d73785edc50c2e6622b2dc62af7e2bc05a95efff7d413dde2e403a1e32` |
| Generated builder | `5520df38cfdebded9f4aadede97a77d20612aa3a9abfc057cd77eba6515c4290` |
| Raw translated IR | `40d54012e608282410c90e850637f71359c73321fc9762f64a7086347601fdc7` |
| Final pre-diagonal integer IR | `dbe3c0f7fdf24efb61c7ac05ca9f553ebdec9d518970b2e657d49eda3eb59fc7` |
| Balanced polynomial JSON | `08a10683e1f9e8897cc6bbc5c293895287b93c6251ac62033044e12a330e7b38` |
| Complete decimal table | `50167c7f2873a2022c5c1c7dbff735eec097e9c7f60c6624c7abb0ff34cd37ec` |

I checked all **324** bound files against immutable Git blobs and worktree
bytes. `SOURCE_HASHES.json` records them and the complete incremental path
list. That diff contains only the new packet, its historical research archive
and the new scalar-row workflow. `SOURCE_EXCERPTS.json` records original-byte
passage hashes, whole-source hashes and locators. No source was normalized
merely to make its hash match.

The parent review archived at commit
`563178a040c7e075fed14e6b913ea8e6cb09440d`, directory
`research/independent-local-reviews/2026-11-09/mixed/`, matches my original
report, findings, decision and archive manifest byte for byte. It supplies
earlier reviewed context, not acceptance of this new map.

## Earlier arguments and actual domain

I read `AGENTS.md`, the audit-history protocol, the nine-obligation contract,
the new proof and implementation, and the actual supplying arguments:

- Round-five `geometry_round5.tex`: the fused subtraction chart, its retained
  nonzero-real-f guard, and the two-place scalar proxy, including the place
  above 41. The proxy is `Re(k_H*w)`, with `w=h_S*tau`; it is not the proposed
  exploratory `Re(k_H*tau)`.
- `scalar-preparation-zero/PROOF.md`: positivity of r and N, physical pole
  input `42rN^2`, square absorption to conic coefficient `42r`, the old
  normalized witness conventions, and permitted zero witness cases.
- `factored-pole-reduction/PROOF.md` and its earlier Version 13 factored-pole
  passage: both conic maps and the positive-input zero branch. Its older
  affine constants are not copied into this changed application.
- The parent's mixed-normalization and height proofs: the actual detector
  inputs and orders, scalar order 31, anchor exponent 2010 and affected
  consumers. Their arithmetic dependencies remain conditional.
- Original Opus A/tri notes and scripts, the composed-map notes, the six
  exploratory direction notes, and the Codex vetting/correction record.

The current point chart keeps `x_S=h_S^2`, the same totally positive
`F=x_P*x_S+D`, and the same equation for `w`. The shifted guard excludes
`Q=S-P=O`; the previously permitted `S=-P`, sign and tangent cases are not
restricted. The arithmetic domain gives
`beta=2401+2754(2X+1)^2>=2401`, `r=beta(beta-1)(32beta+343)>0` and `N>0`.
The proof of N positivity uses the unchanged nonidentity H chart and the
positive norm tree before any pole witness is chosen. There is no circular
positivity deduction from the changed pole rows.

This layer introduces no new approximation or existence choice. Its source
maps fix the actual points, indices, w, f(Q), scalar proxy, norm-tree output,
three detector inputs, sixteen detector functions and anchor parameter.
Thus the unchanged primary and alternate identity branches, split/inert
places, split-41 proxy, simultaneous scalar preparation and all height
consumers continue to concern the same objects. After the final diagonal
map, those objects are recovered through the inverse coordinate map; one
does not apply the old local arithmetic interpretation directly to newly
scaled numerical coordinates.

## A: exact constant row operations

Replacing x_S by h_S squared in only the numerator of the w equation is
valid because both defining rows for `x_S=h_S^2` remain. The denominator
F remains unchanged. I decoded the actual raw residuals over rational named
coordinates and solved for the constant combinations from their coefficient
differences. They are exactly

```
u0_new-u0_old = -(39/8)*g0 + 18*g1,
u1_new-u1_old =  (9/2)*g0 - (39/4)*g1.
```

Here g0,g1 are the actual raw `S.chart.x.0/1.definition` rows. Retaining
them makes the row operation invertible over Q. The identity coordinate
map works in both directions. There is no division by a variable or new
choice of a square root. The different constants in older integer-scaled
exploratory rows are a normalization issue; I checked the constants against
the actual raw source rather than interchanging those displays. The current
claim is over Q, as required by the Diophantine representation.

## tri: the normalization and both witness maps

The old private coordinates Z and T0 are respectively
`scalar.W2.quadratic` and `scalar.preparationT.quadratic`. T0 is a normalized
auxiliary; it is not the physical pole input. The old Bh slot is also a
normalized auxiliary. This distinction is essential.

I derived r from the actual `r*ri-1` residual, L from the coefficient of Z
in the old preparation row, and k from the old Bh row. These give

```
r*ri=1,  Z=N^2,  T0=L*Z,  B_old=e*(Z+k*T0),
k=521079743268/81331739215,
mu=184460384539620,
mu*(1+k*L)=42*r.
```

The last equality is an exact identity in the actual inputProduct/rPair1/
rThree coordinates, not an equality only at sampled inputs. I determined
mu from the constant coefficients in this encoding, then verified every
nonconstant coefficient as well.

The new equations are `ri*T=42*N^2` and `B_new=e*T`. Because `r*ri=1`,
they force the physical quantity `T=42rN^2`. The polynomial identity

```
r*(ri*T-42*N^2)-T*(r*ri-1)=T-42*r*N^2
```

establishes this without introducing an inverse of N, e or a conic witness.
The source maps are

```
old -> new: T=42*r*Z, B_new=mu*B_old;
new -> old: Z=N^2, T0=L*N^2, B_old=B_new/mu.
```

My independent check verifies their complete defining-row identities. For
example the new T row under the forward map is
`42*Z*(r*ri-1)+42*(Z-N^2)`. The new Bh row becomes
`mu*(old Bh row)+mu*k*e*(T0-LZ)`. In reverse, the old Z and T0 rows vanish
identically, and the old Bh row is
`(new Bh row + e*(T-42rN^2))/mu`. The second-conic residuals agree exactly
under `B_new=mu*B_old`; the coefficients `3mu^2,2mu,-102mu` become
`3,2,-102`. Omitting that scale would not give the claimed transport.

These maps are inverse on source solutions and fix every outside coordinate.
They remain algebraically valid when N=0 or e=0, even though the arithmetic
domain independently excludes N=0. The only variable inverse used is the
already retained r inverse; mu is a fixed nonzero rational. No conic zero
witness or allowed sign branch is removed.

I scanned every raw residual for each private coordinate. The old Z occurs
only in its square definition, preparation definition and Bh definition;
T0 occurs only in preparation and Bh; Bh only in its definition and the
second conic. The new T occurs only in preparation and Bh, and the new Bh
has the same two consumers. Exactly five common rows change, the Z square
row disappears, and **358** other raw rows are identical by coordinate name.
The actual inverse guards are identical. All test, shifted-chart and proxy
aliases are identical. Only the three private common semantic aliases
`scalar.preparationT`, `scalar.Bh` and `scalar.Bsemantic` change their formal
expressions, precisely as accounted for by the maps. Thus formal alias
equality is not incorrectly used for different stored normalizations.

A and tri have disjoint replaced rows and compatible common coordinates,
so their composition preserves the same rational input projection. This is
an algebraic equivalence layer, unlike the parent's changed detector
normalization, which needed a fresh arithmetic completeness argument.

## Compilation, actual conics and zero branches

The full compiler, gate and elimination checks were replayed at the changed
source. The same unused preparationU/preparationV slots have no consumers;
their omission has a free extension. The four conic transports were applied
anew to the resulting actual normalization.

For each compiled conic I independently derived H and its positive coefficient
b from the actual quadratic polynomial, checked

```
17*b*q2 + 3*H^2 - 2*s2*H - s2^2,
```

and verified every private consumer and every lifted residual. In this
candidate all four affine encodings are `H=17*normalized_e-Bh.quadratic`.
The scalar encoding therefore differs from earlier packets' stored constants;
the earlier proof is used as a template with checked inputs, not as a license
to reuse its old normalization.

The new equations have `H=s*v`, `Q2=Q^2` and
`17*b*Q2+3*v^2-2*s*v-s^2=0`. For an old solution with s nonzero, set
`v=H/s`, `Q=q/s`, `Q2=q2/s^2`. At s=0, the old square rows and conic give
`17*b*q^2+3*H^2=0`. Since b>0, H=q=0, so `v=Q=Q2=0` supplies a new
solution. In the reverse direction, `H=s*v`, `q=s*Q`, `q2=s^2*Q2`,
`s2=s^2` work for every s; the old conic is s squared times the new one.
There is no cancellation at zero. The affine Bh coordinate is reconstructed
using its nonzero constant coefficient.

The three detector b values and the scalar conic coefficient `b=42r>0`
are unchanged. The scalar physical input remains `42rN^2`. The new T and
Bh maps preserve both objects, rather than conflating them. Every exterior
compiled row is unchanged by the four transports, and all four discarded
square slots have exactly the claimed private consumers. These facts justify
composition on the full inherited domain.

## Diagonal map and complete coefficient check

The supplied 35-coordinate map has integer exponents `(a_i,b_i)` specifying
`old_z_i=3^a_i*2^b_i*new_z_i`; unlisted exponents are zero. I verified its
actual coordinate names, all factors and the fixed input. Negative exponents
produce nonzero rational factors and hence no extra domain restriction.
There are 34 nonzero ternary exponents and 9 nonzero dyadic exponents, with
overlap giving 35 affected coordinates. This is a specified map; no LP
solver, floating-point optimum or coefficient-minimality claim is required.

After substitution at `S=3^2010`, I independently compared every resulting
rational quadratic row with its primitive integer row by a nonzero coefficient
ratio and checked integer primitivity. I expanded all 348 squared rows using
unordered term pairs with doubled cross terms, compared the complete sparse
polynomial, and independently parsed every decimal-table coefficient. The
script imports no author producer or checker. No sampled evaluation replaces
these polynomial identities.

The independently reproduced result is:

| Property | Result |
| --- | ---: |
| Variables, including the unchanged input | 379 |
| Quadratic residuals | 348 |
| Quartic monomials | 26,021 |
| Degree | 4 |
| Integer content | 1 |
| Input fourth-power coefficient | 1 |
| Maximum coefficient digits / bits | 425 / 1410 |
| Active variables | All 379 |

The exact maximum integer is recorded in `INDEPENDENT_CHECKS.json`, and the
complete decimal table is bound above. Each diagonal factor and row divisor
is a nonzero rational. Over Q, the sum of squared rows vanishes exactly when
every row vanishes, so this stage preserves the parent's input projection.

I ran the authorized reproduction command in a fresh output directory:

```
python3 -B research/scalar-row-reduction/reproduce.py --output /tmp/quartic-row379-review/replay
```

Its comparison baseline matches my earlier independent #17 raw replay byte
for byte. Source/row mutation checks, gate/compiler checks, omission, all four
conic checks and complete diagonal/table checks passed. Reviewer-owned
`independent_checks.py` separately derives the identities and measurements
described above. The final audit-history self-test also passed; its structural
and negative-control results are not mathematical proof acceptance.

## Nine application obligations

All nine obligations are addressed within this conditional local scope:

| Obligation | Required versus constructed input and checked consumer |
| --- | --- |
| Source hypotheses | Rational source equations on the retained positive chart/pole domain, including r*ri=1; the maps preserve that domain and every outside object. |
| Constructed objects | Actual w, physical42rN², conic coefficient42r, normalized T0 and Bh are distinguished. Derived row identities identify the replacements. |
| Domain/index coverage | Both maps cover every rational source solution and permitted sign/zero witness. No prime, index or limiting-family restriction changes. |
| Transition maps | Both directions and mu are explicit; forward/reverse polynomial identities and the full second conic agree at the actual normalization. |
| Consumed object identity | w, f(Q), Re(k_H*w), N, physical pole inputs and all detector functions retain their identities; every private consumer was scanned. |
| Conventions | Same Q coefficients, K basis1,sqrt2, S=3^2010 and raw row conventions. The input-fixed two-prime factors and row divisors are nonzero rationals. |
| Local conditions | Same real/finite scalar and detector conditions; positive conic coefficients justify the zero branch. No new simultaneous choice is needed. |
| Exceptional cases | r=0 remains excluded by its inverse; N/e zero cause no map failure; Q=O guard, S=-P, chart signs and s=0 conic branches remain covered. |
| Downstream consumers | Composition preserves the parent rational input projection and its same arithmetic orders/height consumers. Complete finite coefficients and stated size are independently checked. |

## Historical archive, corrections and v1.2 scope

`prior-investigation/INVENTORY.json` has SHA-256
`41bc1810e952fff5fbe86c640fcf97f977fa5c3050fa74bab0dff3d7e4daf767`.
I checked **all 208 entries** against the actual original files: 199 Opus
research files under the original exploration directory and 9 original Codex
vetting files. Their bytes, including original whitespace, agree exactly.
`ARCHIVE_PROVENANCE.json` records each original path and hash. I also read
the six original direction notes and the full vetting correction record.

The archive scope is adequately disclosed: original notes, selected scripts,
search results and measured receipts are retained; large old build trees,
binaries and full old generated tables are excluded. Historical scripts keep
their original local paths and are not represented as portable reproduction
entry points. The current candidate has its own source-driven runner using
standard-library Python and Node. This byte-preservation and coverage review
does not certify every exploratory claim in the archive.

In particular the handoff and findings correctly retain, rather than silently
rewrite, the old false W/trace/pole-invariance assertion and the overbroad
high-order-chain claim. The correction record distinguishes a changed detector
route from the present exact scalar maps and limits search bounds to their
models. The original composed A/tri evidence already records the Bh rescaling;
the current proof checks it at #17's actual normalization. Credit to the
Opus discoveries and Codex integration is consistent with these sources.

Tau's trace-unit/sign, guard and anchor obligations, B/C's changed three-adic
predicates, dropped-test soundness, other speculative eliminations and future
detector/scalar-order layers remain outside this acceptance. A local tau sign
diagnostic is not presented as a global counterexample. An unsuccessful tree
transfer to this package's objects is not treated as an established Version13
defect. Neither the old fixed-row LP bound nor later restricted searches are
accepted here as universal optima. Finite measurement receipts for these
unproved candidates do not become arithmetic acceptance by being archived.

I accept the declared **conditional non-release** scope under v1.2. The result
does not cross the next below-300 publication threshold. It claims no new
current edition or replacement current artifact; the actual diff leaves
README, Version13 TeX/PDF, current release surfaces, existing packets and the
acceptance register unchanged. Leaving them unchanged is justified for these
specific claims, while the new proof, source/application inventory, findings,
archive and handoff receive their own review. This is not a general metadata
exemption from release duties.

The original global arithmetic/published-source closure, Kato/current-source
integration, current-manuscript incorporation and historical stdout root-cause
limitations remain open. Public destination/CI/table readback and the designated
App check are separate duties; I make no independent public readback claim.
The source-bound local decision and selected-files archive supplied with this
report may be cited in a subsequent appropriate review record. They do not
authorize acceptance of a changed source or the next two proposed layers.
