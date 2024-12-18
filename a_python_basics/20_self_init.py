# class Instructor:
#     pass


# instructor_1 = Instructor()
# instructor_1.name = "riss"
# instructor_1.address = "seoul"
# instructor_2 = Instructor()
# instructor_2.name = "riss"
# instructor_2.address = "delhi"
# print(instructor_1.name)


class Instructor:
    def __init__(self, instructor_name, address) -> None:
        self.name = instructor_name
        self.address = address
        self.followers = 0  # default attribute can modify but deos not require


instructor_1 = Instructor("riss", "seoul")
instructor_2 = Instructor("jenny", "delhi")
instructor_3 = Instructor("mohan", "daegu")
instructor_4 = Instructor("leo", "ulsan")
instructor_4.followers = 40
print(instructor_1.name, instructor_1.address, instructor_1.followers)
print(instructor_2.name, instructor_2.address, instructor_2.followers)
print(instructor_3.name, instructor_3.address, instructor_3.followers)
print(instructor_4.name, instructor_4.address, instructor_4.followers)
