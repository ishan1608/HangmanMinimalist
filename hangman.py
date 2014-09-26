import random
import string
import os
import platform

# Defining the text file containing the list of words
WORDLIST_FILENAME = "words.txt"
MAX_GUESSES = 8

def loadWords():
    # Returns a list of valid words. Words are taken from the file words.txt
    
    print "Loading word list from file..."
    # Open file for reading with no buffering
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # Read the file in single line
    line = inFile.readline()
    # Split all the words separated by whitespaces
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    # Choose a word at random which the user have to guess
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    # Separating out each character from the secretWord
    # Each character is stored only once
    secretLetters = {};
    for letter in secretWord:
        secretLetters[letter] = True;

    # Checking for the non-existence of any character from the secretWord
    # The result is stored as True of False
    result = True;
    for sl in secretLetters:
        if not sl in lettersGuessed:
            result = False;
            break;
    return result;

def getGuessedWord(secretWord, lettersGuessed):
    # Returns the guessed word in a specific format
    # Example - the word 'apple' with the guessed characters ['a', 'b','l','s','e']
    # would look like this 'a_ _ l _ '
    result = "'";
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter;
        else:
            result += '_ ';
    result += "'";
    return result;


def getAvailableLetters(lettersGuessed):
    # Return the list of letters that are available to be used
    # The letters returned are in lowercase
    availableLetters = string.ascii_lowercase;
    for letter in lettersGuessed:
        availableLetters = availableLetters.replace(letter, '');
    return availableLetters;

def clearTerminal():
    # Clears the terminal on which the output is being displayed.
    # Works at least on Windows and Linux, I haven't tested it on Mac OS
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def hangman(secretWord):
    # Total number of wrong guesses allowed is 8
    numberOfGuesses = MAX_GUESSES
    # The letters guessed by the user
    lettersGuessed = {}
    # Welcome message
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %s letters long.' %(str(len(secretWord)))
    # Infinite loop which breaks from inside the loop's conditions
    while True:
        print '-------------'
        if not isWordGuessed(secretWord, lettersGuessed):
            # Word not guessed
            if numberOfGuesses == 0:
                # All guesses exhausted, end the game
                print 'Sorry, you ran out of guesses. The word was %s.' %(secretWord)
                break
            else:
                # Guesses left, Display guesses left and available letters
                print 'You have %s guesses left.' %(str(numberOfGuesses))
                print 'Available letters: %s' %(getAvailableLetters(lettersGuessed))
                # Take input from the user
                guessedLetter = raw_input('Please guess a letter: ')
                # Clearing the terminal
                # Can use and cannot use depending on the preference
                clearTerminal()
                if guessedLetter in lettersGuessed:
                    #  Already guessed letter, display guessed word
                    print 'Oops! You\'ve already guessed that letter:%s' %(getGuessedWord(secretWord, lettersGuessed))
                else:
                    # New guess, add to lettersGuessed
                    lettersGuessed[guessedLetter] = True
                    if guessedLetter not in secretWord:
                        # Wrong Guess, decrement number of guesses
                        print 'Oops! That letter is not in my word:%s' %(getGuessedWord(secretWord, lettersGuessed))
                        numberOfGuesses -= 1
                    else:
                        # Correct guess
                        print 'Good guess:%s' %(getGuessedWord(secretWord, lettersGuessed))
        else:
            # Word guessed
            print 'Congratulations, you won!'
            break

# Execution sequence of the game
# Load the words from file
wordlist = loadWords()
# Choose a secret word for the user to guess
secretWord = chooseWord(wordlist).lower()
# Start the game for user
hangman(secretWord)