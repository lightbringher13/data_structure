# simple example of while loop
count = 1
while count <= 5:
    print(count)
    count = count + 1
print("out of loop")

# while - else block
count = 1
while count <= 5:
    print(count)
    count = count + 1
    # if count == 3:
    #     break
else:  # sign of no break sucessfully executed
    print("in else block")
print("out of loop")

# user input terminate while loop
num = int(input("enter a num(-1 to quit): "))
while num != -1:
    print(num)
    num = int(input("enter a num(-1 to quit): "))
else:
    print("in else block")
print("out of loop")

# boolean
count = 0
while True:
    print(count)
    count = count + 1
    if count == 5:
        break
else:
    print("in else block")
print("out of loop")

# assignment
num = int(input("enter a num(0 to quit): "))
sum = 0
while num != 0:
    sum = sum + num
    num = int(input("enter a num(0 to quit): "))
else:
    print("in else block")
print(sum)
print("out of loop")
