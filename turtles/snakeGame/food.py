from turtle import Turtle
import random


class Food(Turtle):
    """A class to manage the food in the game"""

    COLORS = [
        '#ff0000',  # Red
        '#ff8c00',  # Dark Orange
        '#ffd700',  # Gold
        '#00ff00',  # Lime
        '#00ffff',  # Cyan
        '#1e90ff',  # Dodger Blue
        '#8a2be2',  # Blue Violet
        '#ff00ff',  # Magenta
        '#ff1493',  # Deep Pink
        '#ff4500',  # Orange Red
        '#ff7f50',  # Coral
        '#ffdab9',  # Peach Puff
        '#32cd32',  # Lime Green
        '#00ff7f',  # Spring Green
        '#00ced1',  # Dark Turquoise
        '#9932cc',  # Dark Orchid
        '#ff69b4',  # Hot Pink
        '#ff6347',  # Tomato
        '#da70d6',  # Orchid
    ]

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.randomize_color()
        self.speed("fastest")

    def randomize_color(self):
        """Choose a random color each time the food is regenerated"""
        self.color(random.choice(self.COLORS))

    def refresh(self):
        """Refresh the food in a new color and location when the colliding with the snake"""
        self.randomize_color()
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)