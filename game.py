import pygame # Pygame Documentation: https://www.pygame.org/docs/
import sys

from lib.constants import *
from utils import change_simulation_speed


from lib.vector import Vector
from lib.body import Planetoid, Orbit

from time import sleep

from lib.vector import Vector

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

# Simulation timing
clock = pygame.time.Clock()
running = True; dt = 0; earth_hours_passed = 0.0
current_simulation_speed = SIMULATION_SPEED_MODES[3]

# Main loop
while running:

    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # KEY HANDLING
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    # KEY HANDLING
    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False
    elif keys[pygame.K_KP_PLUS]:
        current_simulation_speed = change_simulation_speed(1, current_simulation_speed)
        print("+")
    elif keys[pygame.K_KP_MINUS]:
        current_simulation_speed = change_simulation_speed(-1, current_simulation_speed)
        print("-")
    elif keys[pygame.K_SPACE]:
        current_simulation_speed = change_simulation_speed(0, current_simulation_speed)
    elif keys[pygame.K_w]:
        pass
    elif keys[pygame.K_a]:
        pass
    elif keys[pygame.K_s]:
        pass
    elif keys[pygame.K_d]:
        pass

    # Fill the background
    screen.fill(BLACK)
    # Draw the background image
    screen.blit(background_image, (0, 0))

    text_surface = font.render(f"Solar System Viewer", True, text_color)
    text_rect = text_surface.get_rect(center=(CENTER[0], 50))
    screen.blit(text_surface, text_rect)

    text_surface = font.render(f"Earth Years: {earth_hours_passed/EARTH_HOURS_PER_EARTH_YEAR:.5f}", True, text_color)
    text_rect = text_surface.get_rect(center=(100, 100))
    screen.blit(text_surface, text_rect)

    #
    # Move and Draw the solar System
    #
    for object in solar_system:
        object.move(dt * current_simulation_speed / EARTH_HOURS_PER_EARTH_YEAR)
        object.draw(screen)

    # Update the display
    pygame.display.flip()

    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000 # limits FPS to 60
    earth_hours_passed += dt * current_simulation_speed

# Quit Pygame
pygame.quit()
sys.exit()
