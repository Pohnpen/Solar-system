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
DARK_GREY = (64, 64, 64)
LIGHT_GREY = (211, 211, 211)
RED = (255,0,0)

# Load the background image
# Replace 'background_image.jpg' with the path to your image file
background_image = pygame.image.load('data/sprites/stars_1k_tex.jpg')
# Optional: Scale the image to your screen size
background_image = pygame.transform.scale(background_image, window_size)

# Define constants
TIME_FACTOR = 1 / 365
PX_PER_AU = 400
# Draw a circle in the center of the window
CENTER = (window_size[0] // 2, window_size[1] // 2)
LEFT_TOP = (0, 0)
BOTTOM_RIGHT = (1000, 1000)

# TEXT STUFF
font = pygame.font.Font(None, 24)
text_color = WHITE

mercury = Orbit(Vector(CENTER[0],CENTER[1]), distance=0.387*PX_PER_AU, period=88/365)
venus = Orbit(Vector(CENTER[0],CENTER[1]), distance=0.723*PX_PER_AU, period=225/365)
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
    # Draw the background image
    screen.blit(background_image, (0, 0))

    # SUN DISPLAY
    pygame.draw.circle(screen, YELLOW, CENTER, 50)

    # MERCURY DISPLAY
    mercury.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, mercury.center.tuple, mercury.distance, width=1)
    pygame.draw.circle(screen, DARK_GREY, mercury.orbital_position.tuple, 4)
    # Render the text for Mercury
    text_surface = font.render("Mercury", True, text_color)
    text_rect = text_surface.get_rect(center=(mercury.orbital_position + Vector(50,20)).tuple)
    screen.blit(text_surface, text_rect)

    # VENUS DISPLAY
    venus.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, venus.center.tuple, venus.distance, width=1)
    pygame.draw.circle(screen, LIGHT_GREY, venus.orbital_position.tuple, 9)
    # Render the text for Venus
    text_surface = font.render("Venus", True, text_color)
    text_rect = text_surface.get_rect(center=(venus.orbital_position + Vector(50, 20)).tuple)
    screen.blit(text_surface, text_rect)

    # EARTH DISPLAY
    earth.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, earth.center.tuple, earth.distance, width=1)
    pygame.draw.circle(screen, BLUE, earth.orbital_position.tuple, 10)
    # Render the text for Earth
    text_surface = font.render("Earth", True, text_color)
    text_rect = text_surface.get_rect(center=(earth.orbital_position + Vector(50, 20)).tuple)
    screen.blit(text_surface, text_rect)

    # MOON DISPLAY
    moon.move(TIME_FACTOR)
    moon.center = earth.orbital_position
    pygame.draw.circle(screen, WHITE, earth.orbital_position.tuple, 20, width=1)
    pygame.draw.circle(screen, GREY, moon.orbital_position.tuple, 5)
    # Render the text for Moon
    text_surface = font.render("Moon", True, text_color)
    text_rect = text_surface.get_rect(center=(moon.orbital_position + Vector(50, 20)).tuple)
    screen.blit(text_surface, text_rect)

    # MARS DISPLAY
    mars.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, mars.center.tuple, mars.distance, width=1)
    pygame.draw.circle(screen, RED, mars.orbital_position.tuple, 5)
    # Render the text for Mars
    text_surface = font.render("Mars", True, text_color)
    text_rect = text_surface.get_rect(center=(mars.orbital_position + Vector(50, 20)).tuple)
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()
    sleep(0.1)

# Quit Pygame
pygame.quit()
sys.exit()
