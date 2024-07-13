import input_validations

# Get user input
def get_difficulty_input():
    return input_validations.validate_answer("Choose a difficulty, Type 'easy' or 'hard. \n",
                           lambda x: x in ['easy', 'hard'],
                           'That is not a valid input')


def get_higher_lower_guess_input():
    return input_validations.validate_answer("Write 'higher' or 'lower'. \n",
                           lambda x: x in ['higher', 'lower'],
                           'That is not a valid input')


def get_guess_the_number_guess_input(number):
    return input_validations.validate_integer(f"Guess what number I am thinking about. It is between 1 and {number}: \n", 'It has to be a whole number.')



def restart():
    """Asks if user wants to restart."""
    return input_validations.is_valid_yes_no('Do you want to restart the game? (yes/no)')


def play_something_new():
    """Asks if user wants to restart."""
    return input_validations.is_valid_yes_no('Do you want to play another game? (yes/no)')
