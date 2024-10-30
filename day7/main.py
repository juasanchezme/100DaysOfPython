stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.

#For each letter in the chosen_word, add a "_" to 'display'.

#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display=[]
word=[]
for letter in chosen_word:
  word.append(letter)
  letter="_"
  display.append(letter)


print(display)

index1=-1

indstage=6

for i in chosen_word:
  index1+=1

  while "_" in display and lives > 0:
    

    guess = input("Guess a letter: ").lower()

    if guess not in word:
      lives-=1
      indstage-=1
      print(stages[indstage])


    index=-1
    for letter in chosen_word:
      index+=1

      if letter == guess:
        display[index]=letter



    print(f"te quedan {lives} vidas")
    print(display)

if lives==0:
  print("you loose")
  print(stages[0])
else:
  print("you win")