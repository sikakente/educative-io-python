"""
Problem Statement
----------------
Given the root of a binary tree, return its maximum depth.  A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Input
-----
Tree

Output
-------
maximum depth of binary tree
"""


def max_depth(root):
    def helper(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1

        return 1 + max(helper(node.left), helper(node.right))

    return helper(root)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
