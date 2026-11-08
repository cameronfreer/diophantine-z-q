# Independent internal AI review: scalar preparation zero

Reviewer: `/root/independent_math_review`  
Date: 2026-11-08 UTC  
Review type: separate-agent internal AI mathematical review, **not human peer review**.

**Verdict: acceptable within the stated inherited assumptions; no material local objection identified.** The change from `W=1+N` and general preparation to `W=N` and preparation zero has a valid separate soundness/completeness argument for the actual order-31 chain. The Version 13 normalization, exceptional cases, finite preparation, real limit, final congruence progression and downstream objects match the sources reviewed below.

This verdict does not prove any inherited global arithmetic input, accept a current manuscript, assert priority or optimality, or create a protocol acceptance record. It follows the completed #9/#11 review at `/tmp/quartic-independent-review/REPORT.md`; it does not modify or retroactively enlarge that report. I read this revised route anew, including its additional primary sources and changed completeness requirements.

## Frozen scope

The reviewed worktree is `/tmp/codex-glazer389-review-3j08z564/pr383`, at commit `a1f9233049cc0f8aeb2a6ccd7e7b613cec3c1ec0`, parent `e3444641dffc2d1cf5a9791111d584110e5dd111`. The #9 and #11 packet files were compared byte-for-byte to the parent commit. No author source, branch, manuscript, acceptance register or GitHub object was edited by this reviewer.

| Source | SHA-256 |
| --- | --- |
| New `APPLICATION_CONTRACT.json` | `ebe792aa48c59f825d0f35835e05ba824f30c9ca411af0776cd1b2ffb38c7cc7` |
| New `PROOF.md` | `79bb5a8c5ce16c6b4559848739aeb78b7d23eb4a90f2ff0ad8ccf97a3674280a` |
| New `SOURCE_BINDINGS.json` | `f6136f6e29025d0620ece7fbae4bfd04552b1795a061fdeb04f6d3b2e5d3d45d` |
| `manuscripts/quartic_v13.tex` | `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd` |
| Version 13 `addition.tex` | `91b278b3ca1684df93e32883d8046a2accda970efc1ed9159b095183092d5a09` |
| Parent chain `PROOF.md` | `710088f6d9517c966a55a54e9d6adb383a335d705b7b4ca5a0f1dbde16f6be4d` |
| This review's `SOURCE_HASHES.json` | `66b934a8a652b0c8166da9c627bff263597400c34300ccb32437f626a277ab03` |

The 58-file source manifest freezes the packet, declared dependencies, unchanged parent packets, and protocol. Declared hashes were verified rather than updated. The substantive application sites are new `PROOF.md:7` (objects and consumers), `:55` (positivity and soundness), `:108` (finite preparation), and `:141` (simultaneous real/finite completeness), together with the actual patch, checker, reproduction driver, and generated quadratic systems.

Historical sources actually read include the Version 13 preparation-zero lemma and proof at lines 10563–10636; the real-progression lemma and proof at lines 10638–10694; the earlier scalar construction in `addition.tex:631–704`; the simultaneous-prime statement and definitions at lines 16566–16604; and the separation/deeper-primary argument at approximately lines 19705–19746. I also read the joint-chart nonzero proof, pole normalization, square absorption, and the parent chain, scalar proxy, detector and height arguments, which were already frozen in the completed #9/#11 review.

## Source theorem and exact normalization

The Version 13 predicate uses `Bsource=17b` and

```
p_source^2 = 17b(1-e_source)(1+3e_source),
h_source = e_source(17b-b^2),
17b q_source^2 = (s_source^2-Bsource*h_source)
                  (s_source^2+3 Bsource*h_source).
```

Its soundness statement excludes negative odd valuations outside `{2,3,17}` for nonzero b, including all allowed zero-witness cases. Its converse requires positive `b<17`, square reduced denominator, local squares in Q2,Q3,Q17, and valuations at least 3,1,2 respectively. The new application checks these stronger conditions; it does not invoke the general converse as permission to set a private witness to zero.

The packet's normalization is correct:

