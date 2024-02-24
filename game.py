# Pygame Documentation: https://www.pygame.org/docs/

import pygame
import sys
from lib.orbit import Orbit
from lib.vector import Vector
from time import sleep


PX_PER_AU = 400
TIME_FACTOR = 1/365


# Initialize Pygame
pygame.init()

# Set up the display
# window_size = (1000, 1000)  # Width and height of the window
window_size = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Solar System Viewer")
imp = pygame.transform.scale(pygame.image.load("data/sprites/stars_1k_tex.jpg"), window_size)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (225, 225, 0)
BLUE = (0, 0, 225)
GREY = (128, 128, 128)
DARK_GREY = (64, 64, 64)
LIGTH_GREY = (99, 99 ,99)
RED = (225, 0, 0)
LIGTH_BROWN = (214, 181, 117)
BROWN = (94, 62, 23)


# Define constants
# TODO: PX PER AU
# Draw a circle in the center of the window
CENTER = (window_size[0] // 2, window_size[1] // 2)

LEFT_TOP = (0, 0)
BOTTOM_RIGHT = (1000, 1000)

mercury = Orbit(Vector(CENTER[0],CENTER[1]), distance=0.39*PX_PER_AU, period=0.241)
venus = Orbit(Vector(CENTER[0],CENTER[1]), distance=0.72*PX_PER_AU, period=0.615)
earth = Orbit(Vector(CENTER[0],CENTER[1]), distance=1.0*PX_PER_AU, period=1.0)
moon = Orbit(earth.orbital_position(), distance=20, period=27/365)
mars = Orbit(Vector(CENTER[0],CENTER[1]), distance=1.52*PX_PER_AU, period=1.881)
phobos = Orbit(mars.orbital_position(), distance=20, period=1/365)
deimos = Orbit(mars.orbital_position(), distance=30, period=2/365)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(BLACK)
    screen.blit(imp, (0, 0))


    # Static Sun
    pygame.draw.circle(screen, YELLOW, CENTER, 50)


    # Mercury Movement
    mercury.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, CENTER, mercury.distance, width=1)
    pygame.draw.circle(screen, DARK_GREY, mercury.orbital_position().tuple(), 2)

    # Venus Movement
    venus.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, CENTER, venus.distance, width=1)
    pygame.draw.circle(screen, LIGTH_GREY, venus.orbital_position().tuple(), 9)

    # Earth Movement
    earth.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, CENTER, earth.distance, width=1)
    pygame.draw.circle(screen, BLUE, earth.orbital_position().tuple(), 10)

    # Moon Movement
    moon.center = earth.orbital_position()
    moon.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, earth.orbital_position().tuple(), moon.distance, width=1)
    pygame.draw.circle(screen, GREY, moon.orbital_position().tuple(), 2)

    # Mars Movement
    mars.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, CENTER, mars.distance, width=1)
    pygame.draw.circle(screen, RED, mars.orbital_position().tuple(), 5)

    # Phobos Movement
    phobos.center = mars.orbital_position()
    phobos.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, mars.orbital_position().tuple(), phobos.distance, width=1)
    pygame.draw.circle(screen, LIGTH_BROWN, phobos.orbital_position().tuple(), 4)

    # Deimos Movement
    deimos.center = mars.orbital_position()
    deimos.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, mars.orbital_position().tuple(), deimos.distance, width=1)
    pygame.draw.circle(screen, BROWN, deimos.orbital_position().tuple(), 4)

    # TODO: Create an orbit called "Earth" object at the CENTER with a distance of 1.0 AU and a period of 1.0 EY
    # TODO: move the earth every frame by 1/365
    # TODO: draw the earth circle at that orbital_position

    # Update the display
    pygame.display.flip()

    sleep(0.1)

# Quit Pygame
pygame.quit()
sys.exit()
