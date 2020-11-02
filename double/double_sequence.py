from collections import abc
from typing import TypeVar

T = TypeVar('T')

def double(x: abc.Sequence[T]) -> Sequence[T]:
    return x * 2
