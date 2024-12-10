from turtle import Turtle, Screen
# s1 = Screen()
# t1 = Turtle()
# t1.shape("turtle")
# t1.pencolor("red")
# t1.fillcolor("green")
# t1.color("red", "green")  # (pencolor, fillcolor)
# t1.fd(100)
# t1.begin_fill()
# t1.circle(100)  # draw a circle
# t1.speed(10)
# t1.end_fill()
# t1.pu()  # penup
# print(t1.isdown())  # is pen down return bool
# t1.fd(100)
# t1.begin_fill()  # starting filling
# t1.speed(10)
# t1.pd()  # pendown
# t1.hideturtle()  # hide turtle
# print(t1.isvisible())
# t1.circle(50)
# t1.fillcolor("red")
# t1.end_fill()  # end filling
# print(t1.pos())
# t1.goto(0, 0)  # goto certain positon
# t1.showturtle()  # show the turtle
# s1.mainloop()

# coding exercise
# draw shape

import random


class DrawShpaes:
    def __init__(self, sides=0,  length=100):
        self.sides = sides
        self.length = length

    def set_color(self):
        return random.random(), random.random(), random.random()

    def draw_shapes(self, obj):
        if self.sides == 0:
            obj.circle(self.length)
        else:
            turning_angle = 360 / self.sides
            for i in range(self.sides):
                obj.fd(100)
                obj.rt(turning_angle)
            obj.color(self.set_color())

    def draw_random_direction(self, obj):
        angle = [0, 90, 180, 270]
        obj.rt(random.choice(angle))
        obj.color(self.set_color())
        obj.pensize(25)
        obj.fd(100)

    def draw_turtle_star(self, obj):
        obj.speed("fastest")
        obj.color("red", "orange")
        obj.begin_fill()
        for i in range(36):
            obj.fd(600)
            obj.rt(170)
        obj.end_fill()

    def draw_many_circles(self, obj):
        obj.speed("fastest")
        for i in range(72):
            obj.color(self.set_color())
            obj.circle(200)
            obj.rt(5)

    def draw_random_dots(self, obj):
        obj.speed("fastest")
        for i in range(40):
            obj.color(self.set_color())
            obj.pu()
            obj.goto(random.randint(-100, 100), random.randint(-100, 100))
            obj.pd()
            obj.dot(20, self.set_color())


if __name__ == "__main__":
    t1 = Turtle()
    s1 = Screen()
    # for i in range(3, 8):
    #     d1 = DrawShpaes(i)
    #     d1.draw_shapes(t1)
    # for i in range(10):
    #     d1 = DrawShpaes()
    #     d1.draw_random_direction(t1)
    d1 = DrawShpaes()
    # d1.draw_turtle_star(t1)
    # d1.draw_many_circles(t1)
    d1.draw_random_dots(t1)
    s1.mainloop()
