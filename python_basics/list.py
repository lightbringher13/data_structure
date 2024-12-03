numbers = [10, 0, -1, 7]

# list can have multiple types
mixedList = ["riss", "jeeny", True, 10.10]
names = ["riss", "leo"]
print(mixedList)
print(len(mixedList))

# list slicing
print(mixedList[-1:-4:-1])
print(numbers[::2])

# sort ascending order
numbers.sort()
print(numbers)

# reverse the order
numbers.reverse()
print(numbers)

# print max number
print(max(numbers))

# add elements at the end of the list
numbers.append(45)

# add at the index
numbers.insert(2, 32)

# add list at the end of the list
numbers.extend([1, 23, 43, 43])
print(numbers)

# change the multuple elements always rhs iterable
numbers[1:3] = [44]

# remove the element only the firs occurence
numbers.remove(10)
numbers.pop()
print(numbers)
