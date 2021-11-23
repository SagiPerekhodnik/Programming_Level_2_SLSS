# Relaxing Snowscape
# Author: Ubial


import random
import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOUR = BLACK

SCREEN_WIDTH  = 1024
SCREEN_HEIGHT = 768
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Relaxing Snowscape"


class Snowflake:
    """Snowflake on the screen
    Attributes:
        size: radius of snowflake in px
        coords: {x: int, y:int}
        y_vel: falling velocity in px/sec
        colour: (r, g, b)
    """
    def __init__(self):
        self.size = 2
        # randomly place the snow on the screen
        self.coords = [
            random.randrange(0, SCREEN_WIDTH),
            random.randrange(0, SCREEN_HEIGHT)
        ]
        self.y_vel = 4
        self.colour = WHITE

    def update(self):
        """Update the location of the snow"""
        # Changes the y portion of the coords
        self.coords[1] += self.y_vel

        # Reset position of snowflake if it reaches bottom
        if self.coords[1] > SCREEN_HEIGHT:
            self.coords = [
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(-25, 0)
            ]


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_snowflakes = 250
    snowflakes = []
    # Create snowflakes in foreground
    for i in range(num_snowflakes-150):
        close_snowflake = Snowflake()
        close_snowflake.size = random.choice([4, 5, 6])
        close_snowflake.y_vel = random.choice([1, 2])
        snowflakes.append(close_snowflake)
    for i in range(num_snowflakes-100):
        close_snowflake = Snowflake()
        close_snowflake.size = random.choice([3, 4])
        close_snowflake.y_vel = random.choice([2, 3])
        snowflakes.append(close_snowflake)
    # Create snowflakes in background
    for i in range(num_snowflakes):
        snowflakes.append(Snowflake())


    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        for snow in snowflakes:
            snow.update()

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        pygame.draw.rect(screen, (150, 150, 255), [0, 500, SCREEN_WIDTH, 300])

        # draw the snowflakes
        for snow in snowflakes:
            pygame.draw.circle(screen, snow.colour, snow.coords, snow.size)

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()