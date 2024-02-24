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
RED = (255, 0, 0)
LIGHT_BROWN = (214, 181, 117)
BROWN = (94, 62, 23)

# Load the background image
background_image = pygame.image.load('data/sprites/stars_1k_tex.jpg')
# Scale the image to your screen size
background_image = pygame.transform.scale(background_image, window_size)

# Define constants
SIMULATION_SPEED = 24
HOURS_PER_SIMULATION_SEC = SIMULATION_SPEED/(365*24)
PX_PER_AU = 400

# Coordinate Constants
CENTER = (window_size[0] // 2, window_size[1] // 2)
LEFT_TOP = (0, 0)
BOTTOM_RIGHT = (1000, 1000)

# TEXT initialization
font = pygame.font.Font(None, 24)
text_color = WHITE

mercury = Orbit(Vector(CENTER[0],CENTER[1]), distance=0.387*PX_PER_AU, period=88/365)
venus = Orbit(Vector(CENTER[0],CENTER[1]), distance=0.723*PX_PER_AU, period=225/365)
earth = Orbit(Vector(CENTER[0],CENTER[1]), distance=1.0*PX_PER_AU, period=1.0)
moon = Orbit(earth.orbital_position, distance=20, period=27/365)
mars = Orbit(Vector(CENTER[0],CENTER[1]), distance=1.524*PX_PER_AU, period=1.88)
phobos = Orbit(mars.orbital_position, distance=20, period=0.32/365)
deimos = Orbit(mars.orbital_position, distance=30, period=1.26/365)

# Simulation timing
clock = pygame.time.Clock()
running = True; paused = False; dt = 0; earth_years_passed = 0.0
delta_time = lambda: dt*HOURS_PER_SIMULATION_SEC

def change_simulation_speed(mode, current=SIMULATION_SPEED):
    MODES = [0, 24, 7*24, 30*24, 365*24]
    if mode == 0:
        return 0
    new = MODES.index(current) + mode
    if new in range(len(MODES)):
        return MODES[new]
    return current


# Main loop
while running:

    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # KEY HANDLING
    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False
    elif keys[pygame.K_KP_PLUS]:
        SIMULATION_SPEED = change_simulation_speed(1)
        print("+")
    elif keys[pygame.K_KP_MINUS]:
        SIMULATION_SPEED = change_simulation_speed(-1)
        print("-")
    elif keys[pygame.K_SPACE]:
        SIMULATION_SPEED = change_simulation_speed(0)
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
    screen.blit(background_image, LEFT_TOP)

    text_surface = font.render(f"Earth Years: {earth_years_passed:.3f}", True, text_color)
    text_rect = text_surface.get_rect(center=(100,100))
    screen.blit(text_surface, text_rect)

    # SUN DISPLAY
    pygame.draw.circle(screen, YELLOW, CENTER, 50)

    # MERCURY DISPLAY
    mercury.move(delta_time())
    pygame.draw.circle(screen, WHITE, mercury.center.tuple, mercury.distance, width=1)
    pygame.draw.circle(screen, DARK_GREY, mercury.orbital_position.tuple, 4)
    # Render the text for Mercury
    text_surface = font.render("Mercury", True, text_color)
    text_rect = text_surface.get_rect(center=(mercury.orbital_position + Vector(50,20)).tuple)
    screen.blit(text_surface, text_rect)

    # VENUS DISPLAY
    venus.move(delta_time())
    pygame.draw.circle(screen, WHITE, venus.center.tuple, venus.distance, width=1)
    pygame.draw.circle(screen, LIGHT_GREY, venus.orbital_position.tuple, 9)
    # Render the text for Venus
    text_surface = font.render("Venus", True, text_color)
    text_rect = text_surface.get_rect(center=(venus.orbital_position + Vector(50, 20)).tuple)
    screen.blit(text_surface, text_rect)

    # EARTH DISPLAY
    earth.move(delta_time())
    pygame.draw.circle(screen, WHITE, earth.center.tuple, earth.distance, width=1)
    pygame.draw.circle(screen, BLUE, earth.orbital_position.tuple, 10)
    # Render the text for Earth
    text_surface = font.render("Earth", True, text_color)
    text_rect = text_surface.get_rect(center=(earth.orbital_position + Vector(50, 20)).tuple)
    screen.blit(text_surface, text_rect)

    # MOON DISPLAY
    moon.move(delta_time())
    moon.center = earth.orbital_position
    pygame.draw.circle(screen, WHITE, earth.orbital_position.tuple, 20, width=1)
    pygame.draw.circle(screen, GREY, moon.orbital_position.tuple, 5)
    # Render the text for Moon
    text_surface = font.render("Moon", True, text_color)
    text_rect = text_surface.get_rect(center=(moon.orbital_position + Vector(50, 20)).tuple)
    screen.blit(text_surface, text_rect)

    # MARS DISPLAY
    mars.move(delta_time())
    pygame.draw.circle(screen, WHITE, mars.center.tuple, mars.distance, width=1)
    pygame.draw.circle(screen, RED, mars.orbital_position.tuple, 5)
    # Render the text for Mars
    text_surface = font.render("Mars", True, text_color)
    text_rect = text_surface.get_rect(center=(mars.orbital_position + Vector(50, 20)).tuple)
    screen.blit(text_surface, text_rect)

    # Phobos Movement
    phobos.center = mars.orbital_position
    phobos.move(delta_time())
    pygame.draw.circle(screen, WHITE, mars.orbital_position.tuple, phobos.distance, width=1)
    pygame.draw.circle(screen, LIGHT_BROWN, phobos.orbital_position.tuple, 2)

    # Deimos Movement
    deimos.center = mars.orbital_position
    deimos.move(delta_time())
    pygame.draw.circle(screen, WHITE, mars.orbital_position.tuple, deimos.distance, width=1)
    pygame.draw.circle(screen, BROWN, deimos.orbital_position.tuple, 2)


    # Update the display
    pygame.display.flip()
    #sleep(0.1)

    # limits FPS to 60
    # delta_time is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    earth_years_passed += delta_time()

# Quit Pygame
pygame.quit()
sys.exit()
