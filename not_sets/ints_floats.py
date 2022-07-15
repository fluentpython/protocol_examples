"""
This script shows that `int` is not a subset of `float`.
It finds an `int` that is not a member of the set of `float`.
"""

from math import log

i = 1
while True:
    try:
        f = float(i)
    except OverflowError:
        f = -1
    if f != i:
        print(i, log(i, 10), f, sep='\n')
        break
    i *= 10

