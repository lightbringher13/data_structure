# Human   base/parent/super class
#   |
#   v
# Male    derived/child/sub class


# inheritance
# base/parent/super --> derived/child/sub
class Human:
    def __init__(self, num_heart) -> None:
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart

    def eat(self):
        print("i can eat")

    def work(self):
        print("i can work")


# Male inherit Human
# can have own attributes, methods
class Male(Human):
    # sub class own attribute
    # when written own attribute
    # must write super().__init__() to use super attributes
    def __init__(self, name, heart) -> None:
        super().__init__(heart)  # to access super attribute
        self.name = name

    # sub class own method
    def flirt(self):
        print("i can flirt")
    # sub class own method

    def display(self):
        print(f"hi, i am {self.name} and i have {self.num_heart} heart.")

    # method overriding
    def work(self):
        super().work()  # access super()
        print("i can work with code")


male_1 = Male("riss", 1)
male_1.eat()
male_1.work()
male_1.flirt()
print(male_1.name)
print(male_1.num_eyes)
print(male_1.num_nose)
male_1.display()
