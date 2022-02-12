import unittest
import pytest
from datastructures.trees.binary_tree_utils import BinaryTree, NULL_MARKER
from datastructures.trees.max_depth_binary_tree import max_depth


@pytest.mark.parametrize("values,expected", [
    ([3, 9, 20, NULL_MARKER, NULL_MARKER, 15, 7], 3),
    ([1, NULL_MARKER, 2], 2)
])
def test_max_depth(values, expected):
    tree = BinaryTree().build_tree(values)
    assert expected == max_depth(tree.root)


if __name__ == '__main__':
    unittest.main()
