# Independent internal AI review: PR #9, then PR #11

Reviewer: `/root/independent_math_review`  
Date: 2026-11-08 UTC  
Review type: independent internal AI mathematical review by a separate agent; **not human peer review**.

The reviewed local applications are mathematically acceptable within their stated inherited assumptions. I found **no material objection** to PR #9's four-conic projection equivalence or PR #11's scalar-chain soundness/completeness transfer and smaller-anchor application. This verdict is confined to the frozen research packets below. It does not establish the inherited global arithmetic theorem, accept the current manuscript, establish priority or optimality, or constitute the protocol's machine-readable acceptance record.

I read `AGENTS.md` and `docs/audit-history/PROTOCOL.md` before review. I reviewed #9 before #11, read the earlier arguments themselves, and checked the revised route rather than treating earlier approval or successful computation as mathematical evidence for it. I did not modify the author packets, branches, manuscript, acceptance register, or GitHub.

## Frozen scope and evidence

The review used the clean worktree `/tmp/codex-glazer389-review-3j08z564/prchain` at `e3444641dffc2d1cf5a9791111d584110e5dd111`. Its parent, PR #9, is `6fd131e7ca150d7a023bcb6ac4f1971912705fab`. Every #9 packet file in this worktree was compared byte-for-byte to that parent commit.

| Binding | SHA-256 |
| --- | --- |
| #9 `APPLICATION_CONTRACT.json` | `1ed004c5e93dd014b6a546902fb6fc03ecde61fafcbd9c2f23d8206cc83719bb` |
| #9 `PROOF.md` | `364309a61432b4de3615852175cab0faa7a3aeb9d5d251f4da521454277198d4` |
| #11 `APPLICATION_CONTRACT.json` | `a670f64ed1ff5926b0579522684870aee397a64a3b23a3413f9df0e3e13acbc9` |
| #11 `PROOF.md` | `710088f6d9517c966a55a54e9d6adb383a335d705b7b4ca5a0f1dbde16f6be4d` |
| #11 `SOURCE_BINDINGS.json` | `13ef75e44755682a5b88c56dccfbbd4dd4fae63fc091338fcf43b4f9c3c82a7e` |
| Supplying `manuscripts/quartic_v10.tex` | `9559b22cc581346da1b3150fa9b8dfb62cfb048f6aac0b866448ae7ae879ff38` |
| This review's `SOURCE_HASHES.json` | `12d7490aae5de767c5323d5055243139830010c90c70f21b1c5bcd4d91e3e8b8` |

`SOURCE_HASHES.json` inventories 52 exact source files, including both packets, their bound dependencies, and additional primary passages consulted. Declared hashes were verified, not refreshed. The primary manuscript consulted is byte-identical to `036cebe4f1a4aa7ca89820a9b48f3629b4c364d6:manuscripts/quartic_v10.tex` (Git blob `d7ac6f5e9f196b536188f8f48fe287182cbc29a7`).

The substantive review covers #9 `PROOF.md` lines 10–140 and its producer/checker/reproduction code; #11 `PROOF.md` lines 8–231 and its patch/checker/reproduction code; the contracts' nine obligations; the resulting old, factored, and scaled quadratic systems; and the actual scalar, pole, anchor, and height consumers. The finite checks do not replace the uniform arguments below.

## PR #9: four factored conics

**Verdict: acceptable as a rational projection equivalence on the retained parent domain.**

The historical argument is genuinely present in Version 13 `addition.tex`, “Factored poles and the preparation conic,” lines 595–615. Its detector variable is `F`, with semantic `H=17F`; this converts coefficients 867 and 34 to 3 and 2. I also read the older `02-squares/REPORT.md`, including its separate four-factor completeness argument and its warning about the stored scalar input's sign. These supply prior justification for the template, not approval of this particular compiled application. The scalar-preparation conic appearing in those sources is a separate transformation and is not silently included in #9.

The actual parent `builder.cjs:263` uses

```
H = E(17-T),   s2=s^2,   q2=q^2,
17 b q2 + 3H^2 - 2s2 H - s2^2 = 0.
```

