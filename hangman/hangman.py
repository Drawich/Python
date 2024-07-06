import random
import os
import string
from hangman_pictures import stages
from hangman_words import word_list


def handle_guess(guess, word, updated_list, updated_lives):
    if guess in word:
        updated_list = update_displayed_list(guess, word, updated_list)
        print(f'Good guess! "{guess}" is in the word.')
    else:
        updated_lives = decrement_lives(guess, word, updated_lives)
        print(f'Oops! "{guess}" is not in the word.')

    return updated_list, updated_lives


def answer_validation(answer, valid_answer, already_guessed):
    while True:
        if answer not in valid_answer:
            answer = input('That is not a valid answer. Try again: \n').lower()
        elif answer in already_guessed:
            answer = input('You have already guessed this letter. Guess another: \n').lower()
        else:
            break
    return answer


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    elif os.name == 'nt':
        _ = os.system('cls')
    else:
        print('\n' * 100)


def update_displayed_list(guessed_letter, word, old_list):
    updated_list = old_list[:]  # Create a copy of old_list
    for index, letter in enumerate(word):
        if guessed_letter == letter:
            updated_list[index] = guessed_letter
    return updated_list


def decrement_lives(guessed_letter, word, current_lives):
    if guessed_letter not in word:
        current_lives -= 1
    return current_lives


# Display welcome message
print('Welcome to the Hangman Game!')

while True:
    # Initialize game variables
    chosen_word = random.choice(word_list)
    displayed_list = ['_'] * len(chosen_word)
    guessed_letters = []
    incorrect_guesses = []
    lives = 6
    alphabet = list(string.ascii_lowercase)

    while True:
        clear_screen()
        print(f'Incorrect guesses: {" ".join(incorrect_guesses)}')
        print(f'You have {lives} lives left.')
        print(' '.join(displayed_list))
        print(stages[lives])
        user_guess = input('Guess a letter: \n').lower()
        user_guess = answer_validation(user_guess, alphabet, guessed_letters + incorrect_guesses)
        if user_guess in chosen_word:
            guessed_letters.append(user_guess)
        else:
            incorrect_guesses.append(user_guess)

        displayed_list, lives = handle_guess(user_guess, chosen_word, displayed_list, lives)

        if '_' not in displayed_list:
            clear_screen()
            print(f"{' '.join(displayed_list)}\nCongratulations! You guessed the word: {chosen_word}")
            break

        if lives == 0:
            clear_screen()
            print(f"The word was: {chosen_word}\nYou ran out of lives, you lose!")
            break

    play_again = input("Do you want to play again? (yes/no)\n").lower()
    play_again = answer_validation(play_again, ['yes', 'no', 'y', 'n'], guessed_letters + incorrect_guesses)
    if play_again in ['no', 'n']:
        break

print('\n Thank you for playing Hangman!')
