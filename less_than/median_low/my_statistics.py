from collections.abc import Iterable
from typing import Any, TypeVar, Protocol


class StatisticsError(ValueError):
    pass


class Sortable(Protocol):
    def __lt__(self, other: Any) -> bool: ...


SortableT = TypeVar('SortableT', bound=Sortable)


def median_low(data: Iterable[SortableT]) -> SortableT:
    """Return the low median value of data."""
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError('no median for empty data')
    if n % 2 == 1:
        return data[n // 2]
    else:
        return data[n // 2 - 1]
