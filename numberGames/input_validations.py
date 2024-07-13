# input_validations.py

def is_valid_yes_no(x):
    """Validate more bidders input: must be 'yes', 'no', 'y', or 'n'."""
    return x.lower() in ['yes', 'y', 'no', 'n']


def validate_integer(question, invalid_text):
    """Validates integer input."""
    while True:
        response = input(question)
        if response.isdigit() and int(response) > 0:
            return int(response)
        else:
            print(invalid_text)


def validate_float(question, invalid_text):
    """Validates float input."""
    while True:
        response = input(question)
        if response.isdigit() and response > 0:
            float_value = float(response)
            return float_value
        else:
            print(invalid_text)


def validate_answer(question, valid_responses, invalid_text):
    """Ensures valid user input and prompts for retry if invalid."""
    while True:
        response = input(question).strip().lower()

        if callable(valid_responses):
            if not valid_responses(response):
                print(invalid_text)
            else:
                return response
        else:
            if response not in valid_responses:
                print(invalid_text)
            else:
                return response
