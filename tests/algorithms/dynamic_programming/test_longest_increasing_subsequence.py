import unittest
import pytest
from algorithms.dynamic_programming.longest_increasing_subsequence import \
    longest_increasing_subsequence, longest_increasing_subsequence_bottom_up


@pytest.mark.parametrize("nums,expected", [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1)
])
def test_longest_increasing_subsequence(nums, expected):
    assert expected == longest_increasing_subsequence(nums)


@pytest.mark.parametrize("nums,expected", [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1)
])
def test_longest_increasing_subsequence(nums, expected):
    assert expected == longest_increasing_subsequence_bottom_up(nums)


if __name__ == '__main__':
    unittest.main()
