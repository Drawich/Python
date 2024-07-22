from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Constants
MOVE_INTERVAL = 0.05
WINNING_SCORE = 5


class Game:
    """Class to manage the game"""
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    WALL_COLLISION_THRESHOLD = 280

    def __init__(self):
        """Initialize the game"""
        self.screen = Screen()
        self.screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Ping Pong")
        self.screen.tracer(0)

        self.ball = Ball()
        self.scoreboard = Scoreboard()
        self.left_paddle = Paddle(-350)
        self.right_paddle = Paddle(350)

        self.setup_keybindings()

    def setup_keybindings(self):
        """Set up key bindings"""
        self.screen.onkey(self.left_paddle.up, "w")
        self.screen.onkey(self.left_paddle.down, "s")
        self.screen.onkey(self.right_paddle.up, "Up")
        self.screen.onkey(self.right_paddle.down, "Down")

        self.screen.listen()

    def start_new_game(self):
        """Start a new game"""
        self.ball.reset()
        self.scoreboard.reset_scores()
        self.run()

    def check_collisions(self):
        self.check_wall_collisions()
        self.check_paddle_collisions()
        self.check_score()

    def check_wall_collisions(self):
        if abs(self.ball.ball.ycor()) > self.WALL_COLLISION_THRESHOLD:
            self.ball.bounce_y()

    def check_paddle_collisions(self):
        if (self.ball.ball.distance(self.left_paddle.paddle) < 50 and self.ball.ball.xcor() < -320) or \
                (self.ball.ball.distance(self.right_paddle.paddle) < 50 and self.ball.ball.xcor() > 320):
            self.ball.bounce_x()

    def check_score(self):
        if self.ball.ball.xcor() < -400:
            self.handle_score("right")
        elif self.ball.ball.xcor() > 400:
            self.handle_score("left")

    def handle_score(self, side):
        if side == "left":
            self.scoreboard.l_point()
        elif side == "right":
            self.scoreboard.r_point()

        if self.scoreboard.l_score >= WINNING_SCORE or self.scoreboard.r_score >= WINNING_SCORE:
            if self.scoreboard.l_score >= WINNING_SCORE:
                winner = "Left"
            else:
                winner = "Right"

            self.scoreboard.show_winner(winner)
            self.screen.update()
            self.pause_until_new_game()
        else:
            self.ball.reset()

    def pause_until_new_game(self):
        self.screen.update()
        self.screen.listen()
        self.screen.onkey(self.start_new_game, "Return")
        self.screen.mainloop()

    def run(self):
        """Run the game loop"""
        game_is_on = True
        while game_is_on:
            self.screen.update()
            self.ball.move()
            self.check_collisions()
            time.sleep(MOVE_INTERVAL)

        self.screen.mainloop()
