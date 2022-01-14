import unittest
import pytest
from algorithms.dynamic_programming import partition_problem as pp


@pytest.mark.parametrize("numbers,expected", [
    ([1, 2, 3, 4], True)
])
def test_recursive_partition_problem(numbers, expected):
    actual, subsets = pp.recursive_partition_problem(numbers)
    assert expected == actual


@pytest.mark.parametrize("numbers,expected", [
    ([1, 2, 3, 4], True)
])
def test_memoized_partition_problem(numbers, expected):
    actual, subsets = pp.memoized_partition_problem(numbers)
    assert expected == actual


@pytest.mark.parametrize("numbers,expected", [
    ([1, 2, 3, 4], True),
    ([2, 4, 5], False)
])
def test_bottom_up_partition_problem(numbers, expected):
    assert expected == pp.bottom_up_partition_problem(numbers)


if __name__ == '__main__':
    unittest.main()