```
E=17 e_source,
Pnorm=p_source/b, Snorm=s_source/b, Qnorm=q_source/b^2.
```

Indeed `Bsource*h_source=b^2 E(17-b)`. The normalized first residual is `17/b` times the source first residual, and the normalized second residual is `1/b^4` times the source second residual. All factors are nonzero on the proved domain. Independent Laurent-polynomial expansion checked these exact identities, including the factor seventeen; no normalization is inferred from matching notation alone.

For the new physical input `b=rho W^2`, `rho=42r`, absorb W by `Pnew=W Pnorm` and `Qnew=W Qnorm`. This yields coefficient `17rho`, while `T=b` remains the physical input in `E(17-T)`. The omitted after-absorption preparation witnesses reconstruct as `u=rho W`, `v=0`, giving `u^2=rho T`. The unabsorbed prepared value is `Wu=b`, as required by preparation zero. Reverse absorption divides only by W, which is proved positive before using any pole equation.

The four conic factorizations are reapplied to the newly compiled rows. Their reverse maps do not divide by the factored variable, and their forward zero lifts use positive semantic coefficients. None of the permitted private zero branches is lost.

## Soundness on every constructed rational solution

The actual polynomial beta satisfies beta>=2401 and r>0. The retained joint chart has equations `f=g^2`, `fF=s^2`, and `h_P s k_H=1-x_P f-j_P s`. If f were zero, s would be zero and the last equation would give 0=1. Thus `g_H!=0`, and the rational coefficient `A=g_0^2+2g_1^2` is strictly positive. In the new chain `N>=A^2/r>0`, so `W=N` and physical b are nonzero and positive independently of the new pole.

At a consumed prime, odd `R_p=v_p(r)` remains positive by the actual input-polynomial argument; poles of X give even `v_p(r)=6v_p(X)`. Since 42 is a unit there, the preparation-zero obstruction applied to physical b gives `R_p+2v_p(N)>0`, hence `v_p(N)>-R_p/2` directly. The old subtraction of the outer constant is no longer used.

All four norm nodes and their opposite-parity coefficient valuations are unchanged. Their descent gives the same bounds culminating in `v_p(Tproxy)>(963/32)R_p`. Zero leaves use valuation infinity. The first four bounds establish the formal-group premises at every place above p before the proxy is used. The same guarded `H` and `R=S-P`, the same rational proxy, and the same split-41 trace argument therefore give `v_p((a-1)/h)>=31`. Integral nonzero h gives `v_p(a-1)>=31`; no assertion of order `31R_p` is needed.

Thus the exact same radical and nonzero scalar index reach the order-31 height consumer. The smaller anchor `3^2130`, its `3^1064 | a-1` condition, all three height inequalities, and the order-45/order-12 detector conclusions remain applicable. This change does not substitute the scalar norm N for the distinct field norm in the physical anchor.

## Finite preparation and squareclasses

For an integer input, r and rho are fixed positive integers. At p|r, the chosen leaf depths `>=16R_p+1` give inner-node depths `>=17R_p+2` and root depth `v_p(N)>=16R_p+2`. At primes dividing 42 but not r, and at 17 when r is a unit, positive depths of all five leaves give `v_p(N)>=2`. These conditions follow by actual substitution into the new chain, rather than from the former unit argument for `1+N`.

Complete residue computations for the integer polynomial independently confirm

```
rho = 4 mod 32,  rho = 81 mod 243,  rho = 13 mod 17.
```

Thus rho has valuation 2 and square unit part at 2, valuation 4 and square unit part at 3, and square unit residue 13=8^2 at 17. Multiplication by `N^2` preserves those local squareclasses. The imposed depths give the converse's required lower valuations (in fact stronger ones).

At primes dividing rho the new N is integral. Outside that support, `v_p(b)=2v_p(N)` is even, even when negative. Consequently the reduced denominator is a square. Real positivity was proved separately. The argument therefore checks every finite hypothesis of the preparation-zero converse for the actual physical b.

