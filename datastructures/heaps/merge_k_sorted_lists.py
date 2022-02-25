"""
Problem Statement
----------------
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Input
-----
list of sorted linked lists

Output
-------
a single merged sorted list
"""
import heapq


def merge_k_lists(lists):
    k = len(lists)
    if k == 0:
        return None

    head = merged_list = None
    min_heap = []

    for node_idx, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.value, node_idx))

    while min_heap:
        _value, min_node_idx = heapq.heappop(min_heap)
        min_node = lists[min_node_idx]
        if head is None:
            head = merged_list = min_node
            min_node = min_node.next
            merged_list.next = None
        else:
            merged_list.next = min_node
            min_node = min_node.next
            merged_list = merged_list.next
            merged_list.next = None

        lists[min_node_idx] = min_node
        if min_node:
            heapq.heappush(min_heap, (min_node.value, min_node_idx))

    return head


if __name__ == '__main__':
    import doctest

    doctest.testmod()
