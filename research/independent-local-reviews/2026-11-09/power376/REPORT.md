# Independent review: uniform odd-power detectors, second layer

Reviewer: `/root/independent_math_review`. Date: **2026-11-09 UTC**.
Review type: **independent internal AI review**, not human peer review.
I did not propose the odd-power chain, author its application proof, edit the
author packet, or create repository acceptance-register or App records.

**Decision: accepted within the stated conditional local scope at commit
`32abb654ec295e28b51f92a51d7f12d4c5a626ec`.** The changed detector
application, its simultaneous completeness argument, the specified
376-variable/425-digit representation, and the declared v1.2 handoff scope
pass this review. No material local objection remains; no author correction
was required during this review. This is a fresh review of the changed
arithmetic route, not a transfer of the parent's approval. The inherited
global arithmetic qualifications remain in force.

This decision covers the order-46/scalar-order-31 layer only. It does not
accept the later scalar-order-47/detector-order-50 variant, a global theorem,
current-manuscript incorporation, an optimality claim, public-destination
readback, or designated App authorization.

## Exact sources and history

Worktree: `/tmp/codex-glazer389-review-3j08z564/power376`.
Parent: `ce15e8ece219a2bb000075a5a79f6ffd9bea6dfd`.
Packet: `research/odd-power-detectors/`.

| Artifact | SHA-256 |
| --- | --- |
| `PROOF.md` | `5d20636e3ab9a6d7b54cca4a2efa6a802d0f91984ec0be49c1c1b8875a80b1ab` |
| `APPLICATION_CONTRACT.json` | `ed2f867c6782967b214bee58ca2f18da46b605d89268023418cac146b5083a08` |
| `SOURCE_BINDINGS.json` | `137cbe223f9ac68431d64952c22d5957befb80b64930307f7a539e0a1662e366` |
| `DIAGONAL_WEIGHTS.json` | `807b6e84bac26d3cc82801cd8fa4215fb0c59753e482a664b0502f603f20e108` |
| Generated builder | `a25814180709259815045a316b6a06953e2cc14e42c31b812d8716a7b6190496` |
| Raw translated IR | `4c38160e31788986174a9791d5d71c1135016ebf39dd7d940b8225277765dd35` |
| Final pre-diagonal integer IR | `b2ead69d8a09bb71296258464f2be445e7e054e16c7a52820795aa422916d33a` |
| Balanced polynomial JSON | `8ae4128979e5b3d45620077e5b0ec3574ae68d130464257d5e07cda6e0495ece` |
| Complete decimal table | `b2fe4f569707a9b548a3b9a8221e0b060bce83a2c03cd38f83791a30ed48b9c1` |

All **337** bound files match the immutable Git blobs and worktree bytes.
The entire incremental diff consists of the twelve new packet files and
its workflow. No earlier mathematical packet, current manuscript, release
surface, or earlier review is altered. `SOURCE_HASHES.json` records the
complete path list and hashes. `SOURCE_EXCERPTS.json` binds actual source
passages by original-byte excerpt hashes and whole-source hashes.

I read the actual v10 one-place proof at lines 11031–11064, its preparation
zero pole statement and argument, the round-four small-prime reapplication
at lines 142–153, the round-five normalization argument, and the full
round-seven detector normalization/completeness argument. I also read the
new proof, contract and implementation; the actual mixed-normalization,
precision-51, height, scalar-preparation-zero and scalar-row arguments; the
v10 simultaneous construction at lines 11220–11360; and the Version 13
fixed-data prime theorem at lines 16566–16604. Earlier verdicts were used
as locators, not as replacements for those arguments.

The parent's independently authored 20-file selected archive at
`a2d259fed72f6310e0ccfac9cdd1bc346b88782e`, directory
`research/independent-local-reviews/2026-11-09/row379/`, matches my originals
byte for byte, including the audit log, manifest and manifest digest. All
208 entries of the contributed historical research inventory also still
match their actual original files: 199 Opus files and nine Codex vetting
files. This includes original whitespace. `ARCHIVE_PROVENANCE.json`
records that check and its selected-archive boundary.

