# Higher detector precision: a measured coefficient tradeoff

Above #12's 383-variable preparation-zero layer, the existing long logarithm
supports uniform relative precision 51 at the retained primes. Two complete
compiled circuits exploit orders 46 and 47:

| Variant | Variables | Residuals | Monomials | Maximum coefficient digits / bits |
| --- | ---: | ---: | ---: | ---: |
| #12, order 45 | 383 | 352 | 26,019 | 682 / 2266 |
| Order 46, anchor 2016 | 386 | 355 | 26,046 | 646 / 2146 |
| Order 47, anchor 2016 | 386 | 355 | 26,037 | 646 / 2146 |

These are research alternatives, not a replacement for #12's better variable
count. The additional cost is one weight coordinate per detector. We have not
established a higher-order circuit at the original variable count or a general
lower bound preventing one. No claim of circuit optimality is made.

The [proof](PROOF.md) covers the tail, exact weight identities, actual label
comparisons, simultaneous real/finite completeness and all three height
consumers. The [application contract](APPLICATION_CONTRACT.json) and
[source bindings](SOURCE_BINDINGS.json) freeze the arguments and their inputs.
The inherited global arithmetic is conditional; no current-manuscript
acceptance is created by this packet.

Reproduce either alternative from the repository root (Python 3 and Node,
no network or third-party packages):

```sh
python3 -B research/higher-detector-precision/experiment.py --order 46 --exponent 2016 --output build/higher46
python3 -B research/higher-detector-precision/experiment.py --order 47 --exponent 2016 --output build/higher47
```

Use absent or empty output directories. The replay verifies the source hashes,
builds the unchanged parent for raw comparison, reconstructs the new weights,
checks all other raw rows and guards, rejects three source mutations, replays
the compiler, proves the unused-coordinate omission, transports all four
conics, and reconstructs every scaled row and quartic coefficient. Expected
outputs are frozen in `EXPECTED.json`. Finite checks do not establish the
uniform arithmetic proof.

Order 51 is the best uniform relative bound for this fixed truncation: at the
admitted prime 53 and formal depth one its error has valuation exactly 51.
This concerns the local truncation lemma, not optimality of other logarithms.
For the displayed scalar margin, moving beyond order 46 does not reduce the
selected anchor further. A useful next variable-saving search therefore has
to change the shared weight circuit or another part of the construction.
