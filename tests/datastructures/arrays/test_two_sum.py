import unittest
import pytest
from datastructures.arrays import two_sum as ts


@pytest.mark.parametrize("numbers,target,expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1])
])
def test_memoized_can_sum(numbers, target, expected):
    assert expected == ts.two_sum(numbers, target)


if __name__ == '__main__':
    unittest.main()
