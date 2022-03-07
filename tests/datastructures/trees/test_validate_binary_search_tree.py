import unittest
import pytest
from datastructures.trees.binary_tree_utils import BinaryTree, NULL_MARKER
from datastructures.trees.validate_binary_search_tree import is_valid_bst


@pytest.mark.parametrize("values,expected", [
    ([2, 1, 3], True),
    ([5, 1, 4, NULL_MARKER, NULL_MARKER, 3, 6], False)
])
def test_is_valid_bst(values, expected):
    tree = BinaryTree().build_tree(values)
    assert expected == is_valid_bst(tree.root)


if __name__ == '__main__':
    unittest.main()
