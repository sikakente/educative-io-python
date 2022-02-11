import unittest
import pytest
from datastructures.trees.binary_tree_utils import BinaryTree
from datastructures.trees.binary_tree_level_order_traversal import level_order_traversal


@pytest.mark.parametrize("values,expected", [
    ([3, 9, 20, "*", "*", 15, 7], [[3], [9, 20], [15, 7]]),
    ([1], [[1]]),
    ([], [])
])
def test_level_order_traversal(values, expected):
    tree = BinaryTree().build_tree(values)
    assert expected == level_order_traversal(tree.root)


if __name__ == '__main__':
    unittest.main()
