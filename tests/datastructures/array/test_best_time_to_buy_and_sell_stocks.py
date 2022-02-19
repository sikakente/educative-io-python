import unittest
import pytest
from datastructures.arrays.best_time_to_buy_sell_stocks import max_profit


@pytest.mark.parametrize("prices,expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0)
])
def test_max_profit(prices, expected):
    assert expected == max_profit(prices)


if __name__ == '__main__':
    unittest.main()
