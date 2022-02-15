import unittest
import pytest
from datastructures.strings.minimum_window_substring import minimum_window_substring


@pytest.mark.parametrize("s, t,expected", [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("ab", "b", "b"),
    ("abc", "cba", "abc"),
    ("bbaac", "aba", "baa")
])
def test_minimum_window_substring(s, t, expected):
    assert expected == minimum_window_substring(s, t)


if __name__ == '__main__':
    unittest.main()
