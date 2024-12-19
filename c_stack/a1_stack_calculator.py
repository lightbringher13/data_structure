# infix to prefix
# tip: parenthesis first and then left to right
# (3 + 4) * (5 - 2) + 6 / 2 --> + * + 3 4 - 5 2 / 6 2
# infix to postfix
# (3 + 4) * (5 - 2) + 6 / 2 --> 3 4 + 5 2 - * 6 2 / +

# prefix to infix
# tip: find two number and the closest operator and left to right
#  + * + 3 4 - 5 2 / 6 2 --> (3 + 4) * (5 - 2) + (6 / 2)
# prefix to postfix
# preifix to infix and infix to postfix

# postfix to infix
# tip: find two number and the closest operator and left to right
# 3 4 + 5 2 - * 6 2 / + --> (3 + 4) * (5 - 2) + (6 / 2)
# postfix to prefix
# postfix to infix and infix to prefix

from a_stack import Stack


def operator_priority(letter):
    operator_priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "(": 0
    }
    return operator_priority[letter]


def infix_to_postfix(infix):
    postfix = []
    operator = Stack()
    for letter in infix:
        if letter == "(":
            operator.push(letter)
        elif letter in ["+", "-", "/", "*"]:
            while not operator.is_empty() and operator_priority(operator.top()) >= operator_priority(letter):
                postfix.append(operator.pop())
            operator.push(letter)
        elif letter == ")":
            while not operator.is_empty() and operator.top() != "(":
                postfix.append(operator.pop())
            operator.pop()
        else:
            postfix.append(letter)
    while not operator.is_empty():
        postfix.append(operator.pop())
    return postfix


def basic_operation(letter, a, b):
    if letter == "+":
        return a + b
    elif letter == "-":
        return a - b
    elif letter == "/":
        return a // b
    elif letter == "*":
        return a * b


def postfix_calculator(postfix):
    nums = Stack()
    for letter in postfix:
        if letter in ["+", "-", "/", "*"]:
            top = nums.pop()
            before_top = nums.pop()
            nums.push(basic_operation(letter, int(before_top), int(top)))
        else:
            nums.push(int(letter))
    return nums.pop() if not nums.is_empty() else None


if __name__ == "__main__":
    infix = input("enter an infix: ").strip().split(" ")
    print(infix)
    postfix = infix_to_postfix(infix)
    print(postfix)
    print(postfix_calculator(postfix))
# 6 + ( 3 + 2 ) * 4