The original frontier note supplies the chain idea but incorrectly says
that W, its trace and the pole input stay unchanged. The later vetting note
explicitly corrects that assertion, and the current proof uses the
correction. Historical components have therefore been located and a new
connecting application has been reviewed. This does not imply that the
current Version 13 incorporates this application; incorporation is pending.

## Actual circuit, domain and test coverage

Write K=Q(sqrt(2)), with normalized unramified valuations v(p)=1. The
three actual scales are A=1,C0²,(C0+C1)², where C is the existing field
product of the four root abscissae. These are the same positive rational
square scales, at least one. They are not replaced by a field norm.
The construction retains

```
t=A*lambda, delta=98*t-1,
F=t*(t-1/49)*(t-1/50)*(t-1/2450)*(t-32/1225),
e=(A*delta)^5/F, q1=e/delta, E=q1*delta^2=e*delta=1/R.
```

The source positive chart gives t>=32/1225 and delta>=39/25. All factors
of F are nonnegative there. The actual defining equation
`q1*F=A*(A*delta)^4` has a strictly positive right side, so F>0 and
q1,E>0. In particular, clearing the new q1 denominators introduces no
zero branch on the allowed source domain.

The order-one product already needs the stored q1² and q1³. The new chain
stores q1⁶, q1¹², q12=q1²³, h=q1⁴⁶, q46=q1⁹¹, q46² and q46³. It uses
seven weight coordinates per detector instead of eight. I decoded the
actual affine aliases and checked each defining residual as an identity
over Q[u], u=q1; the exponents are 2,3,6,12,23,46,91,182,273. The actual
q12 and q46 quotient denominators both equal q1. The delta³ expression
is still an affine alias using existing Fmiddle, Fsquare and t; it is not
an extra allocated coordinate or an unstored product counted as free.

Against a fresh exact parent baseline, precisely nine old e³/e⁶/e¹² rows
disappear, six q1⁶/q1¹² rows appear, and three q12 definitions change.
All **351** other common raw rows, all common formal aliases and all inverse
guards are identical by named coordinate. This equality concerns formal
expressions, not the values of expressions depending on the changed weights.
The baseline raw IR equals my earlier independent row379 replay byte for byte.

The actual order list is

```
[46,12,1,1,1,1,1,1,1,1,12,46,46,46,46,46].
```

Index 0 is the primary H test; index 1 is the input primary inverse root;
indices 2–4 are the other primary roots; indices 5–9 are the five conjugated
alternate inverse abscissae; index 10 is the input cross comparison;
indices 11–13 are the three Lucas-label cross comparisons; index 14 is
L1-beta; and index 15 is the literal field Lucas polynomial. All sixteen
field functions are retained. In the actual product code, the two order-12
tests are evaluated as `1+q12*(D1²+D10²)+q12²*D1²*D10²`; the eight low tests
are two groups of four, and the six high tests two groups of three. The
unchanged symmetric recursion is the product expansion over K. Thus the
order-12 pair changes weight as well as the six high tests; no consumer is
silently omitted or assigned the parent's old normalization.

## Soundness at one common place

For every test of order m in {1,12,46}, the supplied one-place input is
`d=D/delta^(2m-1)`. Since R=1/(e*delta), direct Laurent calculation gives

```
R*(d/R^m)^2 = e^(2m-1)*delta^(-(2m-1))*D^2
            = q1^(2m-1)*D^2.
```

The delta denominators are respectively 1,23,91. At every consumed finite
contact the five delta values are -1,1,24/25,-24/25,39/25, all units outside
S={2,3,5,7,13,17}. The map phi(t)=-49+1/t sends the five contacts to the
required height contacts. A pole of t maps to -49, distinct from them
outside S. The square scale contributes an even valuation correction;
at a consumed odd valuation of R, v(d)=v(D).

