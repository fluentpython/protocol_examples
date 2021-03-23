import mymax
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
