import pygame

WHITE = (255, 255, 255)
STANDARD_FONT = pygame.font.Font(None, 24)

class PyGameDrawCircleMixin():
    #
    # Interfaces that must be implemented by
    #
    @property
    def position(self):
        # returns the position of the object as a tuple, defaults to (0,0)
        return (0,0)

    @property
    def radius(self):
        # returns the radius of the object in pixels, defaults to 1.0
        return 1.0

    @property
    def solid(self):
        # returns 0 for solid, any number for border thickness in px
        return 0

    @property
    def color(self):
        # returns RGB tuple for color, defaults to white
        return WHITE

    #
    # Drawing interface
    #
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius, width=self.solid)


class PyGameDrawText():

    def __init__(self, text, color=WHITE, font=STANDARD_FONT):
        self.text = text
        self.color = color
        self.font = font

    @property
    def position(self):
        # returns the position of the object as a tuple, defaults to (0,0)
        return (0, 0)

    #
    # Drawing interface
    #
    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.position)
        surface.blit(text_surface, text_rect)