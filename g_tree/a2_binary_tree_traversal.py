"""
preorder: MLR
inorder: LMR
postorder: LRM
reconstruct binary tree: you need an inorder traversal
 + postorder or preorder to uniquely define the binary tree
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None


class BinaryTreeTraversal:
    def __init__(self):
        self.root = None

    def preorder_traversal(self, node):
        """Preorder: Visit Root, then Left, then Right"""
        if node:
            print(node.value, end=" ")  # Visit the root
            self.preorder_traversal(node.left)  # Traverse left subtree
            self.preorder_traversal(node.right)  # Traverse right subtree

    def inorder_traversal(self, node):
        """Inorder: Visit Left, then Root, then Right"""
        if node:
            self.inorder_traversal(node.left)  # Traverse left subtree
            print(node.value, end=" ")  # Visit the root
            self.inorder_traversal(node.right)  # Traverse right subtree

    def postorder_traversal(self, node):
        """Postorder: Visit Left, then Right, then Root"""
        if node:
            self.postorder_traversal(node.left)  # Traverse left subtree
            self.postorder_traversal(node.right)  # Traverse right subtree
            print(node.value, end=" ")  # Visit the root


# Example Usage
if __name__ == "__main__":
    tree = BinaryTreeTraversal()

    # Constructing a sample tree:
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7

    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("Preorder Traversal:")
    tree.preorder_traversal(tree.root)  # Output: 1 2 4 5 3 6 7
    print("\nInorder Traversal:")
    tree.inorder_traversal(tree.root)   # Output: 4 2 5 1 6 3 7
    print("\nPostorder Traversal:")
    tree.postorder_traversal(tree.root)  # Output: 4 5 2 6 7 3 1
