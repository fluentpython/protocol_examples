from typing import Protocol


# T = TypeVar('T')  # <1>

class Repeatable(Protocol):
    def __mul__[T](self: T, repeat_count: int) -> T: ...  # <2>


# RT = TypeVar('RT', bound=Repeatable)  # <3>

def double[RT: Repeatable](x: RT) -> RT:  # <4>
    return x * 2
