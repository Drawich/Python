import colorgram
import turtle
import random
import os


def generate_colors_from_image(image_path):
    """Picks 20 different colors from the image and saves it in a list"""
    formatted_picked_colors = []

    colors = colorgram.extract(image_path, 20)
    for color in colors:
        if color.rgb.r >= 240 or color.rgb.g >= 240 or color.rgb.b >= 240:
            continue
        else:
            red, green, blue = color.rgb.r, color.rgb.g, color.rgb.b
            formatted_color = f"#{red:02x}{green:02x}{blue:02x}"
            formatted_picked_colors.append(formatted_color)

    return formatted_picked_colors


def close_screen(the_turtle, the_screen):
    """Closes down both the turtle and screen"""
    the_turtle.bye()
    the_screen.bye()


def drawing(the_turtle, number_of_dots, list_of_colors):
    """Generates the drawing"""
    for dot_count in range(number_of_dots):
        draw_dot(the_turtle, list_of_colors)
        the_turtle.penup()
        the_turtle.forward(50)
        the_turtle.pendown()

        if (dot_count + 1) % 10 == 0:
            next_row(the_turtle)


def draw_dot(paintbrush, list_of_colors):
    """Draws a circle with a randomized color from list"""
    radius = 20
    chosen_color = random.choice(list_of_colors)
    paintbrush.dot(radius, chosen_color)


def next_row(the_turtle):
    the_turtle.penup()
    the_turtle.setheading(90)   # Turn turtle to face upwards
    the_turtle.forward(50)      # Move turtle upwards
    the_turtle.setheading(180)  # Turn turtle to face left
    the_turtle.forward(500)     # Move turtle to the leftmost position
    the_turtle.setheading(0)    # Turn turtle to face right again
    the_turtle.pendown()


def main():
    # Set up variables
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(150)
    screen = turtle.Screen()
    width = 1200
    height = 800
    amount_dots = 100

    # Screen setup
    screen.setup(width, height)
    screen.bgcolor("lightblue")
    screen.title("Turtle Graphics Example")

    # Get the absolute path to the 'image.jpg' file inside 'hirstPainting' folder
    script_dir = os.path.dirname(__file__)
    image_path = os.path.join(script_dir, 'image.jpg')

    # Generate list of colors from image
    list_of_colors = generate_colors_from_image(image_path)

    # Starting position setup
    t.penup()
    t.goto(0, 0)             # Move turtle to the center of the screen
    t.setheading(225)        # Set initial heading to bottom-left direction
    t.forward(250)           # Move turtle to the starting position
    t.setheading(0)          # Set heading to the right direction
    t.pendown()

    # Drawing
    drawing(t, amount_dots, list_of_colors)

    # Exit on click
    screen.exitonclick()


if __name__ == "__main__":
    main()
