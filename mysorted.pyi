import sys
from typing import (
    TypeVar, overload, Optional, 
    Any, Iterable, Callable, List, Protocol
)

class _SupportsLestThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

_T = TypeVar('_T')
_LT = TypeVar('_LT', bound=_SupportsLestThan)

if sys.version_info >= (3,):
    def sort(
        self,  # type: list 
        *, 
        key: Optional[Callable[[_T], _LT]] = ...,
        reverse: bool = ...,
    ) -> None: ...
else:
    def sort(
        self,  # type: list
        cmp: Callable[[_T, _T], Any] = ..., 
        key: Callable[[_T], Any] = ..., 
        reverse: bool = ...,
    ) -> None: ...


if sys.version_info >= (3,):
    def sorted(
        iterable: Iterable[_LT], 
        key: None = ..., 
        reverse: bool = ...
    ) -> List[_LT]: ...
else:
    def sorted(
        iterable: Iterable[_T],
        cmp: None = ...,
        key: None = ...,
        reverse: bool = ...
    ) -> List[_T]: ...
