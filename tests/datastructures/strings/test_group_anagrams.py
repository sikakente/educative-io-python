import unittest
import pytest
from datastructures.strings import group_anagrams as ga


@pytest.mark.parametrize("strings,expected", [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']]),
])
def test_group_anagrams(strings, expected):
    assert sorted(expected) == sorted(ga.group_anagrams(strings))


if __name__ == '__main__':
    unittest.main()
