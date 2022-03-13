from datastructures.trees.binary_tree_utils import TreeNode

NULL_NODE = "NULL"
SEPERATOR = "|"


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        """

        if not root:
            return ""
        serialized = []
        queue = [(root, 0), None]
        while queue:
            current = queue.pop(0)
            if current:
                node, insert_position = current
                if len(serialized) < insert_position + 1:
                    length_to_extend = (insert_position + 1) - len(serialized)
                    serialized = serialized + [NULL_NODE] * length_to_extend

                if node:
                    serialized[insert_position] = str(node.value)
                    if node.left:
                        left_position = (2 * insert_position) + 1
                        queue.append((node.left, left_position))
                    if node.right:
                        right_position = (2 * insert_position) + 2
                        queue.append((node.right, right_position))
            else:
                if queue:
                    queue.append(None)

        return SEPERATOR.join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """
        if data == "":
            return None

        tree_values = data.split(SEPERATOR)
        tree_values = [NULL_NODE if value == NULL_NODE else int(value) for value in tree_values]
        root = TreeNode(value=tree_values[0])

        def insert_nodes(node, values, parent_level):
            if parent_level == len(values):
                return
            left_node_position = (2 * parent_level) + 1
            right_node_position = (2 * parent_level) + 2
            if left_node_position < len(values):
                left_value = values[left_node_position]
                if left_value != NULL_NODE:
                    left_node = TreeNode(left_value)
                    node.left = left_node
                    insert_nodes(node.left, values, left_node_position)
            if right_node_position < len(values):
                right_value = values[right_node_position]
                if right_value != NULL_NODE:
                    right_node = TreeNode(right_value)
                    node.right = right_node
                    insert_nodes(node.right, values, right_node_position)

        insert_nodes(root, tree_values, 0)
        return root


class Codec2:

    def serialize(self, root):
        accumulator = []

        def preorder(node):
            if node:
                accumulator.append(str(node.value))
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return SEPERATOR.join(accumulator)

    def deserialize(self, data):
        if data == "":
            return None

        tree_values = data.split(SEPERATOR)
        tree_values = [int(value) for value in tree_values]

        parent = root = TreeNode(value=tree_values[0])
        n = len(tree_values)
        i = 1
        stack = [TreeNode(value=float("inf"))]

        while i < n:
            current_val = tree_values[i]
            if current_val < parent.value:
                new_node = TreeNode(value=current_val)
                parent.left = new_node
                stack.append(parent)
                parent = new_node
                i += 1
            else:
                if parent.value < current_val < stack[-1].value:
                    new_node = TreeNode(value=current_val)
                    parent.right = new_node
                    parent = new_node
                    i += 1
                else:
                    parent = stack.pop()

        return root
