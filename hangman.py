# simple hang man game

import random

def welcome():
    
    while True:
        name = input("Welcome! What is your name?: ")
        if name.isalpha() == True:
            print(f"Welcome {name}!\n")
            break
        else:
            print("\nPlease enter a valid name.\n")
            continue
        
def playAgain():
    while True:
        userResponse = input("Would you like to play again?: ")
        if userResponse.lower() == "y":
            break
        elif userResponse.lower() == "n":
            exit(0)
            
def gameRun():
    gameRunning = True
    wordsList = ["Python", "Java", "Programming"]
    guessCorrect = ["Nice Guess!", "Awesome!", "Good job!"]
    wordToGuess = random.choice(wordsList)
    wordGuessList = []
    wordGuessListUnderscore = []
    for x in range(len(wordToGuess)):
        wordGuessList += wordToGuess[x]
        wordGuessListUnderscore += "_"
    while gameRunning:
            
        print("Guess the word: ", "".join(wordGuessListUnderscore))
        userGuess = input("Enter a letter: ")
        if userGuess.isalpha() == True:
            for x in wordGuessList:
                if userGuess.lower() == x.lower():
                    print(random.choice(guessCorrect))
                    
        else:
            print("\nPlease enter a letter.\n")
            continue
        

welcome()
gameRun()