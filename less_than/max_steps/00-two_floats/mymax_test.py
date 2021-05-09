import mymax
import pytest


@pytest.mark.parametrize(
    'a, b, expected',
    [
        (1.1, 2.2, 2.2),
        (-3.1, -1.3, -1.3),
        (4.2, 4.2, 4.2),
    ],
)
def test_two_floats(a: float, b: float, expected: float) -> None:
    result: float = mymax.max(a, b)
    assert result == expected