The original one-place statement has p>76176. I have not applied that
statement verbatim at smaller primes. Its proof uses the pole obstruction
outside {2,3,17}, unramifiedness and integral normalized valuations. These
are the actual inputs supplied outside S, as in the round-four argument.
It accepts arbitrary d in K and varying positive integer orders, without
assuming d integral before applying it.

To rederive the inference, put r=v_p(R), odd. Each nonzero nonconstant term
has odd valuation r+2(v(d)-mr), so its factor has that valuation or zero,
whichever is smaller. At each place above p, v(W)<=0. Let l be their maximum.
Then v_p(Tr(W^-1))>=-l, and the pole certificate gives
`0<v_p(B)<=r+2l`. Hence r>0 and l>-r/2. At a place attaining l, every factor
valuation is at least l; consequently `v(d)>(m-3/4)r>=m-3/4` and integral
valuations give v(D)>=m. A zero test satisfies this immediately. The same
maximizing place works for all sixteen tests, including split and inert p.

Every weight is positive, so W is at least one at each real embedding.
Therefore W0>=1, N(W)>0 and the reciprocal trace is nonzero. I checked the
actual raw residuals `2*W0*n=N(W)` and `E*B=n²`. They give exactly
`B=R/Tr(W^-1)^2`, including the factor two in the trace. This is the object
consumed by the pole predicate. Only R and the underlying field test
functions retain their former values; W, its trace, B and private pole
witnesses generally change.

## Consumers and all exceptional branches

The depth conclusions reach the same actual point/logarithm consumers as
in the mixed parent. This must be checked after establishing the new
normalization, rather than inferred from unchanged text alone.

G12 supplies relative precision 51 at the retained primes. I rederived
`a13=-54756974/6936596275`, whose denominator is 5²*7*17*29*37*41*53.
The j=13 tail loses at most one valuation and still has order 51r; the
entire j>=14 tail has lower bound `4jr-floor((4j+1)/10)>=51r`. The floor
increment is at most one per step, so the bound increases by at least three
and the tail converges. The depth-one obstruction to uniform precision 52
at p=53 is not bypassed or used. Primary depth 46 already makes the weak
primary relative error at least 184; G2 supplies input precision 12.

The actual two-anchor ratios are u_i/h and (u_i-n_i)/(h-1), not the earlier
v10 h-4 normalization. One of the two integer denominators is a p-unit.
Formal-domain tests and the cross congruence first transfer integrality;
only then may relative errors be consumed as absolute errors. If U_i=O,
then L_i=u_i=0; the alternate point is the negative guarded root and is
nonidentity. Its cross comparison and unit ratio give the required
divisibility of n_i without dividing by an identity logarithm. This covers
every primary index, including Lucas indices. Inert conjugation preserves
valuation. The literal Lucas residual thus receives order 46 and the
reduced input numerator receives order 12.

The scalar norm tree, its actual proxy Re(k_H*w_S), both places above 41,
and scalar order 31 are unchanged. The root-product projective height
application still concerns the same C and labels. The endpoint uses
alpha=577/32, `H=3*2^106*(2^32*3^9)^6*46410^18+128`,
`c*=2*3^1004`, `b*=c*-1`, and S=3^2010. I checked the exact scalar and
Lucas integer inequalities, the bound 40H<2^670 and b*>67000, and the
final-input constants 4712/4775 and 4616/4775. The Lucas comparison ratio
is increasing on B>=b*: its power exponent is 64*46-2308=636; the remaining
numerator increases and denominator decreases. The final-input gap at
|a|=301 is 22/4775 and increases thereafter. Both signs of a are covered
by |a|>=|a-1|-1. The label-height B here is distinct from detector pole B.
The 2/3-integrality anchors and the unchanged final beta/input inference
remain part of the inherited conditional argument.

## Simultaneous completeness for the new pole inputs

