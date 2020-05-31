import sys
from typing import TYPE_CHECKING
import pytest # type: ignore

import mysorted as my


def test_sort_list_int():
    # type: () -> None
    given = [2, 3, 0, 6, 5, 1, 4]
    expected = [6, 5, 4, 3, 2, 1, 0]
    my.sort(given, reverse=True)
    assert given == expected
    if TYPE_CHECKING:
        reveal_type(given)
        reveal_type(expected)


def test_sort_list_str_key():
    # type: () -> None
    given = [u'mango', u'pear', u'apple', u'kiwi', u'banana']
    expected = [u'pear', u'kiwi', u'mango', u'apple', u'banana']    
    my.sort(given, key=len)
    assert given == expected
    if TYPE_CHECKING:
        reveal_type(given)
        reveal_type(expected)


def test_sort_list_str_bad_key_not_callable():
    # type: () -> None
    given = [u'mango', u'pear', u'apple', u'kiwi', u'banana']
    bad_key = 1
    if TYPE_CHECKING:
        reveal_type(bad_key)
    with pytest.raises(TypeError) as exc:
        my.sort(given, key=bad_key)
    assert "'int' object is not callable" in str(exc)


def test_sort_list_str_bad_key_arity():
    # type: () -> None
    given = [u'mango', u'pear', u'apple', u'kiwi', u'banana']
    def bad_key():
        # type: () -> object
        return object()
    if TYPE_CHECKING:
        reveal_type(bad_key)
    with pytest.raises(TypeError) as exc:
        my.sort(given, key=bad_key)
    assert 'bad_key()' in str(exc)
    assert 'argument' in str(exc)


py3_only = pytest.mark.skipif(sys.version_info < (3,),
                             reason='requires Python 3')
py2_only = pytest.mark.skipif(sys.version_info >= (3,),
                             reason='requires Python 2.7')

@py3_only
def test_sort_list_str_bad_key_return_py3():
    # type: () -> None
    given = [u'mango', u'pear', u'apple', u'kiwi', u'banana']
    def bad_key(_):
        # type: (str) -> object
        return object()
    if TYPE_CHECKING:
        reveal_type(bad_key)
    with pytest.raises(TypeError) as exc:
        my.sort(given, key=bad_key)
    assert "'<' not supported" in str(exc)


@py2_only
def test_sort_list_str_cmp_py2():
    # type: () -> None
    given = [u'mango', u'pear', u'apple', u'kiwi', u'banana']
    def value(char):  # case-insenstive letter distance from 'A'
        return ord(char.upper()) - ord('A')
    def weight(text):  # sum of value of each char
        return sum(value(char) for char in text)
    def weight_cmp(a, b):
        return cmp(weight(a), weight(b))
    expected = ['banana', 'pear', 'mango', 'apple', 'kiwi']
    my.sort(given, cmp=weight_cmp)
    assert given == expected
    if TYPE_CHECKING:
        reveal_type(given)
        reveal_type(expected)

@py2_only
def test_sort_list_str_bad_cmp_arity_py2():
    # type: () -> None
    given = [u'mango', u'pear', u'apple', u'kiwi', u'banana']
    def bad_cmp():
        # type: () -> object
        return object()
    if TYPE_CHECKING:
        reveal_type(bad_cmp)
    with pytest.raises(TypeError) as exc:
        my.sort(given, key=bad_cmp)
    assert 'bad_cmp()' in str(exc)
    assert 'argument' in str(exc)
