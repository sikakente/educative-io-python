import unittest
import pytest
from datastructures.arrays import merge_intervals as mi


@pytest.mark.parametrize("intervals,expected", [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5], [0, 1]], [[0, 5]]),
])
def test_merge_intervals(intervals, expected):
    assert expected == mi.merge_intervals(intervals)


@pytest.mark.parametrize("intervals,expected", [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5], [0, 1]], [[0, 5]]),
])
def test_merge_intervals_faster(intervals, expected):
    assert expected == mi.merge_intervals_faster(intervals)


if __name__ == '__main__':
    unittest.main()
