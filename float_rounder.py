# float_rounder.py

import math, decimal

# multiplying an int by a float when the product is a decimal between -1 and 1
def multiplyByFloat(n,multiplier):
    d = decimal.Decimal(str(multiplier))
    d2 = decimal.Decimal(str(n))
    numOfDecimals = (d.as_tuple().exponent + d2.as_tuple().exponent) * -1
    n = int(n * (10 ** numOfDecimals))
    multiplier = int(multiplier * (10 ** numOfDecimals))
    if round((n * multiplier)/(10 ** (numOfDecimals*2)),numOfDecimals) == int(round((n * multiplier)/(10 ** (numOfDecimals*2)),numOfDecimals)):
        return int(round((n * multiplier)/(10 ** (numOfDecimals*2)),numOfDecimals))
    else:
        return round((n * multiplier)/(10 ** (numOfDecimals*2)),numOfDecimals)
