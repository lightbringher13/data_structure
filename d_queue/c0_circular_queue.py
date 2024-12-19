class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.front = -1
        self.rear = -1
        self.items = [None] * capacity

    def enqueue(self, value):
        if self.is_full():
            print("CircularQueue is full")
            return
        if self.is_empty():
            self.front = 0  # Initialize front when adding the first element
        # Circular increment for rear
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("CircularQueue is empty")
            return None
        value = self.items[self.front]  # Retrieve the value at the front
        self.items[self.front] = None  # Clear the slot (optional)
        # Circular increment for front
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.size == 0:  # Reset front and rear when the queue becomes empty
            self.front = -1
            self.rear = -1
        return value

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def peek(self):
        if self.is_empty():
            print("CircularQueue is empty")
            return None
        return self.items[self.front]

    def __len__(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("CircularQueue is empty")
            return
        print("Queue contents:", end=" ")
        index = self.front
        for _ in range(self.size):
            print(self.items[index], end=" ")
            index = (index + 1) % self.capacity  # Circular increment
        print()


if __name__ == "__main__":
    cq = CircularQueue(5)

    # Enqueue elements
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)

    # Display queue
    cq.display()  # Output: Queue contents: 10 20 30 40 50

    # Try to enqueue when full
    cq.enqueue(60)  # Output: CircularQueue is full

    # Dequeue elements
    print("Dequeued:", cq.dequeue())  # Output: Dequeued: 10
    print("Dequeued:", cq.dequeue())  # Output: Dequeued: 20

    # Display queue after dequeue
    cq.display()  # Output: Queue contents: 30 40 50

    # Enqueue more elements
    cq.enqueue(60)
    cq.enqueue(70)

    # Display queue
    cq.display()  # Output: Queue contents: 30 40 50 60 70

    # Peek at the front element
    print("Front element:", cq.peek())  # Output: Front element: 30

    # Check if the queue is full
    print("Is full?", cq.is_full())  # Output: Is full? True

    # Dequeue remaining elements
    while not cq.is_empty():
        print("Dequeued:", cq.dequeue())

    # Check if the queue is empty
    print("Is empty?", cq.is_empty())  # Output: Is empty? True
