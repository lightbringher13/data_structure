# simple example of break
count = 0
while count <= 10:
    count = count + 1
    if count == 7:
        break
    print("hi")
    print(count)
print("out from loop")

# break in nested for loop out of inner loop only still continue with outer loop
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [1, 2, 3, 4, 5, 6, 7, 8]
for i in list1:
    print(f"i => {i}\n")
    for j in list2:
        print(f"j => {j}")
        if i == 5 and j == 4:
            break
    print(f"out of inner loop => {j}")
print("out of all loop")

# simple example of coutinue
count = 0
while count <= 10:
    count = count + 1
    if count == 7:
        continue
    print("hi")
    print(count)
print("out from loop")

# simple example of pass
for i in range(5):
    pass


def func():
    pass

# Indentation
# very importand it is indication of a block
