"""
A random picker is a collection with a ``pick`` method that pops one
random item each time it's called.
"""

import typing

class RandomPicker(typing.Protocol):
    def pick(self) -> int: ...

