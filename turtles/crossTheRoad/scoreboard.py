from turtle import Turtle

POSITION_LEVEL = (-250, 270)
POSITION_LIVES = (245, 270)
FONT = ("Courier", 16, "normal")
FONT_GAME_OVER = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    """
    A class to manage and display the scoreboard in a Turtle graphics application.

    Attributes:
        level (int): Current level of the game.
        lives (int): Remaining lives of the player.
    """

    def __init__(self):
        """Initializes the scoreboard with default values and sets up Turtle properties."""
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.lives = 5
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the previous text and updates the scoreboard with current level and lives."""
        self.clear()
        self.goto(POSITION_LEVEL)
        self.write(f"Level {self.level}", align="center", font=FONT)
        self.goto(POSITION_LIVES)
        self.write(f"Lives {self.lives}", align="center", font=FONT)

    def reset_scores(self):
        self.level = 1
        self.lives = 5
        self.update_scoreboard()

    def level_up(self):
        """Increases the level by 1 and updates the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def collide(self):
        """Decreases the number of lives by 1 and updates the scoreboard."""
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        """Displays a 'GAME OVER' message in the center of the screen."""
        self.goto(0, 0)
        self.hideturtle()
        self.write("GAME OVER", align="center", font=FONT_GAME_OVER)
        self.goto(0, -30)
        self.write("Press 'enter' to start a new game...", align="center", font=FONT)

