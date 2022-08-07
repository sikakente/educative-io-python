"""
Problem Statement
----------------
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting
them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.  
Given the root of a binary tree, return the maximum path sum of any non-empty path.


Input
-----
tree

Output
-------
maximum path sum
"""
from collections import namedtuple

PathSum = namedtuple("PathSum", "path_sum, max_sum")


def max_path_sum(root):
    def mps(node):
        if node is None:
            return PathSum(path_sum=float("-inf"), max_sum=float("-inf"))
        if node.left is None and node.right is None:
            return PathSum(path_sum=node.value, max_sum=node.value)

        left_path_sum, left_max_sum = mps(node.left)
        right_path_sum, right_max_sum = mps(node.right)

        path_sum_using_left = max(left_path_sum + node.value, node.value)
        path_sum_using_right = max(right_path_sum + node.value, node.value)
        max_path_sum_of_children = max(path_sum_using_right, path_sum_using_left)

        path_sum_using_both_child_nodes = left_path_sum + right_path_sum + node.value
        max_sum_children = max(left_max_sum, right_max_sum)
        max_sum = max(max_path_sum_of_children, path_sum_using_both_child_nodes, max_sum_children)
        return PathSum(path_sum=max_path_sum_of_children, max_sum=max_sum)

    return mps(root).max_sum


if __name__ == '__main__':
    import doctest

    doctest.testmod()
