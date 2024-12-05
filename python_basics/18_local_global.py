a = 10  # global


def display():
    a = 15
    print(a)


display()  # print local a -> 15


# ------------------------------------------------------------------
b = 10  # global


def display():

    print(b)


display()  # print global a -> 10

# ------------------------------------------------------------------


def display():
    c = 11
    print(c)


display()  # print global a -> 10
# print(c) can access local c

# ------------------------------------------------------------------

d = 123


def display():
    # d = 10

    def show():
        # d = 15
        print(d)  # find local and then out and then global
    show()


display()

# ------------------------------------------------------------------

e, f = 5, 6


def display():
    if e < f:
        g = e + f


# print(g) can not access local scope

# ------------------------------------------------------------------
a = 10


def display():
    global a
    a = a + 1  # you can access but can not modify unless use global
    print(a)


display()

# ------------------------------------------------------------------


def display():
    a = 20

    def show():
        global a
        # a = a + 1  # there is no gloabl
        a = 30
        print(a)
    print(a)
    show()
    print(a)


display()
print(a)  # created a global inside the function

# ------------------------------------------------------------------
# coding assignment
name = "Jenny's"


def display():
    global name
    name = name + "Lectures"


print(name)
display()
print(name)
