# Independent review of mixed detector normalization

Reviewer: `/root/independent_math_review`. Date: **2026-11-09 UTC**.
This is a separately authored **independent internal AI review**, not human
peer review. I did not author this mathematical construction, edit its source
packet, or create a repository/App acceptance record. I read the actual earlier
arguments and reviewed the changed application anew under `AGENTS.md`, the audit
integration protocol and research-review protocol v1.2.

**Decision: accept the stated conditional local mathematical application and
its measured 380-variable, 644-digit construction at the final source below.**
No material objection remains in this reviewed scope. The generated-comment
finding was corrected by the author and is retained in this report and
`FINDINGS.json`. This decision does not accept the inherited global arithmetic
inputs, claim current-manuscript incorporation, establish full published-source
closure, certify a public destination, authorize the designated App check, or
assert optimality.

## Exact target and evidence

The initial target was `6b4c2b58c871e35dada6bd15cd359b863e45838f`. The final
reviewed commit is **`eb00b7c9c5be2e8666c0403c750c6c780cf78563`**, with parent
`59c59e5589d86036ee41994c82a2b900fce85c2d` (the reviewed height layer).
The packet is `research/mixed-detector-normalization/`.

| Binding | SHA-256 |
| --- | --- |
| `PROOF.md` | `3dfb7eb74c10358744a41c4c7bfa36d154fae149f6748e3082fa6013c11b2abd` |
| `APPLICATION_CONTRACT.json` | `1ac61dfe4b5e4e14cc5a8dace1fd9178d62299a4d522734edc9695a4b7aad7a1` |
| `SOURCE_BINDINGS.json` | `6b887df56ffe26e86422d464b3a951a5e29e1166e49c7af005c93be1f015b629` |
| Final generated builder | `a2ce824132ce99feba6e814ca5eaf2070dfccaffab4fa0bdb950054a13699f55` |
| Raw translated IR | `f6ac117625f054cf6fec0863f1a3417b0f5305a9e477e901e098387a6a6fac40` |
| Final pre-diagonal integer IR | `e49006b9f4ca7f9b1e1077d5f5a736450a5d034cae2507247d8ddaf629382d24` |
| Balanced polynomial JSON | `4e2bf4a0047eee53e63991d60f742d8bb175640b008189deacad348a0e261d18` |
| Complete decimal table | `995c84c33620e8a407a4d83b5c79fb864187874460a218e18ce25c5f8877e796` |

`SOURCE_HASHES.json` records all 100 manifest-bound files, independently checked
against both committed Git blobs and worktree bytes. `SOURCE_EXCERPTS.json`
records whole-source and original-byte passage hashes, precise line ranges and
the excerpt rule. The final change from the initial target has only five paths:
the comment-generating patch, expected builder hash, author finding, manifest
and separate manifest digest. Proof, contract, executable equations, checker
and runner are unchanged. The whole incremental diff from the height parent
contains only this packet and its new workflow.

The earlier height report and findings at commit
`a5ffef4019cd68b48c40e9f9d52d0a1cf8217859`, directory
`research/independent-local-reviews/2026-11-09/height/`, match my original files
byte for byte. Their report and findings hashes are, respectively,
`f66c70170f4465bd6ff400d5b481752118f6174645ac3c17b116ad5d1e10e2db`
and `45c6500db80c4e6338e36a06afe4116adae82656c290e3d549c6d65a60005007`.
They are earlier evidence, not authorization for the present changed proof.

## Source arguments and mathematical assessment

The relevant original proof is `manuscripts/quartic_v10.tex`,
`lem:v5-one-place` (11031–11064), with its pole statement `hyp:o8-pole`
(7698–7732) and completeness construction (11220–11360). The one-place
statement has the old large-prime cutoff. I did **not** silently drop it: its
proof uses the pole obstruction outside `{2,3,17}`, unramifiedness and integral
normalized valuations. The actual-local-consumers paragraph in round four
explicitly makes this reapplication. The old round-four contact map and its
larger exceptional list are not substituted for the later map. Round five's
new map, contacts and unit computations supply the present exceptional set.