The replacement uses `H=sv`, `Q2=Q^2`, and `17bQ2+3v^2-2sv-s^2=0`. For every new solution, reconstruction by `q=sQ`, `q2=s^2Q2`, `s2=s^2` makes the old second-conic and old square residuals vanish. This direction never divides by `s` and is sound at `s=0`.

Conversely, when `s!=0`, the displayed divisions provide the lift. When `s=0`, the old equations give `17bq^2+3H^2=0`; positivity of semantic `b` forces `q=H=0`. The new witnesses `v=Q=Q2=0` then work. No rational-point existence theorem, genericity condition, or inverse guard is being assumed for this zero branch. The private witnesses need not be in bijection.

The positivity premises hold before using the replaced second conics. In `detector_round7.tex`, “Nonzero domains and quadratic degree,” the positive chart and `q1 F=A U^4` force `F,q1,E>0`; the real factor products give `W0>=1`, positive norm, and `B=n^2/E>0`. `detector_round8.tex` preserves those conclusions for the promoted order-12 factor. In `geometry_round7.tex`, the actual input gives `r>0` and the retained norm tree gives `W>=1`. Thus the scalar coefficient after square absorption is `rho=42r>0`, while its physical pole input remains `rho W^2`. These two objects are correctly distinguished.

The stored affine normalization was checked rather than inferred from names. In the reviewed compiled source, detectors have `H=17E-h`; the scalar has `H=-184460384539603 E-1181808857731824 h`. The nonzero coefficient of `h` permits its reconstruction from `H=sv`. A zero semantic `H` need not mean zero stored `h`.

The full consumer scan and lifted polynomial checks passed for all four blocks. The only consumers of each block's four private slots are its `Bh.definition`, `s2.definition`, `q2.definition`, and `secondConic`. All 341 exterior rows are retained. Twelve rows change and four defining square rows disappear. The input and fixed anchor remain the same. This covers all old residuals, not just the displayed conic.

The input-fixed diagonal change and primitive nonzero rational row normalization preserve the common zero set. Over Q, the sum of squares vanishes exactly when all residuals vanish. The resulting 385-variable quartic therefore has the same input projection as the parent on its inherited domain.

Historical disposition: **prior justification found** for the factored-conic template; the present compiled application has now received this separate internal AI review. Manuscript disposition: **pending**. No global historical acceptance is carried forward by this verdict.

## PR #11: scalar chain and anchor

**Verdict: acceptable as a conditional soundness/completeness transfer; it is not a pointwise equivalence between the old and new norm witnesses.**

I read the actual round-seven norm descent and preparation argument; both prior search records; the round-five proxy proof, especially its uniform two-place argument; the round-three general pole normalization and completeness inputs; the round-four square absorption; the varying-anchor proof; and the round-eight height proof and all its consumers. The earlier searches state restricted failures, not a general circuit lower bound. I make no priority claim for the new arrangement.

### Actual chain, domain, and soundness

The constructed values are the same rational coefficients `A,B` of `f(H)` and `C,D0` of `f(Q)`, where `Q=S-P`, together with the same `Tproxy=Re(k_H w_S)` and `y=Tproxy/r^16`. The inverse powers are `r^-1,r^-3,r^-7,r^-15`. The unchanged inverse of `f(Q)_0` keeps `Q` nonidentity; the shared chart still excludes an identity `H`. These are the points consumed by the proxy, not merely related points.

The implemented chain is exactly

```
J3=D0^2+r^-15*y^2,
J2=C^2+r^-15*J3^2,
J1=B^2+r^-15*J2^2,
N=A^2/r+r^-16*J1^2,
W=1+N.
```

All divisions use the existing nonzero positive `r`. Four stored right squares and four outputs keep the cost at eight coordinates. The raw comparison replaces six rows, changes the two root rows, and preserves the other 360 rows after identifying the root output by its actual name. The change to the fixed anchor is separately declared.

Normalize `v_p(p)=1`. For every consumed prime outside `{2,3,5,7,13,17}`, odd `R=v_p(r)` is positive: a pole of the actual input X gives `v_p(r)=6v_p(X)`, which is even. This argument uses the actual polynomial beta, not an unrestricted independent beta.

