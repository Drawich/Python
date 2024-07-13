import game_setup
import format_layout_text
import get_input


def correct_guess(guess, correct_number):
    if guess == correct_number:
        return True, ''
    elif guess > correct_number:
        return False, 'too high'
    elif guess < correct_number:
        return False, 'too low'


def display_score(lives, max_number):
    print(f"You have {lives} attempts remaining to guess the number")
    print(f"I'm thinking of a number between 1 and {max_number}")


def start_guess_the_number():
    score = 0
    iterations = 1
    lives, number_of_questions, highest_number = game_setup.level()
    the_number = int(game_setup.pick_number(highest_number))
    print(game_setup.intro_guess_the_number())
    format_layout_text.clear()
    display_score, display_lives = game_setup.display_score_and_lives(score, lives)
    print(display_score + display_lives + '\n')
    while iterations <= number_of_questions:
        # print(the_number)  # testing purposes
        iterations += 1
        guess = get_input.get_guess_the_number_guess_input(highest_number)

        results, feedback = correct_guess(guess, the_number)

        if results:
            score += 1
            input('That is correct! Press enter to continue.. ')
            format_layout_text.clear()
            display_score, display_lives = game_setup.display_score_and_lives(score, lives)
            print(display_score + display_lives + '\n')
            the_number = int(game_setup.pick_number(highest_number))
        elif not results and lives > 1:
            lives -= 1
            print(f'That is {feedback}!')
        else:
            print('You ran out of lives! Games over!')
            print(f'Your final score is: {score}/{number_of_questions}')
            input("Press enter to continue.. ")
            format_layout_text.clear()
            return