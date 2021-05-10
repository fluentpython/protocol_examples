from typing import TypeVar, Protocol, Any


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...


LessT = TypeVar('LessT', bound=SupportsLessThan)


def max(a: LessT, b: LessT) -> LessT:
    if b < a:  # refactored to use <
        return a
    return b

