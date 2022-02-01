"""
Problem Statement
----------------
Given the head of a linked list,
remove the nth node from the end of the list
and return its head.

Input
-----
Linked list

Output
------
linked list
"""


def remove_nth_node(linked_list_node, n):
    if n == 0:
        return linked_list_node
    current_node = linked_list_node
    list_size = 0
    stack = []
    while current_node:
        stack.append(current_node)
        current_node = current_node.next
        list_size += 1

    if n > list_size:
        return None

    node_to_remove = None
    while n > 0:
        node_to_remove = stack.pop()
        n -= 1

    # if items remain
    head = None
    if stack:
        n_1_node = stack[-1]
        n_1_node.next = node_to_remove.next
    elif node_to_remove:
        head = node_to_remove.next
        node_to_remove.next = None
        return head

    return stack[0] if stack else None


if __name__ == '__main__':
    import doctest

    doctest.testmod()
