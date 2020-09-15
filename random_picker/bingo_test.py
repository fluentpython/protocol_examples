from typing import Set, List

from bingo import Cage


def test_pick_in_range() -> None:
    n = 75
    expected_balls: Set[int] = set(range(1, n + 1))
    cage: Cage = Cage()
    ball: int = cage.pick()
    assert ball in expected_balls


def pick_all(rp: RandomPicker) -> List[int]
    n = 75
    picked: List[int] = [rp.pick() for _ in range(n)]
    return picked


def test_pick_all():
    n = 75
    expected_balls: List[int] = list(range(1, n + 1))

    picked: List[int] =
