from typing import TypeVar, Protocol, Any


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...


def max(a: SupportsLessThan, b: SupportsLessThan) -> SupportsLessThan:
    if b < a:  # refactored to use <
        return a
    return b

