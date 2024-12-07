# class and objects
# ex) class -> instructor
# attributes -> name, age...
# methods -> teach,run,work...
# object -> instructor jiya, riss...
# ClassName is pascal case
# class Instructor:
#     pass


# Instructor_1 = Instructor()
# print(type(Instructor_1))

# # assignment create two objects


# class CarDesign:
#     pass


# car1 = CarDesign()
# car2 = CarDesign()

# class Instructor:
#     pass


# instructor_1 = Instructor()
# instructor_1.name = "riss"
# instructor_1.address = "seoul"
# instructor_2 = Instructor()
# instructor_2.name = "riss"
# instructor_2.address = "delhi"
# print(instructor_1.name)

# attributes what object has
# class Instructor:
#     def __init__(self, instructor_name, address) -> None:
#         self.name = instructor_name
#         self.address = address
#         self.followers = 0  # default attribute can modify but deos not require


# instructor_1 = Instructor("riss", "seoul")
# instructor_2 = Instructor("jenny", "delhi")
# instructor_3 = Instructor("mohan", "daegu")
# instructor_4 = Instructor("leo", "ulsan")
# instructor_4.followers = 40
# print(instructor_1.name, instructor_1.address, instructor_1.followers)
# print(instructor_2.name, instructor_2.address, instructor_2.followers)
# print(instructor_3.name, instructor_3.address, instructor_3.followers)
# print(instructor_4.name, instructor_4.address, instructor_4.followers)

# methods what object does
class Instructor:
    followers = 0  # class object variable

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def display(self, subject):
        # self is only attached to attributes
        print(f"HI, i am {self.name}, i have {
              self.followers} followers. i teach {subject}")

    def update_followers(self, follower_name):
        print(f"follwer : {follower_name}")
        self.followers = self.followers + 1

    def update_following(self):
        print(f"following {self.follwers_name}")


instructor_1 = Instructor("riss", "seoul")
instructor_1.update_followers("jenny")
instructor_1.display("python")
instructor_2 = Instructor("jenny", "delhi")
instructor_1.update_followers("riss")
instructor_1.display("python")
