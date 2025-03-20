
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

screen = Screen()
screen.colormode(255)

def ranColor():
    a,b,c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return a,b,c


width = 2
timmy.speed(0)
for angle in range(0, 365, 5):
    timmy.pencolor(ranColor())
    timmy.width(width)
    timmy.circle(100)
    timmy.setheading(angle)

    
   
    

    

screen.exitonclick()