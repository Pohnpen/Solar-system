# Body of Solar system

from math import pi

from . import *

class Planetoid():

    def __init__(self, radius, mass, name, orbit=Orbit(Vector(0,0),0,0)):
        self.radius = float(radius)
        self.mass = float(mass)
        self.orbit = orbit
        self.name = str(name)

    @property
    def is_static(self):
        if self.orbit.is_static:
            return True
        return False

    @property
    def position(self):
        # returns the position of the Planetoid as a Vector
        return self.orbit.orbital_position()

    def gravitational_force(self, other):
        distance = self.position.distance(other.position)
        force = GRAVITATIONAL_CONSTANT * (self.mass * other.mass) / distance**2
        return force

    def move(self, delta_time):
        self.orbit.move(delta_time)

    def __str__(self):
        return f"{self.name} is at {self.position}"

if __name__ == "__main__":
    sun = Planetoid(500, 100, "Sun")
    earth = Planetoid(5, 1, "Earth", Orbit(Vector(0, 0), 1, 1))
    sun.move(0.5)
    earth.move(0.5)
    print(sun)
    print(earth)
