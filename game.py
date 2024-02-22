# Pygame Documentation: https://www.pygame.org/docs/

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (1000, 1000)  # Width and height of the window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Circle in the Center")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(BLACK)

    # Draw a circle in the center of the window
    center = (window_size[0] // 2, window_size[1] // 2)  # Calculate the center of the window
    pygame.draw.circle(screen, WHITE, center, 50)  # Draw circle with radius 50

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
