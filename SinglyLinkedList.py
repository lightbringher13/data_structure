# Node class for individual elements of the list
class Node:
    def __init__(self, data=None):
        self.data = data  # Data to store
        self.next = None  # Reference to the next node

# Singly Linked List class


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # Insert at the beginning of the list
    def insert_at_head(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point new node to current head
        self.head = new_node  # Update head to the new node

    # Insert at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If list is empty, new node is head
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Append the new node

    # Delete a node by value
    def delete(self, key):
        current = self.head
        previous = None

        # If the list is empty
        if not current:
            print("List is empty!")
            return

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next  # Move head to the next node
            current = None  # Delete the current node
            return

        # Traverse the list to find the key to be deleted
        while current and current.data != key:
            previous = current
            current = current.next

        # If the key is not present
        if current is None:
            print("Key not found in the list!")
            return

        # Unlink the node from the linked list
        previous.next = current.next
        current = None  # Delete the current node

    def remove_nth_from_end(self, n):
        first = self.head
        second = self.head

        # Move `first` pointer `n` steps ahead
        for _ in range(n):
            if first is None:  # Check if `n` is greater than the length of the list
                print("n is larger than the list length")
                return
            first = first.next

        # Special case: if `first` is None after moving `n` steps,
        # it means we need to remove the head node
        if not first:
            self.head = self.head.next  # Move head to the next node
            return

        # Move both pointers until `first` reaches the end of the list
        while first.next:
            first = first.next
            second = second.next

        # Now `second` points to the node just before the nth node from the end
        removed_data = second.next.data  # For display purposes
        second.next = second.next.next  # Skip the nth node from the end
        print(f"Removed: {removed_data}")

    # Display the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Search for an element in the list
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False


# Example usage
linked_list = SinglyLinkedList()

# Insert elements
linked_list.insert_at_head(1)
linked_list.insert_at_head(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(4)
linked_list.insert_at_end(5)
linked_list.insert_at_end(6)
linked_list.insert_at_end(7)
linked_list.insert_at_end(8)
linked_list.insert_at_end(9)
linked_list.insert_at_end(10)
linked_list.insert_at_end(11)


# Display the list
linked_list.display()

# # Search for an element
# print("Element found:", linked_list.search(4))

# # Delete an element
# linked_list.delete(3)
# linked_list.display()
linked_list.remove_nth_from_end(4)
linked_list.display()
