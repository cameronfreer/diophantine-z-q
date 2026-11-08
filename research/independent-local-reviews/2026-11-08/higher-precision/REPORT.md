# Independent internal AI review: higher detector precision

Reviewer: `/root/independent_math_review`  
Date: 2026-11-08 UTC  
Review type: independent internal AI mathematical review by a separate agent; **not human peer review**.

**Verdict: acceptable within the stated inherited assumptions, for both implemented orders 46 and 47; no material local objection identified.** The unchanged G12 polynomial has the claimed uniform relative precision 51 on the stated local domain. The two new weight circuits realize their advertised orders, and the comparison, completeness and height arguments support anchor `3^2016` with the measured coefficient bounds.

This verdict is limited to the frozen research alternative and its local applications. It does not establish the inherited global arithmetic theorem, accept a current manuscript, assert circuit/anchor optimality or historical priority, or create a protocol acceptance record. The previous #9/#11 and preparation-zero reports remain separate and unchanged.

## Exact snapshot and scope

The final reviewed revision is `bc51100fd3ada82df0dac55d6f1d235219430c74`, in `/tmp/codex-glazer389-review-3j08z564/precision`, above the initial packet commit `4c669cc` and the preparation-zero parent `a1f9233049cc0f8aeb2a6ccd7e7b613cec3c1ec0`.

| Binding | SHA-256 |
| --- | --- |
| `APPLICATION_CONTRACT.json` | `f8f5cbd6042a86ec244e0ca7c75d62df209e238283268358ec8453b9855ee77d` |
| `PROOF.md` | `e6a825c3b85a9c56a6a2678ad0fa411ecedec53a005a0464efb45677f056054c` |
| `SOURCE_BINDINGS.json` | `f129baf00c40b37833e5e94173cce93c9f59ce768981e071347a19592860b931` |
| `manuscripts/quartic_v10.tex` | `9559b22cc581346da1b3150fa9b8dfb62cfb048f6aac0b866448ae7ae879ff38` |
| `manuscripts/quartic_v13.tex` | `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd` |
| This review's `SOURCE_HASHES.json` | `18ea20e6d09679155b3ebfeecf896743f74ba9f6bd9ae27071b6eadc45d03535` |

The 60-file manifest inventories the exact packet and dependencies. All author-declared source hashes were checked. The final clarification changes only the proof's primary-identity paragraph, its matching contract obligation, and hashes; I inspected that complete diff and acknowledge the revised binding. Computational sources and outputs are byte-identical to the version used for the fresh replays.

I read `AGENTS.md` and the audit protocol before classifying the application. Relevant earlier arguments read directly include:

- `quartic_v10.tex:9199–9258`: the actual recurrence, invariant-differential identity, factorial denominator bound and its original large-prime conclusion.
- `proofs/prior/round5/geometry_round5.tex:1–95`: actual G12 circuit, real nonvanishing, and the extension of the coefficient argument to the present exception set.
- `proofs/prior/round5/arithmetic_round5.tex:145–182`: G2 order 12, small-prime conventions and comparison requirements.
- `proofs/prior/round6/arithmetic_round6.tex:173–200`: the earlier weaker order-45 application.
- `quartic_v13.tex:19689–19746`: actual ratios `u_i/h`, `(u_i-n_i)/(h-1)`, integrality-first comparison, separation and deeper-primary CRT.
- The one-place proof and definitions at `quartic_v13.tex:11031` onward, with `detector_round7.tex` supplying the current contact-unit normalization and all local/real completeness estimates.
- The actual scalar chain, preparation-zero, varying-anchor and round-eight height arguments, already frozen and reviewed in the preceding reports, with their dependency effects rechecked here.

Current application/consumer sites are `PROOF.md:8` (logarithm), `:59` (circuits), `:91` (local comparisons), `:133` (completeness), `:169` (all height consumers), and `:200` (measured alternatives), plus the actual experiment/checker implementations and generated IRs. No author source, branch, manuscript, acceptance register or GitHub object was edited by this reviewer.

