# Pygame Documentation: https://www.pygame.org/docs/

import pygame
import sys
from lib.orbit import Orbit
from lib.vector import Vector

TIME_FACTOR = 1/(365)

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (1000, 1000)  # Width and height of the window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Solar System Viewer")
# earth = pygame.draw.move.circle(screen, BLUE, (217,217), 10)
# orbit = pygame.draw.circle(screen, WHITE, CENTER, 400, width=1)
# move = pygame.display.info(earth, orbit)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (225, 225, 0)
BLUE = (0, 0, 225)
GREY = (128, 128, 128)


# Define constants
# Draw a circle in the center of the window
CENTER = (window_size[0] // 2, window_size[1] // 2)
LEFT_TOP = (0, 0)
BOTTOM_RIGHT = (1000, 1000)

# EARTH = pygame.draw.circle(screen, BLUE, (225,225), 10)
earth = Orbit(Vector(0,0), distance=1.0, period=1.0)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(BLACK)

    pygame.draw.circle(screen, YELLOW, CENTER, 50)
    pygame.draw.circle(screen, BLUE, (217,217), 10)
    pygame.draw.circle(screen, GREY, (850, 850), 5)
    pygame.draw.circle(screen, WHITE, CENTER, 400, width=1)





    # TODO: Create an orbit called "Earth" object at the CENTER with a distance of 1.0 AU and a period of 1.0 EY
    # TODO: move the earth every frame by 1/365
    # TODO: draw the earth circle at that orbital_position

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
