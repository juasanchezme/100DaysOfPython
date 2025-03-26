from turtle import Screen, Turtle
from snake import Snake
import random
import time
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    


        
    

screen.exitonclick()