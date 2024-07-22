from turtle import Turtle


class Scoreboard(Turtle):
    FONT_STYLE_SCORE = ("Courier", 80, "normal")
    FONT_STYLE_MESSAGE = ("Courier", 20, "normal")
    SCORE_POSITIONS = [(100, 200), (-100, 200)]

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Displays scoreboard with current score."""
        for position, score in zip(self.SCORE_POSITIONS, [self.r_score, self.l_score]):
            self.goto(position)
            self.write(score, align="center", font=self.FONT_STYLE_SCORE)

    def l_point(self):
        """Adds a point to the left side."""
        self.l_score += 1
        self.clear_scoreboard()
        self.update_scoreboard()

    def r_point(self):
        """Adds a point to the right side."""
        self.r_score += 1
        self.clear_scoreboard()
        self.update_scoreboard()

    def reset_scores(self):
        """Resets scores at the start of a new game."""
        self.l_score = 0
        self.r_score = 0
        self.clear_scoreboard()
        self.update_scoreboard()

    def clear_scoreboard(self):
        """Clears the scoreboard."""
        self.clear()

    def show_winner(self, winner):
        """Displays who the won"""
        self.goto(0, 0)
        self.color("white")
        self.write(f"Player {winner} wins!\nPress 'enter' to start new game..",
                   align="center", font=Scoreboard.FONT_STYLE_MESSAGE)
