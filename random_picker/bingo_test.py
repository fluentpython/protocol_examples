from typing import Set, List

import pytest

from randompicker import RandomPicker
from bingo import Cage


def test_pick_in_range() -> None:
    n = 75
    expected_balls: Set[int] = set(range(1, n + 1))
    cage: Cage = Cage()
    ball: int = cage.pick()
    assert ball in expected_balls


def pick_all(rp: RandomPicker) -> List[int]:
    n = 75
    picked: List[int] = [rp.pick() for _ in range(n)]
    return picked


def test_pick_all() -> None:
    n = 75
    cage: Cage = Cage()
    picked: List[int] = pick_all(cage)
    assert len(picked) == n
    sorted_balls: List[int] = list(range(1, n + 1))
    assert picked != sorted_balls
    assert set(picked) == set(sorted_balls)

"""
Mypy flags an error in the following test::

    bingo_test.py:39: error: Argument 1 to "pick_all" has incompatible type "object"; expected "RandomPicker"
"""
def test_no_pick_method() -> None:
    with pytest.raises(AttributeError) as e:
        pick_all(object())
    assert "'object' object has no attribute 'pick'" in str(e.value)

"""
Mypy flags an error in the following test::

    bingo_test.py:59: error: Argument 1 to "pick_all" has incompatible type "StringPicker"; expected "RandomPicker"
    bingo_test.py:59: note: Following member(s) of "StringPicker" have conflicts:
    bingo_test.py:59: note:     Expected:
    bingo_test.py:59: note:         def pick(self) -> int
    bingo_test.py:59: note:     Got:
    bingo_test.py:59: note:         def pick(self) -> str
"""

class StringPicker():
    def pick(self) -> str:
        return 'A string'

def test_broken_pick_method_does_not_return_int() -> None:
    sp = StringPicker()
    result = pick_all(sp)
    assert not isinstance(result[0], int)
