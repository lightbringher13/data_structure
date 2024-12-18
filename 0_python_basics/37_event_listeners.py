from turtle import Turtle, Screen
s1 = Screen()
t1 = Turtle()


def up():
    t1.seth(90)
    t1.fd(20)


def down():
    t1.seth(270)
    t1.fd(20)


def left():
    t1.seth(180)
    t1.fd(20)


def right():
    t1.seth(0)
    t1.fd(20)


def clear_screen():
    t1.clear()
    t1.pu()
    t1.home()
    t1.pd()


def move_forward():
    t1.fd(100)


def move_backward_smaller():
    t1.seth(180)
    t1.fd(10)


def move_forward_smaller():
    t1.fd(10)


def tilt_left():
    t1.lt(10)
    t1.fd(10)


def tilt_right():
    t1.right(10)
    t1.fd(10)


s1.listen()
s1.onkey(up, "Up")
s1.onkey(down, "Down")
s1.onkey(right, "Right")
s1.onkey(left, "Left")
s1.onkey(clear_screen, "c")
s1.onkey(move_forward, "space")
s1.onkey(move_forward_smaller, "f")
s1.onkey(move_backward_smaller, "b")
s1.onkey(tilt_left, "l")
s1.onkey(tilt_right, "r")

s1.mainloop()
