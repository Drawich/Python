from turtle import Turtle


class Paddle:
    MOVEMENT_INCREMENT = 20

    def __init__(self, x_position):
        """Initialize the paddle object."""
        self.paddle = Turtle()
        self.setup(x_position)

    def setup(self, x_position):
        """Set up the paddle's initial position and appearance."""
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.setx(x_position)
        self.paddle.color("white")

    def up(self):
        """Move the paddle upwards."""
        new_y = self.paddle.ycor() + Paddle.MOVEMENT_INCREMENT
        self.paddle.sety(new_y)

    def down(self):
        """Move the paddle downwards."""
        new_y = self.paddle.ycor() - Paddle.MOVEMENT_INCREMENT
        self.paddle.sety(new_y)
