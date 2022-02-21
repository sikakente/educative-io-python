import unittest
import pytest
from datastructures.arrays import spiral_matrix as spm


@pytest.mark.parametrize("matrix,expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
])
def test_spiral_matrix(matrix, expected):
    assert expected == spm.spiral_matrix(matrix)


if __name__ == '__main__':
    unittest.main()
