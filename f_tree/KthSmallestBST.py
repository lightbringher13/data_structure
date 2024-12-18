from collections import deque


class TreeNode:
    def __init__(self, data, right=None, left=None) -> None:
        self.data = data
        self.right = right
        self.left = left


def kth_smallest(root, k):
    stack = []
    count = 0
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        count += 1
        if count == k:
            print(root.data)
            return
        root = root.right


# Constructing the BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)
root.left.left.left = TreeNode(1)

# Finding the 3rd smallest element
kth_smallest(root, 3)  # Output: 3
