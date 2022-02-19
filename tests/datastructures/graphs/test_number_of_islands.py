import unittest
import pytest
from datastructures.graphs.number_of_islands import num_islands


@pytest.mark.parametrize("grid,expected", [
    ([
         ["1", "1", "1", "1", "0"],
         ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "0"]
     ], 1),
    ([
         ["1", "1", "0", "0", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "1", "0", "0"],
         ["0", "0", "0", "1", "1"]
     ], 3)
])
def test_num_islands(grid, expected):
    assert expected == num_islands(grid)


if __name__ == '__main__':
    unittest.main()
