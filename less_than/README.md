# Protocol: Supports Less Tham


A PEP 544 protocol to support type hints for functions that depend on items
implementing `__lt__`—any function that relies on sorting, for example.

```python
class _SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

_T = TypeVar('_T')
_T1 = TypeVar('_T1')
_LT = TypeVar('_LT', bound=_SupportsLessThan)
```


## Example: sorted()

### Python 3

```python
@overload
def sorted(__it: Iterable[_LT], *,
           key: None = ...,
           reverse: bool = ...) -> List[_LT]: ...
@overload
def sorted(__it: Iterable[_T], *,
           key: Callable[[_T], _LT] = ...,
           reverse: bool = ...) -> List[_T]: ...
```


| hint | prevents bug |
| ---- | ----- |
| `it: Iterable[_T]`  | `it` is not iterable |
| `it: Iterable[_LT]` | `_LT` doesn't implement `__lt__` |
| `key: Optional[Callable[[_T], _LT]]` | `key` is not callable or `None`|
|                                      | `key` is callable with arity ≠ 1 |
|                                      | `key` returns type that doesn't implement `__lt__` |


### Python 2

```python
def sorted(__it: Iterable[_T], *,
           cmp: Optional[Callable[[_T, _T1]], float] = ...,
           key: Optional[Callable[[_T], Any]] = ...,
           reverse: bool = ...) -> List[_T]: ...
```


| hint | prevents bug |
| ---- | ----- |
| `it: Iterable[_T]` | `it` is not iterable |
| `cmp: Callable[[_T, _T1], float]` | `cmp` is not callable  |
|                                   | `cmp` is callable with arity ≠ 2 |
|                                   | `cmp` does not return `float` |
| `key: Callable[[_T], Any]]` | `key` is not callable |
|                             | `key` is callable with arity ≠ 1 |


## Example: list.sort()

### Python 3

```python
class list(MutableSequence[_T], Generic[_T]):
    ...
    @overload
    def sort(self: List[_LT], *,
             key: None = ...,
             reverse: bool = ...) -> List[_LT]: ...
    @overload
    def sort(self, *,
             key: Callable[[_T], _LT] = ...,
             reverse: bool = ...) -> List[_T]: ...
```


| hint | prevents bug | test |
| ---- | ------------ | ---- |
| `self: List[_LT]` | `_LT` doesn't implement `__lt__` | `test_sort_items_dont_support_less_than_py3` |
| `key: Callable[[_T], _LT]]` | `key` is not callable | `test_sort_key_not_callable` |
|                             | `key` is callable with arity ≠ 1 | `test_sort_key_wrong_arity` |
|                             | `key` returns type that doesn't implement `__lt__` | `test_sort_bad_key_return_py3` |


### Python 2

```python
class list(MutableSequence[_T], Generic[_T]):
    ...
    def sort(self, *,
            cmp: Optional[Callable[[_T, _T1]], float] = ...,
            key: Optional[Callable[[_T], Any]] = ...,
            reverse: bool = ...) -> List[_T]: ...

```


| hint | prevents bug | test |
| ---- | ------------ | ---- |
| `cmp: Optional[Callable[[_T, _T1], float]]` | `cmp` is not callable or `None` | |
|                                             | `cmp` is callable with arity ≠ 2 | `test_sort_list_str_bad_cmp_arity_py2` |
|                                             | `cmp` does not return `float` | |
| `key: Optional[Callable[[_T], Any]]` | `key` is not callable or `None` | |
|                                      | `key` is callable with arity ≠ 1 | |
