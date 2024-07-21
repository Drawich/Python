from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVE_INTERVAL = 0.1
COLLISION_DISTANCE = 15
WALL_COLLISION_THRESHOLD = 295
TAIL_COLLISION_DISTANCE = 10

# Setup screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create snake, food, and scoreboard instances
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Setup initial scoreboard
scoreboard.setup_scoreboard()

# Set keyboard bindings to control movements of snake
key_bindings = {
    "Up": snake.up,
    "Down": snake.down,
    "Left": snake.left,
    "Right": snake.right
}
for key, action in key_bindings.items():
    screen.onkey(action, key)

screen.listen()


# Game loop function
def run_game():
    continue_game = True
    while continue_game:
        screen.update()
        time.sleep(MOVE_INTERVAL)

        snake.move()  # Makes the snake move forward

        # Detect collision with food
        if snake.head.distance(food) < COLLISION_DISTANCE:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        # Detect collision with wall
        if abs(snake.head.xcor()) > WALL_COLLISION_THRESHOLD or abs(snake.head.ycor()) > WALL_COLLISION_THRESHOLD:
            scoreboard.game_over()
            continue_game = False

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < TAIL_COLLISION_DISTANCE:
                scoreboard.game_over()
                continue_game = False


# Run the game
run_game()

# Exit the game cleanly
screen.update()
screen.exitonclick()
