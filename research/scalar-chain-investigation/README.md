# Order-31 scalar chain: smaller coefficients above PR #9

This author research proposal changes the scalar norm tree at the same
coordinate cost. Its local descent gives order 31 instead of 28, allowing
the anchor to decrease from 3^2364 to 3^2130. The global arithmetic remains
conditional and the new application is pending independent review.

| Construction | Variables | Maximum coefficient digits | Monomials |
| --- | ---: | ---: | ---: |
| PR #9 | 385 | 757 | 26,235 |
| New scalar chain, general preparation | **385** | **682** | 26,200 |
| Chain combined with preparation zero | **383** | **682** | 26,019 |

Both new variants were built and checked. Their exact coefficient maximum
is `28902 * 3^1420`, with bit length 2,266. All variables occur, the degree
is four, the integer content is one, and the input fourth-power coefficient
is one. The four conic factorizations of #9 are included in both counts.

The 385-variable route retains the general scalar preparation. It can be
reviewed separately from the preparation-zero proposal's simultaneous
real/finite-place argument. That makes the scalar chain and smaller anchor
a focused next change above #9; preparation zero can follow separately.

Read [PROOF.md](PROOF.md) for the exact norm tree, valuation descent, finite
completeness transfer, and all three height consumers. The application
contract is an author submission, not an acceptance. The source checker
checks the actual raw rows, preserves all outside rows, and rejects five
negative controls; the original generic gate, conic-transport and diagonal
checkers then verify the complete finite construction.

From the repository root:

```sh
python3 -B research/scalar-chain-investigation/reproduce.py --output build/chain31-replay
```

The output directory must be absent or empty. This verifies the frozen
package's source manifest and rebuilds the two changed circuits. It does
not rerun the parent's entire 23-stage arithmetic-report pipeline or accept
the inherited theorem. Results and source versions are recorded alongside
this note. Neither upstream review PR is changed by this investigation.
