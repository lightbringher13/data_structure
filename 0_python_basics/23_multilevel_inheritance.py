# Human   base/parent/super class
#   |
#   v
# Male    base/parent/super class or derived/child/sub class
#   |
#   v
# Male    derived/child/sub class


# object class is the parent of all class
class Human(object):
    can_breathe = True

    def __init__(self, num_heart) -> None:
        self.eyes = 2
        self.heart = num_heart

    def eat(self):
        print("i can eat")

    def work(self):
        print("i can work")


class Male(Human):
    def __init__(self, name, num_heart) -> None:
        super().__init__(num_heart)
        self.name = name
        self.num_heart = num_heart

    def sleep(self):
        print("i can sleep")


class Boy(Male):
    def __init__(self, num_heart, can_dance, name) -> None:
        super().__init__(name, num_heart)
        self.know_dancing = can_dance

    def work(self):
        Human.work(self)
        print("i can code")


boy_1 = Boy(1, True, "riss")
boy_1.eat()
boy_1.work()
print(boy_1.can_breathe)
print(boy_1.name, boy_1.num_heart, boy_1.know_dancing)
Human.work(boy_1)
print(boy_1.eyes)