No old W, trace, pole input or pole witness is reused. I checked the order
of choices against the actual source construction. Fix the integer input,
scalar finite depths and real near-identity H0; then choose the shifted
scalar point and anchor divisibility, root labels/points and three scales.
Fix L0 and a compact real neighborhood avoiding all comparison poles.
This supplies uniform real bounds and lower finite valuation bounds on
all sixteen D before selecting contact primes. The scalar preparation-zero
argument keeps its physical input 42rN² in (0,17) on that neighborhood.

The supplying prime theorem permits arbitrary fixed denominator modulus,
prime cutoff and real lower bound, after those data have been fixed. No
uniform theorem with growing moduli is substituted. Merge repeated contact
forms while retaining their incidence in each detector. Each detector has
five distinct contacts and scale one supplies at least two forms globally.
The established gcd conditions still make the primary progression
Pi^46*M_minus, alternate progression M_plus and h=h0 mod L0 compatible.
The parent's depth-47 primary choice is more than sufficient. A positive
tail of this progression meets the fixed real neighborhood and supplies
the actual final H. It need not be the parent's former H.

At each selected contact, v(R)=1 and delta is a unit. A successful test
has v(D)>=m, so `v(q1^(2m-1)*D²)>=1`. At the other split place every
nonzero nonconstant term has odd valuation, making its inverse factor
residue zero or one; zero tests give residue one. The reciprocal trace
therefore has residue one or two and is a unit. The new B has positive
contact valuation. Away from those contacts the unchanged product formula
for R has even valuations; dividing by the rational trace square preserves
parity. This includes zeros of delta away from contacts. Consequently the
reduced denominator of B is square. The same Gaussian congruences give
its required squareclasses in Q2,Q3,Q17.

For fixed A, q1 is asymptotic to `98^4*A^4/lambda`. Thus the new weights
decay as lambda^-1, lambda^-23 and lambda^-91. Bounded tests give
W=1+O(lambda^-1), reciprocal trace tending to two, and
`B~1/(4*98^6*A^6*lambda)`. A stronger fixed real lower bound therefore
makes all three new inputs belong to (0,17).

At p=2,3,17 let s=v_p(A)+v_p(98), nu=v_p(v), where v=D0²w² is the fixed
source denominator form. Once nu is sufficiently large, v(delta)=s-nu,
v(e)=5s, and

```
v(q_m)=(2m-1)*(nu+4s).
```

The slopes in nu are 1,23,91, all positive even if a fixed s is negative.
The preselected lower bounds on v(D) therefore make every factor tend to
one. Choose the finite depth so that the trace is sufficiently close to
two, also above ramified 2. Then `v_p(B)=nu-6s-2v_p(2)`, giving the actual
required bounds v2(B)>=3, v3(B)>=1 and v17(B)>=2 simultaneously. These are
stronger fixed choices within the same prime theorem. With positivity,
squareclasses, square denominator and real upper bound already checked,
the preparation-zero converse supplies new private pole witnesses.

The earlier A row operation and tri maps retain their domain and actual
scalar object. In particular tri uses the nonzero constant
mu=184460384539620 and its Bh rescaling; this detector change alters no
scalar row. All four factored conic maps were checked anew against this
replay. Their actual H is 17e-Bh. For s!=0 the map is H=s*v, q=s*Q;
at s=0 the old conic gives `17*b*q²+3*H²=0`, with b>0, hence q=H=0
and v=Q=0 is valid. The reverse substitution works for every s, including
zero; it does not cancel s. Every private-coordinate consumer and every
exterior row is accounted for. The detector coefficient b is its newly
constructed positive pole input; the scalar coefficient remains 42r.

## Finite reproduction and the representation actually measured

I ran the complete source-driven reproduction in fresh output:

```
python3 -B research/odd-power-detectors/reproduce.py \
  --output /tmp/quartic-power376-review/replay
```

The runner, gate verification, quadratic reduction, four conic transports,
diagonal verification and all five source mutation controls passed. My
separately written `independent_checks.py` imports no author checker. It
reconstructs the chain and actual consumers from named raw polynomial
coefficients, proves the four conic substitutions, derives every diagonal
row through its nonzero rational scale and primitive integer normalization,
expands all squared rows, and independently parses the full decimal table.
This is complete coefficient comparison, not evaluation at sample points.

