import unittest
import pytest
from datastructures.trees.binary_tree_utils import BinaryTree, NULL_MARKER
from datastructures.trees.serialize_tree import Codec


@pytest.mark.parametrize("values", [
    ([2, 1, 3]),
    ([]),
    ([1, 2]),
    ([1, NULL_MARKER, 2]),
    ([5, 3, 6, 2, 4, NULL_MARKER, NULL_MARKER, 1])
])
def test_serialize_deserialize_tree(values):
    tree = BinaryTree().build_tree(values)
    serializer = Codec()
    deserializer = Codec()
    serialized_tree = serializer.serialize(tree.root)
    deserialized_tree = deserializer.deserialize(serialized_tree)
    BinaryTree().preorder(tree.root, [])
    BinaryTree().preorder(deserialized_tree, [])
    assert BinaryTree().preorder(tree.root, []) == BinaryTree().preorder(deserialized_tree, [])


if __name__ == '__main__':
    unittest.main()
