from collections.abc import Iterable
from typing import Any, TypeVar, Protocol


class StatisticsError(ValueError):
    pass


class SupportsLessThan(Protocol):
    def __lt__(self, __other: Any) -> bool: ...


SupportsLessThanT = TypeVar('SupportsLessThanT', bound=SupportsLessThan)


def median_low(data: Iterable[SupportsLessThanT]) -> SupportsLessThanT:
    """Return the low median value of data."""
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError('no median for empty data')
    if n % 2 == 1:
        return data[n // 2]
    else:
        return data[n // 2 - 1]
