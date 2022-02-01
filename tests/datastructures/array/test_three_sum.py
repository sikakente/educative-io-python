import unittest
import pytest
from datastructures.arrays import three_sum as ts


@pytest.mark.parametrize("numbers,expected", [
    ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
    ([], []),
    ([0], [])
])
def test_bottom_up_longest_common_subsequence(numbers, expected):
    assert expected == ts.three_sum(numbers)


if __name__ == '__main__':
    unittest.main()
