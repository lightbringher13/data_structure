# hashtable
# table: list, slot size: usually 2**n

# hash function: indexing locate the value
# ex) f(k) = k % m
# f(k) = (k % p) % m not too good too much collison
# perfect hash function: key -> slot 1:1 impossible
# universial hash function: prbality(collison) = 1/m this is hard too
# c - universial hash function: c/m, set, search, remove O(1)

# good hash function
# fast computation == easy formula
# less collison
# trade off relationship

# collison resolution method
# key -> hash function -> index
# -> if collison -> cluseter -> collison resolution method
# open addressing: linear probing, quadratic probing,
# double hashing

# linear probing: collison -> go down until blank
# -> makes cluster less cluster better

# quadratic probing: collison -> k, k+1**2, k+2**2, K+3**2
# double hasing: collison -> two hash function

# chainig: each slot is linked list

# hash table functionality
# how to deal with cluster size
# hash function, collison resolution method, load factor

# load factor: n(stored item count) / M(slot count)
# load factor: 0<= load factor < 1
# load factor == 0.5 half occupied
# cluster size: n/m <= 1/2, double the slot sizes -> O(1)

# good hash table -> c - universial hash function + n/m <= 50%
# collison resoltion method does not matter wether
# open addressing or chaining
class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.hash_table[index]:
            if pair[0] == key:
                pair[1] = value  # Update the value if key already exists
                return
        # Append new key-value pair
        self.hash_table[index].append([key, value])

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.hash_table[index]):
            if pair[0] == key:  # Check the key in the pair
                del self.hash_table[index][i]
                return True
        return False  # Key not found

    def search(self, key):
        result = self.get(key)
        if result:
            print(f"Found: {result}")
        else:
            print("Key not found")

    def get(self, key):
        index = self._hash(key)
        for pair in self.hash_table[index]:
            if pair[0] == key:
                return pair[1]  # Return the value
        return None  # Key not found

    def display(self):
        print(self.hash_table)
