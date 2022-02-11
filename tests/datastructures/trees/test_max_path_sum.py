import unittest
import pytest
from datastructures.trees.binary_tree_utils import BinaryTree, NULL_MARKER
from datastructures.trees.max_path_sum import max_path_sum


@pytest.mark.parametrize("values,expected", [
    ([1, 2, 3], 6),
    ([-10, 9, 20, NULL_MARKER, NULL_MARKER, 15, 7], 42),
    ([2, -1], 2)
])
def test_max_path_sum(values, expected):
    tree = BinaryTree().build_tree(values)
    assert expected == max_path_sum(tree.root)


if __name__ == '__main__':
    unittest.main()
