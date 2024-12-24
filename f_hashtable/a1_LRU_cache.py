class Node:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value

# MRU(Most Recently Used), LRU(Least Recently Used)

# get: use the dict to find the node -> O(1)
# move the node at front

# put: use dict to find and update -> O(1)
# not exist insert at the front
# if cache exceeds capacity remove LRU(tail)


class LruCache:
    def __init__(self, capacity):
        self.head = Node(0, 0)
        self.capacity = capacity
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        self.head.next.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
