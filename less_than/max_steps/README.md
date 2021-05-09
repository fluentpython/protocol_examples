# Type hinting `builtin.max()`

```python
>>> max(3.1416, 2.1783)
3.1416
>>> max(5, 8)
8
>>> from fractions import Fraction
>>> max(Fraction(5, 8), Fraction(7, 12))
Fraction(5, 8)
>>> max('beta', 'alpha')
'beta'
>>> max([10, 11, 12], [10, 12])
[10, 12]
>>> max({10, 11, 12}, {10, 12})
{10, 11, 12}
>>> max('beta', 'alpha', key=len)
'alpha'
```
