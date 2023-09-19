from random import shuffle
from art import text2art
import random
print(text2art("Jumble!"))

def scramble(input):
    word = list(input)
    shuffle(word)
    output = ''.join(word)
    return output

def game():
    wordIndex = random.randint(0,(len(wordList)-1))
    wordToGuess = wordList[wordIndex]
    print(wordToGuess)
    correct = False
    scrambledWord = scramble(wordToGuess)
    while correct == False:
        if input(f"\nThe jumbled word is - {scrambledWord}\n  Guess - ") == wordToGuess:
            print("\nCorrect!")
            correct = True
        else:
            print("\nNot quite!, try again\n")

wordFile = open("sgb-words.txt", "r")
wordList = list(wordFile.read().split("\n"))
playGame = True
while playGame == True:
    if input("Play game? (y/n) ").lower() == "y":
        game()
    else:
        print("goodbye!")
        playGame = False