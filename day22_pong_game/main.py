from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import scoreBoard
import time

screen = Screen()
screen.setup(width=700, height=700)

screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

user_paddle = Paddle((-320, 0))
pc_paddle = Paddle((320, 0))
ball = Ball()
score = scoreBoard()

screen.listen()
screen.onkey(user_paddle.up, "Up")
screen.onkey(user_paddle.down, "Down")
screen.onkey(pc_paddle.up, "w")
screen.onkey(pc_paddle.down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.game_speed)
    #pc_paddle.automatic_mode()
    ball.ball_move()

    if ball.distance(user_paddle) < 30 or ball.distance(pc_paddle) < 30:
        ball.xbounce()

    if ball.xcor() <= -330:
        print("user loses")
        score.update_pc_score()
        ball.rand_heading()
        ball.game_speed = 0.08

    elif ball.xcor() >= 330:
        print("pc loses")
        score.update_user_score()
        ball.rand_heading()
        ball.game_speed = 0.08
        
    


    
    


    

screen.exitonclick()