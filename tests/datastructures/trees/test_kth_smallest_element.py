import unittest
import pytest
from datastructures.trees.binary_tree_utils import BinaryTree, NULL_MARKER
from datastructures.trees.kth_smallest_element_in_bst import kth_smallest_element


@pytest.mark.parametrize("values,k,expected", [
    ([3, 1, 4, NULL_MARKER, 2], 1, 1),
    ([5, 3, 6, 2, 4, NULL_MARKER, NULL_MARKER, 1], 3, 3)
])
def test_kth_smallest_element(values, k, expected):
    tree = BinaryTree().build_tree(values)
    assert expected == kth_smallest_element(tree.root, k)


if __name__ == '__main__':
    unittest.main()
