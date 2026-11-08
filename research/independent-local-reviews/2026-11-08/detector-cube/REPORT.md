# Independent review of detector cubic reuse

Date: November 8, 2026. Reviewer: `/root/independent_math_review`.
This is a separately assigned internal AI review, not human peer review.
The reviewer did not propose or author the cubic simplification. The agent
is identified as Codex; an exact underlying model release is not exposed in
this context. Review tools included local Git, filesystem/shell access,
Python exact arithmetic and Node-based reproduction. No subagent was used.

**Decision: accepted within the stated conditional local scope.** The new
four-gate segment is pointwise equivalent to the previous five-gate segment
over the rationals, fixes all common coordinates, and preserves the actual
downstream weights. The complete default construction has 380 variables and
682-digit coefficients. Composition with the precisely identified order-47
route has 383 variables and 646-digit coefficients. No material mathematical
objection remains within this scope. The inherited arithmetic theorem,
current-manuscript incorporation, general circuit optimality and designated
App acceptance are not established by this review.

## Frozen sources

Reviewed commit: `31563264ba3dfbc3f00b4b08c099e9380caacd42`.
Parent research head: `772fe96a0e65bee76db500d8ef3a7a6b5e884d1f`.
The only additions relative to that parent are the 13-file
`research/detector-cube-reuse` packet and its separate CI workflow. All
previous mathematical packets, consumers, workflows, current manuscript and
acceptance records are unchanged. The policy-only merge ancestry is present.

Principal SHA-256 bindings:

| File in the new packet | SHA-256 |
| --- | --- |
| `PROOF.md` | `e91bffcf999c5862b04903beac1e28675ecbfc5eb92c2921c68576af09989aa6` |
| `APPLICATION_CONTRACT.json` | `bebd3e9bceca3ef7dbd6dcc87d6f95ce9dc9d033bd2225bf62da2f0a421cadad` |
| `cube_patch.py` | `cfde5a2e6e9afbd655a85af529a1a285560eb80347ad41653b6d0018628e02b7` |
| `check_cube.py` | `c03630d1144a5ef59e7d1d8319e27c531748b55f85756ef831d0e30920f50124` |
| `reproduce.py` | `161f6a988b927dab54efee33dfbc319ee00a58def7d6c8d899b08f5b84c6191e` |
| `EXPECTED.json` | `269c9157b8955414cfd05272c5f10d525742b6643908ad5eebbadfd7b823b095` |
| `SOURCE_BINDINGS.json` | `23462ef0798ba6f9cb73bc7ccf1b21184fc9b98356c1a834dd154937841ed8d7` |

`SOURCE_HASHES.json` records all 62 bound committed files, the external
manifest/digest, protocols, exact edit fingerprint and source-comparison
results. All bound paths exist as matching committed blobs. The entire new
packet is covered except the manifest itself and its separate digest.

I read the actual builder assignments and detector loop, the round-seven
normalization and nonzero-domain argument, the new proof, all nine contract
obligations, patch/check/replay implementations, the supplying scalar-chain
and preparation-zero arguments, the verbatim precision-51 proof, the conic
transport and diagonal-scaling consumers, and the research handoff. The
earlier mathematical reports were used to locate evidence and preserve
their conditional scopes, not as a substitute for comparing this changed
route. `AGENTS.md` and both applicable review protocols were read.

## The affine cubic and exact maps

The actual builder evaluates the monic five-contact polynomial with
`t2=t^2` and

```
M=t2*(t+c4)+c3*t+c2.
```

The assignment routine materializes the quadratic part in a coordinate and
retains lower-degree terms as affine aliases. Thus the semantic `M` really
is affine in allocated coordinates. It follows from its actual defining
row that

```
t3=M-c4*t2-c3*t-c2=t^3,
delta3=98^3*t3-3*98^2*t2+3*98*t-1=(98t-1)^3.
```

This is not treating an arbitrary cubic polynomial as a quadratic gate.
It reuses a particular previously materialized product. The independent
checker I wrote decodes the actual aliases into the polynomial ring
`Q[t,q1,q12]` and verifies the normalized defining rows for every detector.
The alias introduces no coordinate or new defining row.

Write `delta=98t-1`, `e=q1*delta`, and retain the actual relation
`E=q1*delta^2`. Here E is the weight, not the anchor exponent. The old rows
give

```
mixA=E^2, mixB=E^3,
mixC=E^3*q1^3=e^6, mixD=mixC^2=e^12,
E*q12=mixD^2=e^24.
```

The new rows give

```
e3=q1^3*delta3=e^3, e6=e3^2=e^6, e12=e6^2=e^12,
E*q12=e12^2=e^24.
```

