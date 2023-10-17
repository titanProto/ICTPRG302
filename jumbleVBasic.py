import random #required to find a random word in list and scrable word

def scramble(input): #start of the word scrable function
    wordToScramble = list(input) #takes the input to the function and changes it to a list, assigning that to wordToScramble, this is necessary due to the way .shuffle works
    random.shuffle(wordToScramble) #this shuffles the list in wordToScramble
    output = ''.join(wordToScramble) #this will create the output variable, joining each letter of the shuffled word to the initially empty variable
    return output #this gives output to the function

wordList = ["apple", "monkey", "trains", "pig", "dogs", "cats"] #the simple word list
wordIndex = random.randint(0,(len(wordList)-1)) #this will give a random number to decide the index of the word that will be guessed from the list
wordToGuess = wordList[wordIndex] #this will assign the word to be guessed as the wordIndex from wordList
scrambledWord = scramble(wordToGuess) #this will use the scramble function to return the wordToGuess as a scrambled word
if input(f"\nThe jumbled word is - {scrambledWord}\n  Guess - ") == wordToGuess: #this statement has both the input and printing of the scrambled word all within the if statement, ends up saving roughly two extra lines, and makes it more easily iterable in future
    print("\nYou have won! :D") #prints winning messsage
else:
    print("\nYou have lost :(") #prints losing message