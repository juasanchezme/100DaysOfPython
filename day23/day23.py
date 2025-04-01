from turtle import Screen
from myturtle import myTurtle
from obstacle import Obstacle

import random

from score import scoreBoard
import time

screen = Screen()
screen.colormode(255)
screen.setup(width=700, height=700)

screen.bgcolor("white")
screen.title("Turtle crossing")
screen.tracer(0)

my_turtle = myTurtle()
score = scoreBoard()

my_obstacles_list = []

for i in range(10):
    obstacle = Obstacle()
    my_obstacles_list.append(obstacle)


screen.listen()
screen.onkey(my_turtle.up, "Up")
screen.onkey(my_turtle.down, "Down")

game_is_on = True
game_speed = 0.2
while game_is_on:
    screen.update()
    time.sleep(game_speed)
    for obstacle in my_obstacles_list:
        obstacle.move()
        if my_turtle.distance(obstacle) < 20:
            print("loose")
            score.game_over()
            game_is_on =False
        if my_turtle.ycor() > 310:
            score.update_user_score()
            my_turtle.goto(0,-330)
            game_speed *=0.9

    
        
    


    
    


    

screen.exitonclick()