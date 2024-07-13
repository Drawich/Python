import random
import get_input
import game_setup
import format_layout_text
from game_data import data_higher_lower


def section_data(number_of_questions):
    """Returns shuffled lists of names, follower counts, descriptions, and countries."""
    names, follower_counts, descriptions, countries = [], [], [], []

    shuffled_data = list(data_higher_lower)
    random.shuffle(shuffled_data)

    for i in range(number_of_questions):
        question = shuffled_data[i]
        names.append(question['name'])
        follower_counts.append(question['follower_count'])
        descriptions.append(question['description'])
        countries.append(question['country'])

    return names, follower_counts, descriptions, countries


def verify_user_guess(user_guess, first_answer, second_answer):
    """Verifies if the user's guess is correct based on follower counts."""
    user_guess = user_guess.lower().strip()
    expected_result = 'higher' if first_answer < second_answer else 'lower'
    return user_guess == expected_result


def start_higher_lower():
    lives, number_of_questions, none = game_setup.level()
    question_names, question_follower_counts, question_descriptions, question_countries = section_data(number_of_questions)
    score = 0
    screen_width = 100
    format_layout_text.clear()
    display_score, display_lives = game_setup.display_score_and_lives(score, lives)
    print(display_score + display_lives)
    print()

    for i in range(number_of_questions - 1):
        intro_first_item = f'{question_names[i]} is a {question_descriptions[i]} from {question_countries[i]} and has {question_follower_counts[i]} followers. '
        intro_second_item = f'{question_names[i+1]} is a {question_descriptions[i+1]} from {question_countries[i+1]}.\n'
        question = f'Do you believe {question_names[i+1]} or {question_names[i]} has the most followers?'
        print(format_layout_text.linebreak_at_char(intro_first_item + intro_second_item, screen_width))
        print(format_layout_text.linebreak_at_char(question + '\n', screen_width))

        first_answer = question_follower_counts[i]
        second_answer = question_follower_counts[i+1]
        user_guess = get_input.get_higher_lower_guess_input()

        if not verify_user_guess(user_guess, first_answer, second_answer):
            lives -= 1
            format_layout_text.clear()

            display_score, display_lives = game_setup.display_score_and_lives(score, lives)
            print(display_score + display_lives)

            print(f"That is wrong. {question_names[i]} has {question_follower_counts[i]} followers while {question_names[i+1]} only has {question_follower_counts[i+1]}.\n")

        else:
            score += 1
            format_layout_text.clear()

            display_score, display_lives = game_setup.display_score_and_lives(score, lives)
            print(display_score + display_lives)
            print('That is correct!\n')

        if lives == 0:
            print("Game over! You ran out of lives.")
            break

    print(f"Your final score is {score}/{number_of_questions}.")
    return
start_higher_lower()