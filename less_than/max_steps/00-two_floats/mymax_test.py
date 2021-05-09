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
def test_two_ints(a: float, b: float, expected: float) -> None:
    result: float = mymax.max(a, b)
    assert result == expected
