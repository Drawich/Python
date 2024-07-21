from drawWithTurtle import DrawWithTurtle

if __name__ == "__main__":
    """
    Main script to start the drawing simulation.

    Usage:
        Run this script to initialize and start the drawing simulation.
        The drawing simulation allows users to control a turtle using keyboard keys 'w', 's', 'a', 'd' for movement
        and 'c' to clear the screen and reset the turtle's position.
    """
    drawer = DrawWithTurtle()
    drawer.start()
