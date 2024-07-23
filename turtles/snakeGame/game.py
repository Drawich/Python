from food import Food
from scoreBoard import ScoreBoard
from turtle import Screen
from snake import Snake
import time


class Game:
    """Class to manage the game"""
    # Constants
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    MOVE_INTERVAL = 0.1
    COLLISION_DISTANCE = 15
    WALL_COLLISION_THRESHOLD = 295
    TAIL_COLLISION_DISTANCE = 10

    def __init__(self):
        """Initialize the game"""
        self.screen = Screen()
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = ScoreBoard()
        self.setup_screen()
        self.setup_keybindings()

    def setup_screen(self):
        self.screen.setup(width=Game.SCREEN_WIDTH, height=Game.SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        self.scoreboard.setup_scoreboard()

    def setup_keybindings(self):
        """Set up key bindings"""
        key_bindings = {
            "Up": self.snake.up,
            "Down": self.snake.down,
            "Left": self.snake.left,
            "Right": self.snake.right,
            "Return": self.start_new_game  # Corrected: pass function reference without ()
        }
        for key, action in key_bindings.items():
            self.screen.onkey(action, key)

        self.screen.listen()

    def start_new_game(self):
        """Start a new game"""
        self.snake.reset_snake()
        self.food.refresh()
        self.scoreboard.reset_game()
        self.run()

    def run(self):
        """Starts and runs the game"""
        continue_game = True
        while continue_game:
            self.screen.update()
            time.sleep(Game.MOVE_INTERVAL)

            self.snake.move()  # Makes the snake move forward

            # Detect collision with food
            if self.snake.head.distance(self.food) < Game.COLLISION_DISTANCE:
                self.food.refresh()
                self.scoreboard.increase_score()
                self.snake.extend()

            # Detect collision with wall
            if (abs(self.snake.head.xcor()) > Game.WALL_COLLISION_THRESHOLD
                    or abs(self.snake.head.ycor()) > Game.WALL_COLLISION_THRESHOLD):
                self.scoreboard.reset_game()
                self.scoreboard.game_over()
                continue_game = False

            # Detect collision with tail
            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < Game.TAIL_COLLISION_DISTANCE:
                    self.scoreboard.game_over()
                    self.scoreboard.reset_game()

    def main(self):
        # Run the game
        self.run()

        # Exit the game cleanly
        self.screen.update()
        self.screen.mainloop()
