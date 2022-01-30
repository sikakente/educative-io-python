import unittest
import pytest
from datastructures.strings import longest_substring_without_repeating_characters as ls


@pytest.mark.parametrize("input_str,expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3)
])
def test_longest_substring_without_repeating_characters(input_str, expected):
    assert expected == ls.longest_substring_without_repeating_characters(input_str)


if __name__ == '__main__':
    unittest.main()
