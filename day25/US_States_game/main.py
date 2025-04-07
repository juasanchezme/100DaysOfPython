import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")

# setting an image as background
image = "./day25/US_States_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()


# Readind CSV with pandas
data = pd.read_csv("./day25/US_States_game/50_states.csv")

# serie to list
states = data["state"].to_list()

# correct guesses list
correct_guesses = []
score = 0 


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"Guess a state {score}/50", prompt="Write a USA State name").title()

    if answer_state == "Exit":

        # states_to_learn.csv

        states_to_learn = []
        for state in states:
            if state not in correct_guesses:
                states_to_learn.append(state)

        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("./day25/US_States_game/states_to_learn.csv")
        
        break

    if answer_state in correct_guesses:
        print("ya está en la lista")
        

    elif answer_state in states and answer_state not in correct_guesses:
        print("si")
        # taking the x and y information of the row of the chosen state
        x_cord = int(data[data["state"] == answer_state]["x"])
        y_cord = int(data[data["state"] == answer_state]["y"])
        my_turtle.write(answer_state)
        my_turtle.goto(x_cord,y_cord)

        correct_guesses.append(answer_state)
        score += 1
    
    else:
        print("no está")
    



screen.exitonclick()