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

# Define constants
# Draw a circle in the center of the window
CENTER = (window_size[0] // 2, window_size[1] // 2)
LEFT_TOP = (window_size[0] // 3, window_size[1] // 3)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(BLACK)

    # TODO: Set the Sun back to 50 and the Earth to 10 radius
    # 1 Sun's radius = 0.0046524726 AU
    pygame.draw.circle(screen, YELLOW, CENTER, 0.0046524726)

    # TODO: Draw a BLUE circle at the top-left coordinate of the screen.
    pygame.draw.circle(screen, BLUE, LEFT_TOP, 10)

    # TODO: Draw a GREY circle at the bottom-right coordinate of the screen.

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
