"""
Problem Statement
----------------
Given the head of a singly linked list, reverse the list, and return the reversed list.


Input
-----
a linkedlist head node

Output
-------
a reversed linked list
"""


def reverse_list(head):
    r = q = None
    p = head

    while p:
        r = q
        q = p
        p = p.next
        q.next = r
        if p is None:
            # we have reached the tail so set the head
            head = q

    return head


if __name__ == '__main__':
    import doctest

    doctest.testmod()
