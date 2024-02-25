# Pygame Documentation: https://www.pygame.org/docs/

import pygame
import sys
from time import sleep

from lib.constants import *
from lib.vector import Vector
from lib.body import Planetoid, Orbit

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
sun = Planetoid(100, 333, "Sun", YELLOW, Orbit(Vector(CENTER[0],CENTER[1]),0,0))
mercury = Planetoid(3, 0.055, "Mercury", DARK_GREY, Orbit(Vector(CENTER[0],CENTER[1]), distance=0.39*PX_PER_AU, period=0.241))
venus = Planetoid(9, 0.815, "Venus", LIGTH_GREY, Orbit(Vector(CENTER[0],CENTER[1]), distance=0.72*PX_PER_AU, period=0.615))
earth = Planetoid(10, 1, "Earth", BLUE, Orbit(Vector(CENTER[0],CENTER[1]), distance=1.0*PX_PER_AU, period=1.0))
moon = Planetoid(2, 0.0012, "Moon", GREY, Orbit(earth, distance=20, period=27/365))
mars = Planetoid(4, 0.107, "Mars", RED, Orbit(Vector(CENTER[0],CENTER[1]), distance=1.52*PX_PER_AU, period=1.881))
phobos = Planetoid(2, 0.0005, "Phobos", BROWN, Orbit(mars, distance=20, period=0.32/365))
deimos = Planetoid(2, 0.00025, "Deimos", LIGTH_BROWN, Orbit(mars, distance=30, period=1.26/365))

solar_system = [sun,mercury,venus,earth,moon,mars,phobos,deimos]

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
    for object in solar_system:
        object.move(TIME_FACTOR)
        object.draw(screen)

    """
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
    pygame.draw.circle(screen, WHITE, CENTER, venus.orbit.distance, width=1)
    pygame.draw.circle(screen, LIGTH_GREY, venus.position.tuple(), 9)
    text_surface = font.render(f"{venus.name}", True, text_color)
    text_rect = text_surface.get_rect( center= (venus.position + Vector(0, 20)).tuple() )
    screen.blit(text_surface, text_rect)

    # Earth Movement
    earth.move(TIME_FACTOR)
    #earth.draw()
    pygame.draw.circle(screen, WHITE, CENTER, earth.orbit.distance, width=1)
    pygame.draw.circle(screen, BLUE, earth.position.tuple(), 10)
    text_surface = font.render(f"{earth.name}", True, text_color)
    text_rect = text_surface.get_rect( center= (earth.position + Vector(0, 40)).tuple() )
    screen.blit(text_surface, text_rect)

    # Moon Movement
    moon.orbit.center = earth.position
    moon.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, earth.position.tuple(), moon.orbit.distance, width=1)
    pygame.draw.circle(screen, GREY, moon.position.tuple(), 2)
    text_surface = font.render(f"{moon.name}", True, text_color)
    text_rect = text_surface.get_rect( center= (moon.position + Vector(0, 20)).tuple() )
    screen.blit(text_surface, text_rect)

    # Mars Movement
    mars.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, CENTER, mars.orbit.distance, width=1)
    pygame.draw.circle(screen, RED, mars.position.tuple(), 5)
    text_surface = font.render(f"{mars.name}", True, text_color)
    text_rect = text_surface.get_rect( center= (mars.position + Vector(0, 50)).tuple() )
    screen.blit(text_surface, text_rect)

    # Phobos Movement
    phobos.orbit.center = mars.position
    phobos.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, mars.position.tuple(), phobos.orbit.distance, width=1)
    pygame.draw.circle(screen, LIGTH_BROWN, phobos.position.tuple(), 2)
    text_surface = font.render(f"{phobos.name}", True, text_color)
    text_rect = text_surface.get_rect( center= (phobos.position + Vector(0, 20)).tuple() )
    screen.blit(text_surface, text_rect)

    # Deimos Movement
    deimos.orbit.center = mars.position
    deimos.move(TIME_FACTOR)
    pygame.draw.circle(screen, WHITE, mars.position.tuple(), deimos.orbit.distance, width=1)
    pygame.draw.circle(screen, BROWN, deimos.position.tuple(), 2)
    text_surface = font.render(f"{deimos.name}", True, text_color)
    text_rect = text_surface.get_rect( center= (deimos.position + Vector(0, 30)).tuple() )
    screen.blit(text_surface, text_rect)

    """

    # Update the display
    pygame.display.flip()

    sleep(0.1)

# Quit Pygame
pygame.quit()
sys.exit()
