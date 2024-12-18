# method overloading
# does not support overloading find the last one
# but you can use default arguement
# compile time
class Demo:
    def add(self, a, b, c=0):
        return a + b + c

    def mul(self, *args):
        total = 1
        for i in args:
            total = total * i
        print(total)
    # def add(self, a, b, c):
    #     return a + b + c


d = Demo()
print(d.add(2, 3))
d.mul(2, 3)
print(d.add(2, 3, 4))
d.mul(2, 3, 5)

# method overriding
# same name same parameter
# runtime


class Father:
    def sleep(self):
        print("sleep from 10 pm ~ 5 am")

    def eat(self):
        print("eating")


class Son(Father):
    # method overriding
    def sleep(self):
        print("sleep 12 am ~ 8 am")

    def eat(self):
        print("eat bad food")


son = Son()
son.eat()
son.sleep()
