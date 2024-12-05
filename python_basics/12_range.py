# simple example of range()
a = range(5)
print(a[0])
print(a[1])

# range() step size
a = range(0, 10, 3)
for i in a:
    print(i)

# range() negetive step size
a = range(10, 0, -2)
for i in a:
    print(i)

a = range(-1, -10, -2)
for i in a:
    print(i)

# coding exercise
# sum until 100
sum = 0
for i in range(101):
    sum = i + sum
print(sum)

# coding exercise
# find even numbers until 100
numbers = []
for i in range(1, 101):
    numbers.append(i)
for num in numbers:
    if num % 2 != 0:
        numbers.remove(num)
print(numbers)

# coding exercise
# FizzBuzz Job interview Question
# order of the condition is very important
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
