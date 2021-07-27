from collections.abc import Iterable
from decimal import Decimal
from fractions import Fraction
from typing import TypeVar

_Number = TypeVar('_Number', float, Decimal, Fraction)


class StatisticsError(ValueError):
    pass


def median_low(data: Iterable[_Number]) -> _Number:
    """Return the low median value of data."""
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError('no median for empty data')
    if n % 2 == 1:
        return data[n // 2]
    else:
        return data[n // 2 - 1]
