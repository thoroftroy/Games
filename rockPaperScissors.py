#File that is strange
import random
import time
exitVal = "ZZZ"
choices = ["Rock","Paper","Scissors"]  
valid = ["1","2","3"] 
screenClear = 15

def settings(screenClear):
    print("Aprox how many characters tall is your screen")
    screenClear = input()
    return screenClear

def clearScreen(screenClear):
    i = 0
    while i <= screenClear:
        print("|")
        i += 1
        
def multiplayer(screenClear):
    print("Player 1 make a move")
    print("Rock[1]  Paper[2]  Scissors[3]")
    player1Choice = input()
    clearScreen(screenClear)
    print("Player 2 make a move")
    print("Rock[1]  Paper[2]  Scissors[3]")
    player2Choice = input()
    clearScreen(screenClear)
    time.sleep(1)
    if(player1Choice == "1") and (player2Choice == "1"):
        print("Ya'll tie")
    elif(player1Choice == "1") and (player2Choice == "2"):
        print("Player 2 wins")
    elif(player1Choice == "1") and (player2Choice == "3"):
        print("Player 1 wins")
    elif(player1Choice == "2") and (player2Choice == "1"):
        print("Player 1 wins")
    elif(player1Choice == "2") and (player2Choice == "2"):
        print("Ya'll tie")
    elif(player1Choice == "2") and (player2Choice == "3"):
        print("Player 2 wins")
    elif(player1Choice == "3") and (player2Choice == "1"):
        print("Player 2 wins")
    elif(player1Choice == "3") and (player2Choice == "2"):
        print("Player 1 wins")
    elif(player1Choice == "3") and (player2Choice == "3"):
        print("Ya'll tie")
    else:
        if(player1Choice not in valid):
            print("Please type valid inputs Player 1")
        elif(player2Choice not in valid):
            print("Please type valid inputs Player 2")
        multiplayer()

def singleplayer():
    print("Make a move")
    print("Rock[1]  Paper[2]  Scissors[3]")
    choice = input()
    player2Choice = choices[random.randint(0,len(choices)-1)]
    if(choice == "1"):
        if(player2Choice == "Rock"):
            print("You tie")
        elif(player2Choice == "Paper"):
            print("You lose")
        elif(player2Choice == "Scissors"):
            print("You win")
        else:
            print("You should never see this message")
    elif(choice == "2"):
        if(player2Choice == "Rock"):
            print("You win")
        elif(player2Choice == "Paper"):
            print("You tie")
        elif(player2Choice == "Scissors"):
            print("You lose")
        else:
            print("You should never see this message")
    elif(choice == "3"):
        if(player2Choice == "Rock"):
            print("You lose")
        elif(player2Choice == "Paper"):
            print("You win")
        elif(player2Choice == "Scissors"):
            print("You tie")
        else:
            print("You should never see this message")
    else:
        print("Please input an option")
        singleplayer()
    
def main():
    choice = "None"
    while choice != exitVal:
        print("How many players do you have [1] or [2] (or [3] for config) or",exitVal,"to exit")
        choice = input()
        if(choice == "1"):
            print("Single player selected")
            singleplayer()
        elif(choice == "2"):
            print("Multiplayer selected")
            multiplayer(screenClear)
        elif(choice == "3"):
            print("Entering config")
            settings(screenClear)
        else:
            print("Please enter a valid input")
    
main()
