from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score: {self.highscore}", False, ALIGNMENT, FONT)
        with open("data.txt", mode="w") as file:
            file.write(str(self.highscore))

    def reset(self):
        if self.score > self.highscore: 
            self.highscore = self.score
        self.score = 0
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.show_score()
