print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____ 
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/_____ / 
*******************************************************************************
''')

print("Welcome to Space Adventure.")
print("Your mission is to find the hidden alien artifact.")

# First decision point
first_choice = input("You're at a crossroad, do you want to go left towards the forest or right towards the cave?\nType 'left' or 'right': ").lower()

if first_choice == 'right':
    print(''' 
    _____                 _ 
   |  __ \\               | |
   | |__) |_ _ _ __   ___ | |_
   |  ___/ _` | '_ \\ / _ \\| __|
   | |  | (_| | | | | (_) | |_
   |_|   \\__,_|_| |_|\\___/ \\__|
   
    You walked into a cave and got lost in the darkness. Try again!
    ''')
elif first_choice == 'left':
    print(''' 
     __      __    _  _       _    
     \\ \\    / /   | || |     | |   
      \\ \\  / /__  | || |__   | |__ 
       \\ \\/ // _ \\ | || '_ \\ | '_ \\
        \\  /|  __/ | || | | || | | |
         \\/  \\___| |_||_| |_||_| |_|
    ''')
    print("You've successfully navigated through the forest!")

    # Second decision point
    second_choice = input("You see a spaceship or a small hut. Where will you go?\nType 'spaceship' or 'hut': ").lower()
    
    if second_choice == "spaceship":
        print(''' 
              _______
            /       \\
           /         \\       ______
          |           |     |____  |
           \\         /          / /
            \\_______/          /_/
            
            You've entered an alien spaceship, but you triggered the alarm! Game over.
        ''')
    elif second_choice == "hut":
        print(''' 
             ________
            /        \\
           |          |
           |  _    _  |
           | | \\  / | |
           | |  \\/  | |
           | |______| |
           |__________|
           
           You found the hidden alien artifact inside the hut. Congratulations, you win!
        ''')

# End of game
print("Thank you for playing Space Adventure!")
