import sys

builtin_sorted = __builtins__['sorted']  # type: ignore


if sys.version_info >= (3,):
    def sort(self, key=None, reverse=False):
        list.sort(self, key=key, reverse=reverse)
else:
    def sort(self, cmp=None, key=None, reverse=False):
        list.sort(self, cmp=cmp, key=key, reverse=reverse)


if sys.version_info >= (3,):
    def sorted(iterable, key=None, reverse=False):
        return builtin_sorted(iterable, key=key, reverse=reverse)
else:
    def sorted(iterable, cmp=None, key=None, reverse=False):
        return builtin_sorted(iterable, cmp=cmp, key=key, reverse=reverse)
