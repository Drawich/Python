from turtle import Turtle, Screen


def draw_grass():
    """
    Draws green grass on the top and bottom of the screen.

    This function creates a Turtle instance and uses it to draw two filled rectangles
    representing green grass at the top and bottom of the screen.
    """
    GRASS_WIDTH = 600
    GRASS_HEIGHT = 120
    GRASS_COLOR = "green"

    screen = Screen()
    screen.tracer(0)  # Disable screen updates for faster drawing

    # Create a turtle for drawing
    painter = Turtle()
    painter.speed(0)  # Set the drawing speed (0 is the fastest)

    # Draw top grass
    draw_rectangle(painter, -GRASS_WIDTH/2, 180, GRASS_WIDTH, GRASS_HEIGHT, GRASS_COLOR)

    # Draw bottom grass
    draw_rectangle(painter, -GRASS_WIDTH/2, -300, GRASS_WIDTH, GRASS_HEIGHT, GRASS_COLOR)

    painter.hideturtle()


def draw_rectangle(turtle, x, y, width, height, color):
    """
    Draws a filled rectangle using the given Turtle instance.

    Args:
        turtle (Turtle): The Turtle instance used for drawing.
        x (int): The x-coordinate of the bottom-left corner of the rectangle.
        y (int): The y-coordinate of the bottom-left corner of the rectangle.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        color (str): The fill color of the rectangle.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()