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
        self.head = Node()  # Dummy head node
        self.tail = Node()  # Dummy tail node
        self.head.next = self.tail  # Head points to tail initially

    def insert_front(self, value):
        """Inserts a new node at the beginning (after dummy head)."""
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def insert_last(self, value):
        """Inserts a new node at the end (before dummy tail)."""
        new_node = Node(value)
        current = self.head

        while current.next != self.tail:  # Find the last real node
            current = current.next

        current.next = new_node
        new_node.next = self.tail  # Ensure new node points to dummy tail

    def search(self, value):
        """Searches for a node with the given value."""
        current = self.head.next  # Start from first real node
        while current != self.tail:
            if current.data == value:
                return current  # Found the node
            current = current.next
        return None  # Not found

    def delete_by_value(self, value):
        """Deletes the first node with the given value."""
        prev = self.head
        current = self.head.next

        while current != self.tail:  # Traverse until dummy tail
            if current.data == value:  # Found the node to delete
                prev.next = current.next  # Remove node by skipping it

                # If the deleted node was the last real node, ensure it points to the tail
                if current.next == self.tail:
                    prev.next = self.tail  # Ensure last real node points to dummy tail

                return  # Exit after deleting the first occurrence

            prev, current = current, current.next

        print("No value found")  # Value not in the list

    def traverse(self):
        """Prints all elements in the linked list."""
        current = self.head.next
        while current != self.tail:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def iter(self):
        """Returns an iterator for the linked list."""
        current = self.head.next
        while current != self.tail:
            yield current.data  # Yield each node's data
            current = current.next

    def length(self):
        """Returns the number of real nodes in the list (without using a size variable)."""
        count = 0
        current = self.head.next
        while current != self.tail:
            count += 1
            current = current.next
        return count


if __name__ == "__main__":
    # ✅ Example Usage
    ll = SinglyLinkedList()
    ll.insert_front(10)
    ll.insert_front(20)
    ll.insert_last(30)
    ll.insert_last(40)

    print("\nBefore Deletion:")
    ll.traverse()  # Expected: 20 -> 10 -> 30 -> 40 -> None

    ll.delete_by_value(10)
    print("\nAfter Deleting 10:")
    ll.traverse()  # Expected: 20 -> 30 -> 40 -> None

    ll.delete_by_value(40)
    print("\nAfter Deleting 40 (last real node):")
    ll.traverse()  # Expected: 20 -> 30 -> None

    ll.delete_by_value(99)  # Expected: No value found

    print("\nFinal Length:", ll.length())  # Expected: 2

    print("\nIterating through list:")
    for value in ll.iter():
        print(value, end=" ")  # Expected: 20 30
