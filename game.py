# Pygame Documentation: https://www.pygame.org/docs/

import pygame
import sys

from time import sleep

from lib.orbit import Orbit
from lib.vector import Vector

# Initialize Pygame
pygame.init()
infoObject = pygame.display.Info()
screen_width, screen_height = infoObject.current_w, infoObject.current_h
window_size = (screen_width, screen_height)  # Width and height of the window
# Set up the display in fullscreen mode
screen = pygame.display.set_mode((screen_width, screen_height))#, pygame.FULLSCREEN)
pygame.display.set_caption("Solar System Viewer")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (225, 225, 0)
BLUE = (0, 0, 225)
GREY = (128, 128, 128)
RED = (255,0,0)


# Define constants
TIME_FACTOR = 1 / 365
PX_PER_AU = 400
# Draw a circle in the center of the window
CENTER = (window_size[0] // 2, window_size[1] // 2)
LEFT_TOP = (0, 0)
BOTTOM_RIGHT = (1000, 1000)

# TODO: Create an orbit called "Earth" object at the CENTER with a distance of 1.0 AU and a period of 1.0 EY
earth = Orbit(Vector(CENTER[0],CENTER[1]), distance=1.0*PX_PER_AU, period=1.0)
moon = Orbit(earth.orbital_position, distance=20, period=27/365)
mars = Orbit(Vector(CENTER[0],CENTER[1]), distance=1.524*PX_PER_AU, period=1.88)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(BLACK)

    # SUN DISPLAY
    pygame.draw.circle(screen, YELLOW, CENTER, 50)

    # EARTH DISPLAY
    earth.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, earth.center.tuple, earth.distance, width=1)
    pygame.draw.circle(screen, BLUE, earth.orbital_position.tuple, 10)

    # MOON DISPLAY
    moon.move(TIME_FACTOR)
    moon.center = earth.orbital_position
    pygame.draw.circle(screen, WHITE, earth.orbital_position.tuple, 20, width=1)
    pygame.draw.circle(screen, GREY, moon.orbital_position.tuple, 5)

    # MARS DISPLAY
    mars.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, mars.center.tuple, mars.distance, width=1)
    pygame.draw.circle(screen, RED, mars.orbital_position.tuple, 5)

    # Update the display
    pygame.display.flip()
    sleep(0.1)

# Quit Pygame
pygame.quit()
sys.exit()
