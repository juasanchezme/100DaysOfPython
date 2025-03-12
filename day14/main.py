from art import logo, vs
from col_data import colombian_data as data
from random import randint

print(logo)

def generador():
    return data[randint(0, len(data))]

personaA = generador()
gameOver = False
score = 0

while not gameOver:
    
    personaB = generador()

    print(f"compare A: {personaA["name"]}, a {personaA["description"]}")
    print(vs)
    print(f"Againt B: {personaB["name"]}, a {personaB["description"]}")

    guess = input().lower()

    
    if guess == "a":
        if personaA["follower_count"] > personaB["follower_count"]:
            score += 1
            print(f"You're right, current score {score}")
        else:
            print(f"sorry, that's Wrong, final score {score}")
            break
    else:
        if personaA["follower_count"] < personaB["follower_count"]:
            score += 1
            print(f"You're right, current score {score}")
        else:
            print(f"sorry, that's Wrong, final score {score}")
            break
    
    personaA = personaB
    print("\n" * 20)

