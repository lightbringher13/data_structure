class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, value):
        """Add an item to the top of the stack."""
        self.items.append(value)

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def pop(self):
        """Remove and return the top item of the stack."""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.items.pop()

    def top(self):
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            print("Stack is empty. No top element.")
            return None
        return self.items[-1]

    def __len__(self):
        """Return the size of the stack."""
        return len(self.items)

    def display(self):
        """Display the items in the stack."""
        print(self.items)


if __name__ == "__main__":
    s = Stack()
    for i in range(10):
        s.push(i + 1)
    s.display()
    print(s.top())
    for i in range(11):
        print(s.pop())
