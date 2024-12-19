# list vs linked list
# search: list is easier using index
# search: linkde list is harder following every node
# insert: linkded list is easier
# insert: list is harder. after insert move the value to right
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.root = None  # Start with an empty list

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.root
        self.root = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.root is None:  # If the list is empty
            self.root = new_node
            return
        current = self.root
        while current.next:  # Traverse to the end
            current = current.next
        current.next = new_node  # Link the new node at the end

    def delete_by_value(self, value):
        current = self.root
        if current and current.data == value:  # If the value is at the head
            self.root = current.next
            current = None
            return True  # Confirm deletion
        prev = None
        while current and current.data != value:  # Traverse to find the value
            prev = current
            current = current.next
        if not current:  # Value not found
            return False
        prev.next = current.next  # Bypass the node to delete it
        current = None
        return True  # Confirm deletion

    def traverse(self):
        if self.root is None:
            print("Singly Linked List is empty")
            return
        current = self.root
        while current:  # Traverse through the list
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicate the end of the list

    def search(self, key):
        if self.root is None:
            print("Singly Linked List is empty")
            return False
        current = self.root
        while current:  # Traverse to find the key
            if current.data == key:
                return True
            current = current.next
        return False  # Key not found

    def length(self):
        count = 0
        current = self.root
        while current:  # Count each node
            count += 1
            current = current.next
        return count

    # generator
    def __iter__(self):
        current = self.root
        while current:
            yield current.data  # unlike return it continues the process
            current = current.next


if __name__ == "__main__":
    s = SinglyLinkedList()
    s.insert_at_beginning(10)
    s.insert_at_beginning(20)
    s.insert_at_end(30)
    for i in s:
        print(i)
