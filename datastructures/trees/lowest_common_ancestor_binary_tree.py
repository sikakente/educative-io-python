"""
Problem Statement
----------------
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.  According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Input
-----
three nodes

Output
-------
The node representing the lowest common ancestor
"""


def lowest_common_ancestor(root, p, q):
    if root is None:
        return root
    if root.value == p.value or root.value == q.value:
        return root
    left_node_search = lowest_common_ancestor(root.left, p, q)
    right_node_search = lowest_common_ancestor(root.right, p, q)

    if left_node_search is None:
        return right_node_search
    if right_node_search is None:
        return left_node_search
    return root


if __name__ == '__main__':
    import doctest

    doctest.testmod()
