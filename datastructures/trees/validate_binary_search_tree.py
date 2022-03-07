"""
Problem Statement
----------------
Given the root of a binary tree, determine if it is a valid binary search tree (BST).  A valid BST is defined as follows:  The left subtree of a node contains only nodes with keys less than the node's key. The right subtree of a node contains only nodes with keys greater than the node's key. Both the left and right subtrees must also be binary search trees.


Input
-----
a tree

Output
-------
true or false
"""


def is_valid_bst(root):
    def is_valid(node, min_so_far, max_so_far):
        # if empty node or leaf node
        if not node:
            return True
        node_value = node.value
        if node_value >= max_so_far or node_value <= min_so_far:
            return False
        return is_valid(node.left, min_so_far, node_value) and is_valid(node.right, node_value, max_so_far)

    return is_valid(root, float("-inf"), float("inf"))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
