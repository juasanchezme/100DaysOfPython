from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len = 1.2 ,stretch_wid = 1.2)
        self.color("yellow")
        self.speed(0)
        self.rand_location()
    
    def rand_location(self):
        x, y = random.randint(-330, 330), random.randint(-330, 330)
        self.goto(x,y)

