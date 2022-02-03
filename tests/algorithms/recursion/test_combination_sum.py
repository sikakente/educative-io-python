import unittest
import pytest
from algorithms.recursion import combination_sum as cs


@pytest.mark.parametrize("candidates,target,expected", [
    ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
    ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ([2], 1, []),
])
def test_combination_sum(candidates, target, expected):
    assert expected == cs.combination_sum(candidates, target)


if __name__ == '__main__':
    unittest.main()
