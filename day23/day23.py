from turtle import Screen
from myturtle import myTurtle

from score import scoreBoard
import time

screen = Screen()
screen.setup(width=700, height=700)

screen.bgcolor("white")
screen.title("Turtle crossing")
screen.tracer(0)

my_turtle = myTurtle()
score = scoreBoard()

screen.listen()
screen.onkey(my_turtle.up, "Up")
screen.onkey(my_turtle.down, "Down")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
        
    


    
    


    

screen.exitonclick()