The pole implication for the physical input `42rW^2` gives `v_p(W)>-R/2`; equality to zero of the odd integer `R+2v_p(W)` is impossible. Because `R>0`, the ultrametric inequality gives `v_p(N)>-R/2` even if `1+N` cancels. At the root the summand coefficient valuations are `-R,-16R`; at every inner node they are `0,-15R`. Their parities differ for odd R. Thus each summand must separately exceed the parent bound.

Independent recomputation gives the strict bounds, divided by R:

| Value | Bound |
| --- | ---: |
| A | 1/4 |
| J1 | 31/4 |
| B | 31/8 |
| J2 | 91/8 |
| C | 91/16 |
| J3 | 211/16 |
| D0 | 211/32 |
| y | 451/32 |
| Tproxy | 963/32 |

Zero leaves are covered by valuation infinity. The first four bounds put both coefficients of each reciprocal abscissa at positive valuation. At these odd unramified primes this supplies the formal-group premise at every place above p, before the proxy is invoked.

The prior proxy proof `geometry_round5.tex:98–219` explicitly allows every positive requested scalar order. It proves `k_H/k_Q=((a-1)/h)u`, with `u=1 mod p^4` at all places, and `w_S k_Q=-h_P mod p` without dividing by `h_P`. At the place above 41 where `h_P` is nonunit, integrality of `h_S` and the identity `w_S k_Q=h_S l_Q` supply the congruence. Half-trace then gives the same rational unit `U0=1 mod p`; hence `v_p(Tproxy)=v_p((a-1)/h)`.

As a supplementary exact check, the two square roots of 2 modulo 41 are 17 and 24, giving fixed `h_P=-1+(7/4)sqrt(2)` residues 39 and 0; the negative half-trace is 1. This finite calculation is not the proof of the uniform split-prime assertion.

Thus `v_p(Tproxy)>(963/32)R` gives integral valuation at least 31. The retained integer `h!=0` implies `v_p(a-1)>=31`. The same radical is consumed downstream: outside the exception set, the omitted contact `beta-2401=2754(2X+1)^2` and the infinity contact have even order, and the other three contacts are pairwise distinct modulo p. Accordingly `M_S(beta)^31 | a-1`. The packet correctly does **not** claim order `31R`.

### Completeness, all primes, and order of choices

For integral X, r is a fixed positive integer. At `p|r`, requiring each of `A,B,C,D0,y` to have valuation at least `16R+1` makes each inner node at least `17R+2`, hence at least `16R+1`. At the root, division by r still leaves `v_p(N)>=16R+2`. At a prime dividing 42 but not r, positive leaf depth makes N positive-depth; the additional 17 condition when r is a unit is harmless and attainable. Therefore W is a unit on the support of `42r`.

At primes outside that support, `v_p(42rW^2)=2v_p(W)` is even, including negative valuations. On its support the prepared value is integral. This proves square reduced denominator, rather than simply assuming it from the displayed square factor. The fixed integer-input squareclass calculation for `42r` gives squares in Q2, Q3 and Q17; multiplication by the nonzero rational square `W^2` preserves those classes. Real positivity is automatic.

The source general pole converse (`quartic_v10.tex:7704–7730`, and its completeness statement/proof at approximately 7884 onward) requires precisely positivity, square reduced denominator, and those three local squareclasses. It does **not** require the detector preparation-zero conditions `b<17` and special lower valuations. #11 retains free general-preparation witnesses, so no unproved specialization is used. The conic parametrization endpoint and subsequent square absorption remain covered by their earlier exact maps; no new private inverse is inserted.

The stronger bounds are finite and attainable in the source's quantified order: choose H deep enough for A,B; hold H fixed and choose Q deeper for C,D0 and Tproxy. For the scaled proxy the condition is `v_p(Tproxy)>=32R+1`. At exceptional primes continuity and `w_S -> 0` as `Q -> O` supply arbitrary finite depth; the soundness proxy equality at good primes is not misused there. Choose the additional finite anchor divisibility at the same stage. With S fixed, continuity in H preserves these bounds in a progression. Roots, scales and the continuity modulus therefore still precede contact-prime selection and the final `Pi^44 | h` condition. No requirement to put the same contact prime into both h and h-1 has been introduced.

### Smaller anchor and every height consumer

