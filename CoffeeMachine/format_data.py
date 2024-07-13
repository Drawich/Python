import sys
import os


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