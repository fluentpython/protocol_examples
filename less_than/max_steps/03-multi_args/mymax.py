from typing import TypeVar, Protocol, Any


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...


LessT = TypeVar('LessT', bound=SupportsLessThan)


def max(first: LessT, *rest: LessT) -> LessT:
    candidate = first
    for current in rest:
        if candidate < current:
            candidate = current
    return candidate
