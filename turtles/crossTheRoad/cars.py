from turtle import Turtle, Screen
import random

STARTING_X = 300
MOVE_DISTANCE = 10
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
MAX_RANDOM = 10


# Function to generate random colors
def generate_random_color():
    """Generates a random hexadecimal color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()  # Hide the turtle initially to avoid extra turtle for all_cars on screen

    def create_car(self):
        """Creates a new car if random condition is met."""
        global MAX_RANDOM
        if random.randint(1, MAX_RANDOM) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.showturtle()  # Makes each car visible
            new_car.penup()
            new_car.color(generate_random_color())
            new_car.goto(STARTING_X, random.randint(-170, 170))
            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves all cars in the `all_cars` list backward."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_movement(self):
        """Increases the speed of cars and adjusts the random creation rate."""
        self.car_speed += MOVE_INCREMENT
        global MAX_RANDOM
        if MAX_RANDOM > 2:
            MAX_RANDOM -= 2
        else:
            MAX_RANDOM = 2

    def reset_cars(self):
        """Resets speed of cars"""
        global MAX_RANDOM
        self.car_speed = STARTING_MOVE_DISTANCE
        MAX_RANDOM = 10