The uniform anchor source applies to every even exponent with unchanged packing coefficient 3. At E=2130 it gives all four labels odd, X integral at 2 and 3, and `0!=a-1` divisible by `2*3^1064`. The source proves parity from the product's leading residues before using the odd-index formal valuation formula, so this application is not circular. The actual guarded shifted point and norm `N_K(w)` are the anchor's inputs; no replacement by the scalar chain N is made.

The height input used here is exactly the parent's conditional bound

```
h(beta) <= Hheight * M_S(beta)^(577/32),
Hheight = 3*2^106*(2^32*3^9)^6*46410^18 + 128.
```

This is absolute logarithmic height, and Hheight has 665 bits. The anchor excludes X=-1/2, so beta is not 2401; positivity excludes the other forbidden finite contacts. I have not re-proved the inherited geometric/modularity/isogeny inputs that supply this height bound.

With `c*=2*3^1064` and `b*=3^1064`, the three consumer checks are valid:

1. Scalar: `1-(577/32)/31=415/992`, and `(c*)^415>(4Hheight)^992` gives `h(beta)<|a-1|/4` for every admissible index.
2. Lucas: `2-4*(577/32)/45=143/360`, and `(b*)^143>(24Hheight)^360` contradict the unchanged transfer estimate if the literal Lucas polynomial is nonzero. The function `B^(143/360)` is increasing and `B>=|a|>=b*`, so the endpoint comparison covers the entire required domain. The retained nonzero b root permits the Lucas conclusion `log B>|a|-3`.
3. Input: order 12 and `alpha<19` give the stated upper bound `(12/5)log(40Hheight)+(19/5)h(beta)`. Exact checks `40Hheight<2^670`, `100*670<b*`, and `b*>152` imply the strict contradictory bound `(487/500)|a|+19/20<|a|-3`.

These are separate checks of the actual scalar, Lucas, and input uses. The final inference from beta integral and X integral at 2,3 to X integral everywhere remains unchanged, including the leading-coefficient valuation one at 17. Completeness allows the weaker finite index divisibility for the smaller anchor.

### Conics and coefficient consumers after the changed chain

Factoring was reapplied to the newly compiled chain, rather than authorized by #9's verdict. Its actual semantic coefficients remain positive, its private consumer sets remain the four designated rows per block, and all conic lift identities replay. In this compilation the affine H constants happen to agree with #9; the verification derives them from the actual rows and does not assume that agreement.

The diagonal map uses `2130=6*355`, fixes the input, and has only nonzero rational coordinate factors and row divisors. It recovers the original semantic height scales after decoding; no square property of a rescaled stored coordinate is assumed. Full coefficient expansion agrees with the emitted quartic.

Historical disposition: **prior inputs and their relevant connecting arguments found** for norm descent, the two-place proxy, finite preparation, the uniform anchor and all height consumers. The new chain and its connections have received this review. The search does not establish absence of a similar earlier chain or historical priority. Manuscript disposition: **pending**.

## Contract obligations

I compared the contents of all nine obligations in both author contracts, not only their status fields.

| Obligation | PR #9 | PR #11 |
| --- | --- | --- |
| Source hypotheses | Positive actual b verified from retained domain. | Odd positive contacts, same proxy/pole/height hypotheses checked. |
| Constructed objects | Actual compiled H, private slots, and semantic b identified. | Actual four coefficients, proxy, chain outputs, and guard identified. |
| Index/domain coverage | Both s=0 and s!=0, all four poles, all rational parent solutions. | Every consumed prime, both places, zero leaves, every integer-input completeness choice. |
| Transition maps | Explicit lifts and nonzero affine/row normalizations. | Soundness/completeness transfer, unchanged absorption, fresh conic replay and diagonal decoding. |
| Object identity | Reconstructed original witnesses and fixed outside data. | Same H,Q,index quotient, radical, anchor norm, and three height consumers. |
| Coefficient conventions | Q, fixed nonzero constants, correct stored/semantic distinction. | Q(sqrt(2)), normalized rational valuations, exact inverse powers and logarithmic height. |
| Local conditions | Real positivity; finite local data unchanged. | Both-place formal premises, all preparation primes, split 41, same exception set. |
| Exceptional cases | Zero s, zero q/H, nonzero stored h at semantic H=0. | Zero leaves, nonidentity guards, all chart signs and pole zero branches. |
| Downstream consumption | Full private incidence scan, 341 unchanged rows, fixed input. | 360 unchanged raw rows, exact root role, every height use, current compiled conics and quartic. |

