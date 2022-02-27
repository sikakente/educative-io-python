import unittest
import pytest
from datastructures.trees.binary_tree_utils import BinaryTree, NULL_MARKER, find_node
from datastructures.trees.lowest_common_ancestor_binary_tree import lowest_common_ancestor


@pytest.mark.parametrize("root_values,p,q,expected", [
    ([3, 5, 1, 6, 2, 0, 8, NULL_MARKER, NULL_MARKER, 7, 4], 5, 1, 3),
    ([3, 5, 1, 6, 2, 0, 8, NULL_MARKER, NULL_MARKER, 7, 4], 5, 4, 5),
    ([1, 2], 1, 2, 1)
])
def test_lowest_common_ancestor(root_values, p, q, expected):
    tree = BinaryTree().build_tree(root_values)
    p = find_node(tree.root, p)
    q = find_node(tree.root, q)
    lca = lowest_common_ancestor(tree.root, p, q)
    if lca:
        assert expected == lca.value
    else:
        assert lca is None


if __name__ == '__main__':
    unittest.main()
