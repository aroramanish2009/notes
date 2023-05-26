# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import sys

WORDLIST_FILENAME = "words.txt"

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
 
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
 
 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
 
 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
 
 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
 
 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
 
 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for s_letter in secret_word:
        if s_letter not in letters_guessed:
            return (False)
    return (True)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    for s_letter in secret_word:
        if s_letter not in letters_guessed:
            secret_word = secret_word.replace(s_letter, "_ ")
    return (secret_word)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    for letter in letters_guessed:
        all_letters = all_letters.strip(letter)
    return (all_letters)
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    x = 6
    input_warn_counter = 3
    letters_guessed = []
    print ('Welcome to the game Hangman!')
    print ("I am thinking of a word that is {} letters long".format(len(secret_word)))
    print ('-------------')
    while x >= 0:
        print ('You have {} warnings left'.format(input_warn_counter))
        print ('You have {} guesses left'.format(x))
        print ('Available letters:', get_available_letters(letters_guessed))
        while input_warn_counter >= 0 and x >= 0:
            letter_guessed = str(input("Please guess a letter:"))
            letter_guessed = letter_guessed.lower()
            if letter_guessed not in string.ascii_lowercase or letter_guessed in letters_guessed:
                input_warn_counter -= 1
                if input_warn_counter < 0 and letter_guessed not in string.ascii_lowercase:
                    print ("Oops! That is not a valid letter.  You have no warnings left")
                    print ("so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                    print ('-------------')
                    x -= 1
                    input_warn_counter = 3
                    print ('You have {} warnings left'.format(input_warn_counter))
                    print ('You have {} guesses left'.format(x))
                elif input_warn_counter < 0 and letter_guessed in letters_guessed:
                    print ("Oops! You've already guessed that letter. You have no warnings left")
                    print ("so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                    print ('-------------')
                    x -= 1
                    input_warn_counter = 3
                    print ('You have {} warnings left'.format(input_warn_counter))
                    print ('You have {} guesses left'.format(x))
                elif letter_guessed not in string.ascii_lowercase:
                    print ("Oops! That is not a valid letter. You have {} warnings left".format(input_warn_counter))
                    print (get_guessed_word(secret_word, letters_guessed))
                    print ('-------------')
                elif letter_guessed in letters_guessed:
                    print ("Oops! You've already guessed that letter. You have {} warnings left".format(input_warn_counter))
                    print (get_guessed_word(secret_word, letters_guessed))
                    print ('-------------')
            else:
                break
        letters_guessed.append(letter_guessed)
        if is_word_guessed(secret_word, letters_guessed):
            print ('Good guess:', secret_word)
            print ('-------------')
            print ('Congratulations, you won!')
            print ('Your total score for this game is: {}'.format(x * len(set(secret_word))))
            sys.exit()
        elif letter_guessed in secret_word:
            print ('Good guess', get_guessed_word(secret_word, letters_guessed))
            print ('-------------')
        else:
            if x > 0:
                print ('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                print ('-------------')
                if letter_guessed in "aeiou":
                    x -= 2
                else:
                    x -= 1
            else:
                x -= 1
                break
    print ('Sorry, you ran out of guesses. The word was {}'.format(secret_word))

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if len(my_word) == len(other_word):
        match = False
        for i in range(len(my_word)):
            if my_word[i] != "_":
                if my_word[i] == other_word[i] and my_word.count(my_word[i]) == other_word.count(my_word[i]):
                    match = True
                else:
                    return (False)
        if match:
            return (True)
    else:
        return (False)



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    options = ""
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            options = options + other_word + " "
    if options:
        prCyan (options)
    else:
        prRed ("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    x = 6
    input_warn_counter = 3
    letters_guessed = []
    prCyan ('Welcome to the game Hangman!')
    prCyan ("I am thinking of a word that is {} letters long".format(len(secret_word)))
    prPurple ('-------------')
    while x >= 0:
        prYellow ('You have {} warnings left'.format(input_warn_counter))
        prYellow ('You have {} guesses left'.format(x))
        print ('Available letters:', get_available_letters(letters_guessed))
        prPurple ('-------------')
        if letters_guessed:
            guessed = ''.join(str(x) for x in letters_guessed)
            prYellow ('Letters Guessed already: ' + guessed)
            prPurple ('-------------')
            prGreen ('Enter * for Hints')
            prPurple ('-------------')
        while input_warn_counter >= 0 and x >= 0:
            letter_guessed = str(input("Please guess a letter:"))
            if letter_guessed != "*":
                letter_guessed = letter_guessed.lower()
                if letter_guessed not in string.ascii_lowercase or letter_guessed in letters_guessed:
                    input_warn_counter -= 1
                    if input_warn_counter < 0 and letter_guessed not in string.ascii_lowercase:
                        prRed ("Oops! That is not a valid letter.  You have no warnings left")
                        print ("so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                        prPurple ('-------------')
                        x -= 1
                        input_warn_counter = 3
                        prYellow ('You have {} warnings left'.format(input_warn_counter))
                        prYellow ('You have {} guesses left'.format(x))
                    elif input_warn_counter < 0 and letter_guessed in letters_guessed:
                        prRed ("Oops! You've already guessed that letter. You have no warnings left")
                        print ("so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                        prPurple ('-------------')
                        x -= 1
                        input_warn_counter = 3
                        prYellow ('You have {} warnings left'.format(input_warn_counter))
                        prYellow ('You have {} guesses left'.format(x))
                    elif letter_guessed not in string.ascii_lowercase:
                        prRed ("Oops! That is not a valid letter. You have {} warnings left".format(input_warn_counter))
                        print (get_guessed_word(secret_word, letters_guessed))
                        prPurple ('-------------')
                    elif letter_guessed in letters_guessed:
                        prYellow ("Oops! You've already guessed that letter. You have {} warnings left".format(input_warn_counter))
                        print (get_guessed_word(secret_word, letters_guessed))
                        prPurple ('-------------')
                else:
                    break
            else:
                my_word = get_guessed_word(secret_word, letters_guessed).replace('_ ','_')
                show_possible_matches(my_word)
        letters_guessed.append(letter_guessed)
        if is_word_guessed(secret_word, letters_guessed):
            prPurple ('############################################')
            print ("\033[92m #  Good guess: \033[00m", secret_word)
            prPurple ('############################################')
            prRed   ('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            prGreen ('% Congratulations, you won!                 %')
            prGreen ('% Your total score for this game is: {}'.format(x * len(set(secret_word))) + "     %")
            prRed   ('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            sys.exit()
        elif letter_guessed in secret_word:
            prPurple ('###########################################')
            print ("\033[92m #  Good guess: \033[00m", get_guessed_word(secret_word, letters_guessed))
            prPurple ('###########################################')
        else:
            if x > 0:
                print ("\033[91m Oops! That letter is not in my word: \033[00m", get_guessed_word(secret_word, letters_guessed))
                prPurple ('-------------')
                if letter_guessed in "aeiou":
                    x -= 2
                else:
                    x -= 1
            else:
                x -= 1
                break
    prRed ('Sorry, you ran out of guesses. The word was {}'.format(secret_word))


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
