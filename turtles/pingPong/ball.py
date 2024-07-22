from turtle import Turtle


class Ball:
    """Initialize the ball object."""
    def __init__(self):
        self.ball = Turtle()
        self.setup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def setup(self):
        """Set up the ball's initial position and appearance."""
        self.ball.shape("circle")
        self.ball.shapesize(stretch_wid=1, stretch_len=1)
        self.ball.color("white")
        self.ball.penup()

    def move(self):
        """Move the ball based on its current x_move and y_move."""
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the y direction of the ball."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the x direction of the ball and increase the speed."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        """Reset the ball's position and its speed."""
        self.ball.goto(0,0,)
        self.bounce_x()
        self.move_speed = 0.1
