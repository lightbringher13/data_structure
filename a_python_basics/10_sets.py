set1 = {10, 56, 89, 90, "riss", True, 10, 1}
print(set1)

# dict
set2 = {}
print(type(set2))

# set()
# does not have index
# sets are unordered collections
# but mutable  can add,remove, modify
# Duplicate values are automatically removed.
set3 = set()
print(type(set3))

# set add()
set3.add(89)
print(set3)

# set remove()
set3.remove(89)
print(set3)

# set pop()
set1.pop()
print(set1)

# can add immutable data
set1.add((23, 23))
print(set1)

# union sets vs |
set1 = {"riss", "Ram", "Jenny"}
set2 = {"riss", "ani", "lvo"}
set3 = {"kane", "rovo"}
# print(set1.union(set2))
# print(set1 | set2 | set3)
# print(set1.union(["jen", "kat"]))  # union covert dynamically
# # print(set1 | ["jen", "jordan"]) | only with sets

# # update does union and update
# set1.update(set2)
# print(set1)

# # intersection same element
# print(set1.intersection(set2))
# print(set1 & set2)

# # intersection_update
# print(set1.intersection_update(set2))

# # difference
# print(set1.difference(set2))
# print(set1 - set2)
# print(set1.difference(set2, set3))
# print(set1.difference_update(set2))

# symmetric_difference union - intersection
print(set1.symmetric_difference(set2))  # method can not do multiple
# print(set1 ^ set2 ^ set3)
# print(set1.symmetric_difference_update(set2))

# isdisjoint() non intersection returns bool
print(set1.isdisjoint(set2))
print(set1.isdisjoint(["jen", "mo", "su"]))

# # subset returns bool
# print(set1.issubset(set2))
# print(set1.issubset(["jen", "mo", "su"]))
# print(set1 <= set2)

# # superset every element is in superset returns bool
# print(set1.issuperset(set2))
# print(set1.issuperset(["jen", "mon", "ur"]))
# print(set1 >= set2)

# # clear() empty set
# print(set2.clear())

# # delete set itself
# del set2
# print(set2) return error no set2
