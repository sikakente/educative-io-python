"""
Linked list module which creates
"""


class Node:
    def __init__(self, next_node, value):
        self.next = next_node
        self.value = value

    def __str__(self):
        return f"Node(value={self.value},next={self.next})"


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

    def to_array(self, reverse=False, node=None):
        items = []
        current = node or self.head
        while current:
            items.append(current.value)
            current = current.next
        return items if reverse else items[::-1]

    def __str__(self):
        return f"LinkedList(size={self.size})"


def build_list(values, reverse=False):
    if reverse:
        values = reversed(values)
    linked_list = LinkedList()
    for val in values:
        linked_list.add_first(val)
    return linked_list


def build_list_with_cycle(values, cycle_position, reverse=False):
    linked_list = build_list(values, reverse=reverse)
    current = linked_list.head
    if cycle_position < 0:
        return linked_list
    current_position = 0
    node_to_insert_cycle = None
    while current:
        if current_position == cycle_position:
            node_to_insert_cycle = current
            break
        current_position += 1

    tail = linked_list.head
    while tail.next:
        tail = tail.next

    if node_to_insert_cycle:
        tail.next = node_to_insert_cycle

    return linked_list


def list_size(node):
    size = 0
    if node:
        current = node
        while current:
            current = current.next
            size += 1

    return size


def to_array(node, reverse=False):
    items = []
    current = node
    while current:
        items.append(current.value)
        current = current.next
    return items if reverse else items[::-1]
