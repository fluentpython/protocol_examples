#!/usr/bin/env python3

from fractions import Fraction
from typing import TYPE_CHECKING, List, Optional

import mymax as my

def demo_args_float() -> None:
    a, b = 2.5, 3.5
    expected = b
    result = my.max(a, b)
    assert result == expected
    print((a, b), '->', result)


def demo_args_fraction() -> None:
    a, b = Fraction(5, 8), Fraction(7, 12)
    expected = a
    result = my.max(a, b)
    assert result == expected
    print((a, b), '->', result)
    print(result.numerator, result.denominator, sep='/')
    if TYPE_CHECKING:
        reveal_type(a)
        reveal_type(b)
        reveal_type(result)


def demo_args_str() -> None:
    a, b = 'apple', 'banana'
    expected = b
    result = my.max(a, b)
    assert result == expected
    print((a, b), '->', result)
    print(result.upper())
    if TYPE_CHECKING:
        reveal_type(a)
        reveal_type(b)
        reveal_type(result)

###################################### intentional type errors



def main():
    import sys
    for name, val in globals().items():
        if name.startswith('demo') or ('-e' in sys.argv and name.startswith('error')):
            print('_' * 20, name)
            val()

if __name__ == '__main__':
    main()
