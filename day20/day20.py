from turtle import Screen, Turtle
import random
import time
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

segments = []

x_cor = -20
for i in range(3):
    snake = Turtle(shape="square")
    snake.penup()
    snake.color("white")
    snake.goto(x=x_cor,y=0)
    segments.append(snake)
    x_cor += 20



while True:
    screen.update()
    time.sleep(0.05)
    for segment in segments:
        segment.forward(10)
        
    

screen.exitonclick()