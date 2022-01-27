import unittest
import pytest
from algorithms.dynamic_programming import game_scoring as gs


@pytest.mark.parametrize("runs,expected", [
    (5, 10),
    (0, 1)
])
def test_recursive_game_scoring(runs, expected):
    assert expected == gs.recursive_game_scoring(runs)


@pytest.mark.parametrize("runs,expected", [
    (5, 10),
    (0, 1)
])
def test_memoized_game_scoring(runs, expected):
    assert expected == gs.memoized_game_scoring(runs)


@pytest.mark.parametrize("runs,expected", [
    (5, 10),
    (0, 1)
])
def test_bottom_up_game_scoring(runs, expected):
    assert expected == gs.bottom_up_game_scoring(runs)


if __name__ == '__main__':
    unittest.main()
