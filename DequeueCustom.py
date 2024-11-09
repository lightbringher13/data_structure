class Deque:
    def __init__(self):
        self.items = []  # Initialize an empty list for the deque

    # Add an item to the front of the deque
    def push_front(self, item):
        self.items.insert(0, item)  # Insert at the front (index 0)

    # Add an item to the rear of the deque
    def push_rear(self, item):
        self.items.append(item)  # Append at the rear (end of the list)

    # Remove and return the item from the front
    def pop_front(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove the first element (front)
        else:
            print("Deque is empty")

    # Remove and return the item from the rear
    def pop_rear(self):
        if not self.is_empty():
            return self.items.pop()  # Remove the last element (rear)
        else:
            print("Deque is empty")

    # Check if the deque is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return the size of the deque
    def __len__(self):
        return len(self.items)

    # Show the current deque
    def show(self):
        print(self.items)
