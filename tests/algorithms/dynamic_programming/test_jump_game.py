import unittest
import pytest
from algorithms.dynamic_programming import jump_game as jp


@pytest.mark.parametrize("steps,expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False)
])
def test_jump_game(steps, expected):
    assert expected == jp.jump_game(steps)


@pytest.mark.parametrize("steps,expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False)
])
def test_jump_game_faster(steps, expected):
    assert expected == jp.jump_game_faster(steps)


if __name__ == '__main__':
    unittest.main()
