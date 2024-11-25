import random
word_list = ["aardvark", "baboon", "camel"]

chosenWord = random.choice(word_list)
print(chosenWord)

placeholder = ""

for letter in chosenWord :
    placeholder += "_"

print(placeholder)
display = ["_" for i in range(len(chosenWord))]
contador = 4
while contador != 0:
    guess = input("guess a letter: ").lower()
    if guess not in chosenWord:
        contador -= 1
    index = -1

    for letter in chosenWord:
        index +=1
        if letter ==  guess:
            display[index] = letter
        
        elif letter in display:
            continue

        else:
            display[index] = "_"
            
    print(display)
    if not "_" in display:
        break
    

        
            
    
        



