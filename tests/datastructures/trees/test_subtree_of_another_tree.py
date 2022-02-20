import unittest
import pytest
from datastructures.trees.subtree_of_another_tree import is_sub_tree
from datastructures.trees.binary_tree_utils import BinaryTree, NULL_MARKER


@pytest.mark.parametrize("root_values, sub_root_values,expected", [
    ([3, 4, 5, 1, 2], [4, 1, 2], True),
    ([3, 4, 5, 1, 2, NULL_MARKER, NULL_MARKER, NULL_MARKER, NULL_MARKER, 0], [4, 1, 2], False)
])
def test_is_sub_tree(root_values, sub_root_values, expected):
    root_tree = BinaryTree().build_tree(root_values)
    sub_root_tree = BinaryTree().build_tree(sub_root_values)
    assert expected == is_sub_tree(root_tree.root, sub_root_tree.root)


if __name__ == '__main__':
    unittest.main()
