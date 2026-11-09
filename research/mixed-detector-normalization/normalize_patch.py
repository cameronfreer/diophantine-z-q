"""Use the older delta^-3 normalization only for the six high tests.

Input is the actual order-45 builder after inherited substitutions.
"""
import re


def transform(source):
    old = "let q45=rquot('detector'+r+'.q45',sq(mixedHigh),q1cube,'positive_order_one_weight');"
    new = "let q45=rquot('detector'+r+'.q45',sq(mixedHigh),q1,'positive_order_one_weight');"
    assert source.count(old) == 1
    result = re.sub(r'\b45\b', '46', source.replace(old, new))
    return result.replace('q45', 'q46').replace('E45', 'E46')
