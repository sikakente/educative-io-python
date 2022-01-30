import unittest
import pytest
from algorithms.dynamic_programming import longest_common_subsequence as lcs


@pytest.mark.parametrize("text_1,text_2,expected", [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0)
])
def test_recursive_longest_common_subsequence(text_1, text_2, expected):
    assert expected == lcs.recursive_longest_common_subsequence(text_1, text_2)


@pytest.mark.parametrize("text_1,text_2,expected", [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0)
])
def test_bottom_up_longest_common_subsequence(text_1, text_2, expected):
    assert expected == lcs.bottom_up_longest_common_subsequence(text_1, text_2)


if __name__ == '__main__':
    unittest.main()
