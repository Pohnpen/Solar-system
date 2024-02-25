import pygame

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
        return (255, 255, 255)

    #
    # Drawing interface
    #
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius, width=self.solid)
