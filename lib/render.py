import pygame

from .vector import Vector

class PyGameDrawCircleMixin():
    #
    # Interfaces that must be implemented by
    #
    @property
    def position(self):
        # returns the position of the object as a tuple, defaults to (0,0)
        return Vector(0,0)

    @property
    def radius(self):
        # returns the radius of the object in pixels, defaults to 1.0
        return 1.0

    @property
    def width(self):
        # returns 0 for solid, any number for border thickness in px
        return 0

    @property
    def color(self):
        # returns RGB tuple for color, defaults to white
        return (255, 255, 255)

    #
    # Drawing interface
    #
    def draw(self, surface, offset=[0,0]):
        offset_position = (self.position + Vector(*offset)).tuple()
        pygame.draw.circle(surface, self.color, offset_position, self.radius, width=self.width)


class PyGameDrawText():

    def __init__(self, text, color=(255, 255, 255)):
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
    def draw(self, surface, font):
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.position)
        surface.blit(text_surface, text_rect)
