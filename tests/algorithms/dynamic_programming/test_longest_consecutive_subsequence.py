import unittest
import pytest
from algorithms.dynamic_programming.longest_consecutive_subsequence import \
    longest_consecutive_subsequence, \
    longest_consecutive_subsequence_using_sliding_window, \
    lcs_linear_run_time


@pytest.mark.parametrize("nums,expected", [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
])
def test_longest_consecutive_subsequence(nums, expected):
    assert expected == longest_consecutive_subsequence(nums)


@pytest.mark.parametrize("nums,expected", [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
])
def test_longest_consecutive_subsequence_using_sliding_window(nums, expected):
    assert expected == longest_consecutive_subsequence_using_sliding_window(nums)


@pytest.mark.parametrize("nums,expected", [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
])
def test_lcs_linear_run_time(nums, expected):
    assert expected == lcs_linear_run_time(nums)


if __name__ == '__main__':
    unittest.main()
