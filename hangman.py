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
    count = 0
    gameRunning = True
    wordsList = ["Python", "Java", "Programming"]
    guessCorrect = ["Nice Guess!", "Awesome!", "Good job!"]
    wordToGuess = random.choice(wordsList)
    wordGuessList = []
    wordGuessListUnderscore = []
    
    for x in range(len(wordToGuess)):
        wordGuessList += wordToGuess[x]
        wordGuessListUnderscore += "_"
    
    numOfLetters = len(wordGuessList)
    
    while gameRunning:
        
        if count == numOfLetters:
            print("\nYou win!")
            print(f"You guessed the word {wordToGuess}!\n")
            gameRunning = False
            break
        
        print("Guess the word: ", "".join(wordGuessListUnderscore))
        userGuess = input("Enter a letter (or word if you know it): ")
        if userGuess.isalpha() == True:
            
            if userGuess.lower() == wordToGuess.lower():
                print("\nYou win!")
                print(f"You guessed the word {wordToGuess}!\n")
                gameRunning = False
                break
            
            for x in range(len(wordGuessList)):
                if userGuess.lower() == wordGuessList[x].lower():
                    print(random.choice(guessCorrect))
                    wordGuessListUnderscore[x] = wordGuessList[x]
                    count += 1
                    
        else:
            print("\nPlease enter a letter.\n")
            continue
        

welcome()
gameRun()