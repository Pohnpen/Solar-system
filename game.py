# Pygame Documentation: https://www.pygame.org/docs/

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (1000, 1000)  # Width and height of the window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Solar System Viewer")

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

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(BLACK)

    pygame.draw.circle(screen, YELLOW, CENTER, 50)
    pygame.draw.circle(screen, BLUE, LEFT_TOP, 10)
    pygame.draw.circle(screen, GREY, BOTTOM_RIGHT, 5)

    # TODO: draw a white non solid circle (search pygame documentation) of the orbit of the earth ((0,0), 1 AU distance)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
