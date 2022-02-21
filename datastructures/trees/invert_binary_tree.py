"""
Problem Statement
----------------
Given the root of a binary tree, invert the tree, and return its root.


Input
-----
a binary tree

Output
-------
An inverted binary tree
"""


def invert_tree(root):
    def invert(node):
        if node:
            node.left, node.right = node.right, node.left
            invert_tree(node.left)
            invert_tree(node.right)

    invert(root)
    return root


if __name__ == '__main__':
    import doctest

    doctest.testmod()
