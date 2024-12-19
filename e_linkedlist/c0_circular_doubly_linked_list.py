class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        # If the list is empty
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Circular link
            new_node.prev = self.head  # Circular link
        else:
            # Traverse to the last node
            last = self.head.prev  # The last node will be the previous of the head
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    # Insert at the front of the list
    def insert_at_front(self, data):
        new_node = Node(data)
        # If the list is empty
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Circular link
            new_node.prev = self.head  # Circular link
        else:
            last = self.head.prev  # Get the last node (tail)
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node
            self.head = new_node  # Update head to the new node

    # Display the list
    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    # Delete a node by value
    def delete(self, key):
        # If the list is empty
        if not self.head:
            print("List is empty")
            return

        current = self.head
        prev_node = None
        while True:
            if current.data == key:
                # If there's only one node
                if current == self.head and current.next == self.head:
                    self.head = None
                    return

                # If the node to be deleted is the head
                if current == self.head:
                    last = self.head.prev  # Get the last node (tail)
                    self.head = self.head.next  # Move the head to the next node
                    last.next = self.head
                    self.head.prev = last

                else:
                    prev_node.next = current.next
                    current.next.prev = prev_node

                return

            prev_node = current
            current = current.next
            if current == self.head:
                break
        print("Key not found!")

    def find_node_by_key(self, key):
        current = self.head
        if not self.head:
            return None
        while True:
            if current.data == key:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def splice(self, start_key, end_key, insert_key):
        if not self.head:
            print("The list is empty. Cannot splice.")
            return

        # Step 1: Find start, end, and insert nodes by key
        start_node = self.find_node_by_key(start_key)
        end_node = self.find_node_by_key(end_key)
        insert_node = self.find_node_by_key(insert_key)

        if not start_node or not end_node or not insert_node:
            print("Invalid keys for splicing.")
            return

        # Step 2: Detach the spliced segment from the list
        start_prev = start_node.prev
        end_next = end_node.next

        # Reconnect the list after removing the spliced segment
        start_prev.next = end_next
        end_next.prev = start_prev

        # Step 3: Insert the spliced segment at the insert position
        insert_next = insert_node.next

        # Connect the spliced segment
        start_node.prev = insert_node
        insert_node.next = start_node

        end_node.next = insert_next
        insert_next.prev = end_node


# Example usage
cdll = CircularDoublyLinkedList()
# cdll.insert_at_end(10)
# cdll.insert_at_end(20)
# cdll.insert_at_end(30)
# cdll.insert_at_front(5)
# cdll.display()  # Output: 5 10 20 30

# cdll.delete(20)
# cdll.display()  # Output: 5 10 30

# Inserting elements
for i in range(1, 11):  # Adding 10 elements (1 to 10)
    cdll.insert_at_end(i)

print("Original List:")
cdll.display()

# Splicing: Remove a section of 3 nodes starting at position 2, insert after position 7
cdll.splice(2, 6, 7)

print("After Splice:")
cdll.display()
