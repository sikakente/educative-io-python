import unittest
import pytest
from algorithms.dynamic_programming import min_subset_sum_difference as mss


@pytest.mark.parametrize("numbers,expected", [
    ([1, 2, 3, 9], 3),
    ([1, 2, 7, 1, 5], 0),
    ([1, 3, 100, 4], 92),
])
def test_min_subset_sum_difference(numbers, expected):
    assert expected == mss.min_subset_sum_difference(numbers)


if __name__ == '__main__':
    unittest.main()
