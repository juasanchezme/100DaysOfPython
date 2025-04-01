from turtle import Turtle

UP = 90
DOWN = 270

class myTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.setheading(90)
        self.resizemode("user")
        self.shapesize(stretch_wid =1,stretch_len= 1)
        self.goto(0,-330 )

    
    def up(self):
        self.setheading(UP)
        self.move_turtle()
     
    def down(self):
        self.setheading(DOWN)
        self.move_turtle()
    
    def move_turtle(self):
        self.forward(20)