## Infinite-tail coverage and the precision-52 obstruction

The application correctly distinguishes the source's formal-series proof from its original large-prime theorem statement. It does not simply remove the original cutoff from that theorem. The recurrence and invariant-differential calculation are identities over Q; the denominator estimate holds for every prime. The current field is `K=Q(sqrt(2))`, the normalized valuations have `v(p)=1`, and every admitted place is unramified. The parameter `D=11-6sqrt(2)` has norm 49, so it is a unit on this domain. The good formal branch has `v(w)=4r`, with integral `r=v(z)>=1`.

Independent exact computation gives

```
a13 = -54756974/6936596275,
6936596275 = 5^2 * 7 * 17 * 29 * 37 * 41 * 53.
```

All admitted denominator primes occur to exponent one; hence `v(a13)>=-1`, and `v(a13*w^13)>=52r-1>=51r`.

For every omitted index j>=14, the factorial estimate and integrality of valuations give

```
v(a_j*w^j) >= 4jr - floor((4j+1)/(p-1))
            >= 4jr - floor((4j+1)/10).
```

At r=1, the right side is 51 for j=14. Increasing j by one increases it by at least three, since the floor argument rises by 4/10. For larger r the difference from `51r` increases by `(4j-51)(r-1)>=0`. This proves the bound for **all** j>=14, not a sampled or truncated coefficient range. The bounds tend to infinity. Adding the separate j=13 estimate controls the complete infinite tail.

Multiplication by z gives absolute error at least 52r. The formal logarithm has valuation r: the unchanged weak estimate `log_E/z in 1+p^(4r)O` follows from the same first-term and factorial argument, or from the applicable formal isometry. Dividing by that nonzero logarithm gives relative precision at least 51r. There is no use of a logarithm quotient at an identity point in this deduction.

At the admitted prime 53 and r=1, the first omitted term has valuation exactly 51, since 53 divides the reduced denominator of a13 exactly once. For every j>=14, the sharper bound `4j-floor((4j+1)/52)` starts at 55 and increases by at least three. Therefore later terms cannot cancel the leading omitted term. The relative error has valuation exactly 51. A depth-one local formal parameter exists on this good model, so uniform precision 52 is unavailable on the stated local domain. This is not a counterexample to a particular global witness construction and is not a claim about all conceivable approximants.

The real polynomial is unchanged: all nonconstant coefficients are negative, and the previously checked positive value G12(1) supplies the same lower bound on the real chart. No new logarithm denominator exclusion, chart branch or exceptional prime is introduced. The input G2 retains its separately justified precision 12.

## Exact weight circuits and the objects they feed

The actual retained data are positive `q1`, `E=q1*delta^2=1/R`, and `mixedHigh=E^22*q1^24`. The two circuits give:

- Order 46: `V=mixedHigh*delta`, then `q46=V^2/q1=E^45*q1^46`.
- Order 47: `V=mixedHigh*E`, then `q47=V^2/q1=E^46*q1^47`.

Equivalently, using `(q1,delta)` exponents, the final weights are `(91,90)` and `(93,92)`, exactly `e^(2m-1)/delta` with `e=q1*delta`. Independent exponent arithmetic checked both identities. No scalar from `delta^2=E/q1` has been lost. All divisions are by the already positive q1. Each gate is quadratic and uniquely determines its output on the retained domain.

The original semantic pole quantity remains `B=R/Tr(W^-1)^2`; the weight change does not silently replace R. All sixteen underlying field test values and the two order-12/eight order-one tests are retained. The six high tests are the primary inverse root, the three long-log cross tests, `L1-beta`, and the literal Lucas residual. Their order is changed consistently to the selected m.

