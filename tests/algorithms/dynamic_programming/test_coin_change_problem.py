import unittest
import pytest
from algorithms.dynamic_programming import coin_change_problem as cc


@pytest.mark.parametrize("amount,denoms,expected", [
    (10, [25, 10, 5, 1], 4),
])
def test_recursive_coin_change(amount, denoms, expected):
    assert expected == cc.recursive_coin_change(amount, denoms, len(denoms))


@pytest.mark.parametrize("amount,denoms,expected", [
    (10, [25, 10, 5, 1], 4),
])
def test_memoized_coin_change(amount, denoms, expected):
    assert expected == cc.memoized_coin_change(amount, denoms, len(denoms))


@pytest.mark.parametrize("amount,denoms,expected", [
    (10, [25, 10, 5, 1], 4),
])
def test_bottom_up_coin_change(amount, denoms, expected):
    assert expected == cc.bottom_up_coin_change(amount, denoms, len(denoms))


if __name__ == '__main__':
    unittest.main()