Round five already proves the uniform `delta^-3` normalization with input
`D/delta^(m+1)`; round seven proves the uniform `delta^-1` route. Round eight's
detector note supplies the exact two order-twelve tests and their common
product. This history supports the component identities. Mixing the two
normalizations at the actual consumers is the new application reviewed here.

**Actual circuit and domain.** Put `t=A*lambda`, `delta=98t-1`, with the five
contact polynomial `F`, `e=(A*delta)^5/F`, and `R=1/(e*delta)`. The actual
scales are `1,C0^2,(C0+C1)^2`, not the norm of the root product. Their retained
lower bounds give `A>=1`. The positive chart and the equation
`q1*F=A*(A*delta)^4` give `delta>=39/25`, `F>0`, `q1>0` and `E=q1*delta^2>0`.
Thus the quotient denominator in the new last gate cannot vanish on an
allowed source solution. A zero branch of its isolated cleared equation is
not being substituted for this source domain.

The cubic reuse and successive squares give exactly
`q12=e^23/delta`, `h=q12^2=e^46/delta^2`. Hence `q1*qHigh=h^2` gives
`qHigh=e^91/delta^3`. My own polynomial decoding of the affine aliases and
actual defining rows gives, in `Q[t,q1,z]`, the old constraint
`q1^3*z=q1^92*delta^88` and the new constraint
`q1*z=q1^92*delta^88` in all three detector blocks. The q1 cube is still
stored and used by the low product and cubic reuse. No coordinate is silently
replaced by a new unstored product. The optional parent's `highLift` is
unneeded; this is the default coordinate budget, not the optional budget.

The exact order/index coverage is:

| Source tests | Actual functions | Order |
| --- | --- | ---: |
| 0 | Primary `g_H` | 46 |
| 1 | Primary input `g_UA` | 12 |
| 2–4 | Three remaining primary inverse roots | 1 |
| 5–9 | Five conjugated alternate inverse abscissae | 1 |
| 10 | Input cross comparison | 12 |
| 11–13 | Three Lucas-label cross comparisons | 46 |
| 14 | `L1-beta` | 46 |
| 15 | Literal field Lucas polynomial | 46 |

The raw aliases for all sixteen field tests are unchanged. The builder
partitions them into eight low tests, two order-twelve tests, and six high
tests; its symmetric blocks and uniform pair multiply exactly the assigned
`1+q*D^2` factors. Every outside residual, gate and guard agrees after the
explicit order-label match, apart from the tracked anchor parameter.
This is equality of formal coordinate expressions. It is **not** equality
of evaluated W, trace, or private pole inputs, since the high weight changes.

**One common place.** For general input `d=D/delta^j`, direct substitution
in `R*(d/R^m)^2` gives weight
`e^(2m-1)*delta^(2m-1-2j)`. Thus the actual triples `(m,j)` are
`(1,1),(12,12),(46,47)`. The six high tests really require
`D/delta^47`, not the low normalization at order 46. The one-place proof
allows arbitrary field inputs, unequal positive orders and zero inputs;
it assumes no prior integrality of these normalized inputs.

At a retained odd contact, the unimodular map `phi(t)=-49+1/t` places `t`
at one of the five finite contacts. A pole of t maps to -49, which is
distinct from the target contacts outside the stated exceptional set.
The delta values are `-1,1,24/25,-24/25,39/25`, all units there. Because
A is a rational square, its fifth-power valuation correction is even;
the required valuation `r=v_p(R)` is odd. In `K=Q(sqrt(2))`, these primes
are unramified and normalized valuations are integral, including inert
places. Thus normalizing by delta does not change the consumed valuation.

For a nonzero d, each nonconstant factor term has odd valuation
`r+2(v(d)-m*r)`. Its factor valuation is its minimum with zero. With
`l=max_{places|p} v(W)<=0`, trace integrality gives
`v_p(Tr(W^-1))>=-l`. The pole obstruction for the odd valuation of
`Bpole=R/Tr(W^-1)^2` implies `0<v_p(Bpole)<=r+2l`, hence `r>0` and
`l>-r/2`. At a place attaining l every factor valuation is at least l,
since all are nonpositive. Consequently
`v(d)>(m-3/4)r>=m-3/4`, so `v(d)>=m`. A zero d satisfies this directly.
This establishes one common successful place for **all** tests, not a
separately chosen place for each one. It gives the asserted radical orders;
it need not claim divisibility to order `m*r`.

