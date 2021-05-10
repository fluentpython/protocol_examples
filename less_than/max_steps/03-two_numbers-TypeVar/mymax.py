from decimal import Decimal
from fractions import Fraction
from typing import TypeVar

NumberT = TypeVar('NumberT', float, Decimal, Fraction)


def max(a: NumberT, b: NumberT) -> NumberT:
    if a >= b:
        return a
    return b
