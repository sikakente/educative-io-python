import unittest
import pytest
from datastructures.graphs.connected_components_in_graph import num_connected_components


@pytest.mark.parametrize("n, edges,expected", [
    (5, [[0, 1], [1, 2], [3, 4]], 2),
    (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1)
])
def test_num_connected_components(n, edges, expected):
    assert expected == num_connected_components(n, edges)


if __name__ == '__main__':
    unittest.main()
