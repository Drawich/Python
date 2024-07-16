def validate_text_input(question, valid_responses, invalid_text):
    while True:
        response = input(question).strip().lower()
        if callable(valid_responses):
            if valid_responses(response):
                return response
            else:
                print(invalid_text)
        else:
            if response in valid_responses:
                return response
            else:
                print(invalid_text)


def validate_float_input(question, invalid_text):
    """Validates float input."""
    while True:
        response = input(question)
        try:
            float_value = float(response)
            if float_value >= 0:
                return float_value
            else:
                print(invalid_text)
        except ValueError:
            print(invalid_text)
