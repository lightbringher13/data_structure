from a0_queue import Queue


def josephus_problem(n, k):
    q = Queue()
    for i in range(1, int(n)+1):
        q.enqueue(i)
    q.display()
    while len(q) > 1:
        for _ in range(int(k)-1):
            # make it circular append the deleted
            q.enqueue(q.dequeue())  # evaluate the arguement first
        removed = q.dequeue()
        print(f"removed = {removed}")
        q.display()
    return q.dequeue()


if __name__ == "__main__":
    print(josephus_problem(10, 4))
