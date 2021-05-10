from decimal import Decimal
from fractions import Fraction
from typing import TypeVar, Iterable

import mymax
from mymax import LessT

import pytest


NumberT = TypeVar('NumberT', float, Decimal, Fraction)


@pytest.mark.parametrize(
    'a, b, expected',
    [
        (1, 2, 2),
        (-3, -1, -1),
        (4, 4, 4),
    ],
)
def test_two_ints(a: int, b: int, expected: int) -> None:
    result = mymax.max(a, b)
    assert result == expected


def test_two_numbers() -> None:
    result = mymax.max(Fraction(1, 3), Fraction(1, 4))
    assert result == Fraction(1, 3)


@pytest.mark.parametrize(
    'a, b, expected',
    [
        (1, 2, 2),
        (0.1, 0.01, 0.1),
        (Fraction(1, 3), Fraction(1, 2), Fraction(1, 2)),
        (Decimal('-1.3'), Decimal('-1.2'), Decimal('-1.2')),
    ],
)
def test_two_numbers_params(a: NumberT, b: NumberT, expected: NumberT) -> None:
    result = mymax.max(a, b)
    assert result == expected


def test_two_comparables() -> None:
    result = mymax.max('a', 'B')
    assert result == 'a'


@pytest.mark.parametrize(
    'a, b, expected',
    [
        ('ab', 'ac', 'ac'),
        ([1, 2, 3], [1, 3], [1, 3]),
        ({1, 2, 3}, {1, 3}, {1, 2, 3}),
    ],
)
def test_two_comparables_params(a: LessT, b: LessT, expected: LessT) -> None:
    result = mymax.max(a, b)
    assert result == expected


@pytest.mark.parametrize(
    'first, rest, expected',
    [
        (7, [], 7),
        ('ab', ['ac', 'aa'], 'ac'),
        (9, [3, 1, 2], 9),
    ],
)
def test_multi_params(first: LessT, rest: Iterable[LessT], expected: LessT) -> None:
    result = mymax.max(first, *rest)
    assert result == expected
