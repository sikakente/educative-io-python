import unittest
import pytest
from datastructures.arrays.missing_number import missing_number


@pytest.mark.parametrize("nums,expected", [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
])
def test_missing_number(nums, expected):
    assert expected == missing_number(nums)


if __name__ == '__main__':
    unittest.main()
