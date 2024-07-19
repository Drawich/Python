import format_data


def validate_text_input(question, validation, invalid_text):
    """Validate text input based on provided validation criteria.

    Args:
        question (str): The question or prompt to display to the user.
        validation (callable or list): Validation function or list of valid responses.
        invalid_text (str): Message to display when input is invalid.

    Returns:
        str: Valid user response.
    """
    while True:
        user_response = input(format_data.break_line_at_char(question, ' ')).strip().lower()
        if callable(validation):
            if validation(user_response):
                return user_response
            else:
                print(invalid_text)
        elif user_response in validation:
            return user_response
        else:
            print(invalid_text)


def validate_int_input(question, validation=None):
    """Validate integer input based on provided validation criteria.

    Args:
        question (str): The question or prompt to display to the user.
        validation (callable or None): Validation function or None for no additional validation.

    Returns:
        int: Valid user integer response.

    Raises:
        ValueError: If user input cannot be converted to an integer.
    """
    while True:
        invalid_message = 'Please, provide a number within the range.'
        user_response = input(format_data.break_line_at_char(question, ' ')).strip().lower()
        try:
            int_user_response = int(user_response)
            if callable(validation):
                if validation(int_user_response):
                    return int_user_response
                else:
                    print(invalid_message)
            elif validation is None:
                return int_user_response
            else:
                print(invalid_message)
        except ValueError:
            print('Your response has to be written as a whole number.')
