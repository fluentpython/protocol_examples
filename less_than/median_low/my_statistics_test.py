from math import isclose

from new_statistics import median_low


class SortableThing:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f'SortableThing({self.value})'


def test_float() -> None:
    l = [1 / n for n in range(1, 10)]
    m = median_low(l)
    assert isclose(m, 1 / 5)


def test_str() -> None:
    l = list('abcd')
    m = median_low(l)
    assert m == 'b'


def test_sortable_thing() -> None:
    l = [SortableThing(n) for n in range(1, 8)]
    m = median_low(l)
    print(m)
    assert m.value == 4
