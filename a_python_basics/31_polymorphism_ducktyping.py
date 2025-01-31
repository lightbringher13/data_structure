# polymorphism: has multiple forms
# ducktyping, opeartor overloading
# method overloading, method overriding
# ducktyping: method is more important. find method first
# does not care about the type
# “If it looks like a duck, swims like a duck
# and quacks like a duck, then it probably is a duck.”
def square(x):
    return x ** 2


print(square(5.5))  # dynamic typing: do not need to specify type
# float square(float x) -> static typing: specify type


class Duck:
    def swim(self):
        print("i can swim")

    def speak(self):
        print("Quack Quack")


class Dog:
    def swim(self):
        print("i can swim")

    def speak(self):
        print("Woof Woof")


class Person:
    def speak(self):
        print("Blah Blah")


class Demo:
    def display(self, obj):
        obj.swim()
        obj.speak()
        print("information displayed")


demo = Demo()
duck = Duck()
dog = Dog()
person = Person()
demo.display(duck)
demo.display(dog)
# demo.display(person) no swim method() raise error