The finite preparation is possible in the stated order. Formal neighborhoods at any fixed finite set have finite-index preimages in the integer orbit; this includes exceptional primes without assuming good reduction there. Choose H first for its two coefficients. With H fixed, the scalar point can be chosen deeper for the other coefficients and Tproxy. `w_S -> 0` as `R -> O` makes the proxy arbitrarily small at those places despite a fixed denominator in k_H. The required proxy depth `>=32R_p+1` is finite. Subsequent continuity in H preserves all bounds on a sufficiently divisible fixed progression.

## Actual real limit and simultaneous final choice

The prior Version 13 scalar expression is different from the order-31 chain. Its earlier acceptance would not justify simply dropping the outer constant here. The new proof recomputes the relevant limit correctly.

For fixed nonidentity H0, as R tends to the identities in both real embeddings, `C,D0,y` tend to zero, then `J3,J2` tend to zero, but **J1 tends to B^2**. Therefore

```
N -> (A^2+r^-15 B^4)/r,
b -> (42/r)(A^2+r^-15 B^4)^2.
```

Independent symbolic expansion confirms this limit. As H0 tends to both real identities, its reciprocal coefficients A,B tend to zero, so that limit can be made arbitrarily small. First choose H0 to make the limit less than 17/8; then an actual finite nonzero R makes b<17/4. This is a genuine two-stage choice, not an invocation of an unrelated point at the limit. The retained guard excludes R=O; arbitrarily large positive nonzero indices suffice.

The real-progression source applies to the closure G of the actual simultaneous orbit. Its identity component G0 can be a proper subtorus; no independence of the two real angles is assumed. Multiplication by an integer divisible by `m0=|G/G0|` maps G onto G0. A progression with both residue and modulus divisible by m0 has dense positive tail in G0. Thus integer multiples meeting any prescribed finite congruence conditions can also approach both real identities at the initial H0 and R choices.

After R is fixed, continuity supplies a nonempty open neighborhood U of H0 in G0 with `0<b(H,R)<17`. Enlarging the finite continuity modulus does not affect this real neighborhood. The remaining labels, roots and scales are chosen before contact primes. Each retained comparison pole set is an inverse image of a finite set under a nonzero multiplication/translation on a real factor. The projections of G0 onto the identity circles are surjective, so each such set has Haar measure zero in G0 and the finite union cannot cover U. There is a nonempty smaller open set with compact closure in U avoiding all poles. All real comparison bounds can consequently be fixed before the later prime/progression moduli.

I checked the enlarged-modulus application against the actual simultaneous-prime theorem, not only the quoted gcd conclusions. The data supplied have distinct integer contact forms after clearing denominators and merging repetitions while retaining incidences; the distinct scale-one contacts ensure k>=2. The odd squarefree M is the odd support of the fixed L0 with seven removed. The source separately treats seven by its ray condition and two by its modulo-16 condition. The theorem allows the required fixed q, M, real bound and cutoff; none grows during the asymptotic invocation. The inherited separated-prime argument applies to these fixed forms.

The theorem gives pairwise norm coprimalities and `v2(d_-)=6`, `v2(d_+)=2`. For `M_±=lcm(d_±/4)`, this means `v2(M_-)=4`, M+ odd, and no odd common divisor. Because the odd support of L0 is excluded from these orders and `64|L0`, the stated gcds are indeed `gcd(M_-,L0)=16`, `gcd(M_+,L0)=1`. The cutoff and separation give `gcd(Pi,M_+ L0)=1`. Since `64|h0`, the three conditions

```
h=0 mod Pi^44 M_-,   h=1 mod M_+,   h=h0 mod L0
```

are compatible. The resulting progression has residue and modulus divisible by m0 because it refines the last congruence. Its dense positive tail meets the chosen real neighborhood. This produces an **actual final H** with the scalar finite conditions, b<17, all comparison bounds, primary depth 45 and the required opposite-place conditions simultaneously. No contact prime was selected before the data it must avoid were fixed, and no post-selection bound was treated as uniform in an unknown modulus.

The specialized pole converse now applies to the same b used by the generated equations. Its witnesses can be normalized, square-absorbed with W=N, and factored as above. This completes the local completeness transfer, conditional on the inherited arithmetic and prime-existence inputs.

