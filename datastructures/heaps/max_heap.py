class MaxHeap:

    def __init__(self, values):
        self.elements = values or []
        self.size = len(self.elements)
        self._build_heap()

    def _build_heap(self):
        for idx in reversed(range(self.size)):
            self._heapify_down(idx)

    def insert(self, value):
        self.elements.append(value)
        self.size += 1
        self._heapify_up(self.size - 1)
        return self.elements

    def extract_min(self):
        if self.is_empty():
            return None
        minimum_element = self.elements[0]
        # swap with end
        self._swap(0, -1)
        self.elements.pop()
        self.size -= 1

        if not self.is_empty():
            self._heapify_down(0)
        return minimum_element

    def is_empty(self):
        return self.size == 0

    def find_max(self):
        return None if self.is_empty() else self.elements[0]

    def _heapify_up(self, idx):
        parent_idx = self.parent(idx)
        current_value = self.elements[idx]
        if 0 <= parent_idx < self.size:
            parent_value = self.elements[parent_idx]
            if current_value > parent_value:
                self._swap(idx, parent_idx)
                self._heapify_up(parent_idx)

    def _heapify_down(self, idx):
        left_child_idx = self.left_child(idx)
        current_value = self.elements[idx]
        if 0 <= left_child_idx < self.size:
            left_child_value = self.elements[left_child_idx]
            greater_of_children_idx = left_child_idx
            right_child_idx = self.right_child(idx)
            if 0 <= right_child_idx < self.size:
                right_child_value = self.elements[right_child_idx]
                if right_child_value > left_child_value:
                    greater_of_children_idx = right_child_idx
            if current_value < self.elements[greater_of_children_idx]:
                self._swap(idx, greater_of_children_idx)
                self._heapify_down(greater_of_children_idx)

    def _swap(self, x, y):
        self.elements[x], self.elements[y] = self.elements[y], self.elements[x]

    @staticmethod
    def left_child(parent):
        return 2 * parent + 1

    @staticmethod
    def right_child(parent):
        return 2 * parent + 2

    @staticmethod
    def parent(child):
        return child // 2
