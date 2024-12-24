# list vs linked list
# search: list is easier using index
# search: linkde list is harder following every node
# insert: linkded list is easier
# insert: list is harder. after insert move the value to right

# using dummy node is essential
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = Node()  # Dummy node as the head

    def insert_at_beginning(self, value):
        """Insert a new node at the beginning."""
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def insert_at_end(self, value):
        """Insert a new node at the end."""
        new_node = Node(value)
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node

    def delete_by_value(self, value):
        """Delete the first node with the specified value."""
        current = self.head  # Start from the dummy node
        while current.next and current.next.data != value:
            current = current.next
        if current.next:  # Found the node to delete
            current.next = current.next.next
        else:
            print(f"Value {value} not found")

    def traverse(self):
        """Traverse and print all the nodes in the list."""
        current = self.head.next  # Skip the dummy node
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        """Search for a node with the specified key."""
        current = self.head.next  # Skip the dummy node
        while current:
            if current.data == key:
                print(f"Value found: {key}")
                return current
            current = current.next
        print(f"Value {key} not found")
        return None

    def length(self):
        """Return the number of real nodes in the list."""
        count = 0
        current = self.head.next  # Skip the dummy node
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        """Make the list iterable."""
        current = self.head.next  # Skip the dummy node
        while current:
            yield current.data  # Yield the data of the current node
            current = current.next


if __name__ == "__main__":
    sll = SinglyLinkedList()

    # Insert at the beginning
    sll.insert_at_beginning(10)
    sll.insert_at_beginning(20)
    sll.insert_at_beginning(30)

    # Insert at the end
    sll.insert_at_end(40)
    sll.insert_at_end(50)

    # Traverse the list
    print("List contents:")
    sll.traverse()  # Output: 30 -> 20 -> 10 -> 40 -> 50 -> None

    # Search for a value
    sll.search(20)  # Output: Value found: 20
    sll.search(60)  # Output: Value 60 not found

    # Delete a value
    sll.delete_by_value(10)
    print("List after deleting 10:")
    sll.traverse()  # Output: 30 -> 20 -> 40 -> 50 -> None

    # Get the length of the list
    # Output: Length of the list: 4
    print(f"Length of the list: {sll.length()}")

    # Iterate through the list using the generator
    print("Iterating through the list:")
    for value in sll:
        print(value, end=" -> ")
    print("None")
