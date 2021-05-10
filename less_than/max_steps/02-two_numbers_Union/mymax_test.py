from decimal import Decimal
from fractions import Fraction
from numbers import Number

import pytest

import mymax as my


@pytest.mark.parametrize(
    'a, b, expected',
    [
        (1.1, 2.2, 2.2),
        (-3.1, -1.3, -1.3),
        (4.2, 4.2, 4.2),
    ],
)
def test_two_floats(a: float, b: float, expected: float) -> None:
    result: float = my.max(a, b)
    assert result == expected


def test_two_numbers() -> None:
    result = my.max(Fraction(1, 3), Fraction(1, 4))
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
def test_two_numbers_params(a: my.Number, b: my.Number, expected: my.Number) -> None:
    result = my.max(a, b)
    assert result == expected
