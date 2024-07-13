import get_input
import random


def intro_guess_the_number():
    return('Welcome to the Number Guessing Game!')


def level():
    """Prompts the user to choose a difficulty level and returns lives and question count."""
    user_choice = get_input.get_difficulty_input()
    number_of_lives = lives(user_choice)
    question_count = number_of_questions(user_choice)
    extra = 5
    return number_of_lives, question_count, extra


def lives(difficulty_level):
    """Returns the number of lives based on the chosen difficulty level."""
    return 5 if difficulty_level == 'hard' else 10


def number_of_questions(difficulty_level):
    """Returns the number of questions based on the chosen difficulty level."""
    return 50 if difficulty_level == 'hard' else 25

def pick_number(highest_number):
    return random.randint(1, int(highest_number))


def display_score_and_lives(score, lives):
    """Formats and returns strings for displaying score and lives."""
    terminal_width = 100
    score_str = f"Score: {score}"
    lives_str = f"Lives left: {lives}"
    display_score = score_str.ljust(terminal_width // 2)
    display_lives = lives_str.rjust(terminal_width // 2)
    return display_score, display_lives


