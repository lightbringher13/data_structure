class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  # Dummy head node
        self.tail = Node()  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def delete_by_value(self, data):
        """Delete the first node with the specified value."""
        current = self.head.next  # Start after the dummy head
        while current != self.tail:  # Traverse until the dummy tail
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return  # Exit after deleting the node
            current = current.next
        print(f"Value {data} not found")

    def traverse_forward(self):
        """Traverse and print all nodes from head to tail."""
        current = self.head.next  # Skip the dummy head
        while current != self.tail:  # Stop at the dummy tail
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """Traverse and print all nodes from tail to head."""
        current = self.tail.prev  # Skip the dummy tail
        while current != self.head:  # Stop at the dummy head
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

    def search(self, data):
        """Search for a node with the specified value."""
        current = self.head.next  # Start after the dummy head
        while current != self.tail:
            if current.data == data:
                print(f"Value found: {data}")
                return current
            current = current.next
        print(f"Value {data} not found")
        return None

    def length(self):
        """Return the number of real nodes in the list."""
        count = 0
        current = self.head.next  # Skip the dummy head
        while current != self.tail:
            count += 1
            current = current.next
        return count


if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert at the beginning
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(30)

    # Insert at the end
    dll.insert_at_end(40)
    dll.insert_at_end(50)

    # Traverse forward
    print("Forward traversal:")
    dll.traverse_forward()  # Output: 30 -> 20 -> 10 -> 40 -> 50 -> None

    # Traverse backward
    print("Backward traversal:")
    dll.traverse_backward()  # Output: 50 -> 40 -> 10 -> 20 -> 30 -> None

    # Delete a value
    dll.delete_by_value(10)
    print("After deleting 10:")
    dll.traverse_forward()  # Output: 30 -> 20 -> 40 -> 50 -> None

    # Search for a value
    dll.search(20)  # Output: Value found: 20
    dll.search(60)  # Output: Value 60 not found

    # Length of the list
    # Output: Length of the list: 4
    print(f"Length of the list: {dll.length()}")
