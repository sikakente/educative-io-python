import unittest
import pytest
from datastructures.arrays.matrix_zeroes import set_matrix_zeroes


@pytest.mark.parametrize("matrix,expected", [
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
])
def test_set_matrix_zeroes(matrix, expected):
    assert expected == set_matrix_zeroes(matrix)


if __name__ == '__main__':
    unittest.main()
