from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.8)
        self.penup()
        self.reposition()

    def reposition(self):
        random_x = random.randint(0, 26)*20 - 260
        random_y = random.randint(0, 26)*20 - 260
        self.goto(x=random_x, y=random_y)
        pass
