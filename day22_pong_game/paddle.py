from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.resizemode("user")
        self.shapesize(stretch_wid =1,stretch_len= 3)
        self.goto(position )

    
    def up(self):
        self.setheading(UP)
        self.move_paddle()
     
    def down(self):
        self.setheading(DOWN)
        self.move_paddle()
    
    def move_paddle(self):
        self.forward(20)
    
    def automatic_mode(self, position = 330):
        self.speed(0)
        self.move_paddle()
        if self.ycor() > 330:
            self.down()

        if self.ycor() < -position:
            self.up()



    
