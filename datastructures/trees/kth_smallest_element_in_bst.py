"""
Problem Statement
----------------
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


Input
-----
tree node

Output
-------
the kth smallest value
"""


def kth_smallest_element(root, k):
    def inorder(node, accumulator):
        if node:
            inorder(node.left, accumulator)
            accumulator.append(node.value)
            inorder(node.right, accumulator)
        return accumulator

    return inorder(root, [])[k - 1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