The physical pole input is the correct one. Positivity of every weight
makes W at least one at both real embeddings. Therefore `W0>=1`, `N(W)>0`
and `Tr(W^-1)>0`. My independent raw-polynomial checks verify the circuit's
`2W0*n=N(W)` and `E*Bpole=n^2`. Since `Tr(W^-1)=2W0/N(W)` and `E=1/R`,
the resulting input is exactly `R/Tr(W^-1)^2`. No norm/trace normalization
or factor two is lost. The existing factored conic transports still receive
positive inputs and retain their permitted zero witness branches.

**Precision and all downstream consumers.** I read the preserved precision51
argument, including the actual coefficient recurrence, the j=13 denominator
loss and the entire j>=14 tail. The bound is 51, not 52: at p=53 and depth
one the j=13 relative-tail term has valuation 51 and later terms have
valuation at least 55. For the actual new high order, the primary depth is
at least 46, so its weak relative error is at least 184; the alternate
G12 error is at least 51. Both exceed the required 46. G2 and the input
comparison retain order twelve.

The exact two-anchor ratios are `u_i/h` and `(u_i-n_i)/(h-1)`, with the
guarded nonzero integer denominators. One denominator is a local unit.
The cross comparison transfers integrality before relative logarithm errors
are used as absolute errors; integral primary ratios force numerator depth
at least that of the denominator. If any primary numerator is the identity,
`L_i=0,u_i=0`; the alternate point is the negative of the guarded root.
The alternate unit estimate and cross congruence give
`v(-n_i/(h-1))>=k_i`, and hence `v(n_i)>=k_i`, without a quotient at the
identity. This covers all four labels. Conjugation preserves inert-place
valuation. The actual three Lucas integers, their literal residual, and
the reduced input numerator receive precisely their required divisibilities.
The scalar order-31 chain, shifted point, split-41 proxy and preparation-zero
norm retain their old equations and meanings; no changed weight is consumed
inside that scalar block.

The parent height proof supplies a transfer for every positive integer k,
using the actual field product of four odd root abscissae and the projective
tuple of the three retained scales. Its constant is
`K0=(3H+14)/2`, with `alpha=577/32` and
`H=3*2^106*(2^32*3^9)^6*46410^18+128`. I checked the new k=46 application,
not the parent's chosen k=47. At `E=2010`, `c*=2*3^1004`, `b*=c*-1`,
the exact scalar inequality and the order-46 Lucas endpoint both pass.
The latter has exponent `32*46=1472`. For all `B>=b*`, its ratio is an
increasing positive function: the power of B is `64*46-2308=636>0`,
`(1-6/B^2)^1472` increases and the positive denominator decreases.
Thus the finite endpoint extends to every allowed B. The scalar inequality
extends by the positive exponent `415/992`.

The final input calculation gives exactly
`log B<(4712/4775)|a|+4616/4775<|a|-3`; its gap at 301 is `22/4775`
and increases thereafter. The anchor gives the much larger required lower
bound, as well as 2/3-integrality. After `n=beta`, the leading coefficient
`11016=2^3*3^4*17` also excludes a negative valuation of X at 17: the
quadratic term would still be uniquely minimal. No order-47 conclusion,
stronger scalar radical order, or discarded prime is needed.

**Simultaneous completeness.** This must construct new pole witnesses;
arbitrary old W and pole witnesses cannot be carried over. The parent
optional construction at E2010 supplies the same underlying root and scalar
conditions. Its deeper primary congruence `Pi^46*M_- | h` supplies depth
at least 47; integer multiplication cannot lower formal depth. Alternate
points need only depth one. The same sixteen functions therefore meet the
new successful-place requirements. The claim is reuse of that method with
strengthened preparatory bounds, not a claim that every previously chosen
old witness tuple already meets every new pole condition.

