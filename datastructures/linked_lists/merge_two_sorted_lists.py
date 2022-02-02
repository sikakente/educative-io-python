"""
Problem Statement
----------------
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.


Input
-----
Two sorted linked lists

Output
-------
A single sorted linked list
"""


def merge_two_sorted_lists(list_1, list_2):
    list_3 = head = None
    while list_1 and list_2:
        if list_1.value <= list_2.value:
            if head:
                list_3.next = list_1
                list_3 = list_1
                list_1 = list_1.next
            else:
                head = list_3 = list_1
                list_1 = list_1.next
        else:
            if head:
                list_3.next = list_2
                list_3 = list_2
                list_2 = list_2.next
            else:
                head = list_3 = list_2
                list_2 = list_2.next

    if list_1:
        if list_3:
            list_3.next = list_1
        else:
            head = list_3 = list_1

    if list_2:
        if list_3:
            list_3.next = list_2
        else:
            head = list_3 = list_2

    return head


if __name__ == '__main__':
    import doctest

    doctest.testmod()
