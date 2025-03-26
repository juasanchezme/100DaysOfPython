from turtle import Turtle

class scoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=310)
        self.write(arg= f"Score: {self.score}", move= False, align= "center", font = ('Courier', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg= f"Game Over, Score: {self.score}", move= False, align= "center", font = ('Courier', 20, 'normal'))



    def update_score(self):
        self.score += 1 
        self.clear()
        self.write(arg= f"Score: {self.score}", move= False, align= "center", font = ('Courier', 20, 'normal'))