There is no newly indexed Euler system or inverse-limit construction in either local application. Treating those particular notions as inapplicable is justified here by the explicit finite witness maps and the actual scalar index/radical identification. It does not settle any inherited Kato obligation or endorse a global application by analogy.

## Finite evidence and limits

I ran #9's complete transport/coefficient reproduction with an existing freshly produced parent baseline, after the runner verified its full import/reproduction manifest and source hash. I then ran #11's full focused reproduction from its source, including fresh baseline and changed raw builds, source comparison, all compiler/gate operations, eliminations, conic transport, diagonal substitutions and coefficient checks. Both succeeded, including their negative controls.

Separately, `independent_checks.py` imports no producer/checker. It verifies source bindings and the pinned primary manuscript identity; recomputes the valuation recursion, finite preparation inequalities, the fixed split-41 residues, and all exact integer height margins; and expands every scaled residual square and compares every polynomial coefficient for both outputs. The coefficient checks found:

| Result | Variables | Residuals | Monomials | Exact maximum |
| --- | ---: | ---: | ---: | --- |
| #9 | 385 | 353 | 26,235 | `28902*3^1576` (757 digits, 2513 bits) |
| #11 | 385 | 353 | 26,200 | `28902*3^1420` (682 digits, 2266 bits) |

Both have degree four, integer content one, every variable active, and coefficient one on the fourth power of the input. These finite results do not prove the inherited arithmetic interpretation.

| Artifact | SHA-256 |
| --- | --- |
| #9 source compiled IR | `1e9071816ccb40d562545be08f21ccac76813a64796173d155d0d3ae7dbebb50` |
| #9 factored IR | `89b527cd75560efbd8b3baceb60b8bde8e64a2352334b9d479c0c53bb7c3fd4c` |
| #9 decimal table | `47da004230ff7a20c7a0824738422eb9c29c4a6e6de92455e3d956e979161ecf` |
| #11 compiled IR before factoring | `5b5c6473e17f06c160d7c54453730118d39e97d3767efe03687c8eedc2e14031` |
| #11 factored IR | `8fa75db61ea205ffcfda4dbae107f52e5940c6cb037618dd17b76f90b1c04474` |
| #11 decimal table | `c9e3e65c64c360c1cbf22c44704776c000294a1a7028e6f3f80bbe500243bdfb` |
| `pr9-replay/reproduction-receipt.json` | `b6ce7814cffb79bc4c1e2c719a2a2ba150cf3beee6645c55acbcb5e99066e0d8` |
| `pr11-replay/reproduction-receipt.json` | `aa3c348c3b096d1ff093144677f4a3b909cfdeaaf2abbeac48d85f0faa4ea0a4` |
| `INDEPENDENT_CHECKS.json` | `4d856b858039b675a1df011a989d2aed8630a256252531a91c03f5de96315b85` |

The evidence is under `/tmp/quartic-independent-review/`. This was not a new complete audit of the unchanged generic compiler or of the inherited global theorem. The checked gate/compilation certificates and independent coefficient expansion have the finite scope stated above.

## Remaining obligations

There are no identified material local defects requiring an author repair before this scoped mathematical verdict. The following limitations remain:

- The inherited global group, restricted-converse/pole realization, prime-pattern, geometry/modularity/height, quaternion and Lucas inputs retain their stated conditional status. This review supplies no global arithmetic theorem or complete formal proof.
- Neither packet is incorporated into the current manuscript or its acceptance register. Any such integration requires the actual changed manuscript passages, consumers and hashes to be reviewed and bound under the protocol. Historical acceptance cannot authorize a changed route.
- This report is an independent internal AI assessment, not human peer review. A subsequent properly bound acceptance record must accurately identify its author, reviewed scope, exact contracts, source versions and this report; it must not be manufactured on behalf of another reviewer.

No source, contract or current acceptance binding was changed during this review, so the protocol's mandatory post-change structural check was not triggered by the report files written outside the repository.
