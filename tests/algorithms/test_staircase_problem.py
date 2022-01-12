import unittest
import pytest
from algorithms.dynamic_programming import staircase_problem as sc


@pytest.mark.parametrize("steps,expected", [
    (4, 7),
    (0, 1)
])
def test_recursive_staircase_problem(steps, expected):
    assert expected == sc.recursive_staircase_problem(steps)


@pytest.mark.parametrize("steps,expected", [
    (4, 7),
    (0, 1)
])
def test_memoized_staircase_problem(steps, expected):
    assert expected == sc.memoized_staircase_problem(steps)


@pytest.mark.parametrize("steps,expected", [
    (4, 7),
    (0, 1)
])
def test_bottom_up_staircase_problem(steps, expected):
    assert expected == sc.bottom_up_staircase_problem(steps)


if __name__ == '__main__':
    unittest.main()
