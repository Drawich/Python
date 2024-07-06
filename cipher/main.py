import string


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


def cipher_text(text, shift, direction):
    """Shifts the alphabetical index of each letter in the input based on the shift amount"""
    new_string = ""
    alphabet = string.ascii_lowercase
    if direction not in ['encrypt', 'encode', 'decode', 'decrypt']:
        raise ValueError("Direction must be 'encrypt' or 'decrypt'")
    for char in text:
        if char.isalpha():
            old_index = alphabet.index(char.lower())
            if direction in ('encode', 'encrypt'):
                new_index = (old_index + shift) % len(alphabet)
            elif direction in ('decode', 'decrypt'):
                new_index = (old_index - shift) % len(alphabet)
            else:
                new_index = old_index
            new_char = alphabet[new_index]
            if char.isupper():
                new_char = new_char.upper()
            new_string += new_char
        else:
            new_string += char
    return new_string


def main():
    """
    Main function for executing the cipher program.

    This function prompts the user to choose between encryption and decryption,
    accepts the text and shift amount, performs the specified operation, and
    allows the user to play again if desired.
    """
    while True:
        print('\nWhat would you like to do today?')
        direction = validate_answer("Type 'encode' to encrypt, type 'decode' to decrypt:\n",
                                    lambda x: x in ['encrypt', 'encode', 'decode', 'decrypt'],
                                    'That is not a valid direction.')

        text = validate_answer("Enter the text you want to encrypt or decrypt:\n",
                               lambda x: len(x) > 0 and any(char.isalpha() for char in x),
                               "Please enter a valid text input with at least one alphabetic character.")

        shift = int(validate_answer("Enter the shift number (positive integer):\n",
                                    lambda x: x.isdigit() and int(x) > 0,
                                    'You must enter a positive integer.'))

        encrypted_text = cipher_text(text, shift, direction)
        print(f"The {direction}d text is: {encrypted_text}\n")

        play_again = validate_answer("Do you want to encrypt or decrypt another text? (yes/no)\n",
                                     ['yes', 'y', 'no', 'n'],
                                     "Please, enter 'yes' or 'no'.")
        if play_again in ['n', 'no']:
            break


# Starting game
print('Welcome to the cipher program!')
input('Press enter to start encoding or decoding text...')
main()
print('Thank you for using the cipher program!')
