import random

# randint a<= x <=b
a = random.randint(1, 10)
print(a)

# randrange a<= x < b
a = random.randrange(1, 10)
print(a)

# random() float number 0.0 <= x < 1.0
a = random.random()
print(a)

# uniform() float number from range
# 1.0 <= x <= 5.0
a = random.uniform(1, 5)
print(a)

# choic() pick one element
l = [12, 3213, 56, 3, 7, 8, 9675, 3]
a = random.choice(l)
print(a)

# random.choices() yes dupliicates
# random.sample() no duplicates

# mix the order of the list
random.shuffle(l)
print(l)

# coding exercise
# heads or tails
print("head or tails")
a = random.randint(0, 1)
print(a)
if a == 1:
    print("heads")
else:
    print("tails")

# # coding exercise
# # who will pay the bill
# names = input("Enter everybody's name separated by comma: ")
# names = names.split(",")
# # print(names)
# # choice = random.randrange(0, len(names))
# person_selected = random.choice(names)
# print(f"{person_selected} will pay the bill.")

# index error
# num = [2, 3, 4, 5, 6, 7]
# print(num[len(num)])

# Nested list
list1 = [1, 23, 4, 3, [32, 876, 4, 4, 65, 4,], 453, 53, 4, 423]
print(len(list1))
print(list1[:5])
print(list1[4][0:5])
print(list1[4][::2])
list2 = [10, 34, 90, ["mohan", "shyam", "ram"], 89]
print(list2[3][2])

# coding exercise
# hide money
list1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
location = input("where you want to hide?")
list1[int(location[0])][int(location[1])] = "x"
print(f"{list1[0]}\n{list1[1]}\n{list1[2]}")
