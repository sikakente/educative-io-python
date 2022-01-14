import unittest
import pytest
from algorithms.dynamic_programming import longest_palindromic_subsequence as lps


@pytest.mark.parametrize("string,expected", [
    ("abdbca", 5),
    ("cddpd", 3),
    ("pqr", 1),
])
def test_recursive_longest_palindromic_subsequence(string, expected):
    assert expected == lps.recursive_longest_palindromic_subsequence(string)


@pytest.mark.parametrize("string,expected", [
    ("abdbca", 5),
    ("cddpd", 3),
    ("pqr", 1),
])
def test_memoized_longest_palindromic_subsequence(string, expected):
    assert expected == lps.memoized_longest_palindromic_subsequence(string)


if __name__ == '__main__':
    unittest.main()
