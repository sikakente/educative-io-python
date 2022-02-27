import unittest
import pytest
from datastructures.graphs.utils import create_adjacency_list


@pytest.mark.parametrize("n, edges,expected", [
    (5, [[0, 1], [1, 2], [3, 4]], [{1}, {0, 2}, {1}, {4}, {3}]),
])
def test_adjacency_list(n, edges, expected):
    assert expected == create_adjacency_list(n, edges)


if __name__ == '__main__':
    unittest.main()
