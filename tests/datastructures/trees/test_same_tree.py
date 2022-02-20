import unittest
import pytest
from datastructures.trees.binary_tree_utils import BinaryTree, NULL_MARKER
from datastructures.trees.same_tree import is_same_tree


@pytest.mark.parametrize("tree_1_vals, tree_2_vals,expected", [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, NULL_MARKER, 2], False),
    ([1, 2, 1], [1, 1, 2], False),
    ([1, 1], [1, NULL_MARKER, 1], False)
])
def test_is_same_tree(tree_1_vals, tree_2_vals, expected):
    tree_1 = BinaryTree().build_tree(tree_1_vals)
    tree_2 = BinaryTree().build_tree(tree_2_vals)
    assert expected == is_same_tree(tree_1.root, tree_2.root)


if __name__ == '__main__':
    unittest.main()
