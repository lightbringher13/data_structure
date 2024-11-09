from QueueCustom import Queue


def JP(n, k):
    q = Queue()
    for i in range(n):
        q.push(i + 1)  # Queue starts from 1 to n

    while len(q) > 1:  # Continue until one element remains
        for _ in range(k - 1):
            q.push(q.pop())  # Move the first (k-1) elements to the end
        print(f"Eliminated: {q.pop()}")  # Eliminate the k-th person

    print(f"Last person standing is: {q.pop()}")  # Only one person left


JP(6, 3)
