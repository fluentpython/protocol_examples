from collections.abc import Callable, Iterable
from typing import Protocol, Any, TypeVar, overload, Union

MISSING = object()
EMPTY_MSG = 'max() arg is an empty sequence'

class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

T = TypeVar('T')
LT = TypeVar('LT', bound=SupportsLessThan)
DT = TypeVar('DT')

@overload
def max(arg1: LT, arg2: LT, *_args: LT, key: None = ...) -> LT:
    ...
@overload
def max(arg1: T, arg2: T, *_args: T, key: Callable[[T], LT]) -> T:
    ...
@overload
def max(iterable: Iterable[LT], *, key: None = ...) -> LT:
    ...
@overload
def max(iterable: Iterable[T], *, key: Callable[[T], LT]) -> T:
    ...
@overload
def max(iterable: Iterable[LT], *, key: None = ..., default: DT) -> Union[LT, DT]:
    ...
@overload
def max(iterable: Iterable[T], *, key: Callable[[T], LT], default: DT) -> Union[T, DT]:
    ...
def max(first, *args, key=None, default=MISSING):
    if args:
        series = args
        candidate = first
    else:
        series = iter(first)
        try:
            candidate = next(series)
        except StopIteration:
            if default is not MISSING:
                return default
            raise ValueError(EMPTY_MSG) from None
    if key is None:
        for current in series:
            if candidate < current:
                candidate = current
    else:
        candidate_key = key(candidate)
        for current in series:
            current_key = key(current)
            if candidate_key < current_key:
                candidate = current
                candidate_key = current_key
    return candidate

@overload
def min(arg1: LT, arg2: LT, *_args: LT, key: None = ...) -> LT:
    ...
@overload
def min(arg1: T, arg2: T, *_args: T, key: Callable[[T], LT]) -> T:
    ...
@overload
def min(iterable: Iterable[LT], *, key: None = ...) -> LT:
    ...
@overload
def min(iterable: Iterable[T], *, key: Callable[[T], LT]) -> T:
    ...
@overload
def min(iterable: Iterable[LT], *, key: None = ..., default: DT) -> Union[LT, DT]:
    ...
@overload
def min(iterable: Iterable[T], *, key: Callable[[T], LT], default: DT) -> Union[T, DT]:
    ...
def min(first, *args, key=None, default=MISSING):
    if args:
        series = args
        candidate = first
    else:
        series = iter(first)
        try:
            candidate = next(series)
        except StopIteration:
            if default is not MISSING:
                return default
            raise ValueError(EMPTY_MSG) from None
    if key is None:
        for current in series:
            if current < candidate:
                candidate = current
    else:
        candidate_key = key(candidate)
        for current in series:
            current_key = key(current)
            if current_key < candidate_key:
                candidate = current
                candidate_key = current_key
    return candidate
