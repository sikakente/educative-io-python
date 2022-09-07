import unittest
import pytest
from algorithms.dynamic_programming import max_coin_selection as mcs


@pytest.mark.parametrize("coins,expected", [
    ([3, 9, 1, 2], 11),
])
def test_test_max_coin_selection(coins, expected):
    assert expected == mcs.max_coin_selection(coins)


if __name__ == '__main__':
    unittest.main()