The source comparison checks every raw residual after identifying the renamed high-order blocks. Exactly three last-weight equations change and three lift equations are added. Every other raw row and guard is unchanged; the anchor value is separately checked. The existing q1 square and cube still have consumers in the order-one block, so the measured three-coordinate cost is not based on an unverified deletion.

## Two-anchor soundness, all identity branches and conjugation

The one-place detector proof accepts arbitrary positive integral orders, and its actual valuation proof extends to the current unramified domain with the existing pole obstruction. The contact-unit normalization preserves the test valuations at all consumed contacts. It supplies a single place per contact at which every requested order holds. The primary inverse-root test gives depth at least m for H. The other primary tests and conjugated alternate tests put their respective points into the needed formal groups, at the primary and conjugate places.

For a nonidentity primary numerator, the implemented primary ratio is the raw parameter ratio `L_i=z(U_i)/z(H)`; the alternate one is the conjugated truncated logarithm ratio. The exact full ratios are

```
r_i=u_i/h,   r_i'=(u_i-n_i)/(h-1).
```

The guarded integers h and h-1 are nonzero. At least one is a p-unit, so at least one full ratio is integral. Weak unit estimates preserve the respective valuations before any deep primary numerator hypothesis is used. The cross test then transfers integrality to the other displayed ratio. Only after this step does primary ratio integrality give numerator depth at least the denominator depth m.

Both primary unit corrections now have precision at least 4m. The alternate denominator and the three Lucas numerators have precision at least 51, which exceeds m=46,47. Their full ratios are integral, so relative errors become absolute errors. Thus `L_i=r_i=r_i' mod p^m` for each Lucas label. Multiplying by h and h-1 and subtracting gives `L_i=n_i mod p^m`. The input numerator uses G2 and its order-12 cross test, yielding the corresponding conclusion modulo p^12. The strengthened `L1-beta` test then still supplies the same order-12 input numerator divisibility.

I explicitly checked the identity case for **every** primary U_i. The original draft mentioned the input identity branch only. The final revised proof now records the complete argument: when U_i=O, its raw chart gives L_i=0 and u_i=0. The alternate point is the negative guarded nonidentity root, so its logarithm ratio is defined. The cross test gives `v(L_i')>=k_i`, where k_i is 12 or m. Its unit correction gives the same valuation for `r_i'=-n_i/(h-1)`, and integral h-1 yields `v(n_i)>=k_i`. No `log(O)/z(O)` is formed. This is a valid explanatory clarification, not a discovered counterexample or new arithmetic premise. I reviewed the final paragraph and matching obligation and accept their new hashes.

The alternate charts retain their nonidentity guards. At a split prime, conjugated tests refer to the other place and the full rational label ratios are fixed by conjugation. At an inert prime the automorphism preserves the unique place and its valuation. Thus both splitting types are covered without silently requiring both-place detector success.

All labels are the same integer labels used in the literal Lucas polynomial. Because the compared ratios are integral, substituting their congruences into that integer polynomial transfers order m to its actual value. Likewise the input argument applies to the actual reduced numerator of n-beta. No norm of the height product, different ratio or merely related scalar index is substituted downstream. The scalar order-31 proof and split-41 trace argument are unchanged.

## Completeness with preparation zero and larger primary depth

The new route retains the preparation-zero construction's actual order of choices and real restriction. In particular, scalar finite depths are fixed; H0 is chosen near the two real identities; the actual shifted scalar point Q is then chosen; roots, scales, finite continuity modulus and an open real neighborhood with `0<42rN^2<17` are fixed before contact primes. The scalar chain and its nonzero domain do not change. The earlier real limit, including its nonzero B^4 term before H0 is made small, remains the relevant limit.

