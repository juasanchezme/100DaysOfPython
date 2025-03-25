from turtle import Turtle
STARTING_POSITIONS = [(-40,0),(-20,0),(0,0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[2]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle(shape="square")
            snake.penup()
            snake.color("white")
            snake.goto(position)
            self.segments.append(snake)

    def move(self):
        for seg_ind in range(0, len(self.segments)-1):
            new_x = self.segments[seg_ind + 1].xcor()
            new_y = self.segments[seg_ind + 1].ycor()
            self.segments[seg_ind].goto(new_x,new_y)

        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    