I checked the quantifier order in the actual supplying construction: scalar
finite depths, H0, shifted scalar/root choices, scales, continuity modulus
L0 and a compact real neighborhood avoiding comparison poles are fixed
before contact-prime selection. Their finite lower bounds and real upper
bounds on D are consequently fixed before that call. The original prime
input accepts arbitrary fixed divisibility q, cutoff Y and real lower
bound H, not a growing-modulus uniform estimate. Repeated contact forms
are merged while keeping detector incidences; the five within one detector
are distinct, and scale one ensures at least two forms. Enlarging the
finite divisibility and real bound to cover all three mixed detectors is
therefore permitted. The existing CRT gcds survive the exponent 46, and
the positive progression meets the fixed identity-component neighborhood.
It supplies an actual final H with the scalar and detector conditions
simultaneously.

At a selected contact, `v_p(R)=1`, delta is a unit, and a new high
nonconstant term has valuation at least `1-92+92=1`; the older depth-47
choice is more than enough. At the other place every nonzero nonconstant
term has odd valuation, so each inverse factor has residue zero or one.
At the successful place their product has residue one. The reciprocal trace
has residue one or two, hence is a unit at these odd primes. Zero D causes
no exception. Away from the selected contacts, the contact product formula
for R gives even valuations because `v=D0^2*w^2` and `delta^6` contribute
even valuations. Multiplication by the rational trace square preserves
parity. This also covers primes where delta vanishes away from contacts.
The reduced denominator of the new Bpole is a square. The fixed Gaussian
classes preserve its Q2, Q3 and Q17 squareclasses.

At real infinity, `e -> 98^5*A^5`. The low weights are O(lambda^-1)
and the new high weight is O(lambda^-3). With the fixed test bounds,
`W=1+O(lambda^-1)`, its reciprocal trace tends to two, and
`Bpole ~ 1/(4*98^6*A^6*lambda)`. Thus the actual input eventually lies
in (0,17). At p=2,3,17 let `s=v_p(A)+v_p(98)` and `nu=v_p(v)`.
For sufficiently large nu, `v(delta)=s-nu` and `v(e)=5s`, giving the
three exact weight valuations `nu+4s`, `nu+114s`, and `3nu+452s`.
All slopes in nu are positive, even when the fixed s is negative.
One sufficiently large finite choice handles all detector/test lower
bounds. This makes the trace close enough to two, also above ramified
two, to give `v_p(Bpole)=nu-6s-2v_p(2)`. The necessary lower bounds
3,1,2 at p=2,3,17 follow. The preparation-zero converse therefore supplies
new private pole witnesses, followed by the existing conic transports.
The scalar real bound and local conditions remain true for this final H.
At E2010 the private anchor gate and conic witnesses have the parent's
current meanings. No old pole witnesses, forbidden zero inverses, or limit
points are reused in place of constructed objects.

## Nine-obligation decision

The contract's nine obligations are addressed for this conditional local
scope. The comparisons supporting that decision are explicit above:

| Obligation | Required input, constructed input, and consumer |
| --- | --- |
| Source hypotheses | Arbitrary-order one-place proof with nonzero W/trace, a pole certificate and unramified integral valuations; positivity and the actual small-prime pole implication provide them for the mixed product. Consumed by PROOF 63–116. |
| Constructed objects | Stored positive q1, q12 and h; the actual last quotient yields e^91/delta^3 with no additional coordinate. Consumed by all six high factors, PROOF 19–61. |
| Domain/index coverage | All sixteen tests, all retained contact primes, one common place, split/inert and all primary identity branches are covered. Consumed by logarithm comparisons, PROOF 63–143. |
| Transition maps | `(m,j)=(1,1),(12,12),(46,47)` gives the exact implemented factors; delta-unit scaling preserves valuations. New witnesses are obtained after new Bpole conditions, not by a false projection map. |
| Consumed object identity | Circuit Bpole is R/Tr(W^-1)^2; integer labels, literal Lucas residual and reduced input numerator are unchanged and receive orders 46/12. Scalar proxy remains the same object. |
| Conventions | K=Q(sqrt(2)), rational normalization v(p)=1, exceptional set, factor-two trace convention, field product height and input-fixed rational diagonal map agree. |
| Local conditions | Successful/opposite contacts, even valuations elsewhere, real decay, squareclasses and all small-prime depth bounds hold simultaneously in the original choice order. Consumed by the new pole converse, PROOF 159–219. |
| Exceptional cases | Source positivity excludes F=delta=q1=0; zero D, primary identities, conic zeros, p53 precision loss and ramified p2 trace depth are retained. No stronger quotient domain is assumed. |
| Downstream consumption | Uniform order-46 Lucas contradiction and scalar/input margins pass at E2010; full replay and independent coefficient reconstruction give the stated polynomial. Global inputs remain assumptions. |

