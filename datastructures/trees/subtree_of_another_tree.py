"""
Problem Statement
----------------
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.  A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


Input
-----
two trees

Output
-------
boolean indicating whether the subtree is a tree of the other
"""


def is_sub_tree(root, sub_root):
    def check(tree_node, sub_tree_node):
        if tree_node is None and sub_tree_node is None:
            return True
        if tree_node is None or sub_tree_node is None:
            return False
        if tree_node.value != sub_tree_node.value:
            return False
        return check(tree_node.left, sub_tree_node.left) and check(tree_node.right, sub_tree_node.right)

    def is_sub_tree_helper(tree_node, sub_tree_node):
        if tree_node is None and sub_tree_node is not None:
            return False
        if check(tree_node, sub_tree_node):
            return True
        return is_sub_tree_helper(tree_node.left, sub_tree_node) or is_sub_tree(tree_node.right, sub_tree_node)

    return is_sub_tree_helper(root, sub_root)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
