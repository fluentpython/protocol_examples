# protocol_examples

Examples using `typing.Protocol` from PEP 544

## Notes

### Classic Example: a "file-like object"

From [_PEP 333 – Python Web Server Gateway Interface v1.0_](https://peps.python.org/pep-0333/) (2003):


>    To be considered “file-like”, the object supplied by the application
must have a `read()` method that takes an optional size argument.

The words "file-like" (or "file like") appear with similar implied meaning
in the Python 3.12 distribution:

- 148 times in the documentation;
- 92 times in code comments (`.py` or `.c` source files).

Also, 30 times across 21 PEPs (100, 214, 258, 282, 305, 310, 333, 368, 400, 441, 444, 578, 680, 691, 3116, 3119, 3143, 3145, 3154, 3156, 3333).


Definition in `Lib/wsgiref/types.py`:

```python
class _Readable(Protocol):
    def read(self, size: int = ..., /) -> bytes: ...
```

### Examples as of 2024-05-23

`typing.Protocol` definitions found with `ripgrep`:

```shell
rg "Protocol\)" -g '*.pyi' | sort
```

- 120 definitions on `typeshed/stdlib` (Python standard library)
- 134 definitions on `typeshed/stubs` (external packages)



### Cases to study

- `importlib/resources/abc.py`: `class Traversable(Protocol)`
with several abstract and concrete methods, looks like an ABC but derives from `typing.Protocol`


### Not `typing.Protocol`

- `asyncio/protocols.py`: defines classes `BaseProtocol`, `Protocol` etc. for network protocols



