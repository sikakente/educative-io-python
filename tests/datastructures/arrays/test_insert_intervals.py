import unittest
import pytest
from datastructures.arrays import insert_intervals as ins


@pytest.mark.parametrize("intervals,new_interval,expected", [
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ([[1, 5]], [0, 3], [[0, 5]]),
    ([[1, 5]], [0, 0], [[0, 0], [1, 5]])
])
def test_insert_intervals(intervals, new_interval, expected):
    assert expected == ins.insert_intervals(intervals, new_interval)


if __name__ == '__main__':
    unittest.main()
