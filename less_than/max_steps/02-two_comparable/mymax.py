"""
Q: What is "comparable" in Python?

::
    >>> o1 = object()
    >>> o2 = object()
    >>> sorted([o1, o2])
    Traceback (most recent call last):
      ...
    TypeError: '<' not supported between instances of 'object' and 'object'


A: Objects that implement ``<`` are comparable.
"""


from decimal import Decimal
from fractions import Fraction
from typing import TypeVar, Protocol, Any


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...


LessT = TypeVar('LessT', bound=SupportsLessThan)


# Refactoring needed in ternary op. Use < instead of >= to prevent:
# mymax.py:...: error: Unsupported left operand type for >= ("LessT")
def max(a: LessT, b: LessT) -> LessT:
    return a if b < a else b

