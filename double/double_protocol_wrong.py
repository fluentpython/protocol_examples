from typing import TypeVar, Protocol

T = TypeVar('T')  # <1>

class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T: ...  # <2>

def double(x: Repeatable) -> Repeatable:  # <3>
    return x * 2