## Circuit consumers and finite evidence

The raw comparison preserves coordinate allocation, guards and the fixed anchor. It changes only `scalar.preparationT.definition`, `scalar.Bh.definition`, and `scalar.secondConic`, and deletes only `scalar.preparationConic`. The remaining chain and outside rows are unchanged. The two old unprotected base slots, `scalar.preparationU` (52) and `scalar.preparationV` (53), occur in no residual.

The compiled-to-active omission was checked directly: every residual is unchanged and exactly those unused slots are omitted. Forgetting them and extending with zeros is a valid algebraic projection equivalence for the patched system. That zero extension is distinct from reconstructing the semantic original pole witness `u=rho N`; it does not claim equivalence with the parent's old physical input `rho(1+N)^2`.

A fresh full replay under this review directory passed source comparison, the compiler/gate replay, omission bridge and its negative control, elimination, actual conic transport, diagonal substitutions, and all coefficient checks. A separate script imports no producer/checker and verifies the normalization identities, the exact chain limit, the residue classes, unused-coordinate incidence, and a new complete expansion of every scaled residual square.

The measured output is 383 variables, 352 residuals, 26,019 monomials, degree four, content one, all variables active, input fourth-power coefficient one, and exact maximum `28902*3^1420` (682 digits, 2266 bits).

| Evidence | SHA-256 |
| --- | --- |
| Compiled IR before factoring | `a811164315c7ad4963b581759def450c1773e8e208bf740b5e18e31adf36d4b2` |
| Final polynomial JSON | `68d5aa4f1e71f761f3eeabfc5b949e1b24af434bf0479f6aa9102fce4e99b62e` |
| Decimal table | `8faea54ef4a9d8cf155205a50c956df20d36e3eec4183b50b39b2c0b87183b0d` |
| Fresh replay receipt | `5d894a50db9ba12b218dc36ee34e0a839eeffbab4163ac33cc4aa5b09abc4675` |
| `INDEPENDENT_CHECKS.json` | `6b5634154d9b43d90bca74069e795c251ae64c3f8d79bdcb13aa85c1d7093a12` |

These are finite checks. They do not prove the density argument, the simultaneous-prime theorem or other inherited global arithmetic inputs.

## Nine obligations and remaining scope

All nine contract obligations were read and compared to their sources and consumers:

1. Source hypotheses: every specialized pole hypothesis, including the real bound, was checked.
2. Constructed objects: rho, physical b, prepared T, the chain, and the actual scalar points are correctly distinguished.
3. Domain coverage: arbitrary rational solutions for soundness and every integer input for completeness are covered; every retained prime and final congruence is accounted for.
4. Transition maps: source normalization, square absorption, witness reconstruction, factoring and free omission have explicit justified maps.
5. Object identity: the actual final H in the compatible progression, fixed R, scalar proxy, physical pole input and downstream scalar index agree.
6. Conventions: the same field, rational valuations, chain powers, fixed anchor and input-fixed diagonal decoding are retained.
7. Local conditions: the stronger finite preparation, both formal places, squareclasses and all real requirements are checked simultaneously.
8. Exceptional cases: zero leaves and pole witnesses, nonunit fixed coordinate at 41, and nonidentity guards remain covered.
9. Consumers: order 31, depth 45, input comparison order 12, all height inequalities, unchanged exterior equations and generated quartic are preserved in their actual uses.

No new Euler-system index domain or inverse limit is involved. The finite progression and actual final-point identification are the relevant domain/object checks here; this assessment does not settle inherited Kato or other global obligations.

Historical disposition: **prior preparation-zero and real/finite arguments found** in Version 13. The new chain needed the different limit, stronger finite depths and current prime/anchor connections checked here. There is no priority claim and no inference that every earlier reviewer independently verified these points. Manuscript disposition: **pending**.

There is no identified material local defect requiring an author repair. The inherited global arithmetic remains conditional; current-manuscript integration and correctly authored exact-source acceptance remain separate; this is internal AI review, not human peer review or complete formal verification. The review artifacts were written outside the repository and did not alter protocol-bound sources or acceptance records.
