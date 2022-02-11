import unittest
import pytest
from algorithms.dynamic_programming.climbing_stairs import num_ways_to_climb_stairs


@pytest.mark.parametrize("steps,expected", [
    (2, 2),
    (3, 3)
])
def test_climbing_stairs(steps, expected):
    assert expected == num_ways_to_climb_stairs(steps)


if __name__ == '__main__':
    unittest.main()
