import turtle
import os

import pandas
import pandas as pd
import tkinter as tk
from tkinter import messagebox


def display_instruction(pen, screen_height):
    """Write instructions at the top of the window."""
    pen.goto(0, screen_height // 2 - 50)
    pen.pendown()
    pen.write("Guess all the states you remember, then type 'Exit' when done.",
              align='center', font=("Arial", 18, "bold"))
    pen.penup()


def display_popup(message):
    """Display a popup with the provided message."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo('Message', message)
    root.destroy()  # Close the root window after displaying the message


def setup_screen(image_path):
    """Setup the turtle screen with the given image path."""
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(image_path)
    return screen


def setup_turtle(image_path):
    """Create and return turtles for displaying the image and text."""
    img_turtle = turtle.Turtle()
    img_turtle.shape(image_path)
    img_turtle.penup()

    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()

    return img_turtle, text_turtle


def get_state_input(screen, guessed_list, number_of_states):
    """Prompt the user for state names and return the state name input by the user."""
    answer_state = screen.textinput(f'{len(guessed_list)}/{number_of_states} States Guessed',
                                    prompt="What's another state's name")
    return answer_state if answer_state else None


def update_guessed_states(answer_state, guessed_list, all_states):
    """Update the guessed list only if the state is valid and not already guessed."""
    formatted_state = answer_state.strip().title()
    if formatted_state in all_states:
        if formatted_state not in guessed_list:
            guessed_list.add(formatted_state)
            return formatted_state, False
        else:
            return formatted_state, True
    return formatted_state, False


def handle_state_response(text_turtle, state_row, formatted_state, all_states):
    """Handle user input and update the screen based on whether the state is valid or not."""
    if state_row.empty:
        return f"The state '{formatted_state}' doesn't exist or is misspelled."
    else:
        # Extract coordinates
        x = state_row["x"].values[0]
        y = state_row["y"].values[0]

        # Move the turtle to the coordinates and write the state name
        text_turtle.goto(x, y)
        text_turtle.write(formatted_state, align="center", font=("Arial", 10, "bold"))

        # Remove state from the all_states set if it exists
        all_states.discard(formatted_state)
    return None


def save_missed_states(all_states):
    """Save the list of missed states to a CSV file."""
    states_to_learn = pd.DataFrame(all_states, columns=['Missed States'])
    states_to_learn.to_csv('states_to_learn.csv', index=True)


def main():
    image_path = "blank_states_img.gif"
    csv_path = "50_states.csv"

    # Check for file existence
    if not os.path.isfile(image_path) or not os.path.isfile(csv_path):
        print(f"Error: The file {image_path if not os.path.isfile(image_path) else csv_path} does not exist.")
        return

    # Load data
    states_data = pd.read_csv(csv_path)
    number_of_states = len(states_data)
    ALL_STATES = set(states_data['state'].str.strip().str.title().tolist())
    all_states_minus_guess = set(states_data['state'].str.strip().str.title().tolist())

    # Set up screen and turtles
    screen = setup_screen(image_path)
    img_turtle, text_turtle = setup_turtle(image_path)
    width, height = screen.window_width(), screen.window_height()

    # Display instructions
    display_instruction(text_turtle, height)

    guessed_list = set()

    # Main loop for user input
    while len(guessed_list) < number_of_states:
        answer_state = get_state_input(screen, guessed_list, number_of_states)
        if answer_state:
            formatted_state, already_guessed = update_guessed_states(answer_state, guessed_list, ALL_STATES)

            if already_guessed:
                display_popup(f"You have already guessed {formatted_state}.")
            elif formatted_state == 'Exit':
                break

            state_row = states_data[states_data["state"].str.strip().str.title() == formatted_state]
            message = handle_state_response(text_turtle, state_row, formatted_state, all_states_minus_guess)

            if message:
                display_popup(message)

    all_states_minus_guess = list(all_states_minus_guess)

    # Display missed states
    if len(all_states_minus_guess) > 1:
        missed_states = ', '.join(sorted(all_states_minus_guess[:-1]))
        missed_states += f', and {sorted(all_states_minus_guess)[-1]}'
        message = f"You missed the following states: {missed_states}."
    elif len(all_states_minus_guess) == 1:
        message = f"You missed the following state: {list(all_states_minus_guess)[0]}."
    else:
        message = 'You got all the states right!'

        display_popup(message)

    # Save missed states
    save_missed_states(all_states_minus_guess)

    screen.mainloop()


if __name__ == "__main__":
    main()
