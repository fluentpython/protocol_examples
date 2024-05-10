from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')

def double(x: Sequence[T]) -> Sequence[T]:
    return x * 2
