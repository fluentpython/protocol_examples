import sys
from typing import (
    TypeVar, overload, Optional, 
    Any, Iterable, Callable, List, Protocol
)

class _SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

_T = TypeVar('_T')
_T1 = TypeVar('_T1')
_LT = TypeVar('_LT', bound=_SupportsLessThan)

if sys.version_info >= (3,):
    @overload
    def sort(
        self: List[_LT],
        *, 
        key: None = ...,
        reverse: bool = ...,
    ) -> None: ...
    @overload
    def sort(
        self,
        *, 
        key: Callable[[_T], _LT],
        reverse: bool = ...,
    ) -> None: ...
else:
    def sort(
        self,
        cmp: Optional[Callable[[_T, _T1], Any]] = ..., 
        key: Optional[Callable[[_T], Any]] = ..., 
        reverse: bool = ...,
    ) -> None: ...


if sys.version_info >= (3,):
    @overload
    def sorted(
        iterable: Iterable[_LT], 
        key: None = ..., 
        reverse: bool = ...
    ) -> List[_LT]: ...
    @overload
    def sorted(
        iterable: Iterable[_T], 
        key: Callable[[_T], _LT], 
        reverse: bool = ...
    ) -> List[_T]: ...
else:
    def sorted(
        iterable: Iterable[_T],
        cmp: Optional[Callable[[_T, _T1], Any]] = ..., 
        key: Optional[Callable[[_T], Any]] = ...,
        reverse: bool = ...
    ) -> List[_T]: ...
