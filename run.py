import random
import os

import constants
import hangman


def title_of_game():
    """
    Adds a title to the game
    """
    print("Welcome to hangman! You've got 6 chances to")
    print("guess the right word and to save the hangman!")


def generate_random_word(words):
    """
    Generates a random word for the user to guess and
    displays underlines. The number of letters in the
    generated word will determine how many underlines are
    displayed
    """
    word = random.choice(constants.WORDS)
    return word

def display_word(word, guessed_letters):
    """
    Prints the words as underscores
    """
    value = ""

    for i in range(len(word)):
        if word[i] in guessed_letters:
            value += word[i] + " "
        else: 
            value += "_ "
    print(value)

def display_hangman(lives_left):
    """
    Displays the hangman graphics
    """
    current_graphic = len(hangman.HANGMAN) - lives_left - 1
    print(hangman.HANGMAN[current_graphic])


def display_lives(lives):
    """
    Displays how many lives the user has left
    """
    print("")
    print(f"You have {lives} lives left!")


def display_guessed_letters(letters):
    """
    Displays the letters the user has already guessed
    """
    value = ""
    for i in letters:
        value += i + " "

    print(f"Letters guessed: {value}")


def get_and_validate_guess(excluded_letters):
    while True:
        print("")
        guess = input('Guess a letter: ').lower()

        if len(guess) > 1:
            print("You can only enter 1 letter at a time!")
        elif len(guess) < 1:
            print("You have to enter a letter!")
        elif guess not in constants.ALPHABET:
            print("Please enter a valid letter!")
        elif guess in excluded_letters:
            print(f"You've already guessed {guess}!")
        else:
            return guess

def check_guess(word, letter):
    """
    Checks how many times the guessed letter
    appears in the word
    """
    count_letter = word.count(letter)
    return count_letter


def run_game():
    guessed_letters = []
    lives_left = 6
    correct_answers = 0

    game_word = generate_random_word(constants.WORDS)

    while True:
        print("\033[H\033[2J", end="")
        title_of_game()
        display_hangman(lives_left)
        display_word(game_word, guessed_letters)
        display_lives(lives_left)
        display_guessed_letters(guessed_letters)

        if lives_left == 0:
            print(f"You lost! the word was '{game_word}'")
            return
        if correct_answers == len(game_word):
            print("You won!")
            return

        guess = get_and_validate_guess(guessed_letters)
        guessed_letters.append(guess)

        correct_guess = check_guess(game_word, guess)
        if correct_guess == 0:
            lives_left -= 1
        else: 
            correct_answers += correct_guess


def play_again():
    """
    Gives the user the option to play again after they have won
    or lost. Accepts y and anything that starts with y as "yes".
    """
    return input("Do you want to play again? (y/n): ").lower().startswith("y")


if __name__ == '__main__':
    while True:
        run_game()

        if not play_again():
            break







