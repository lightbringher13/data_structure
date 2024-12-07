#     University           base/parent/super class
#      /    \
#     v      v
#   course  Branch         derived/child/sub class or base/parent/super class
#     |       /   \
#     v      v     v
#     Student    Faculty   derived/child/sub class

class University:
    def __init__(self, u_name) -> None:
        self.u_name = u_name

    def show_details(self):
        print(f"University name is {self.u_name}")


class Course(University):
    def __init__(self, u_name, c_name) -> None:
        super().__init__(u_name)
        self.c_name = c_name

    def show_details(self):
        super().show_details()
        print(f"Course name is {self.c_name}")


class Branch(University):
    def __init__(self, u_name, b_name) -> None:
        super().__init__(u_name)
        self.b_name = b_name

    def show_details(self):
        super().show_details()
        print(f"Branch name is {self.b_name}")


class Student(Course, Branch):
    def __init__(self, u_name, c_name, b_name, s_name) -> None:
        Course.__init__(self, u_name, c_name)  # Initialize Course explicitly
        Branch.__init__(self, u_name, b_name)  # Initialize Branch explicitly
        self.s_name = s_name  # Initialize Student-specific attribute

    def show_details(self):
        Course.show_details(self)  # Explicitly call Course's show_details
        Branch.show_details(self)  # Explicitly call Branch's show_details
        print(f"Student name is {self.s_name}")


class Faculty(Branch):
    def __init__(self, u_name, b_name, f_name) -> None:
        super().__init__(u_name, b_name)
        self.f_name = f_name

    def show_details(self):
        super().show_details()
        print(f"Faculty name is {self.f_name}")


# Create objects
uni = University("Gachon")
course = Course("Gachon", "Python")
brc = Branch("Gachon", "Sujeong")
std = Student("Gachon", "Python", "Sujeong", "Riss")
fac = Faculty("Gachon", "Sujeong", "Leo")

# Display details
uni.show_details()
course.show_details()
brc.show_details()
std.show_details()
fac.show_details()
