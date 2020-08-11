class Node:
    def __init__(self, key, value, parent=None):
        self.keys = [key]
        self.values = [value]
        self.children = []
        self.parent = parent

    def is_leaf(self):
        return len(self.children) == 0

    def get_node_type(self):
        key_count = len(self.keys)
        if key_count == 1:
            return 'TwoNode'
        if key_count == 2:
            return 'ThreeNode'
        if key_count == 3:
            return 'FourNode'
        raise Exception('Error')

    def __str__(self):
        if self.get_node_type() == 'TwoNode':
            return f"""key: {self.keys[0]} -> value: {self.values[0]}"""
        elif self.get_node_type() == 'ThreeNode':
            return f"""key_left: {self.keys[0]} -> value_left: {self.values[0]}
key_right: {self.keys[1]} -> value_right: {self.values[1]}"""


class TwoThreeTree:
    def __init__(self, key, value):
        self.root = Node(key, value)

    def put(self, key, value):
        self.insert(self.root, key, value)

    def insert(self, node: Node, key, value):
        if node is None:
            self.root = Node(key, value)
        if node.get_node_type() == 'TwoNode' and node.is_leaf():
            if node.keys[0] < key:
                node.keys.append(key)
                node.values.append(value)
            else:
                node.keys.insert(0, key)
                node.values.insert(0, value)

        elif node.get_node_type() == 'ThreeNode' and node.is_leaf():
            key_left = node.keys[0]
            key_right = node.keys[1]
            if key < key_left:
                node.keys.insert(0, key)
                node.values.insert(0, value)

            elif key_left < key < key_right:
                node.keys.insert(1, key)
                node.values.insert(1, value)

            elif key > key_right:
                node.keys.append(key)
                node.values.append(value)
            self.handle_four_node(node)

        elif node.get_node_type() == 'TwoNode':
            if node.keys[0] < key:
                self.insert(node.children[1], key, value)
            else:
                self.insert(node.children[0], key, value)
        elif node.get_node_type() == 'ThreeNode':
            key_left = node.keys[0]
            key_right = node.keys[1]
            if key < key_left:
                self.insert(node.children[0], key, value)
            if key_left < key < key_right:
                self.insert(node.children[1], key, value)
            else:
                self.insert(node.children[2], key, value)

    def handle_four_node(self, node: Node):
        if node.parent is None:
            key_middle = node.keys[1]
            value_middle = node.values[1]
            key_left = node.keys[0]
            value_left = node.values[0]
            key_right = node.keys[2]
            value_right = node.values[2]

            new_root = Node(key_middle, value_middle)
            left_node = Node(key_left, value_left)
            right_node = Node(key_right, value_right)

            if len(node.children) == 1:
                left_node.children.append(node.children[0])
            elif len(node.children) == 2:
                left_node.children.append(node.children[0])
                left_node.children.append(node.children[1])
            elif len(node.children) == 3:
                left_node.children.append(node.children[0])
                left_node.children.append(node.children[1])
                right_node.children.append(node.children[2])
            elif len(node.children) == 4:
                left_node.children.append(node.children[0])
                left_node.children.append(node.children[1])
                right_node.children.append(node.children[2])
                right_node.children.append(node.children[3])

            left_node.parent = new_root
            right_node.parent = new_root

            new_root.children.append(left_node)
            new_root.children.append(right_node)

            self.root = new_root
        else:
            parent_node = node.parent
            key_middle = node.keys[1]
            value_middle = node.values[1]
            key_left = node.keys[0]
            value_left = node.values[0]
            key_right = node.keys[2]
            value_right = node.values[2]

            left_node = Node(key_left, value_left)
            right_node = Node(key_right, value_right)

            if len(node.children) == 1:
                left_node.children.append(node.children[0])
            elif len(node.children) == 2:
                left_node.children.append(node.children[0])
                left_node.children.append(node.children[1])
            elif len(node.children) == 3:
                left_node.children.append(node.children[0])
                left_node.children.append(node.children[1])
                right_node.children.append(node.children[2])
            elif len(node.children) == 4:
                left_node.children.append(node.children[0])
                left_node.children.append(node.children[1])
                right_node.children.append(node.children[2])
                right_node.children.append(node.children[3])

            if parent_node.get_node_type() == 'TwoNode':
                if key_middle < parent_node.keys[0]:
                    parent_node.keys.insert(0, key_middle)
                    parent_node.values.insert(0, key_middle)
                    parent_node.children = [left_node, right_node, parent_node.children[1]]
                    left_node.parent = parent_node
                    right_node.parent = parent_node
                else:
                    parent_node.keys.append(key_middle)
                    parent_node.values.append(value_middle)
                    parent_node.children = [parent_node.children[0], left_node, right_node]
                    left_node.parent = parent_node
                    right_node.parent = parent_node
            elif parent_node.get_node_type() == 'ThreeNode':
                if key_middle < parent_node.keys[0]:

                    parent_node.keys.insert(0, key_middle)
                    parent_node.values.insert(0, value_middle)
                    parent_node.children = [left_node, right_node, parent_node.children[1], parent_node.children[2]]
                    left_node.parent = parent_node
                    right_node.parent = parent_node
                    self.handle_four_node(parent_node)

                elif parent_node.keys[0] < key_middle < parent_node.keys[1]:

                    parent_node.keys.insert(1, key_middle)
                    parent_node.values.insert(1, value_middle)
                    parent_node.children = [parent_node.children[0], left_node, right_node, parent_node.children[2]]
                    left_node.parent = parent_node
                    right_node.parent = parent_node
                    self.handle_four_node(parent_node)
                else:
                    parent_node.keys.append(key_middle)
                    parent_node.values.append(value_middle)
                    parent_node.children = [parent_node.children[0], parent_node.children[1], left_node, right_node]
                    left_node.parent = parent_node
                    right_node.parent = parent_node
                    self.handle_four_node(parent_node)


if __name__ == '__main__':
    tree = TwoThreeTree(1, 2)
    tree.put(3, 4)
    tree.put(4, 4)
    tree.put(-1, 4)
    tree.put(31, 4)
    tree.put(41, 4)
    tree.put(5, 4)
    tree.put(42, 4)
    print(tree.root)
    print('--')
    print(tree.root.children[0])
    print('--')
    print(tree.root.children[1])
    print('--')
    print(tree.root.children[2])
    print('--')
