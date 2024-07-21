from turtle import Turtle, Screen
import random

# Constants
COLORS = ['blue', 'red', 'green', 'purple', 'pink', 'orange']
FONT = ('Courier', 18, 'normal')


def generate_turtles():
    """Creates all the turtles and sends them to the starting position."""
    y_coordinate = -100
    turtles = {}

    for color in COLORS:
        turtle_name = f"turtle_{color}"
        turtles[turtle_name] = Turtle(shape="turtle")
        turtles[turtle_name].color(color)
        turtles[turtle_name].penup()
        turtles[turtle_name].goto(x=-220, y=y_coordinate)
        y_coordinate += 50

    return turtles


class TurtleRace:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=500, height=400)
        self.all_turtles = generate_turtles()
        self.user_bet = None
        self.winner_announcement = Turtle()
        self.winner_announcement.hideturtle()
        self.winner_announcement.penup()

    def get_user_bet(self):
        """Prompt the user to make a bet on the winning turtle."""
        while True:
            user_input = self.screen.textinput(title='Make your bet',
                                               prompt=f'Which turtle will win the race? Enter a color from {COLORS}: ')
            if user_input is None:
                return  # User cancelled the input
            elif user_input.lower() in COLORS:
                self.user_bet = user_input.lower()
                return
            else:
                # Invalid color entered
                self.screen.title('Invalid Input')
                self.screen.textinput('Invalid Input', f'Please enter a valid color from {COLORS}.')
                self.screen.title('Turtle Race')

    def conduct_race(self):
        """Conducts the race and determines the winner based on user bet."""
        while True:
            for turtle_name in self.all_turtles:
                turtle = self.all_turtles[turtle_name]
                if turtle.xcor() > 230:
                    winning_turtle_color = turtle.pencolor()
                    if winning_turtle_color == self.user_bet:
                        self.winner_announcement.goto(0, 0)
                        self.winner_announcement.write(f'Congratulations! \n'
                                                       f'The winner is the {winning_turtle_color} turtle.',
                                                       align='center', font=FONT)
                    else:
                        self.winner_announcement.goto(0, 0)
                        self.winner_announcement.write(f'You lost! \n'
                                                       f'The winner is the {winning_turtle_color} turtle.',
                                                       align='center', font=FONT)
                    return

                randomized_distance = random.randint(0, 10)
                turtle.forward(randomized_distance)

    def start_race(self):
        """Starts the race by getting user bet and conducting the race."""
        self.get_user_bet()
        if self.user_bet:
            self.conduct_race()

        self.screen.exitonclick()
