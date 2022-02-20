"""
Problem Statement
----------------
Given the roots of two binary trees p and q, write a function to check if they are the same or not.  Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Input
-----
two trees

Output
-------
boolean indicating whether the trees are the same
"""


def is_same_tree(tree_1, tree_2):
    if tree_1 is None and tree_2 is None:
        return True
    if tree_1 is None and tree_2 is not None:
        return False
    if tree_1 is not None and tree_2 is None:
        return False
    if tree_1.value != tree_2.value:
        return False
    return is_same_tree(tree_1.left, tree_2.left) and is_same_tree(tree_1.right, tree_2.right)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
