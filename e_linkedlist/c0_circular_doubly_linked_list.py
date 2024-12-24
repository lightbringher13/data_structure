class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        # Initialize with a dummy node
        self.head = Node()
        self.head.next = self.head
        self.head.prev = self.head

    def insert_at_beginning(self, value):
        """Insert a new node at the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node

    def insert_at_end(self, value):
        """Insert a new node at the end of the list."""
        new_node = Node(value)
        new_node.prev = self.head.prev
        new_node.next = self.head
        self.head.prev.next = new_node
        self.head.prev = new_node

    def delete_by_value(self, value):
        """Delete the first node with the specified value."""
        current = self.head.next  # Start after the dummy node
        while current != self.head:  # Traverse until we loop back to the dummy node
            if current.data == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next
        print(f"Value {value} not found")

    def traverse_forward(self):
        """Traverse and print the list in forward direction."""
        current = self.head.next  # Start after the dummy node
        while current != self.head:
            print(current.data, end=" -> ")
            current = current.next
        print("HEAD")

    def traverse_backward(self):
        """Traverse and print the list in backward direction."""
        current = self.head.prev  # Start before the dummy node
        while current != self.head:
            print(current.data, end=" -> ")
            current = current.prev
        print("HEAD")

    def search(self, value):
        """Search for the first node with the specified value."""
        current = self.head.next  # Start after the dummy node
        position = 0  # Keep track of the position
        while current != self.head:  # Stop when we circle back to the dummy node
            if current.data == value:
                print(f"Value {value} found at position {position}")
                return current  # Return the found node
            current = current.next
            position += 1
        print(f"Value {value} not found")
        return None

    def length(self):
        """Return the number of real nodes in the list."""
        count = 0
        current = self.head.next  # Start after the dummy node
        while current != self.head:  # Stop when we circle back to the dummy node
            count += 1
            current = current.next
        return count


if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()

    # Insert at the beginning
    cdll.insert_at_beginning(10)
    cdll.insert_at_beginning(20)
    cdll.insert_at_beginning(30)

    # Insert at the end
    cdll.insert_at_end(40)
    cdll.insert_at_end(50)

    # Traverse forward
    print("Forward traversal:")
    cdll.traverse_forward()  # Output: 30 -> 20 -> 10 -> 40 -> 50 -> HEAD

    # Traverse backward
    print("Backward traversal:")
    cdll.traverse_backward()  # Output: 50 -> 40 -> 10 -> 20 -> 30 -> HEAD

    # Delete a value
    cdll.delete_by_value(10)
    print("After deleting 10:")
    cdll.traverse_forward()  # Output: 30 -> 20 -> 40 -> 50 -> HEAD

    # Try to delete a non-existent value
    cdll.delete_by_value(60)  # Output: Value 60 not found
