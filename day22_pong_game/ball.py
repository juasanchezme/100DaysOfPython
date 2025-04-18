from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.rand_heading()
        self.speed(0)
        self.game_speed = 0.08

    def rand_heading(self):
        self.setheading(random.randint(140, 220))
        self.goto(0, random.randint(-310, 310))
    
    def ball_move(self):
        #print(f"Ángulo actual: {self.heading()}")
        self.forward(10)
        self.ybounce()

        
    def ybounce(self):
        # Rebote en los bordes superior e inferior
        if self.ycor() > 290 or self.ycor() < -290:
            self.setheading(-self.heading())  # Refleja la dirección en Y
    
    def xbounce(self):
        # Rebote en los bordes laterales (izquierda y derecha)
        if self.xcor() < -310 or self.xcor() > 310:
            self.setheading(180 - self.heading())  # Refleja la dirección en X
            self.game_speed *= 0.9

            
            
        
  