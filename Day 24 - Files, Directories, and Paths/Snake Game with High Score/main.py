from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
scoreboard = Scoreboard()
food = Food()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

def snake_hits_wall(snek):
    return snek.head.xcor() < -280 or snek.head.xcor() > 280 or \
            snek.head.ycor() < -280 or snek.head.ycor() > 280

def snake_eats_tail(snek):
    for segment in snek.segments[1:]:
        if snek.head.distance(segment) < 10:
            return True
    return False

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()

    if snake.head.distance(food) < 10:
        snake.grow()
        food.reposition()
        scoreboard.increase_score()

    if snake_hits_wall(snake) or snake_eats_tail(snake):
        snake.color("red")
        screen.update()
        time.sleep(1)

        snake.reset()
        scoreboard.reset()

    time.sleep(0.1) # set snake speed
