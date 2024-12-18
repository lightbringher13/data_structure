class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head of the list

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_node  # Add new node at the end
        new_node.prev = current  # Set the previous pointer of the new node

    # Insert at the beginning
    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        new_node.next = self.head  # Set new node's next to the current head
        self.head.prev = new_node  # Set current head's prev to new node
        self.head = new_node  # Make new node the new head

    # Delete a node by value
    def delete(self, key):
        current = self.head

        # If the list is empty
        if not current:
            print("List is empty!")
            return

        # If the node to be deleted is the head
        if current and current.data == key:
            if current.next:  # If there's a next node
                current.next.prev = None
            self.head = current.next
            current = None
            return

        # Traverse the list to find the key to delete
        while current and current.data != key:
            current = current.next

        # If the key is not found
        if current is None:
            print("Key not found in the list!")
            return

        # Unlink the node from the list
        if current.next:  # If it's not the last node
            current.next.prev = current.prev
        if current.prev:  # If it's not the first node
            current.prev.next = current.next
        current = None  # Delete the current node

    # Traverse and print the list

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next

    # Traverse and print the list in reverse
    def print_reverse(self):
        current = self.head
        if not current:
            print("List is empty!")
            return
        # Go to the last node
        while current.next:
            current = current.next
        # Traverse backward using the prev pointer
        while current:
            print(current.data, end=" <-> " if current.prev else "\n")
            current = current.prev


# Example Usage:
dll = DoublyLinkedList()

# Insert some elements
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

# Print list
print("List (from head to end):")
dll.print_list()

# Insert at the head
dll.insert_at_head(5)

# Print list again
print("After inserting 5 at the head:")
dll.print_list()

# Delete a node
dll.delete(20)

# Print list after deletion
print("After deleting 20:")
dll.print_list()

# Print in reverse
print("List (from end to head):")
dll.print_reverse()
