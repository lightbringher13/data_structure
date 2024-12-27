"""
Heap: every parent node >= its child node
No None node fill left

insert, find_max, delete_max

insert: O(logn)
find_max: O(1)
delete_max: O(logn)
make_heap: O(n)
heapify_down: O(logn)
heapify_up: O(logn)
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Insert a new value into the heap."""
        self.heap.append(value)        # Add the new value at the end
        self.heapify_up(len(self.heap) - 1)  # Maintain heap property

    def heapify_up(self, index):
        """Ensure the max-heap property is maintained by moving the element up."""
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            # Swap with the parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def extract_max(self):
        """Remove and return the maximum element from the heap."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self.heapify_down(0)            # Maintain heap property
        return max_value

    def heapify_down(self, index):
        """Ensure the max-heap property is maintained by moving the element down."""
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            max_index = index

            # Check if left child exists and is greater than the current node
            if left_child < len(self.heap) and self.heap[left_child] > self.heap[max_index]:
                max_index = left_child

            # Check if right child exists and is greater than the max candidate so far
            if right_child < len(self.heap) and self.heap[right_child] > self.heap[max_index]:
                max_index = right_child

            # If the current node is the largest, we're done
            if max_index == index:
                break

            # Otherwise, swap and continue
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            index = max_index

    def make_max_heap(self):
        # Start from the last non-leaf node and apply heapify_down to each
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def peek(self):
        """Return the maximum element without removing it."""
        return self.heap[0] if self.heap else None

    def __str__(self):
        """Display the heap."""
        return str(self.heap)


# Example usage:
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
print("Heap after inserts:", heap)   # Should maintain max-heap property
print("Max element extracted:", heap.extract_max())  # Should return 30
# Remaining elements in max-heap order
print("Heap after extracting max:", heap)
