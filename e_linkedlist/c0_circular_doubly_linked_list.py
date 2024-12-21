class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        current = self.head
        if current == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        if current == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail = new_node

    def delete_by_value(self, data):
        if self.head == None:
            print("empty")
            return None
        current = self.head
        while current.data != data:
            current = current.next
            if current == self.head:
                print("value not found")
                return
        if current == self.head:
            if self.head == self.tail:
                self.tail = self.head = None
            else:
                self.head = current.next
                self.head.prev = self.tail
                self.tail.next = self.head
        elif current == self.tail:
            self.tail = current.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        current.prev = None
        current.next = None
        current = None

    def traverse_forward(self):
        if not self.head:
            print("The list is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:  # Stop when we loop back to the head
                break
        print("(back to head)")

    def traverse_backward(self):
        if not self.tail:
            print("The list is empty")
            return
        current = self.tail
        while True:
            print(current.data, end=" -> ")
            current = current.prev
            if current == self.tail:  # Stop when we loop back to the tail
                break
        print("(back to tail)")

    def find_node(self, data):
        if self.head is None:
            print("Circular Doubly Linked List is empty")
            return None
        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            if current == self.head:  # Stop when we've looped back to the head
                break
        print(f"Value {data} not found")
        return None

    def splice(self, start_data, end_data, insert_data):
        start_node = self.find_node(start_data)
        end_node = self.find_node(end_data)
        insert_node = self.find_node(insert_data)

        # Handle invalid nodes
        if not start_node or not end_node or not insert_node:
            print("Invalid nodes for splice operation")
            return

        # Disconnect the range of nodes to splice
        start_prev = start_node.prev
        end_next = end_node.next

        # Connect the list, bypassing the spliced-out range
        start_prev.next = end_next
        end_next.prev = start_prev

        # Insert the spliced-out range after the `insert_node`
        insert_next = insert_node.next
        insert_node.next = start_node
        start_node.prev = insert_node
        end_node.next = insert_next
        insert_next.prev = end_node

        print(f"Spliced nodes from {start_data} to {
              end_data} after {insert_data}")
