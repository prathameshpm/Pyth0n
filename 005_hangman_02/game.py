import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()        # what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have ', lives, ' lives. You have used letters: ', ' '.join(used_letters))

        # what current word is ie W - R D
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))

        # getting user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(user_letter, ' is not in the word ')

        elif user_letter in used_letters:
            print('You already guessed letter: ', user_letter, '. Please try again...')
        
        else:
            print('Please enter a valid character')

    if lives == 0:
        print('You Died. Correct word was: ', word)
    else:
        print('Yayy!! You guessed the word ', word, ' correctly aaand Youuu Wooon...')

hangman()