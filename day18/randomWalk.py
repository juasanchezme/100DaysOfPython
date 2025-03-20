
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

screen = Screen()
screen.colormode(255)

def ranColor():
    a,b,c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return a,b,c


width = 1
for i in range(20):
    timmy.pencolor(ranColor())
    timmy.width(width)
    steps = int(random.random() * 100)
    angle = int(random.random() * 360)
    timmy.setheading(angle)
    timmy.fd(steps)
    width +=1

    

screen.exitonclick()