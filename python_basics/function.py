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
# greet(name="riss", "cs") always positional arguemnt
greet("leo", dept="HR")

# override default arguement
greet("rome", "HR", 23)


# arbitrary arguements
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


def info(**info):
    for key, value in info.items():
        print(key, value)


info(name="riss", age=23, dept="CS")

# assignment


def multiply(*nums):
    mul = 1
    for i in nums:
        mul = i * mul
    print(mul)


multiply(2, 3, -6, 8)
multiply(2, 5, 6, 8, 9)
