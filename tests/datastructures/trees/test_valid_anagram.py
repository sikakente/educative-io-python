import unittest
import pytest
from datastructures.strings.valid_anagram import is_anagram


@pytest.mark.parametrize("s, t,expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False)
])
def test_is_anagram(s, t, expected):
    assert expected == is_anagram(s, t)


if __name__ == '__main__':
    unittest.main()
