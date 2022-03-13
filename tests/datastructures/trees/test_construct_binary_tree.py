import unittest
import pytest
from datastructures.trees.binary_tree_utils import BinaryTree, NULL_MARKER
from datastructures.trees.construct_binary_tree_from_preorder_inorder import build_tree


@pytest.mark.parametrize("preorder,inorder,expected", [
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, 15, 7]),
    ([-1], [-1], [-1])
])
def test_build_tree(preorder, inorder, expected):
    actual = build_tree(preorder, inorder)
    preorder_traversal = BinaryTree().preorder(actual, [])
    assert expected == preorder_traversal


if __name__ == '__main__':
    unittest.main()
