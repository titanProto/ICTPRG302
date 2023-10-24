import random
from art import text2art
print(text2art("Jumble!"))

def scramble(input): # start of the word scrable function
    wordToScramble = list(input) # takes the input to the function and changes it to a list, assigning that to wordToScramble, this is necessary due to the way .shuffle works
    random.shuffle(wordToScramble) # this shuffles the list in wordToScramble
    output = ''.join(wordToScramble) # this will create the output variable, joining each letter of the shuffled word to the initially empty variable
    return output # this gives output to the function

def game(): # this function is the bulk of the original code, but now in a function so it can be run again
    global score # uses the global variable "score"
    wordIndex = random.randint(0,(len(wordList)-1)) # this will give a random number to decide the index of the word that will be guessed from the list
    wordToGuess = wordList[wordIndex] # this will assign the word to be guessed as the wordIndex from wordList
    wordFixer = list(wordToGuess) # wordFixer, splits the word into a list here
    try: # for some reason, sometimes wordFixer breaks when there are no spaces to remove, the try and except was a quick way to fix this
        wordFixer.remove(" ") # wordFixer removes spaces from the list
    except:
        pass # passes the remove line so that no error message comes up, this also means that the removal of a space was not required for this word
    wordToGuess = ''.join(wordFixer) # finally, wordFixer is joind to the word to guess
    scrambledWord = scramble(wordToGuess) # this will use the scramble function to return the wordToGuess as a scrambled word
    correct = False # sets correct to false so that the while loop will run
    while correct == False:
        playerInput = input(f"The jumbled word is - {scrambledWord}\n  Guess - ") # gets the player input for the word
        if playerInput.lower() == wordToGuess: # .lower() in order to remove issues with capitals
            print("\nCorrect!")
            score += 5 # adds 5 to score
            correct = True # sets correct to true to stop the loop
        elif playerInput == "#cheat": # a cheat code for testing purposes, can be removed in the final version
            print(wordToGuess)
        else:
            score -= 1 # removes 1 from score
            print(f"\nCurrent score - {score}\nNot quite!, try again")

def chooseWordFile(input): # a function to choose the word file specifically, so that multiple word files can be had without the need to change the code
    global wordList # uses the global variable "wordList"
    try:
        wordFile = open(input, "r") # opens the word file in read mode
        wordList = list(wordFile.read().split("\n")) # splits the word file into an array variable so that it now acts as the wordList
    except:
        print("file not found, using default word list")

wordList = ["apple", "monkey", "trains", "pig", "dogs", "cats"] # default word list, in the case of a lack of file
chooseWordFile(input("Which word file? - "))
playGame = True
score = 0
while playGame == True: # repeats the game as long as the user wants
    if input("Play game? (y/n) ").lower() == "y":
        game()
        print(f'Score: {score}')
    else:
        print(f'\n\nFinal score: {score}\n{text2art("goodbye!")}')
        playGame = False