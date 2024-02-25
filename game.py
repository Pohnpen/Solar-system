# Pygame Documentation: https://www.pygame.org/docs/

import pygame
import sys
from time import sleep

from lib.orbit import Orbit
from lib.vector import Vector
from lib.body import Planetoid
from lib.constants import *

# Initialize Pygame
pygame.init()

# Set up the display
window_size = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Solar System Viewer")
background_image = pygame.transform.scale(pygame.image.load("data/sprites/stars_1k_tex.jpg"), window_size)

# TEXT initialization
font = pygame.font.Font(None, 24)
text_color = WHITE

# Define constants for coordinates
CENTER = (window_size[0] // 2, window_size[1] // 2)
LEFT_TOP = (0, 0)
BOTTOM_RIGHT = (window_size[0], window_size[1])

# Solar System bodies and orbits
# mercury = Orbit(Vector(CENTER[0],CENTER[1]), distance=0.39*PX_PER_AU, period=0.241)
mercury = Planetoid(3, 10, "Mercury", Orbit(Vector(CENTER[0],CENTER[1]), distance=0.39*PX_PER_AU, period=0.241))

venus = Orbit(Vector(CENTER[0],CENTER[1]), distance=0.72*PX_PER_AU, period=0.615)
earth = Orbit(Vector(CENTER[0],CENTER[1]), distance=1.0*PX_PER_AU, period=1.0)
moon = Orbit(earth.orbital_position(), distance=20, period=27/365)
mars = Orbit(Vector(CENTER[0],CENTER[1]), distance=1.52*PX_PER_AU, period=1.881)
phobos = Orbit(mars.orbital_position(), distance=20, period=0.32/365)
deimos = Orbit(mars.orbital_position(), distance=30, period=1.26/365)

solar_system = []

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # KEY HANDLING
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    # Fill the background
    screen.fill(BLACK)
    screen.blit(background_image, (0, 0))

    text_surface = font.render(f"Solar System Viewer", True, text_color)
    text_rect = text_surface.get_rect(center=(CENTER[0], 50))
    screen.blit(text_surface, text_rect)

    #
    # Move and Draw the solar System
    #

    # Static Sun
    pygame.draw.circle(screen, YELLOW, CENTER, 50)

    # Mercury Movement
    mercury.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, CENTER, mercury.orbit.distance, width=1)
    pygame.draw.circle(screen, LIGTH_BROWN, mercury.position.tuple(), 3)
    text_surface = font.render(f"{mercury.name}", True, text_color)
    text_rect = text_surface.get_rect( center= (mercury.position + Vector(0, 20)).tuple() )
    screen.blit(text_surface, text_rect)

    # Venus Movement
    venus.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, CENTER, venus.distance, width=1)
    pygame.draw.circle(screen, LIGTH_GREY, venus.orbital_position().tuple(), 9)
    text_surface = font.render(f"Venus", True, text_color)
    text_rect = text_surface.get_rect( center= (venus.orbital_position() + Vector(0, 20)).tuple() )
    screen.blit(text_surface, text_rect)

    # Earth Movement
    earth.move(TIME_FACTOR)
    #earth.draw()
    pygame.draw.circle(screen, WHITE, CENTER, earth.distance, width=1)
    pygame.draw.circle(screen, BLUE, earth.orbital_position().tuple(), 10)
    text_surface = font.render(f"Earth", True, text_color)
    text_rect = text_surface.get_rect( center= (earth.orbital_position() + Vector(0, 40)).tuple() )
    screen.blit(text_surface, text_rect)

    # Moon Movement
    moon.center = earth.orbital_position()
    moon.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, earth.orbital_position().tuple(), moon.distance, width=1)
    pygame.draw.circle(screen, GREY, moon.orbital_position().tuple(), 2)
    text_surface = font.render(f"Moon", True, text_color)
    text_rect = text_surface.get_rect( center= (moon.orbital_position() + Vector(0, 20)).tuple() )
    screen.blit(text_surface, text_rect)

    # Mars Movement
    mars.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, CENTER, mars.distance, width=1)
    pygame.draw.circle(screen, RED, mars.orbital_position().tuple(), 5)
    text_surface = font.render(f"Mars", True, text_color)
    text_rect = text_surface.get_rect( center= (mars.orbital_position() + Vector(0, 50)).tuple() )
    screen.blit(text_surface, text_rect)

    # Phobos Movement
    phobos.center = mars.orbital_position()
    phobos.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, mars.orbital_position().tuple(), phobos.distance, width=1)
    pygame.draw.circle(screen, LIGTH_BROWN, phobos.orbital_position().tuple(), 2)
    text_surface = font.render(f"Phobos", True, text_color)
    text_rect = text_surface.get_rect( center= (phobos.orbital_position() + Vector(0, 20)).tuple() )
    screen.blit(text_surface, text_rect)

    # Deimos Movement
    deimos.center = mars.orbital_position()
    deimos.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, mars.orbital_position().tuple(), deimos.distance, width=1)
    pygame.draw.circle(screen, BROWN, deimos.orbital_position().tuple(), 2)
    text_surface = font.render(f"Deimos", True, text_color)
    text_rect = text_surface.get_rect( center= (deimos.orbital_position() + Vector(0, 30)).tuple() )
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    sleep(0.1)

# Quit Pygame
pygame.quit()
sys.exit()
