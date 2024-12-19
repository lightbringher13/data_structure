# encapsulation: hiding the internal details
# use access modifiers: public, protected, pivate
# best to use geter and setter
# encapsule the private and protected with public
class Student:
    def __init__(self, name, rollno, age):
        self.name = name
        self._rollno = rollno
        self.__age = age

    # access private attributes using getter
    def get_age(self):
        return self.__age

    # update private attributes using setter
    def set_age(self, age):
        if age > 35:
            print("invaled age given. age should be less than 35")
        else:
            self.__age = age

    def __display(self):
        print(f"hi i am {self.name} with rollno {
              self._rollno}, age is {self.__age} from Student class")

    def display_private(self):
        self.__display()
