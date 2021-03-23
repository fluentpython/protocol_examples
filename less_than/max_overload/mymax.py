# tag::MYMAX_TYPES[]
from typing import Protocol, Any, TypeVar, overload, Callable, Iterable, Union

class _SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

_T = TypeVar('_T')
_LT = TypeVar('_LT', bound=_SupportsLessThan)
_DT = TypeVar('_DT')

MISSING = object()
EMPTY_MSG = 'max() arg is an empty sequence'

@overload
def max(__arg1: _LT, __arg2: _LT, *_args: _LT, key: None = ...) -> _LT:
    ...
@overload
def max(__arg1: _T, __arg2: _T, *_args: _T, key: Callable[[_T], _LT]) -> _T:
    ...
@overload
def max(__iterable: Iterable[_LT], *, key: None = ...) -> _LT:
    ...
@overload
def max(__iterable: Iterable[_T], *, key: Callable[[_T], _LT]) -> _T:
    ...
@overload
def max(__iterable: Iterable[_LT], *, key: None = ..., default: _DT) -> Union[_LT, _DT]:
    ...
@overload
def max(__iterable: Iterable[_T], *, key: Callable[[_T], _LT], default: _DT) -> Union[_T, _DT]:
    ...
# end::MYMAX_TYPES[]
# tag::MYMAX[]
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
# end::MYMAX[]

@overload
def min(__arg1: _LT, __arg2: _LT, *_args: _LT, key: None = ...) -> _LT:
    ...
@overload
def min(__arg1: _T, __arg2: _T, *_args: _T, key: Callable[[_T], _LT]) -> _T:
    ...
@overload
def min(__iterable: Iterable[_LT], *, key: None = ...) -> _LT:
    ...
@overload
def min(__iterable: Iterable[_T], *, key: Callable[[_T], _LT]) -> _T:
    ...
@overload
def min(__iterable: Iterable[_LT], *, key: None = ..., default: _DT) -> Union[_LT, _DT]:
    ...
@overload
def min(__iterable: Iterable[_T], *, key: Callable[[_T], _LT], default: _DT) -> Union[_T, _DT]:
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
