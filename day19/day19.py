# Event listeners
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()

# when we use a function as an argumentof another function we dont put ()
screen.onkey(key="space", fun=move_forward)





screen.exitonclick()