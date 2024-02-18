# Body of Solar system

from constants import GRAVITATIONAL_CONSTANT
from vector import Vector


class Body():

    def __init__(self, position: Vector, mass: float, radius: float):
        self.position = position
        self.mass = mass # mass of the object
        self.radius = radius # radius of the object

    def gravitational_force(self, other):
        distance = self.position.distance(other.position)
        force = GRAVITATIONAL_CONSTANT * (self.mass * other.mass) / distance**2
        return force


if __name__ == "__main__":
    earth = Body(Vector(3,4), 1, 1)
    moon = Body(Vector(3.4,4.5), 0.16, 0.2)
