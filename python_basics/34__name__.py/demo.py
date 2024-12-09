
print(__name__)


def display(name):
    return name


def do_something():
    print("this funciton is doing something")


# For Testing:
if __name__ == "__main__":
    print("this is demo.py")
    name = input("enter your name")
    print(display(name))
    do_something()
