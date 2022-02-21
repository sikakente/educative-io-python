import unittest
import pytest
from datastructures.arrays import max_water_container as mwc


@pytest.mark.parametrize("heights,expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
])
def test_container_with_most_water(heights, expected):
    assert expected == mwc.container_with_most_water(heights)


if __name__ == '__main__':
    unittest.main()
