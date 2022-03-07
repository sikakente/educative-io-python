"""
Problem Statement
----------------
You are given the head of a singly linked-list. The list can be represented as:  L0 → L1 → … → Ln - 1 → Ln Reorder the list to be on the following form:  L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → … You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Input
-----
a linked list

Output
-------
a list
"""


def reorder_list(head):
    list_items = []
    current = head

    while current:
        list_items.append(current)
        current = current.next

    n = len(list_items)

    if n <= 2:
        return
    start, end = 0, n - 1
    current_index, next_index = start, end

    while start < end:
        list_items[current_index].next = list_items[next_index]
        list_items[next_index].next = None
        if current_index == start:
            start += 1
            current_index = next_index
            next_index = start
        else:
            end -= 1
            current_index = next_index
            next_index = end


if __name__ == '__main__':
    import doctest

    doctest.testmod()
