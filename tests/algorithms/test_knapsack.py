import unittest
import pytest
from algorithms.dynamic_programming import knapsack as ks


@pytest.mark.parametrize("profits,weights,capacity,expected", [
    ([60, 100, 120], [10, 20, 30], 50, 220),
    ([60, 100, 120], [10, 20, 30], 0, 0),
    ([1, 6, 10, 16], [1, 2, 3, 5], 7, 22),
    ([1, 6, 10, 16], [1, 2, 3, 5], 6, 17)
])
def test_recursive_knapsack(profits, weights, capacity, expected):
    assert expected == ks.recursive_knapsack(profits, len(profits), weights, capacity)


@pytest.mark.parametrize("profits,weights,capacity,expected", [
    ([60, 100, 120], [10, 20, 30], 50, 220),
    ([60, 100, 120], [10, 20, 30], 0, 0),
    ([1, 6, 10, 16], [1, 2, 3, 5], 7, 22),
    ([1, 6, 10, 16], [1, 2, 3, 5], 6, 17)
])
def test_memoized_knapsack(profits, weights, capacity, expected):
    assert expected == ks.memoized_knapsack(profits, len(profits), weights, capacity)


@pytest.mark.parametrize("profits,weights,capacity,expected", [
    ([60, 100, 120], [10, 20, 30], 50, 220),
    ([60, 100, 120], [10, 20, 30], 0, 0),
    ([1, 6, 10, 16], [1, 2, 3, 5], 7, 22),
    ([1, 6, 10, 16], [1, 2, 3, 5], 6, 17)
])
def test_bottom_up_knapsack(profits, weights, capacity, expected):
    assert expected == ks.bottom_up_knapsack(profits, len(profits), weights, capacity)


if __name__ == '__main__':
    unittest.main()