For an old solution keep all common coordinates, set the new `e3` by its
displayed formula, and set `e6=mixC`, `e12=mixD`. For a new solution restore
`mixA=E^2`, `mixB=E^3`, `mixC=E^3*q1^3`, `mixD=mixC^2`. The equations imply
`mixC=e6` and `mixD=e12`. These maps supply unique private gate extensions
and are inverse over the common-coordinate projection. The input coordinate
and the shared `q12` are fixed.

The cleared final equation is identical without dividing by E. In
particular, even if `q1=0` or `delta=0`, both cleared circuits impose the same
zero equation on a free `q12`; there is no hidden cancellation discarding
a branch. On the actual arithmetic domain the unchanged source proves
`delta>=39/25`, `A>0`, and `q1*F=A*(A*delta)^4>0`; the nonnegative contact
factors give `F>0`, hence `q1,E>0`. This supplies the stated quotient
interpretation and uniqueness of `q12` in the complete construction.
No division by `delta3`, a point parameter or a private pole witness is
introduced.

## Source applications and actual consumers

| Obligation | Independent assessment |
| --- | --- |
| Source hypotheses | The actual `Fsquare`, `Fmiddle`, q1-cube and E rows supply precisely the identities used. The inherited positive chart supplies the same nonzero domains. |
| Constructed objects | The new object is an affine alias of stored coordinates, followed by three quadratic assignments and the existing cleared quotient. It is not an additional cubic coordinate. |
| Domain and index coverage | Both maps cover every old/new allowed solution and all three detector blocks. No curve point, prime or label is omitted. The local substitution introduces no new infinite index family. |
| Transition maps | The formulas above identify `mixC=e6`, `mixD=e12` and preserve q12 exactly. There is no omitted scalar, sign, field norm or change of normalization. |
| Consumed object | All shared semantic aliases, all guards and every outside raw row agree after decoding coordinate names. The surviving q12, its square, high weights, grouped factors, reciprocal trace and physical pole inputs are the same objects. |
| Coefficients and conventions | The construction remains over Q, with the same K=Q(sqrt(2)) interpretation. The first new product multiplies a stored q1-cube by an affine alias, so all residuals remain quadratic. The input-fixed compiler, conic and diagonal maps retain their existing conventions. |
| Local conditions | Default order 45 changes no detector order, contact radical, scalar depth, anchor, finite modulus or real neighborhood. Optional order 47 is the exact previously reviewed source followed by this pointwise map. |
| Exceptional cases | The cleared-row comparison covers zero E/q1/delta algebraically; the actual positive source excludes them as denominators. Identity primary points, private conic zeros, small primes and the split-41 scalar case retain their existing data and arguments. |
| Downstream consumption | Complete builds and independent coefficient expansion establish the stated output counts and coefficient maxima. The arithmetic completeness/soundness transfer follows from the explicit maps and unchanged consumers, not from those computations alone. |

Twelve old private rows are deleted, nine new private rows are added, and
only three common q12-definition rows change. For default order 45, the
remaining 352 raw rows are identical; for optional order 47, 355 are
identical. My check also verifies that **every common semantic alias** and
every guard is unchanged, not just that the row counts agree. All three
q1-cubes remain present and consumed. No saving is inferred by subtracting
an informal gate estimate: the raw saving of three coordinates persists
through the complete compile, two-slot omission, four conic transports and
diagonal map.

For the default route the sixteen field tests, their orders and actual
values are unchanged. Thus the common-place detector, opposite-place and
small-prime cases, physical pole bounds, order-31 scalar norm, preparation
zero and its simultaneous real/finite choices retain their precise inputs.
The actual constructed shared point H is fixed by the map. The scalar,
Lucas and input height consumers see the same labels and anchor 2130.
Positivity used in the factored-conic zero branch remains positivity of the
same physical inputs. This establishes both soundness and completeness
transfer without a fresh existence or approximation argument.

## Optional order 47 composition

The optional uncubed builder and raw IR equal byte-for-byte the ones in my
earlier independent order-47 replay of
`bc51100fd3ada82df0dac55d6f1d235219430c74`. The default uncubed builder and raw
IR likewise equal the independently reviewed preparation-zero source. The
fresh replay generates these actual baselines, rather than relying on a
prototype directory name. `COEFFICIENT_CHECKS.json` records their hashes.

The supplying precision proof is verbatim at its recorded original hash
`e6a825c3b85a9c56a6a2678ad0fa411ecedec53a005a0464efb45677f056054c`.
I reread its full omitted-tail argument, not only the statement “precision
51.” Its a13 denominator gives valuation at least -1 at every admitted
prime; every j>=14 term is controlled by
`4jr-floor((4j+1)/10)>=51r`, with bounds tending to infinity. The depth-one
p=53 obstruction still prevents a uniform precision-52 claim.

