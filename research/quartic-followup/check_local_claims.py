"""Finite coefficient and valuation checks; not independent proof review."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse
import json


def bernstein(coefficients):
    degree = len(coefficients)-1
    return [sum(coefficients[j]*F(comb(i,j), comb(degree,j)) for j in range(i+1))
            for i in range(degree+1)]


def valuation(n, p):
    result = 0
    while n and n % p == 0:
        n //= p
        result += 1
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    a = [F(1), F(-2,5)]
    for j in range(2,14):
        a.append(a[-1]*F(4*j-5,4*j+1))
    q = [F(1), F(-68,29), F(11358,5945), F(-137172,219965), F(14421,219965)]
    n = [F(1), F(-398,145), F(48424,17835), F(-16398986,14297725),
         F(8855199,48612265), F(-131072,29167359), F(-32768,243061325), F(0),
         F(114688,105731676375)]
    errors = [sum(q[k]*a[j-k] for k in range(min(j,4)+1))-(n[j] if j<len(n) else 0)
              for j in range(13)]
    assert all(x == 0 for x in errors[:12])
    assert all(x > 0 for x in bernstein(q)+bernstein(n))
    exceptional = {2,3,5,7,13,17}
    # Trial division completely factors the finite denominators involved.
    def factors(value):
        result = {}; p = 2
        while p*p <= value:
            if value % p == 0:
                result[p] = valuation(value,p); value //= p**result[p]
            p += 1
        if value > 1: result[value] = 1
        return result
    assert all(e <= 1 for x in q for p,e in factors(x.denominator).items() if p not in exceptional)
    assert all(e <= 2 for p,e in factors(errors[12].denominator).items() if p not in exceptional)
    # For j=13+t, r=1+u, the coarse tail lower bound minus 45r is
    # 7/10 + (18/5)t + 7u + 4tu, with all coefficients nonnegative.
    assert 4*13-1-F(4*13+1,10)-45 == F(7,10)
    assert 48-2 >= 45
    rho = lambda x: 42*(2401+2754*(2*x+1)**2)*(2400+2754*(2*x+1)**2)*(32*(2401+2754*(2*x+1)**2)+343)
    assert all(rho(x)%32 == 4 for x in range(32))
    assert all(rho(x)%243 == 81 for x in range(243))
    assert all(rho(x)%17 == 13 for x in range(17))
    assert 8**2 % 17 == 13
    # Opposite-parity norm descent, recording strict rational multiples of R.
    N = F(-1,2); L=N/2; J=(N+15)/2
    A=(L+1)/2; lower_n=(L+2)/2
    B=(lower_n+2)/2; C=(lower_n+1)/2
    D0=J/2; y=(J+15)/2; T=y+16
    assert [L,J,A,lower_n,B,C,D0,y,T] == [F(-1,4),F(29,4),F(3,8),F(7,8),F(23,16),F(15,16),F(29,8),F(89,8),F(217,8)]
    assert 27 < T < 28
    report = {'status':'PASS','independentAcceptance':False,
              'rationalLog':{'Q':list(map(str,q)), 'N':list(map(str,n)),
                             'zeroErrorCoefficients':list(range(12)), 'firstError':str(errors[12]),
                             'QBernstein':list(map(str,bernstein(q))), 'NBernstein':list(map(str,bernstein(n))),
                             'errorDenominatorFactorization':factors(errors[12].denominator),
                             'relativeOrderAtLeast':45},
              'scalar':{'rhoMod32':4,'rhoMod243':81,'rhoMod17':13,
                        'strictProxyValuationMultiple':str(T),'scalarOrder':28},
              'scope':'Exact finite identities, Bernstein positivity and integer-polynomial congruences. Tail and simultaneous-completeness arguments are written separately.'}
    args.report.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: logarithm coefficients / positivity / tail margins and scalar congruences / order bounds')


if __name__ == '__main__':
    main()
