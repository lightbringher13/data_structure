# Human  Male  base/parent/super class
#   |    /
#   v   v
#    Boy    derived/child/sub class
class Human:
    def __init__(self, name, Num_heart) -> None:
        super().__init__(name)
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = Num_heart

    def eat(self):
        print("i can eat")

    def work(self):
        print("i can work")


class Male:
    def __init__(self, name) -> None:
        print("calling Male init")
        # no need for init method this is the last order
        self.name = name

    def flirt(self):
        print("i can flirt")

    def work(self):
        print("i can code")
# no init function. follows mro and find the init func
# if explicit init function then follows the init
# super().__init__() is preferred dynamically follow mro.
# super().__init__() can initiate default and no argument attributes
# explicitly write class.__init__() for the arguement init


class Boy(Human, Male):  # same method. follows order.
    def __init__(self, name, language, Num_heart) -> None:
        super().__init__(name, Num_heart)
        self.language = language
        self.num_heart = Num_heart

    def sleep(self):
        print("i can sleep")

    # MRO: Method Resolution Order
    # overriden method first, Human second, Male last
    def work(self):
        print("i can test")

    def display(self):
        print(f"i am {self.name} and i am working on {self.language}")


# inherit Human, Male methods
boy_1 = Boy("riss", "python", "1")
boy_1.eat()
boy_1.flirt()

# same methods follows mro
boy_1.work()

# use male method using boy object because if follows HUman first
Male.work(boy_1)

# MRO: Method Resolution Order
print(Boy.mro())
print(Human.mro())
print(Male.mro())
# inherit Human, Male attributes
print(boy_1.num_eyes)
boy_1.display()
