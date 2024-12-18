# public: any class can use
# protected: only within super/sub can use ex) _prptected
# private: only within calss can use ex) __private
# no complete restriction. it is programmer's responsibility

class Student:
    def __init__(self, name, rollno, age):
        self.name = name
        self._rollno = rollno
        self.__age = age

    def __display(self):
        print(f"hi i am {self.name} with rollno {
              self._rollno}, age is {self.__age} from Student class")

    def display_private(self):
        self.__display()


class Branch(Student):
    def show(self):
        print(f"rollno is {self._rollno}")


s1 = Student("riss", 123, 20)
b1 = Branch("leo", 234, 20)
# s1._rollno = 45  # you should not do this
print(s1._rollno)
print(b1._rollno)
s1.display_private()
b1.display_private()
b1.show()

# name mangling: "_ClassName" becomes prefix and use private
print(dir(s1))
print(s1._Student__age)
s1._Student__display()
