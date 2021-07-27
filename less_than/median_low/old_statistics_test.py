from old_statistics import median_low


def test_int() -> None:
    l = range(10)
    m = median_low(l)
    assert m == 4


def test_str() -> None:
    l = 'abcd'
    m = median_low(l)
    assert m == 'b'
