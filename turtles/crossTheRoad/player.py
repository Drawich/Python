from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200


class Player(Turtle):
    def __init__(self):
        """Initialize the player turtle."""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Move the player turtle up."""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        """Move the player turtle down."""
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

    def reset_player(self):
        """Reset the player turtle to the starting position."""
        self.goto(STARTING_POSITION)
