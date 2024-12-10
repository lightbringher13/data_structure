from turtle import Turtle, Screen
import random


class TurtleRace:
    def __init__(self, no_turtles, screen_width=600, screen_height=600):
        self.no_turtles = no_turtles
        self.turtles = []
        self.screen = Screen()
        self.screen.setup(width=screen_width,
                          height=screen_height)  # Set screen size
        self.screen.colormode(255)  # Set colormode for RGB values
        self.screen.title("Turtle Race")  # Set a title for the window
        self.screen_width = screen_width
        self.screen_height = screen_height

    def setup_turtles(self):
        for i in range(self.no_turtles):
            # Create a turtle and configure it
            t = Turtle()
            t.shape("turtle")
            t.color(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            t.speed("fastest")
            t.seth(90)
            t.penup()
            # Position the turtles at starting positions
            start_x = -self.screen_width // 2 + \
                (self.screen_width / self.no_turtles) * i
            t.goto(start_x, -self.screen_height //
                   2 + 50)  # Start near the bottom
            t.pendown()
            self.turtles.append(t)

    def start_race(self):
        flag = True
        while flag:
            for t in self.turtles:
                t.forward(random.randint(5, 20))  # Random step size
                if t.ycor() > self.screen_height // 2 - 50:  # Finish line
                    flag = False
                    print(f"The winner is the turtle with color: {
                          t.fillcolor()}")
                    break

    def run(self):
        self.setup_turtles()
        self.start_race()
        self.screen.mainloop()


if __name__ == "__main__":
    # Customize screen size
    tr1 = TurtleRace(5, screen_width=800, screen_height=800)
    tr1.run()
