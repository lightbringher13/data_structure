class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_the_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node  # Update the head

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.head = self.tail = new_node  # Properly initialize the list
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node  # Update the tail

    def delete_by_value(self, data):
        current = self.head
        while current and current.data != data:  # Traverse to find the node
            current = current.next
        if current == None:
            print("Value not found")
            return
        if current == self.head:  # Node to delete is the head
            self.head = current.next
            if self.head != None:
                self.head.prev = None
        elif current == self.tail:  # Node to delete is the tail
            self.tail = current.prev
            if self.tail != None:
                self.tail.next = None
        else:  # Node to delete is in the middle
            current.prev.next = current.next
            current.next.prev = current.prev
        current = None  # Clear the reference to the deleted node

    def traverse_forward(self):
        current = self.head
        while current:
            print(f"{current.data}", end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.tail  # Start from the tail
        while current:
            print(f"{current.data}", end=" -> ")
            current = current.prev
        print("None")

    def search(self, data):
        current = self.head
        while current and current.data != data:  # Traverse to find the value
            current = current.next
        if current == None:
            print("Value not found")
            return None
        else:
            print(f"Value found: {current.data}")
            return current

    def length(self):
        count = 0
        current = self.head
        while current:  # Traverse to count the nodes
            count += 1
            current = current.next
        return count


if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert at the beginning
    dll.insert_at_the_beginning(10)
    dll.insert_at_the_beginning(20)
    dll.insert_at_the_beginning(30)

    # Insert at the end
    dll.insert_at_end(40)
    dll.insert_at_end(50)

    # Forward traversal
    dll.traverse_forward()  # Output: 30 -> 20 -> 10 -> 40 -> 50 -> None

    # Backward traversal
    dll.traverse_backward()  # Output: 50 -> 40 -> 10 -> 20 -> 30 -> None

    # Delete a value
    dll.delete_by_value(10)
    dll.traverse_forward()  # Output: 30 -> 20 -> 40 -> 50 -> None

    # Search for a value
    dll.search(20)  # Output: Value found: 20
    dll.search(60)  # Output: Value not found

    # Length of the list
    print(dll.length())  # Output: 4
