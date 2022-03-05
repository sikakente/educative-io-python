import unittest
import pytest
from datastructures.arrays.non_overlapping_intervals import erase_overlapping_intervals


@pytest.mark.parametrize("intervals,expected", [
    ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ([[1, 2], [1, 2], [1, 2]], 2),
    ([[1, 2], [2, 3]], 0),
    ([[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2],
      [30, 47], [-40, -26]], 7)
])
def test_erase_non_overlapping_intervals(intervals, expected):
    assert expected == erase_overlapping_intervals(intervals)


if __name__ == '__main__':
    unittest.main()
