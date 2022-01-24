import unittest
import pytest
from algorithms.dynamic_programming import max_sum_subsequence as mss


@pytest.mark.parametrize("numbers,expected", [
    ([1, 6, 10, 14, -5, -1, 2, -1, 3], 25),
    ([-4, 10], 10),
    ([-4], -4),
    ([], 0),
])
def test_max_sum_subsequence(numbers, expected):
    assert expected == mss.max_sum_subsequence(numbers)


if __name__ == '__main__':
    unittest.main()