## Reproduction and retained finding

I ran the full author entry point into the fresh directory
`/tmp/quartic-mixed-review/replay`. It passed source bindings, source
mutation controls, compiler/gate checks, omission, conic transports,
diagonal checks, exact expected hashes and coefficient metrics. The actual
comparison baseline is the parent's **default height** circuit at E2118.
Its raw bytes exactly match my earlier
independent height replay.

My separately written `independent_checks.py` imports no author checker.
It verifies the actual six old/new weight blocks by exact polynomial
decoding, the exact physical norm/trace rows, every outside source section,
the order list and test aliases, normalization exponents, contact units,
small-prime slopes, and exact integer/rational height margins. It then
reconstructs **every** diagonal substitution and nonzero row divisor,
forms the full sum of squared rows using triangular pair expansion, and
independently parses and compares every coefficient of the decimal table.
The result is 380 active coordinates including the fixed input, 349
quadratic residuals, degree four, 26,025 monomials, content one and input
fourth-power coefficient one. The exact maximum is `28902*3^1340`, with
644 decimal digits and 2139 bits. These checks support the finite algebra
and measurement; they do not prove the uniform arithmetic existence inputs.

I identified a nonblocking generated-comment defect in the initial target:
mechanical renaming left the false comment `q46=q1*e^88`; the old semantic
input comment also needed clarification for the mixed route. The proof and
executable rows were already correct. The author corrected the comments
and recorded the finding in the final commit. `freeze_sources.py` verifies
that removing only standalone `//` comment lines leaves every executable
line byte-identical. Its fresh final Node build reproduces the exact initial
raw IR. Thus the earlier complete replay and independent coefficient
reconstruction apply to the final executable source; the corrected builder
has its own new hash. The finding is resolved as a documentation correction,
not erased or reclassified as a new mathematical repair.

The final audit-history self-test passed its historical, mutation and current
application checks. Its output explicitly limits their scope; it does not
register or mathematically establish this independent decision.

## Conditional handoff scope and remaining obligations

I accept the declared v1.2 scope of this **conditional non-release research
contribution**. Its 380-coordinate result does not cross the next below-300
milestone; no new current-manuscript edition, replacement release artifact
or unconditional theorem is claimed. The actual diff leaves README,
Version 13 TeX/PDF, current release surfaces, existing packets, workflows
and acceptance register unchanged, apart from the separately added mixed
workflow. Leaving those current surfaces unchanged is justified by these
claims, not by a metadata exemption from review.

The new handoff links the exact earlier height review, preserves the
cumulative handoff and negative-result archive, attributes the older
normalizations and the author's mixed construction, and distinguishes a
deterministic generator with full-table hashes from a committed full
expansion. The prior unsuccessful chart/log routes, bounded regrouping
probes and archived diagonal LP remain historical evidence with their
limited status; the LP/dual is not a dependency reviewed or accepted here.
The new construction does not establish optimality or reinterpret those
restricted investigations as an impossibility theorem.

The remaining obligations are explicit: inherited global arithmetic and
published-source closure, Kato/current-source integration, current-manuscript
incorporation, the historical stdout root cause, and any required public
readback/release or designated App authorization are not closed by this
report. Public CI/pass and readback information supplied by the author is
not substituted for my local evidence, and this report makes no independent
public-destination verification claim. No new unresolved **local** objection
was found. A subsequent protocol record may bind this exact decision and
archive, but a changed application or source requires renewed review.