The supplied diagonal map has 35 specified coordinates, 35 with nonzero
ternary exponent and nine with nonzero dyadic exponent. Relative to the
parent's weight map, H.chart.j0's ternary exponent changes from zero to one.
The input is fixed. Every diagonal factor and row multiplier is nonzero
over Q, so each step preserves rational input projection. The arithmetic
arguments use the semantic coordinates recovered through the inverse map,
not the newly scaled slots directly. The final
sum-of-squares representation has **376 active variables, 345 rows,
25,964 monomials, degree four, content one, and input fourth-power
coefficient one**. The maximum absolute coefficient has **425 decimal
digits and 1,410 bits**. The complete table has 1,072,788 bytes and the
SHA-256 stated above. `INDEPENDENT_CHECKS.json` includes the actual maximum
integer and complete finite-check coverage.

The audit-history self-test also passed: nine historical dispositions,
seven negative controls, nineteen application-review negative controls,
and three current contracts. It is a structural check and supplies no
proof of the inherited arithmetic. The review is a local Python 3.12.3 /
Node v18.19.1 replay; it is not an independent cross-platform or public
artifact verification. The selected archive contains review records and
receipts; large generated files remain reproducible local artifacts whose
hashes are bound, not an implied committed expansion.

## Contract, handoff and remaining obligations

| Obligation | Reviewed comparison and disposition |
| --- | --- |
| Source hypotheses | Actual small-prime pole obstruction, unramified valuations, nonzero W/trace and fixed-data prime theorem are matched; conditional local application accepted. |
| Constructed objects | Seven actual stored weight gates per detector, exact factor product, R and trace-normalized B identified. |
| Domain and index coverage | All three scales and sixteen tests covered; same common place, split/inert primes and zero tests treated. |
| Transition maps | Exact d=D/delta^(2m-1), factor-two trace identity, parent A/tri and both conic directions checked; no old/new pole-tuple equivalence asserted. |
| Consumed object identity | Actual primary/alternate ratios, literal Lucas residual, input numerator, scalar proxy and root-product height objects retain their meaning. |
| Conventions | Rational coordinates, K basis, normalized valuations, unchanged exceptional set and anchor, positive q1 denominators and input-fixed diagonal map matched. |
| Local conditions | Contact units, other-prime parity, Q2/Q3/Q17 squareclasses and depths, real decay, compatible CRT and density checked together. |
| Exceptional cases | Zero tests, all primary identities, inert conjugation, positive conic zero branch, ramified 2 and exceptional-prime exclusions addressed. |
| Downstream consumers | Orders 1/12/46, scalar31, precision51, all E2010 margins and complete polynomial verified at the actual consumers. |

The handoff is appropriate for a conditional non-release research
contribution. This layer crosses no below-300 threshold and claims no new
current edition or replacement current artifact. Leaving README, current
Version 13 TeX/PDF, release catalog and current acceptance register unchanged
is justified within that declared scope. This is not an exemption from
source manifests, findings, provenance, independent review or later public
readback duties.

The historical record remains cumulative. Its incorrect invariance claim
is preserved with a correction; its earlier broad eight-gate claim above
order 46 is corrected by the later constructive examples. The six-gate
obstruction is restricted to its stated monomial model. I make no universal
gate or coefficient optimality claim and do not accept the archived tau,
B/C, dropped-test or unimplemented higher-order routes. Their unresolved
applications and negative-result limits remain recorded.

Full published-source closure, inherited global/Kato/current-source
integration, final assembled-manuscript incorporation, and the historical
stdout incident remain outside this decision. The designated
`Protocol / independent agent audit` App check and public readback require
their own evidence. Distinct reviewer identity does not eliminate correlated
model error; this report is independently derived internal AI evidence, not
human peer review. Any substantive change to this proof, its actual circuit,
sources or consumers reopens the affected obligations.
