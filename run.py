import random
import os

from assets.words import words
from assets.hangman import hangman

print("Welcome to hangman! You've got 6 chances to")
print("guess the right word and to save the hangman!")

word = ""
lives = 6
correct_letters = []
incorrect_letters = []
guessed_letters = []
win = False

def generate_random_word():
    """
    Generates a random word for the user to guess and
    displays underlines. The number of letters in the
    generated word will determine how many underlines are
    displayed
    """
    global word
    word = random.choice(words)
    word = word.upper()

    for i in word:
        print("_", end=" ")

    return word


def display_hangman():
    if(lives == 6):
        print(hangman[0])
    elif(lives == 5):
        print(hangman[1])
    elif(lives == 4):
        print(hangman[2])
    elif(lives == 3):
        print(hangman[3])
    elif(lives == 2):
        print(hangman[4])
    elif(lives == 1):
        print(hangman[5])
    elif(lives == 0):
        print(hangman[6])

def validate_guess():
    valid_guess = False
    guess = input('\n Guess a letter:')
    if len(guess) > 1:
        print("You can only enter 1 letter at a time!")
    elif guess in correct_letters or guess in incorrect_letters:
        print("You've already guessed that letter!")
    else:
        valid_guess = True

def update_letters():
    """
    Will update 'guessed letters' with the guessed letter,
    and add the letter to the word if the guessed letter
    is in the generated word
    """
    global correct_letters
    global incorrect_letters

    letter = validate_guess()
    for i in word
    if letter in word_letters:
        correct_letters.append(letter)
    else:
        lives -= 1

def update_guessed_letters():
    global guessed_letters
    if letter in word_letters:
        guessed_letters.append(letter)
    print("Guessed letters:")
    print(guessed_letters)

def run_game():
    while win is False and lives != 0:
        display_hangman()
        generate_random_word()
        validate_guess()
        update_letters()
        update_guessed_letters()

run_game()

#def check_letter():
 #   for i in range(len(word)):
  #      if guess == word[i]:
   #         print[i] = guess

"""
generate_random_word()
display_hangman()
display_word()
validate_guess()
#check_letter()
"""





