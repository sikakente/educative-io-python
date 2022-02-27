"""
Problem Statement
----------------
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.  According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Input
-----
a tree and two nodes

Output
-------
the node which is the lowest common ancestor
"""


def lowest_common_ancestor(root, p, q):
    def path_from_root(node, value, path):
        if node is None:
            return
        if node.value == value:
            path.append(node)
            return
        if value < node.value:
            path.append(node)
            return path_from_root(node.left, value, path)

        path.append(node)
        return path_from_root(node.right, value, path)

    p_path = []
    path_from_root(root, p.value, p_path)
    q_path = []
    path_from_root(root, q.value, q_path)

    longer_path = max(p_path, q_path, key=len)
    shorter_path = min(p_path, q_path, key=len)

    while len(longer_path) > len(shorter_path):
        longer_path.pop()

    while q_path and p_path:
        if q_path[-1].value == p_path[-1].value:
            break
        q_path.pop()
        p_path.pop()

    return q_path[-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
