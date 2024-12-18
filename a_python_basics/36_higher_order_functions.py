def add(x, y):
    return x + y


# result = add(2, 1)
addition = add
print(addition(2, 1))
print(addition)
print(add)

# function can be an argument


def greet_louder(name):
    print(f"hi {name.upper()}")


def greet_softer(name):
    print(f"hi {name.lower()}")


def hello(other_def_func, name):
    print("this is display() function")
    other_def_func(name)


hello(greet_louder, "riss")

hello(greet_softer, "RISS")

# return function


def greeting(name):
    print("greeting has bee executed")

    def greet():
        print("Hare Krishma")

    def welcome():
        print("jai shree ram")
    if name == "jenny":
        return greet
    else:
        return welcome


new_func = greeting("jenny riss")
new_func()

# assignment


def add(x, y):
    return x+y


def mul(x, y):
    return x*y


def sub(x, y):
    return x-y


def div(x, y):
    return x/y


def calculator(operator, x, y):
    print(operator(x, y))


calculator(add, 2, 3)
