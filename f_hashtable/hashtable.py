class HashTable:
    def __init__(self, size=10):
        self.size = size
        # Initialize table with empty lists for chaining
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Generate a hash for the given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        # Check if the key already exists and update
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If key does not exist, append new pair
        self.table[index].append([key, value])

    def get(self, key):
        """Retrieve the value associated with a key."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Return None if key not found

    def delete(self, key):
        """Remove the key-value pair from the hash table."""
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True  # Successfully deleted
        return False  # Return False if key not found

    def __str__(self):
        """Display the hash table for debugging."""
        return str(self.table)


# Example usage:
ht = HashTable(size=5)
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("orange", 300)
ht.insert("grape", 400)


print("Hash Table:", ht)  # View the hash table
print("Get apple:", ht.get("apple"))  # Get a value
print("Delete apple:", ht.delete("apple"))  # Delete a key
print("Get apple after deletion:", ht.get("apple"))  # Check if deleted
print("Hash Table after deletion:", ht)  # View the hash table after deletion

# def two_sum(nums, target):
#     hash_table = {}
#     for i, num in enumerate(nums):
#         complement = target - num

#         if complement in hash_table:
#             return [hash_table[complement], i]

#         hash_table[num] = i
#         print(f"  Updated hash_table: {hash_table}\n")

#     return []


# # Example Usage:
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))
