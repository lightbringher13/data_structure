class Deque:
    def __init__(self):
        self.items = []

    def append(self, value):
        self.items.append(value)

    def append_left(self, value):
        self.items.insert(0, value)

    def pop(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        else:
            return self.items.pop()

    def pop_left(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        else:
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        else:
            return self.items[-1]

    def peek_left(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        else:
            return self.items[0]

    def display(self):
        print(self.items)
