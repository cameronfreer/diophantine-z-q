# Follow-up investigations beyond the four-conic PR

These are separate research experiments on top of the 385-variable branch.
They do not alter the focused four-conic PR or the frozen parent package.
All proposed arithmetic changes remain conditional and independently
unaccepted.

| Implemented experiment | Before four conics | After four conics | Change from 385 |
| --- | ---: | ---: | ---: |
| Parent construction | 389 | 385 | 0 |
| Direct biquadratic-chart port | 389 | 385 | 0 |
| Sparse rational logarithm of relative precision 45 | 397 | 393 | +8 |
| Scalar `W=N`, preparation zero | 387 | **383** | **−2** |

The scalar candidate has 352 quadratic residuals, 26,045 quartic monomials,
and maximum coefficient `28902 * 3^1576`: 757 digits, 2,513 bits. Its table
SHA-256 is `d18ae3cf281081e9322969126864a8843f849f2c469e3f7c3b221ed3742166a4`.
Every variable occurs, its content is one, and its `x0^4` coefficient is one.
The full proposed argument and remaining review boundary are in
[SCALAR_ARGUMENT.md](SCALAR_ARGUMENT.md). The application contract is an
author submission for review, not an acceptance record.

Run all four experiments, gate replays, conic transports and complete
coefficient checks from the repository root:

```sh
python3 -B research/quartic-followup/reproduce.py
```

Python's standard library and Node suffice. Outputs and detailed results
go to a fresh directory under `build/`; `--output PATH` selects an absent
or empty directory. This rebuilds the baseline source and matches its
known compiled hash. It does not repeat the parent's entire 23-stage
arithmetic-report pipeline; that pipeline has already passed in the parent
and four-conic PR. Changed arguments require their own review.

The chart experiment retains the primary squared test `f_U=r^2`, which
the package really consumes, and replaces the alternate squared output
by `Y_V=g^4`. Its five scaled field values plus these outputs save no
coordinates against the package's existing fused chart/logarithm circuit.
It does reduce the quartic from 26,235 to 26,041 monomials at the same 385 variables. This measures this implementation, not a lower bound on every chart.

The logarithm experiment has exact order and positivity certificates in
[LOGARITHM.md](LOGARITHM.md). Denominators at 29, 37 and 41 are compatible
with the existing exception set at the required formal depths. However,
materializing and multiplying the new denominator costs two coordinates
per long logarithm after compilation. The original degree-12 completion
already eliminates its polynomial-output coordinates. The measured +8
supersedes the earlier unmeasured −8 estimate for this candidate; it is
not an impossibility result for other approximants or combined circuits.

The 383-variable scalar route is therefore the next proposed mathematical
stack. Keep it separate until its changed completeness argument has been
reviewed against the exact source hypotheses and consumers.
