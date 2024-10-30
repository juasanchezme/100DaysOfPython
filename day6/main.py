def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():    # same as while at_goal() != True:

    if right_is_clear():
        turn_right()
        move()
        turn_right()
    while wall_in_front():
        turn_left()


    move()
    
    