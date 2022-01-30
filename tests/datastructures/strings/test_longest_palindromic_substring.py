import unittest
import pytest
from datastructures.strings import longest_palindromic_substring as lps


@pytest.mark.parametrize("input_str,expected", [
    ("babad", "aba"),
    ("cbbd", "bb"),
])
def test_longest_palindromic_substring(input_str, expected):
    assert expected == lps.longest_palindromic_substring(input_str)


if __name__ == '__main__':
    unittest.main()
