# protocol_less_than
A PEP 544 protocol for parameterized typing of functions that sort


## sorted

### Python 3

```python
@overload
def sorted(__it: Iterable[_LT], *,
           key: None = ...,
           reverse: bool = ...) -> List[_LT]: ...
@overload
def sorted(__it: Iterable[_T], *,
           key: Optional[Callable[[_T], _LT]] = ...,
           reverse: bool = ...) -> List[_T]: ...
```


| hint | prevents bug |
| ---- | ----- |
| `it: Iterable[_T]` | `it` is not iterable |
| `it: Iterable[_LT]` | `_LT` doesn't implement `_SupportsLessThan` |
| `key: Optional[Callable[[_T], _LT]]` | `key` is not callable or `None`|
|                                      | `key` is callable with arity ≠ 1 |
|                                      | `key` returns type that doesn't implement `_SupportsLessThan` |


### Python 2

```python
def sorted(__it: Iterable[_T], *,
           cmp: Callable[[_T, _T], float] = ...,
           key: Optional[Callable[[_T], Any]] = ...,
           reverse: bool = ...) -> List[_T]: ...

```


| hint | prevents bug |
| ---- | ----- |
| `it: Iterable[_T]` | `it` is not iterable |
| `cmp: Callable[[_T, _T], float]` | `cmp` is not callable  |
|                                  | `cmp` is callable with arity ≠ 2 |
|                                  | `cmp` does not return `float` |
| `key: Optional[Callable[[_T], Any]]` | `key` is not callable or `None` |
|                                      | `key` is callable with arity ≠ 1 |