The only primary-progression change is `Pi^44 -> Pi^(m-1)`. The existing fixed-data separated-prime construction provides `gcd(Pi,M_plus*L0)=1`, `gcd(M_minus,M_plus)=1`, and `gcd(M_minus,L0)=16`. Since `64|h0`, these give compatible congruences for either m. The resulting progression still refines `h=h0 mod L0`, and so its residue and modulus remain divisible by the real component-group order m0. Its dense positive tail meets the same previously fixed open real neighborhood. This is an actual final H, not a limiting point.

The primary reduction-order condition first gives depth at least one. Formal multiplication by `p^(m-1)` raises it to at least m, on the same good unramified domain. All integer multiples `[n_i]H` preserve that depth, including identity multiples. The alternate points retain depth one; no contradictory condition requiring a contact prime to divide h-1 is imposed. Exact integer completeness labels and the relative precision 51 supply the high cross tests; their actual Lucas identity and n=beta supply the literal high polynomial tests. The order-12 pair still follows from the available primary depth and G2 precision.

I also checked the changed weights at their actual pole consumers. For every fixed m they retain `q_m=O(lambda^-1)` at real infinity, the same leading pole asymptotic, and eventual physical input in (0,17). At the small primes 2,3,17 the lower-bound expression `nu+(10m-6)(v(A)+v(98))` still tends to infinity as denominator depth nu grows; the scale and lower bounds are already fixed. At a successful contact, every factor is one modulo p. At the other place, inverse factors have residue zero or one by the odd-valuation argument, so the reciprocal trace is a unit (residue one or two). At other primes the unchanged R has even valuation. These facts preserve square reduced denominator, required local squareclasses and lower valuations, and the preparation-zero converse's real bound. All conic zero branches remain allowed.

Thus the larger primary depth is compatible with the scalar real/finite preparation and every detector pole hypothesis. The proof does not ask the prime theorem for uniformity in a changing continuity modulus.

## Anchor 2016 and all three height consumers

The applied height input is the same conditional statement with logarithmic height, exponent `alpha=577/32` and exact 665-bit constant

```
H=3*2^106*(2^32*3^9)^6*46410^18+128.
```

The uniform even-anchor argument at 2016 yields all four labels odd, X integral at 2 and 3, and `0!=a-1 in 2*3^1007 Z`. Its noncircular local parity argument and actual field norm are unchanged. The anchor excludes X=-1/2, and the same positivity excludes all other forbidden height contacts, so the height theorem applies to the actual beta.

Let `c*=2*3^1007`, `b*=3^1007`. Exact independent integer checks confirm:

1. Scalar order 31: `(c*)^415>(4H)^992`, so `h(beta)<|a-1|/4` on the entire admissible index range.
2. Lucas order m: `(b*)^(16m-577)>(24H)^(8m)` for m=46 through 51. Since `2-4alpha/m=(16m-577)/(8m)>0`, the endpoint bounds cover every `B>=|a|>=b*`. For the two implemented orders, the unchanged transfer estimate and `|F|<5B^4` therefore contradict F!=0. The same guarded root supplies the Lucas conclusion `log B>|a|-3`.
3. Input order 12: `40H<2^670`, `b*>67000` and `b*>152` imply the unchanged strict upper bound `(487/500)|a|+19/20<|a|-3` when n!=beta, contradicting Lucas. The final integrality inference for X is unchanged, including prime 17.

The exact comparison at anchor 2010 fails the displayed scalar inequality, and order 45 at anchor 2016 fails the displayed Lucas inequality. Those reported boundary checks are correct for these sufficient estimates. They are not impossibility proofs for other arguments, circuits or anchor presentations. Orders 48–51 have checked numerical margins and the uniform local precision, but this report accepts implemented circuit alternatives only for 46 and 47.

## Finite evidence

I ran both complete experiments freshly in this review directory. They passed raw-source/guard comparison and negative controls; all 342 declared gate identities with an empty unverified list; compiler and free-omission checks; elimination; fresh four-conic transport; every diagonal substitution; and all coefficients. The omission still removes only unused base slots `scalar.preparationU` and `scalar.preparationV`, preserving every compiled residual.

