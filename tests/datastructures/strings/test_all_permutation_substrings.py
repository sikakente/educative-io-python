import unittest
import pytest
from datastructures.strings.all_permutation_substrings import all_permutation_substring


@pytest.mark.parametrize("s,t,expected", [
    ("XYYZXZYZXXYZ", "XYZ", ["YZX", "XZY", "YZX", "XYZ"]),
])
def test_all_permutation_substrings(s, t, expected):
    assert expected == all_permutation_substring(s, t)


if __name__ == '__main__':
    unittest.main()
