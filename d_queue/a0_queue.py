# queue FIFO: First In First Out
#       4 5 6 7 7 7
#     /            ^
#    v              \
# dequeue           enqueue
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.items.pop(0)  # Remove the front item

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def display(self):
        print(self.items)
