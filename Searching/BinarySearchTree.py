class Node:
    def __init__(self, key, value, left_child=None, right_child=None, size=1):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class BinarySearchTree:
    def __init__(self, key, value):
        self.root = Node(key, value)

    def put(self, key, value):
        self.insert_node(self.root, key, value)

    def insert_node(self, current_node: Node, key, value):
        if current_node is None:
            return Node(key, value)
        elif key < current_node.key:
            current_node.left_child = self.insert_node(current_node.left_child, key, value)
        elif key > current_node.key:
            current_node.right_child = self.insert_node(current_node.right_child, key, value)
        else:
            current_node.value = value
        return current_node

    def get(self, key):
        return self.search(key, self.root)

    def search(self, key, node: Node):
        if node is None:
            return None
        elif abs(node.key - key) < 1e-9:
            return node
        elif node.key < key:
            return self.search(key, node.right_child)
        elif node.key > key:
            return self.search(key, node.left_child)

    def max(self):
        return self.max_value(self.root)

    def max_value(self, node: Node):
        if node.right_child is None:
            return node
        else:
            return self.max_value(node.right_child)

    def min(self):
        return self.min_value(self.root)

    def min_value(self, node: Node):
        if node.left_child is None:
            return node
        else:
            return self.min_value(node.left_child)

    def floor(self, key):
        node = self.floor_node(self.root, key)
        if node is None:
            return None
        else:
            return node.key

    def floor_node(self, node: Node, key):
        if node is None:
            return None
        if abs(node.key - key) < 1e-9:
            return node
        elif key < node.key:
            return self.floor_node(node.left_child, key)

        node_t = self.floor_node(node.right_child, key)
        if node_t is not None:
            return node_t
        else:
            return node

    def ceiling(self, key):
        node = self.ceiling_node(self.root, key)
        if node is None:
            return None
        return node.key

    def ceiling_node(self, node: Node, key):
        if node is None:
            return None
        if abs(node.key - key) < 1e-9:
            return node
        elif node.key < key:
            return self.ceiling_node(node.right_child, key)
        node_t = self.ceiling_node(node.left_child, key)
        if node_t is not None:
            return node_t
        return node

    def delete_min(self, node: Node):
        if node.left_child is None:
            return node.right_child
        node.left_child = self.delete_min(node.left_child)
        return node

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def delete_node(self, node: Node, key):
        if node is None:
            return None
        if key < node.key:
            node.left_child = self.delete_node(node.left_child, key)
        elif key > node.key:
            node.right_child = self.delete_node(node.right_child, key)
        else:
            if node.right_child is None:
                return node.left_child
            if node.left_child is None:
                return node.right_child

            t = node
            node = self.min_value(node.right_child)
            node.right_child = self.delete_min(t.right_child)
            node.left_child = t.left_child

        return node


if __name__ == '__main__':
    btree = BinarySearchTree(key=2, value=2)
    btree.put(3, 3313)
    btree.put(-1, 1)
    btree.put(32, 3313)
    btree.put(55, -12313)
    btree.put(311, 3)
    print(btree.get(55).value)
    print(btree.max().value)
    print(btree.min().value)
    print(btree.floor(56))
    print(btree.ceiling(-2))
    btree.delete(2)
    print(btree.get(2) is None)
