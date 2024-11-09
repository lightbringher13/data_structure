class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


# Precedence of operators
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

# Check if character is an operator


def is_operator(c):
    return c in precedence

# Function to convert infix to postfix


def infix_to_postfix(expression):
    output = []
    opstack = Stack()

    for token in expression:
        if token.isdigit():  # If the token is an operand (number), add it to output
            output.append(token)
        elif token == '(':  # If the token is '(', push it to the stack
            opstack.push(token)
        # If the token is ')', pop and output from the stack until '(' is found
        elif token == ')':
            while not opstack.is_empty() and opstack.peek() != '(':
                output.append(opstack.pop())
            opstack.pop()  # Remove '(' from the stack
        else:  # The token is an operator
            while (not opstack.is_empty() and opstack.peek() != '(' and
                   precedence[opstack.peek()] >= precedence[token]):
                output.append(opstack.pop())
            opstack.push(token)

    # Pop all the operators from the stack
    while not opstack.is_empty():
        output.append(opstack.pop())

    return output


# Function to evaluate postfix expression
def evaluate_postfix(postfix_expr):
    stack = Stack()

    for token in postfix_expr:
        if token.isdigit():  # If token is a number, push it to the stack
            stack.push(int(token))
        else:  # The token is an operator, pop two elements and apply the operator
            val2 = stack.pop()
            val1 = stack.pop()

            if token == '+':
                stack.push(val1 + val2)
            elif token == '-':
                stack.push(val1 - val2)
            elif token == '*':
                stack.push(val1 * val2)
            elif token == '/':
                stack.push(val1 / val2)
            elif token == '^':
                stack.push(val1 ** val2)

    return stack.pop()


# Main calculator function
def infix_calculator():
    # Input infix expression
    infix = input(
        "Enter an infix expression (with spaces between elements): ").split()

    # Convert infix to postfix
    postfix_expr = infix_to_postfix(infix)
    print(f"Postfix Expression: {' '.join(postfix_expr)}")

    # Evaluate the postfix expression
    result = evaluate_postfix(postfix_expr)
    print(f"Result: {result}")


# Run the calculator
infix_calculator()
