from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
COLOR = "white"
SCOREBOARD_POSITION = (0, 280)


class ScoreBoard(Turtle):
    """A class to manage the scoreboard in the game"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.load_highscore()
        self.setup_scoreboard()

    def setup_scoreboard(self):
        """Set up the initial scoreboard stating score = 0"""
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard with the current score"""
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase and displays score with +1 when snake collides with food"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays game over message centered on the screen"""
        self.goto(0,0)
        self.color(COLOR)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.score = 0
        self.update_scoreboard()

    def load_highscore(self):
        """Load highscore from a file if it exists"""
        highscore_file = "highscore.txt"
        if os.path.exists(highscore_file):
            with open(highscore_file, "r") as file:
                try:
                    return int(file.read().strip())
                except ValueError:
                    return 0
        else:
            return 0

    def save_highscore(self):
        """Save highscore to a file"""
        highscore_file = "highscore.txt"
        with open(highscore_file, "w") as file:
            file.write(str(self.highscore))