Separately, `independent_checks.py` imports no author producer or checker. It validates the current source hashes and the prose-only revision; computes a13 in product form; verifies the finite periodic floor-step identities supporting the all-index proof; checks both circuit exponent identities and all integer height margins; checks actual omission incidence; and expands every actual scaled residual square, comparing all polynomial coefficients for both alternatives.

| Alternative | Variables | Residuals | Monomials | Maximum coefficient |
| --- | ---: | ---: | ---: | --- |
| Order 46 | 386 | 355 | 26,046 | `28902*3^1344` |
| Order 47 | 386 | 355 | 26,037 | `28902*3^1344` |

Both maxima have 646 decimal digits and 2146 bits. Both quartics have degree four, content one, all variables active, and coefficient one on the fourth power of the fixed input. The 383-variable parent remains smaller in variable count; these alternatives exchange three variables for smaller coefficients.

| Evidence | SHA-256 |
| --- | --- |
| Order 46 final IR | `5a7503db2528d5054f8ea66e4d57fda2dc5797ceee870fef4b54ab48b697f4c3` |
| Order 46 polynomial JSON | `723cfb55c3a95aa14b5bf93abc28324647ccff407e897737d5d5cd54effad087` |
| Order 46 decimal table | `99a4ef561398c928aa5f553b5928592b4c828782c6d8505a4806501c8dbb002d` |
| Order 46 `MEASURED.json` | `90acfe9525a215517d17e3ea0c812493145df00aef7657f357eac9f86a5efbe7` |
| Order 47 final IR | `54c6ba9d3f79bb484e9226e650c15d34fdeb997ce82f0c7352e2b68d03c4bfc6` |
| Order 47 polynomial JSON | `7576ef089f6f5eddc1e70a3befd02ff1a3bdc7877288d6d4acb04a4e245d0b35` |
| Order 47 decimal table | `3f368679b51115c2fff1a895b84998239491942c20813aec004d49de04a2435e` |
| Order 47 `MEASURED.json` | `f53318d6104ff10962803280d719c39e874d1235406f917072fd480f4f9c6288` |
| `INDEPENDENT_CHECKS.json` | `80be8651d12fccf5192258be48ced49fdf2f90024673506765f97d6efcbbf4d8` |

The fresh replays used the computational files at the initial packet revision. I verified those files are unchanged in `bc51100`, and separately verified every final source binding. The final source clarification therefore requires this explicit review acknowledgment, not a duplicate computational run. These finite checks do not prove the uniform arithmetic argument or the inherited global inputs.

## Contract disposition and remaining obligations

All nine author obligations were compared to their definitions, inputs, actual construction and consumers. They are satisfied in this reviewed local scope: source hypotheses; actual constructed objects; all omitted indices and place/identity domains; relative-to-absolute comparison and weight maps; downstream object identity; valuation/field/coefficient conventions; simultaneous local/real conditions; exceptional cases; and every height/coefficient consumer.

The pertinent infinite index set is the full series tail j>=13. Its coverage is established by the exact first coefficient and the monotone estimate for all remaining indices. No Euler system, Kato index set or inverse-limit application changes here; this report does not resolve any inherited obligation of that kind.

Historical disposition: **prior recurrence, coefficient-bound, local-comparison and completeness inputs found and read; the sharper connection to the new orders is supplied and checked here**. No prior proof is called defective merely because it used a weaker sufficient bound. The all-primary identity clarification is recorded as resolved exposition in the final packet. Manuscript disposition: **pending**.

No material local repair remains identified. The inherited global group, pole-realization, prime-pattern, geometric/modularity/height, quaternion and Lucas dependencies remain conditional. Current-manuscript incorporation and properly authored exact-source acceptance remain separate. This report is internal AI review, not human peer review or a complete formal proof, and it is not a machine-readable protocol acceptance record.
