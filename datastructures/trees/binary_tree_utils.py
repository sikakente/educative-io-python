NULL_MARKER = "*"


class TreeNode:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(value={self.value},left={self.left},right={self.right})"


class BinaryTree:

    def __init__(self, value=None):
        self.root = value
        self.size = 0

    def build_tree(self, values):
        if values:
            new_node = TreeNode(value=values[0])
            self.root = new_node
            self.size += 1
            self.insert_nodes(self.root, values, 0)
        return self

    def insert_nodes(self, node, values, parent_level):
        if parent_level == len(values):
            return
        left_node_position = (2 * parent_level) + 1
        right_node_position = (2 * parent_level) + 2
        if left_node_position < len(values):
            left_value = values[left_node_position]
            if left_value != NULL_MARKER:
                left_node = TreeNode(left_value)
                node.left = left_node
                self.size += 1
                self.insert_nodes(node.left, values, left_node_position)
        if right_node_position < len(values):
            right_value = values[right_node_position]
            if right_value != NULL_MARKER:
                right_node = TreeNode(right_value)
                node.right = right_node
                self.size += 1
                self.insert_nodes(node.right, values, right_node_position)

    def preorder(self, node, accumulator):
        if node:
            accumulator.append(node.value)
            self.preorder(node.left, accumulator)
            self.preorder(node.right, accumulator)
        return accumulator

    def inorder(self, node, accumulator):
        if node:
            self.inorder(node.left, accumulator)
            accumulator.append(node.value)
            self.inorder(node.right, accumulator)

        return accumulator

    def postorder(self, node, accumulator):
        if node:
            self.postorder(node.left, accumulator)
            self.postorder(node.right, accumulator)
            accumulator.append(node.value)
        return accumulator


def find_node(node, value):
    if node is None:
        return None
    if node.value == value:
        return node
    return find_node(node.left, value) or find_node(node.right, value)
