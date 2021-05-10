from decimal import Decimal
from fractions import Fraction
from typing import Union

Number = Union[float, Decimal, Fraction]


def max(a: Number, b: Number) -> Number:
    if a >= b:
        return a
    return b
