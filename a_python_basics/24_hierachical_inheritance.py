#    Human           base/parent/super class
#    /    \
#   v       v
# Male    Female     derived/child/sub class
# hierachial class
class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def eat(self):
        print("i can eat")

    def show_details(self):
        print(f"i am {self.name} and i am {self.age}")


class Male(Human):
    def __init__(self, name, age, location) -> None:
        super().__init__(name, age)
        self.location = location

    def sleep(self):
        print("i can sleep")

    def show_details(self):
        print(f"i am {self.name} and i am {
              self.age} and i live in {self.location}")


class Female(Human):
    def __init__(self, name, age, can_dance) -> None:
        super().__init__(name, age)
        self.can_dance = can_dance

    def show_details(self):
        print(f"i am {self.name} and i am {
              self.age} and i can dance {self.can_dance}")

    def work(self):
        print("i can code")


female_1 = Female("jenny", 2, True)
female_1.show_details()
female_1.eat()
male_1 = Male("riss", 20, "seoul")
male_1.show_details()
male_1.eat()


# assignment
#    Person           base/parent/super class
#    /    \
#   v       v
# Student   Faculty     derived/child/sub class
class Person:
    def __init__(self, social_id, nation) -> None:
        self.nation = nation
        self.social_id = social_id

    def eat(self):
        print("i can eat")

    def work(self):
        print("i can work")


class Student(Person):
    def __init__(self, social_id, nation, can_love) -> None:
        super().__init__(social_id, nation)
        self.can_love = can_love

    def show_details(self):
        print(f"number {self.social_id} my nation {
              self.nation} and i have lovers {self.can_love}")

    def work(self):
        print("i can study")


class Faculty(Person):
    def __init__(self, social_id, nation, can_commute) -> None:
        super().__init__(social_id, nation)
        self.can_commute = can_commute

    def show_details(self):
        print(f"number {self.social_id} my nation {
              self.nation} and i commute {self.can_commute}")

    def work(self):
        print("i can organize")

    def get_tuition_fee(self):
        print("get student fee")


student_1 = Student(123, "South korea", True)
student_1.show_details()
student_1.work()
faculty_1 = Faculty(234, "South korea", True)
faculty_1.show_details()
faculty_1.work()
