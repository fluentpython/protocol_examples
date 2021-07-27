from new_statistics import median_low


def test_object() -> None:
    l = [object() for _ in range(1, 10)]
    try:
        median_low(l)
    except TypeError as exc:
        print(repr(exc))


if __name__ == '__main__':
    test_object()
