from turtle import Screen, Turtle
from player import Player
from scoreboard import Scoreboard
from screen import draw_grass
from cars import Car
import time


class Game:
    """Class to manage the game"""
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    def __init__(self):
        """Initialize the game"""
        self.game_is_on = True
        self.screen = Screen()
        self.screen.setup(Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT)
        self.screen.bgcolor("white")
        self.screen.tracer(0)
        self.screen.title("Crossing Game")
        draw_grass()  # Will draw the upper and lower rectangle of grass

        # Setup Player
        self.player = Player()

        # Setup cars
        self.cars = Car()

        # Setup scoreboard
        self.scoreboard = Scoreboard()

        # Setup keybindings
        self.setup_keybindings()

    def setup_keybindings(self):
        """Set up key bindings"""
        self.screen.onkey(self.player.move_up, "Up")
        self.screen.onkey(self.player.move_down, "Down")
        self.screen.listen()

    def start_new_game(self):
        """Start a new game"""
        self.player.reset_player()
        self.scoreboard.reset_scores()
        self.run()

    def wait_for_restart(self):
        """Pause the game and wait for restart"""
        self.screen.update()
        self.screen.onkey(self.start_new_game, "Return")
        self.screen.mainloop()

    def game_over(self):
        """Ends the game and displays game over message."""
        self.game_is_on = False
        self.scoreboard.game_over()
        self.cars.reset_cars()

    def run(self):
        """Run the game loop"""
        self.game_is_on = True
        while self.game_is_on:
            # Create new cars with certain probability and initiate their movements
            self.cars.create_car()
            self.cars.move_cars()

            # Detect collision with car
            for car in self.cars.all_cars:
                if self.player.distance(car) < 20:
                    self.scoreboard.collide()
                    self.player.reset_player()

            # Check if player reached finish line
            if self.player.ycor() > Game.SCREEN_HEIGHT / 2:
                self.scoreboard.level_up()
                self.cars.increase_movement()
                self.player.reset_player()

            # Check game over condition
            if self.scoreboard.lives < 1:
                self.game_over()

            # Update screen
            self.screen.update()
            time.sleep(0.1)

        self.wait_for_restart()
