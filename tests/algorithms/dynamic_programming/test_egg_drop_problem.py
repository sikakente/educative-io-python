import unittest
import pytest
from algorithms.dynamic_programming import egg_drop_problem as egg


@pytest.mark.parametrize("eggs,floors,expected", [
    (6, 8, 8)
])
def test_recursive_egg_drop_problem(eggs, floors, expected):
    assert expected == egg.recursive_egg_drop(eggs, floors)


@pytest.mark.parametrize("eggs,floors,expected", [
    (6, 15, 4)
])
def test_memoized_egg_drop_problem(eggs, floors, expected):
    assert expected == egg.memoized_egg_drop(eggs, floors)


if __name__ == '__main__':
    unittest.main()
