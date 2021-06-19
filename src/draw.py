import turtle
import random

colors = ["blue", "red", "green", "purple"]


def draw_grid(parent):
    grid = turtle.RawTurtle(parent)
    grid.speed("fastest")
    grid.forward(1000)
    grid.left(180)
    grid.forward(2000)
    grid.left(180)
    grid.forward(1000)
    grid.left(90)
    grid.forward(1000)
    grid.left(180)
    grid.forward(2000)


class Triangle:
    def __init__(self, triangle, parent):
        self.triangle = triangle
        self.turtle = turtle.RawTurtle(parent)
        self.turtle.speed("fastest")
        self.turtle.pencolor(colors[random.randint(0, 3)])
        self.turtle.pensize(2)
        self.turtle.ht()
        self.turtle.forward(triangle.side_b)
        self.turtle.left(triangle.angle_c)
        self.turtle.forward(triangle.side_a)
        self.turtle.left(180-triangle.angle_b)
        self.turtle.forward(triangle.side_c)
