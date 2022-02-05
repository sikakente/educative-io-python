import unittest
import pytest
from algorithms.dynamic_programming import jump_game as jp


@pytest.mark.parametrize("input,expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False)
])
def test_jump_game(input, expected):
    assert expected == jp.jump_game(input)


if __name__ == '__main__':
    unittest.main()
