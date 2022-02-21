import unittest
import pytest
from algorithms.dynamic_programming.house_robber_two import rob


@pytest.mark.parametrize("nums,expected", [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3),
    ([1, 3, 1, 3, 100], 103)
])
def test_rob(nums, expected):
    assert expected == rob(nums)


if __name__ == '__main__':
    unittest.main()
