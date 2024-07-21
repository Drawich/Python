from turtle import Turtle, Screen


class DrawWithTurtle:
    MOVE_DISTANCE = 10

    def __init__(self):
        self.drawer = Turtle()
        self.screen = Screen()
        self.setup()

    def setup(self):
        self.screen.listen()
        self.screen.onkey(key="w", fun=self.move_forward)
        self.screen.onkey(key="s", fun=self.move_backward)
        self.screen.onkey(key="d", fun=self.move_right)
        self.screen.onkey(key="a", fun=self.move_left)
        self.screen.onkey(key="c", fun=self.clear)

        self.drawer.shape("classic")
        self.drawer.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def move_forward(self):
        """Move the turtle forwards"""
        self.drawer.forward(self.MOVE_DISTANCE)

    def move_backward(self):
        """Move the turtle backwards"""
        self.drawer.backward(self.MOVE_DISTANCE)

    def move_left(self):
        """Turn the turtle left"""
        self.drawer.left(10)

    def move_right(self):
        """Turn the turtle right"""
        self.drawer.right(10)

    def clear(self):
        """Clear the screen and reset turtle's position"""
        self.drawer.clear()
        self.drawer.penup()
        self.drawer.home()
        self.drawer.pendown()

    def start(self):
        """Start the turtle drawing application"""
        self.screen.exitonclick()
