# An order-45 rational logarithm and its measured cost

This is an internal exact computation, not independent acceptance of a
changed arithmetic construction. It uses the recurrence and coefficient
bound in the parent's `proofs/prior/round5/geometry_round5.tex`, referring
to Version 10 lines 9220–9258, and the actual order-45 consumer in
`proofs/arithmetic_round7.tex`, lines 95–107. The sparse-evaluation idea
comes from Version 13's `addition.tex`, “Rational logarithms”.

Write `G(w)=sum a_j w^j`, with `a_0=1`, `a_1=-2/5` and
`a_j/a_(j-1)=(4j-5)/(4j+1)`. Exact linear algebra gives

```
Q(w) = 1 - (68/29)w + (11358/5945)w^2
       - (137172/219965)w^3 + (14421/219965)w^4,
N(w) = 1 - (398/145)w + (48424/17835)w^2
       - (16398986/14297725)w^3 + (8855199/48612265)w^4
       - (131072/29167359)w^5 - (32768/243061325)w^6
       + (114688/105731676375)w^8.
```

All coefficients of `QG-N` through degree 11 vanish, including the
constraint that `N` has no degree-seven term. Both polynomials have
strictly positive Bernstein coefficients on `[0,1]`, verified exactly.
Thus `Q` is nonzero and `N/Q` is positive on the retained doubled-point
real domain. This does not address Version 13's enlarged H domain,
which is not used here.

At a consumed unramified place above `p>=11`, `p!=13,17`, let the formal
depth be `r>=1`, so `v(w)=4r`. Every nonconstant coefficient of `Q` has
valuation at least −1. Hence `Q(w)=1 mod p` and is a unit even at
29, 37 and 41. These primes do not need to be excluded merely because
they divide a coefficient denominator.

The coefficient of degree 12 in `QG-N` has denominator valuation at
most two outside the existing exceptional set, so its term has valuation
at least `48r-2>=45r`. For `j>=13`, the inherited bound
`v(a_j)>=-(4j+1)/(p-1)` and the finite denominator bound for `Q` give

```
v([w^j](QG-N) w^j) >= 4jr - 1 - (4j+1)/10 >= 45r.
```

For `j=13+t`, `r=1+u`, the final margin is
`7/10 + (18/5)t + 7u + 4tu`, which is nonnegative and tends to infinity
with `j`. Division by the unit `Q(w)` preserves the bound. Multiplication
by the formal parameter adds `r`, giving absolute logarithm precision
at least `46r`. The identity point has exact zero error. The finite
checker records every coefficient identity, Bernstein coefficient and
finite denominator bound used here.

The circuit result is less favorable: using the quadratic basis in
`w,w^2,w^4`, the new denominator and its product with the chart denominator
survive compilation. Each long logarithm has twelve rational coordinates
where the parent has ten. The four replacements therefore give 397
variables before the four conics, or 393 afterwards. This candidate
establishes local feasibility without enlarging the exception set, but
does not lower the variable count.
