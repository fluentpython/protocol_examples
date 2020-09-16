"""
A ``bingo.Cage`` holds integers from 1 to 75, and provides a ``pick`` method
that pops one random integer each time it's called, without repeating.

    >>> n = 75
    >>> balls = set(range(1, n + 1))
    >>> cage = Cage()
    >>> picked = []
    >>> for _ in range(n):
    ...    ball = cage.pick()
    ...    assert ball in balls
    ...    picked.append(ball)
    ...
    >>> set(picked) == balls
    True
    >>> picked != sorted(picked)
    True

When exhausted, ``pick`` raises ``LookupError``:

    >>> cage.pick()
    Traceback (most recent call last):
      ...
    LookupError: no more items

"""

from typing import List
import random

class Cage():
    def __init__(self) -> None:
        self._balls: List[int] = list(range(1, 76))
        random.shuffle(self._balls)

    def pick(self) -> int:
        try:
            return self._balls.pop()
        except IndexError as e:
            raise LookupError('no more items') from e
