import sys
import os

WIDTH = 80  # Screen width variable that is used to center text


# To clear screen
def is_running_in_terminal():
    """Check if the script is running in a terminal."""
    return sys.stdin.isatty()


def clear():
    """Clears the screen if running in a terminal; otherwise, inserts default number of new lines."""
    windows_clear_command = 'cls'
    unix_clear_command = 'clear'

    if is_running_in_terminal():
        if os.name == 'nt':  # For Windows
            _ = os.system(windows_clear_command)
        else:  # For Unix/Linux/Mac
            _ = os.system(unix_clear_command)
    else:
        print('\n' * 50)


def break_line_at_char(text, break_at_character):
    """Inserts line breaks in text after characters_per_line characters from the last occurrence of
    break_at_character."""
    lines = []
    current_line = []
    current_length = 0
    characters_per_line = WIDTH

    for char in text:
        if char == break_at_character and current_length >= characters_per_line:
            lines.append(''.join(current_line))
            current_line = [char]
            current_length = 1
        else:
            current_line.append(char)
            current_length += 1

    lines.append(''.join(current_line))
    return '\n'.join(lines)


def center_text(text):
    """Centers text horizontally within WIDTH."""
    return text.center(WIDTH)


def display_score(score, number_of_questions):
    """Formats and aligns score information to the right within WIDTH."""
    aligned_text = f"Score: {score}/{number_of_questions}".rjust(WIDTH)
    return aligned_text
