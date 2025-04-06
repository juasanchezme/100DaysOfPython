import turtle

screen = turtle.Screen()
screen.title("US States Game")

image = "./day25/US_States_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess a state", prompt="Write a USA State name")


screen.exitonclick()