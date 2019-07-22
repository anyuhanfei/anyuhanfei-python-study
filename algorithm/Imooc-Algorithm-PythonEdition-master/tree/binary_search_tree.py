import random


class TreeNode:
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, key, value):
        if self.root == None:
            self.root = TreeNode(key, value)
            self.count += 1
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node == None:
            node = TreeNode(key, value)
            self.count += 1
            return
        if node.key == key:
            node.value = value
        elif node.key > key:
            self._insert(node.left, key, value)
        else:
            self._insert(node.right, key, value)

    def print_root(self, node = 'root'):
        if node == 'root':
            node = self.root
        if node != None:
            print('%s: %s' % (node.key, node.value))
            self.print_root(node.left)
            self.print_root(node.right)


if __name__ == "__main__":
    b = BinarySearchTree()
    for i in range(0, 10):
        value = random.randint(100, 1000)
        b.insert(i, value)
    b.print_root()
    print(b.count)