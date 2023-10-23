import random
from art import text2art
print(text2art("Jumble!"))

def scramble(input):
    word = list(input)
    random.shuffle(word)
    output = ''.join(word)
    return output

def game():
    global score
    wordIndex = random.randint(0,(len(wordList)-1))
    wordToGuess = wordList[wordIndex]
    wordFixer = list(wordToGuess) # wordFixer, splits the word into a list here
    try: # for some reason, sometimes wordFixer breaks when there are no spaces to remove, the try and except was a quick way to fix this
        wordFixer.remove(" ") # wordFixer removes spaces from the list
    except:
        pass
    wordToGuess = ''.join(wordFixer) # finally, wordFixer is joind to the word to guess
    scrambledWord = scramble(wordToGuess)
    correct = False
    while correct == False:
        playerInput = input(f"\nThe jumbled word is - {scrambledWord}\n  Guess - ")
        if playerInput.lower() == wordToGuess:
            print("\nCorrect!")
            score += 5
            correct = True
        elif playerInput == "#cheat":
            print(wordToGuess)
        else:
            print("\nNot quite!, try again\n")

def chooseWordFile(input):
    global wordList
    try:
        wordFile = open(input, "r")
        wordList = list(wordFile.read().split("\n"))
    except:
        print("file not found, using default word list")

wordList = ["apple", "monkey", "trains", "pig", "dogs", "cats"]
chooseWordFile(input("Which word file? - "))
playGame = True
score = 0
while playGame == True:
    if input("Play game? (y/n) ").lower() == "y":
        game()
        print(f'Score: {score}')
    else:
        print(f'\n\nFinal score: {score}\n{text2art("goodbye!")}')
        playGame = False