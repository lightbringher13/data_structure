class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node = self.head

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, node, data):
        if not node:
            print("node is not valid")
            return None
        new_node = Node(data)
        new_node.prev = node
        new_node.nex = node.next
        if node.next:
            node.next.prev = new_node
        node.next = new_node
        if node == self.tail:
            self.tail = new_node

    def delete_by_value(self, data):
        if self.head == None:
            print("empty")
            return
        current = self.head
        while current and current.data != data:
            current = current.next
        if current == self.head:
            self.head = current.next
            if self.head != None:
                self.head.prev = None
        elif current == self.tail:
            self.tail = current.next
            if self.tail != None:
                self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        current = None

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

    def search(self, data):
        current = self.head
        while current.next:
            current = current.next
        if current.next:
            return True
        else:
            return False

    def length(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count = count + 1
        return count
