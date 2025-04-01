from turtle import Turtle
import random

UP = 90
DOWN = 270

class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(self.rand_color())
        self.setheading(180)
        self.resizemode("user")
        self.shapesize(stretch_wid =1,stretch_len= 3)
        self.goto(self.rand_position())
    
    def rand_position(self):
        x_position = random.randint(-350, 350)
        y_position = random.randint(-310, 310)
        return (x_position, y_position)
    
    def rand_color(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)
    
    def move(self ):
        self.speed(0)
        self.forward(20)

        if self.xcor() < -350:
            self.goto(random.randint(350, 370), random.randint(-310, 310))


