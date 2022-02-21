import unittest
import pytest
from datastructures.arrays.maximum_product_subarray import maximum_product_subarray


@pytest.mark.parametrize("nums,expected", [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([2, 3, -2, 4, -1], 48),
    ([2, 3, 2, 4], 48),
    ([2], 2),
])
def test_maximum_product_subarray(nums, expected):
    assert expected == maximum_product_subarray(nums)


if __name__ == '__main__':
    unittest.main()
