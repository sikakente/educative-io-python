import unittest
import pytest
from datastructures.graphs.graph_valid_tree import valid_tree


@pytest.mark.parametrize("n, edges,expected", [
    (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
    (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    (4, [[0, 1], [2, 3]], False),
    (3, [[1, 0], [2, 0]], True)
])
def test_valid_tree(n, edges, expected):
    assert expected == valid_tree(n, edges)


if __name__ == '__main__':
    unittest.main()
