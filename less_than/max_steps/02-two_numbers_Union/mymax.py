from decimal import Decimal
from fractions import Fraction
from typing import Union

Numeric = Union[float, Decimal, Fraction]


def max(a: Numeric, b: Numeric) -> Numeric:
    if a >= b:
        return a
    return b
