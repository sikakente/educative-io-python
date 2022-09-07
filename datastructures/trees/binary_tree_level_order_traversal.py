"""
Problem Statement
----------------
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


Input
-----
binary tree

Output
-------
list of values in level order 
"""


def level_order_traversal(tree):
    node = tree
    level_traversal = []
    if not tree:
        return level_traversal
    queue = [node, None]
    current_level = []

    while queue:
        current_item = queue.pop(0)
        if current_item:
            current_level.append(current_item.value)
            if current_item.left:
                queue.append(current_item.left)
            if current_item.right:
                queue.append(current_item.right)
        else:
            if queue:
                queue.append(None)
            level_traversal.append(current_level[:])
            current_level = []

    return level_traversal


def zig_zag_level_order_traversal(tree):
    node = tree
    level_traversal = []
    if not tree:
        return level_traversal
    queue = [node, None]
    current_level = []

    reverse = False

    while queue:
        current_item = queue.pop(0)
        if current_item:
            current_level.append(current_item.value)
            if current_item.left:
                queue.append(current_item.left)
            if current_item.right:
                queue.append(current_item.right)
        else:
            if queue:
                queue.append(None)
            if reverse:
                level_traversal.append(current_level[::-1])
            else:
                level_traversal.append(current_level[:])
            current_level = []
            reverse = not reverse

    return level_traversal


if __name__ == '__main__':
    import doctest

    doctest.testmod()
