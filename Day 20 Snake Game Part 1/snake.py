STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# STARTING_POSITIONS.append((-60, 0))
# STARTING_POSITIONS.append((-80, 0))
# STARTING_POSITIONS.append((-100, 0))
# STARTING_POSITIONS.append((-120, 0))
# STARTING_POSITIONS.append((-140, 0))
MOVE_DISTANCE = 20

from turtle import Turtle

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.shapesize(0.8)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[seg_num].setheading(self.segments[seg_num - 1].heading())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
