from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False,
                   ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Ouch, Game Over!", False, ALIGNMENT, FONT)
        self.goto(0, -20)
        self.write(f"Final Score: {self.score}", False, ALIGNMENT, FONT)