The two-anchor argument still uses the actual integral ratios with h and
h-1, transfers integrality through the cross congruence, and covers every
primary identity point by the guarded alternate root. The unchanged
`Pi^46` CRT progression is compatible with the fixed finite conditions and
the real neighborhood from preparation zero. The actual scalar point and
pole inputs are preserved. The order-31 scalar, order-47 Lucas and
order-12 input height comparisons still use the stated H, alpha=577/32 and
anchor `3^2016`; no changed estimate is needed here.

Indeed `mixedHigh=q12^2` is preserved, so `highLift=mixedHigh*E` and
`q47=highLift^2/q1` are preserved exactly. The cubic substitution therefore
composes with that specific reviewed local route. It does not upgrade an
order-45 proof at anchor 2016 or infer correctness from a smaller output
coefficient. The optional result meets the former 383-variable target with
smaller coefficients; it still costs three variables compared with the new
380-variable default. There is no general circuit-minimality conclusion.

## Reproduction and coefficient evidence

I ran both complete replays from the reviewed computational sources into
new directories:

```
python3 -B research/detector-cube-reuse/reproduce.py --output /tmp/quartic-cube-review/order45
python3 -B research/detector-cube-reuse/reproduce.py --order 47 --output /tmp/quartic-cube-review/order47
```

Both exited successfully, including fresh uncubed/cubed builders, four
mutation controls, every gate/compiler operation, two unused slots,
factored conics, diagonal rows and full coefficient checks. Python 3.12.3
and Node 18.19.1 were available locally; this is a local platform replay,
not an independent attestation of GitHub CI.

My independent scripts import no author checker. `independent_check.py`
verifies actual old/new normalized rows in `Q[t,q1,q12]`, with q12 left free,
including the zero cases and all common aliases/guards/outside rows.
`check_coefficients.py` separately expands each primitive row square using
diagonal and doubled cross terms, compares every coefficient with the JSON
quartic and parses every data line in the full decimal table.

| Route | Variables | Rows | Monomials | Maximum absolute coefficient |
| --- | ---: | ---: | ---: | --- |
| 45 / anchor 2130 | 380 | 349 | 26,025 | `28902*3^1420`, 682 digits, 2266 bits |
| 47 / anchor 2016 | 383 | 352 | 26,043 | `28902*3^1344`, 646 digits, 2146 bits |

Both quartics have degree four, integer content one, coefficient one on the
input's fourth power, and every coordinate active. All transformations fix
the input. Decimal-table SHA-256 values are respectively
`373c624d3b1293809e521ab8113052ff473f1b14ea1cde2facb361979515f6e5` and
`8ac84ab634f1636110d9c33df9613612110b44b6e9a044469873b51ef0e91ebc`.
The existing audit-history self-test also passed its historical/current
record checks and 26 negative controls. None of these finite or structural
checks proves an inherited arithmetic theorem.

## Assembly correction and handoff scope

An exploratory import by this reviewer initially generated an ignored
Python cache file. The author's draft inventory accidentally included it,
which would have made source verification fail in a fresh checkout. I
reported that defect. The final commit removes the cache path and file and
records the correction in `FINDINGS.json`; every final bound path is now a
matching committed blob. The construction, checker, proof, contract and
expected outputs are byte-identical to the versions used by the completed
replays. I explicitly acknowledge the corrected final source binding above;
no mathematical repair or refreshed historical approval is involved.

The prototype `baseline383` directory held a cubed candidate. It is not
treated as the pre-cube comparison source or published evidence. The final
runner's fresh `baseline/` outputs equal the previously reviewed uncubed
sources, and those exact hashes are recorded in my checks. This resolves
the provenance ambiguity without relying on a stored PASS label.

The new handoff correctly extends the parent cumulative research archive,
preserves original reports and rejected searches, and provides the actual
new proof, specification, contracts, findings and generator representation.
The optional old count of 386 is retained in the verbatim supplying proof
with its historical meaning. The new 380/383 claims are explicitly
conditional research pending manuscript incorporation. Neither crosses the
next below-300 optimization milestone or replaces the current Version 13
claim, so the previously reviewed reasons for leaving current release
surfaces unchanged still apply. The new source-manifest and research duties
remain applicable and have not been waived by that scope decision.

Public readback, the designated App's exact-revision check and future
received-review reconciliation remain separate. The new CI workflow and
local checks do not authorize that App. Inherited global inputs, full
published-source coverage, attribution questions, Kato/current-source
integration, the old stdout incident's root cause, final assembled-proof
closure and official manuscript/release synchronization retain their stated
open status. No current acceptance register or earlier independent report
was changed by this reviewer.
