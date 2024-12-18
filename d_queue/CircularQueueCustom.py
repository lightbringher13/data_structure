class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k  # Fixed-size list
        # Initially, both front and rear are -1 (queue is empty)
        self.front = -1
        self.rear = -1

    def is_empty(self) -> bool:
        return self.front == -1

    def is_full(self) -> bool:
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        if self.front == self.rear:  # Only one element left in the queue
            self.front = self.rear = -1  # Reset the queue
        else:
            self.front = (self.front + 1) % self.size
        return True

    def front_item(self) -> int:
        if self.is_empty():
            return -1
        return self.queue[self.front]

    def rear_item(self) -> int:
        if self.is_empty():
            return -1
        return self.queue[self.rear]


# Example usage
cq = MyCircularQueue(3)  # Circular queue of size 3
print(cq.enqueue(1))  # Returns True
print(cq.enqueue(2))  # Returns True
print(cq.enqueue(3))  # Returns True
print(cq.enqueue(4))  # Returns False (queue is full)
print(cq.rear_item())  # Returns 3 (last item)
print(cq.is_full())   # Returns True
print(cq.dequeue())   # Returns True
print(cq.enqueue(4))  # Returns True
print(cq.rear_item())  # Returns 4 (new last item)
