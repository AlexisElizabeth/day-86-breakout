from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class BrickManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_bricks = []

    def create_bricks(self):
        for x_coordinate in range(-400, 410, 50):
            for y_coordinate in range(-60, 240, 25):
                new_brick = Turtle("square")
                new_brick.shapesize(stretch_wid=1, stretch_len=2)
                new_brick.penup()
                new_brick.color(choice(COLORS))
                new_brick.goto(x_coordinate, y_coordinate)
                self.all_bricks.append(new_brick)
