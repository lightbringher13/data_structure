import math
# simple function with no parameter


def greet():
    print("hi")
    print("riss")


greet()

# simple function with parameter
# parameter a,b
# arguements 3,4 (actual parameter)


def hap(a, b):
    print(a+b)


hap(3, 4)

# positional arguements


def greet(name, dept, age=30):  # age is default arguement. non-default is first and also required
    print(f"hi, {name}")
    print(f"you are in {dept}")
    print(f"age is {age}")


greet("riss", "CS")

# keyword arguements
# greet(name="riss", "cs") always positional arguemnt comes first
greet("leo", dept="HR")

# override default arguement
greet("rome", "HR", 23)


# arbitrary arguements
# print_numbers(*numbers): Unpacks the list and passes each element as an argument
def add(*numbers):  # tuple (5,7,9)
    c = 0
    for i in numbers:
        c = c + i
    print(c)


add(5, 7, 9)
add(1, 2, 3, 4, 5, 56, 6, 90)
add(1, 2, 3, 4, 52, 2, 21, 23, 231, 3, 312, 90)

# arbitrary arguement + keyword arguement


def add(*numbers, name):  # tuple (1, 2, 3, 4, 5, 56, 6, 90)
    c = 0
    print(name)
    for i in numbers:
        c = c + i
    print(c)


add(1, 2, 3, 4, 5, 56, 6, 90, name="riss")

# arbitrary arguement + positinal arguement


def add(name, *numbers):  # tuple (1, 2, 3, 4, 5, 56, 6, 90)
    c = 0
    print(name)
    for i in numbers:
        c = c + i
    print(c)


add("riss", 1, 2, 3, 4, 5, 56, 6, 90)

# arbitrary keyword arguement
# stored as dictionary


def info(**info):
    for key, value in info.items():
        print(key, value)


info(name="riss", age=23, dept="CS")


# * can unpack elements from lists/tuples


def add(x, y, z):
    return x + y + z


nums = [1, 2, 3]
print(add(*nums))  # Equivalent to add(1, 2, 3)


# ** can unpack dictionaries.


def display_info(name, age):
    print(f"Name: {name}, Age: {age}")


person = {"name": "Alice", "age": 30}
display_info(**person)  # Equivalent to display_info(name="Alice", age=30)


# assignment


def multiply(*nums):
    mul = 1
    for i in nums:
        mul = i * mul
    print(mul)


multiply(2, 3, -6, 8)
multiply(2, 5, 6, 8, 9)

# coding exercise
# how many cans do we need to paint the wall


def No_cans(h, w, coverage):
    no_cans = math.ceil((h*w)/coverage)  # need math library to round up ceil
    print(f"number of cans needed to pain the wall {no_cans}")


height = int(input("what is the height of the wall? "))
width = int(input("what is the width of the wall? "))
coverage = 7
No_cans(height, width, coverage)

# coding exercise
# prime number or not


def isPrime(n):
    if n <= 1:
        print(f"{n} is not a prime number")
        return
    divisors = []
    # need math library
    # prime number 2->sqrt(number) integers check divisible
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)

    if len(divisors) == 0:
        print(f"{n} is prime number")
    else:
        print(f"{n} is divible by {divisors}")


num = int(input("enter a number: "))
isPrime(num)
