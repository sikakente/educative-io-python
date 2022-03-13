"""
Problem Statement
----------------
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


Input
-----
preorder and inorder traversals of a binary tree

Output
-------
a binary tree root node
"""


class TreeNode:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.value},left={self.left},right={self.right})"


def build_tree(preorder, inorder):
    if not preorder:
        return None
    n = len(preorder)

    def build_tree_helper(preorder_index, inorder_nodes):
        if preorder_index >= n:
            return None
        if not inorder_nodes:
            return None
        current_node_value = preorder[preorder_index]
        current_node = TreeNode(value=current_node_value)
        index_of_node_inorder = inorder_nodes.index(current_node_value)
        left_children = inorder_nodes[0:index_of_node_inorder]
        right_children = [] if index_of_node_inorder == n - 1 else inorder_nodes[index_of_node_inorder + 1:]
        current_node.left = build_tree_helper(preorder_index + 1, left_children)
        current_node.right = build_tree_helper(preorder_index + len(left_children) + 1, right_children)
        return current_node

    return build_tree_helper(0, inorder)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
