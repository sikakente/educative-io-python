import unittest
import pytest
from datastructures.trees.binary_tree_utils import BinaryTree


@pytest.mark.parametrize("values,size", [
    ([1, 2, 3, 4, 5, "*", 6, "*", "*", "*", "*", "*", "*", 7, 8], 8),
    ([], 0)
])
def test_build_binary_tree(values, size):
    tree = BinaryTree().build_tree(values)
    assert size == tree.size


if __name__ == '__main__':
    unittest.main()
