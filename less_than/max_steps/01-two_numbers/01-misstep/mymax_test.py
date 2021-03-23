from decimal import Decimal
from fractions import Fraction

import mymax
from mymax import Number

import pytest


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
def test_two_numbers_params(a: Number, b: Number, expected: Number) -> None:
    result = mymax.max(a, b)
    assert result == expected
