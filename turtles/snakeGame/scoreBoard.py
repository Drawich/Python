from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
COLOR = "white"


class ScoreBoard(Turtle):
    """A class to manage the scoreboard in the game"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setup_scoreboard()

    def setup_scoreboard(self):
        """Set up the initial scoreboard stating score = 0"""
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard with the current score"""
        self.clear()
        self.color(COLOR)
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase and displays score with +1 when snake collides with food"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays game over message centered on the screen"""
        self.goto(0,0)
        self.color(COLOR)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

