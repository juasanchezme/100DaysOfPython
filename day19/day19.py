from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=500, height=400)

race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
picked_color = []

def rand_color():
    color = random.choice(colors)
    if color not in picked_color:
        picked_color.append(color)
        return color
    
    else:
        return rand_color()


class RacingTurtle:
    def __init__(self, x, y):
        self.turtle = Turtle(shape="turtle")
        self.turtle.color(rand_color())  # color aleatorio
        self.turtle.penup()
        self.turtle.goto(x, y)

# instancias
turtles = []
y = -60
for i in range(6):
    turtles.append(RacingTurtle(x=-230, y = y))
    y += 30


# movimiento

if user_bet:
    race_on = True

while race_on:               
    for t in turtles:
        if t.turtle.xcor()> 215:
            race_on = False
            print(f"the winner is the {t.turtle.pencolor()} turtle")

        t.turtle.forward(random.randint(1, 10))


    

screen.exitonclick()
