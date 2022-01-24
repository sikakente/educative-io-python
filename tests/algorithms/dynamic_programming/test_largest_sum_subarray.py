import unittest
import pytest
from algorithms.dynamic_programming import largest_sum_subarray as ls


@pytest.mark.parametrize("numbers,expected", [
    ([-4, 2, -5, 1, 2, 3, 6, -5, 1], 12),
    ([-4], -4),
    ([], 0),
])
def test_largest_sum_subarray(numbers, expected):
    assert expected == ls.largest_subarray_sum(numbers)


if __name__ == '__main__':
    unittest.main()
