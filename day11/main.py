from art import logo
import random

print(logo)
gameOn = True

while gameOn:    
    validador = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if validador == "n":
        break

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 10, 10, 10]

    def randomCard():
        """ 
        funcion para generar una carta aleatoria
        """
        return random.choice(cards)

    pcCards = [randomCard() for card in range(2)]
    userCards = [randomCard() for card in range(2)]

    sumPcCards = sum(pcCards)
    print(f"computer's first card is {pcCards[0]} ")
    if sumPcCards == 21 :
        print("Game over, computer Wins")
        break

    def calculo():
        sumUserCards = sum (userCards)

        def aceCard(lista, sumaLista):
            if 11 in lista and sumaLista > 21:
                indice = lista.index(11)  
                lista[indice] = 1

        aceCard(pcCards, sumPcCards)
        aceCard(userCards,sumUserCards)
        print(pcCards, userCards)

        
        if sumUserCards == 21:
            print("Game over, User Wins")
            return False

        if sumUserCards > 21:
            print("Game over, computer Wins")
            return False

        
        return True

    juego = calculo()
    while juego:
        moreCards = input(" Do you want another card y or n ")
        if moreCards == "n":
            sumUserCards = sum(userCards)
            while sumPcCards < 17 :
                pcCards.append(randomCard())
                sumPcCards = sum(pcCards)

            if sumPcCards >22:
                print("Game over, user Wins")
            elif sumPcCards > sumUserCards:
                print("Game over, computer Wins")
            elif sumPcCards < sumUserCards:
                print("Game over, user Wins")
            else:
                print("Game over, it's a draw")
            break
        else:
            userCards.append(randomCard())
            juego = calculo()

    
    print(pcCards, userCards)

