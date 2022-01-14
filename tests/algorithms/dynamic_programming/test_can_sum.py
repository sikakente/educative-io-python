import unittest
import pytest
from algorithms.dynamic_programming import can_sum as cs


@pytest.mark.parametrize("numbers,target,expected", [
    ([1, 2, 3, 4], 5, True)
])
def test_recursive_can_sum(numbers, target, expected):
    assert expected == cs.recursive_can_sum(numbers, target)


@pytest.mark.parametrize("numbers,target,expected", [
    ([1, 2, 3, 4], 5, True)
])
def test_memoized_can_sum(numbers, target, expected):
    assert expected == cs.memoized_can_sum(numbers, target)


@pytest.mark.parametrize("numbers,target,expected", [
    ([1, 2, 3, 4], 5, True),
    ([6, 5, 7], 8, False)
])
def test_bottom_up_can_sum(numbers, target, expected):
    assert expected == cs.bottom_up_can_sum(numbers, target)


if __name__ == '__main__':
    unittest.main()
