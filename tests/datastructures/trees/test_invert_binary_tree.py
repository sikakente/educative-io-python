import unittest
import pytest
from datastructures.trees.invert_binary_tree import invert_tree
from datastructures.trees.binary_tree_utils import BinaryTree, NULL_MARKER
from datastructures.trees.binary_tree_level_order_traversal import level_order_traversal


@pytest.mark.parametrize("values,expected", [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], [])
])
def test_invert_binary_tree(values, expected):
    tree = BinaryTree().build_tree(values)
    inverted_tree = invert_tree(tree.root)
    assert expected == [item for sublist in level_order_traversal(inverted_tree) for item in sublist]


if __name__ == '__main__':
    unittest.main()
