class Node:
    def __init__(self, key, value, left_child=None, right_child=None):
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


if __name__ == '__main__':
    btree = BinarySearchTree(key=2, value=2)
    btree.put(3, 3313)
    btree.put(-1, 3313)
    btree.put(32, 3313)
    btree.put(55, -12313)
    btree.put(311, 3313)
    print(btree.get(55).value)
