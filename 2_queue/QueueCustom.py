class Queue:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)  # Pop from the front (FIFO)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def show(self):
        return self.items
