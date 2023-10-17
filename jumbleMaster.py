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
    correct = False
    scrambledWord = scramble(wordToGuess)
    while correct == False:
        if input(f"\nThe jumbled word is - {scrambledWord}\n  Guess - ") == wordToGuess:
            print("\nCorrect!")
            score += 5
            correct = True
        else:
            print("\nNot quite!, try again\n")

# try:
#     wordFile = open("sgb-words.txt", "r")
#     wordList = list(wordFile.read().split("\n"))
# except:
#     wordList = ["apple", "monkey", "trains", "pig", "dogs", "cats"]
wordList = ["apple", "monkey", "trains", "pig", "dogs", "cats"]
playGame = True
score = 0
while playGame == True:
    if input("Play game? (y/n) ").lower() == "y":
        game()
        print(f'Score: {score}')
    else:
        print(f'\n\nFinal score: {score}\n{text2art("goodbye!")}')
        playGame = False