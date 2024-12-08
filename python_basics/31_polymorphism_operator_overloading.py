# operator overloading
print(int.__add__(1, 2))  # Dunder(Double UNDER score) method
print(str.__add__("1", "2"))  # special methode, predefined method


class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, x):
        return f"{self.real + x.real} + {self.imaginary + x.imaginary}i"


c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(4, 5)

# Python determines the behavior of + based on the types of the operands.
# in this case user defined class ComplexNumber
print(c1 + c2)

# predefined class int
print(1 + 2)
print


class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __gt__(self, other):
        if self.age > other.age:
            print(f"{self.name} will pay the bill")
        else:
            print(f"{other.name} will pay the bill")


p1 = Person("riss", 29)
p2 = Person("leo", 25)
p1 > p2
