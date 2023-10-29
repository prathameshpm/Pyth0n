import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)                 #randomly chooses a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)                    # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()                        # what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have ', lives, ' left. You have used these letters: ', ' '.join(used_letters))

        # what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print('Current Word: ', ' '.join(word_list))

        # getting user input
        user_input = input('Guess a letter: ').upper()
        if user_input in alphabet - used_letters:   # check if letter typed by user is not used earlier
            used_letters.add(user_input)            # add it to list of used letters
            if user_input in word_letters:          # check if user has guessed correct word
                word_letters.remove(user_input)     # remove the guessed letter from word letters
            else:
                lives = lives - 1
                print('Letter is not in the word')

        elif user_input in used_letters:            # check if letter typed by user is already tried
            print("You already guessed that letter. Please try again")

        else:                                       # the typed letter is neither used nor in alphabet
            print("Please type a valid character")

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print('You Died. The word was: ', word)
    else:
        print('You guessed the word correctly')

hangman()