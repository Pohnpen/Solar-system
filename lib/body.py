
from math import pi, sin, cos

from .render import PyGameDrawCircleMixin
from .vector import Vector

class Orbit(PyGameDrawCircleMixin):
    """# Orbit of the object in Solar system"""
    def __init__(self, center: Vector, distance, period, angle=0.0):
        self.parent = None # if a parent moving body is set
        if center.__class__.__name__ == "Planetoid":
            self.parent = center
            self._center = self.parent.position
        else:
            self._center = center    # Barycenter of the orbit
        self.distance = distance # Apsis of a circular orbit in AU
        self.period = period # time (1 Earth Year) for one revolution (2*pi) in radians
        self.current_angle = angle # current angle in radians

    @property
    def center(self):
        if self.parent:
            return self.parent.position
        return self._center

    def orbital_position(self):
        # returns the vector position of the orbit at a certain angle in radians
        if self.is_static:
            return self.center
        return self.center.angular_displacement(self.distance, self.current_angle)

    def move(self, delta_time):
        if not self.is_static:
            self.current_angle += (2*pi)*(delta_time/self.period)

    def __str__(self):
        #return str(self.current_angle)
        return str(self.orbital_position())

    @property
    def position(self):
        return self.center

    @property
    def radius(self):
        return self.distance

    @property
    def width(self):
        return 1 # 1px width

    @property
    def color(self):
        return (255, 255, 255)

    @property
    def is_static(self):
        if self.distance == 0 and self.period == 0:
            return True
        return False

class Planetoid(PyGameDrawCircleMixin):
    """ Body of Solar system"""
    def __init__(self, radius, mass, name, color=(255, 255, 255), orbit=Orbit(Vector(0,0),0,0)):
        self.mass = float(mass)
        self.orbit = orbit
        self.name = str(name)
        self._color = color
        self._radius = float(radius)

    @property
    def is_static(self):
        if self.orbit.is_static:
            return True
        return False

    @property
    def position(self):
        # returns the position of the Planetoid as a Vector
        return self.orbit.orbital_position()

    @property
    def radius(self):
        # returns the radius of the object in pixels, defaults to 1.0
        return self._radius

    @property
    def width(self):
        # returns 0 for solid, planets should be solid in color
        return 0

    @property
    def color(self):
        # returns RGB tuple for color, defaults to white
        return self._color

    def gravitational_force(self, other):
        distance = self.position.distance(other.position)
        force = GRAVITATIONAL_CONSTANT * (self.mass * other.mass) / distance**2
        return force

    def move(self, delta_time):
        self.orbit.move(delta_time)

    def __str__(self):
        return f"{self.name} is at {self.position}"

    def draw(self, surface):
        self.orbit.draw(surface)
        super().draw(surface)

if __name__ == "__main__":
    pass
