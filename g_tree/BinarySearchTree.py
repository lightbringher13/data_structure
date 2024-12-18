class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a new node with the given data."""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """Helper function to insert a node recursively."""
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, data):
        """Search for a node with the given data."""
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        """Helper function to search for a node recursively."""
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)

    def delete(self, data):
        """Delete a node with the given data."""
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        """Helper function to delete a node recursively."""
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node with one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: get the inorder successor (smallest in right subtree)
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete_recursive(node.right, temp.data)
        return node

    def _min_value_node(self, node):
        """Get the node with the minimum value in the tree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """Return an in-order traversal of the tree as a list."""
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        """Helper function for in-order traversal."""
        res = []
        if node:
            res = self._inorder_recursive(node.left)
            res.append(node.data)
            res = res + self._inorder_recursive(node.right)
        return res


# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
print("In-order Traversal:", bst.inorder_traversal())
print("Search 15:", bst.search(15))
bst.delete(10)
print("In-order Traversal after deletion:", bst.inorder_traversal())
