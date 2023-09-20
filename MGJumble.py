import random
from art import text2art
print(text2art("Jumble!"))

def scramble(input):
    word = list(input)
    random.shuffle(word)
    output = ''.join(word)
    return output

def game():
    wordIndex = random.randint(0,(len(wordList)-1))
    wordToGuess = wordList[wordIndex]
    # print(wordToGuess)
    correct = False
    scrambledWord = scramble(wordToGuess)
    while correct == False:
        if input(f"\nThe jumbled word is - {scrambledWord}\n  Guess - ") == wordToGuess:
            print("\nCorrect!")
            correct = True
        else:
            print("\nNot quite!, try again\n")

try:
    wordFile = open("sgb-words.txt", "r")
    wordList = list(wordFile.read().split("\n"))
except:
    wordList = ["apple", "monkey", "trains", "pig", "dogs", "cats"]
playGame = True
while playGame == True:
    if input("Play game? (y/n) ").lower() == "y":
        game()
    else:
        print(text2art("goodbye!"))
        playGame = False