from turtle import Turtle


class Snake:
    """A class to manage the snake of the game."""

    COLOR = '#fff'
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20

    def __init__(self):
        """Initialize the snake with starting segments and set the head."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Initialize the snake with 3 different segments."""
        for position in self.STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Increase the length of the snake by adding a new segment."""
        new_segment = Turtle("square")
        new_segment.color(self.COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Increase the length of the snake by adding a new segment at the tail."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by updating the positions of its segments."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.MOVE_DISTANCE)

    def reset_snake(self):
        """Reset the snake's position to starting positions."""
        for segment, position in zip(self.segments, self.STARTING_POSITIONS):
            segment.goto(position)

        # Remove extra segments
        if len(self.segments) > 3:
            for _ in range(len(self.segments) - 3):
                segment = self.segments.pop()
                segment.goto(1000, 1000)  # moves segment out of the screen
                del segment

    def up(self):
        """Change the snake's direction to move upwards when the UP arrow key is pressed,
        unless the snake is already moving downwards (270 degrees) to avoid colliding
        with itself.

        Usage: Call this method when the UP arrow key is pressed.
        """
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Change the snake's direction to move downwards when the DOWN arrow key is pressed,
        unless the snake is already moving upwards (90 degrees) to avoid colliding
        with itself.

        Usage: Call this method when the DOWN arrow key is pressed."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """Change the snake's direction to move leftwards when the LEFT arrow key is pressed,
        unless the snake is already moving rightwards (0 degrees) to avoid colliding
        with itself.

        Usage: Call this method when the LEFT arrow key is pressed."""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """Change the snake's direction to move rightwards when the RIGHT arrow key is pressed,
        unless the snake is already moving leftwards (180 degrees) to avoid colliding
        with itself.

        Usage: Call this method when the RIGHT arrow key is pressed."""
        if self.head.heading() != 180:
            self.head.setheading(0)
