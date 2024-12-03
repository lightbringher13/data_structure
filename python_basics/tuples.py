tuple1 = (10)
print(type(tuple1))

# you need comma
tuple2 = (10,)
print(type(tuple2))

# tuple indexing and slicing
tuple1 = (12, 231, 34, 32, 1, "riss", "jenny", 23)
print(tuple1[2:])

# tuple is immutable not changable
# tuple1[2] = 1

# tuple support duplcate
tuple1 = (11, 11, 2, 2, 34, 22, 12, 23, 34, 34, 435)

# nested tuple
tuple3 = (tuple1, tuple2)
print(tuple3[1])

# add tuple
tuple3 = tuple1 + tuple2
print(tuple3)

# min, max
print(min(tuple3))
print(max(tuple3))

# count(),index()
print(tuple3.count(12))
print(tuple3.index(435))

# list to tuple
list1 = [12, 23, 2, 32, 3]
print(tuple(list1))


# initiate easily
tuple2 = (5,) * 9
print(tuple2)
