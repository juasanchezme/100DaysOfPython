from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=700, height=700)

screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

user_paddle = Paddle((-320, 0))
pc_paddle = Paddle((320, 0))
ball = Ball()

screen.listen()
screen.onkey(user_paddle.up, "Up")
screen.onkey(user_paddle.down, "Down")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)
    pc_paddle.automatic_mode()
    ball.ball_move()

    
    


    

screen.exitonclick()