"""
Linked list module which creates
"""


class Node:
    def __init__(self, next_node, value):
        self.next = next_node
        self.value = value

    def __str__(self):
        return f"Node(next={self.next},value={self.value})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, value):
        # if head is none
        new_node = Node(None, value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def to_array(self, reverse=False):
        items = []
        current = self.head
        while current:
            items.append(current.value)
            current = current.next
        return items if reverse else items[::-1]

    def __str__(self):
        return f"LinkedList(size={self.size})"


def build_list(values):
    linked_list = LinkedList()
    for val in values:
        linked_list.add_first(val)
    return linked_list


def list_size(node):
    size = 0
    if node:
        current = node
        while current:
            current = current.next
            size += 1

    return size
