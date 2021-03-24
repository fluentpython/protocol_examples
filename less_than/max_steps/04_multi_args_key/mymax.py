"""
Complex numbers don't support ``<``, but we can compare their
modulus a.k.a. absulute values:

    >>> a = 3+4j
    >>> b = 5+4j
    >>> max(a, b, key=abs)
    (5+4j)

"""

from typing import TypeVar, Protocol, Any, Callable, overload


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool:
        ...


T = TypeVar('T')
LessT = TypeVar('LessT', bound=SupportsLessThan)
KeyFun = Callable[[T], LessT]

@overload
def max(first: LessT, *rest: LessT, key: None = ...) -> LessT:
    ...
@overload
def max(first: T, *rest: T, key: KeyFun) -> T:
    ...
def max(first, *rest, key=None):
    candidate = first
    if key is None:
        for current in rest:
            if candidate < current:
                candidate = current
    else:
        candidate_key = key(candidate)
        for current in rest:
            current_key = key(current)
            if candidate_key < current_key:
                candidate = current
                candidate_key = current_key

    return candidate
