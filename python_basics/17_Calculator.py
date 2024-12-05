import platform
import os


def clear_console():
    command = "cls" if platform.system() == "windows" else "clear"
    os.system(command)


def execute(x, y, z):
    if z == "+":
        print(f"{x} + {y} = {x+y}")
    elif z == "-":
        print(f"{x} - {y} = {x-y}")
    elif z == "*":
        print(f"{x} * {y} = {x*y}")
    elif z == "/":
        if y == 0:
            print(f"can not divide with {y}")
        else:
            print(f"{x} / {y} = {x/y}")
    else:
        ("invalid operator. choose form + - / *")


def calculator():
    flag = True
    while flag:
        try:
            first_num = int(input("enter a first number: ").strip())
            second_num = int(input("enter a second number: ").strip())
        except ValueError:
            print("invalid input. try again")
            continue
        operator = input("+\n-\n*\n/\nPick an operation: ").strip()
        execute(first_num, second_num, operator)
        con = input("continue: \"c\", exit: \"x\": ").strip().lower()
        if con not in ["c", "x"]:
            clear_console()
            print("invalid input. try again")
            continue
        if con == "x":
            flag = False
            calculator()  # recursion
        clear_console()


calculator()
