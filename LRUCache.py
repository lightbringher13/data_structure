class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map to store key -> node mapping
        # Creating a dummy head and tail node to avoid checking null pointers.
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Helper function to remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        """Helper function to add a node right after the head."""
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

    def get(self, key: int) -> int:
        """Retrieve the value of the key if present, else return -1."""
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the head (most recently used)
            self._remove(node)
            self._add(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """Insert or update the value for the given key."""
        if key in self.cache:
            # Update the value and move the node to the head (most recently used)
            self._remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            # Remove the least recently used item (which is at the tail's prev)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

        # Add new node to the head
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node


# Example Usage:
cache = LRUCache(2)

cache.put(1, 1)  # Cache: {1: 1}
cache.put(2, 2)  # Cache: {1: 1, 2: 2}
print(cache.get(1))  # Returns 1, Cache: {2: 2, 1: 1}
cache.put(3, 3)  # Evicts key 2, Cache: {1: 1, 3: 3}
print(cache.get(2))  # Returns -1 (not found)
cache.put(4, 4)  # Evicts key 1, Cache: {3: 3, 4: 4}
print(cache.get(1))  # Returns -1 (not found)
print(cache.get(3))  # Returns 3, Cache: {4: 4, 3: 3}
print(cache.get(4))  # Returns 4, Cache: {3: 3, 4: 4}
