"""
Q: Why not define ``Number`` as follows?

::
    Number = Union[float, Decimal, Fraction]


A: Because ``Union`` is not helpful as a return type.

    "Be conservative in what you send, be liberal in what you accept."
    —Postel's Law

"""

from decimal import Decimal
from fractions import Fraction
from typing import TypeVar

NumberT = TypeVar('NumberT', float, Decimal, Fraction)


def max(a: NumberT, b: NumberT) -> NumberT:
    return a if a >= b else b
