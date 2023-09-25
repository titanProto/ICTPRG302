import random

def scramble(input):
    wordToScramble = list(input)
    random.shuffle(wordToScramble)
    output = ''.join(wordToScramble)
    return output

def game():
    wordIndex = random.randint(0,(len(wordList)-1))
    wordToGuess = wordList[wordIndex]
    scrambledWord = scramble(wordToGuess)
    correct = False
    while correct == False:
        if input(f"\nThe jumbled word is - {scrambledWord}\n  Guess - ") == wordToGuess:
            print("\nCorrect!")
            correct = True
        else:
            print("\nNot quite!, try again\n")

wordList = ["apple", "monkey", "trains", "pig", "dogs", "cats"]
game()