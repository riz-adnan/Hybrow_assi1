class Node:
    def __init__(self, data):     #The node has left and right child and data.
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None      #root node
        self.size = 0         #tracks the size

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
        self.size += 1

    def _insert(self, data, node):
        if data < node.data:             
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, node):
        if node is None:
            return False
        elif node.data == data:
            return True
        elif data < node.data:
            return self._search(data, node.left)
        else:
            return self._search(data, node.right)

    def delete(self, data):
        if self.root is None:
            return False
        else:
            self.root, deleted = self._delete(data, self.root)
            if deleted:
                self.size -= 1
            return deleted

    def _delete(self, data, node):
        if node is None:
            return node, False
        deleted = False
        if data == node.data:
            deleted = True
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.data = successor.data
                node.right, deleted = self._delete(successor.data, node.right)
        elif data < node.data:
            node.left, deleted = self._delete(data, node.left)
        else:
            node.right, deleted = self._delete(data, node.right)
        return node, deleted

    def size(self):
        return self.size
''' When the first element is added it is added in the root node. The next element are added recursively in the tree '''