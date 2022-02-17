import unittest
import pytest
from datastructures.strings.valid_palindrome import valid_palindrome


@pytest.mark.parametrize("s,expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True)
])
def test_valid_palindrome(s, expected):
    assert expected == valid_palindrome(s)


if __name__ == '__main__':
    unittest.main()
