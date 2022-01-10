import unittest
import pytest
from algorithms.dynamic_programming import knapsack as ks


@pytest.mark.parametrize("profits,profits_length,weights,capacity,expected", [
    ([60, 100, 120], 3, [10, 20, 30], 50, 220),
    ([60, 100, 120], 3, [10, 20, 30], 0, 0)
])
def test_recursive_knapsack(profits, profits_length, weights, capacity, expected):
    assert expected == ks.recursive_knapsack(profits, profits_length, weights, capacity)


@pytest.mark.parametrize("profits,profits_length,weights,capacity,expected", [
    ([60, 100, 120], 3, [10, 20, 30], 50, 220),
    ([60, 100, 120], 3, [10, 20, 30], 0, 0)
])
def test_memoized_knapsack(profits, profits_length, weights, capacity, expected):
    assert expected == ks.memoized_knapsack(profits, profits_length, weights, capacity)


if __name__ == '__main__':
    unittest.main()
