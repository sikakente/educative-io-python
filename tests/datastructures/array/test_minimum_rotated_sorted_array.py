import unittest
import pytest
from datastructures.arrays.minimum_rotated_sorted_array import min_in_rotated_sorted_array


@pytest.mark.parametrize("nums,expected", [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11)
])
def test_min_in_rotated_sorted_array(nums, expected):
    assert expected == min_in_rotated_sorted_array(nums)


if __name__ == '__main__':
    unittest.main()
