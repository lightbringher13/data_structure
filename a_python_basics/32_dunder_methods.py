# list1 = [1, 0, -1]
# # len function is predefined for type list
# print(len(list1))
# print(list1)
# print(type(list1))


# class Author:
#     def __init__(self, name, book_name, pages):
#         self.book_name = book_name
#         self.pages = pages
#         self.name = name

#     # manually define the len function for user defined class
#     def __str__(self):
#         return f"{self.book_name} by {self.name} with {self.pages}"

#     def __len__(self):
#         return self.pages

#     def __call__(self, *args, **kwds):
#         print("hi object is called")

#     def __del__(self):
#         print("Author has been deleted")


# d = Author("riss", "my life", 300)
# print(len(d))
# print(d)
# d()
# del d
# print(d) object has been deleted. raise error

# coding exercise
# generate a bank acconts


class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance

    # print method should return
    def __str__(self):
        return f"{self._name} has {self.__balance}"

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, money):
        balance = self.get_balance()
        balance = balance + money
        self.set_balance(balance)

    def withdraw(self, money):
        if money > self.get_balance():
            print("money is bigger than balance")
        else:
            balance = self.get_balance()
            balance = balance - money
            self.set_balance(balance)


ba1 = BankAccount("riss", 3000)
print(ba1.get_balance())
ba1.withdraw(3000)
print(ba1.get_balance())
ba1.deposit(4000)
print(ba1.get_balance())
ba1.withdraw(5000)
ba1.deposit(6000)
print(ba1.get_balance())
ba1.withdraw(7000)
print(ba1.get_balance())
print(ba1)
