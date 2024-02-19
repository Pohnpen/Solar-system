# Body of Solar system

from constants import GRAVITATIONAL_CONSTANT
from vector import Vector
from math import pi


class Body():

    def __init__(self, position: Vector, mass: float, radius: float, velocity: float , time=(1, 100)):
        self.position = position
        self.mass = mass # mass of the object
        self.radius = radius # radius of the object
        self.velocity = velocity
        self.time = time

    def gravitational_force(self, other):
        distance = self.position.distance(other.position)
        force = GRAVITATIONAL_CONSTANT * (self.mass * other.mass) / distance**2
        return force

    def centripetal_force(self, other):
        distance = self.position.distance(other.position)
        force = (self.mass * (self.velocity**2)) / distance
        return force

    def velocity_of_object(self, other):
        distance = self.position.distance(other.position)
        velocity = (2 * pi * distance) / self.time
        return ((GRAVITATIONAL_CONSTANT * other.mass) / distance)**0.5


    def position at 


if __name__ == "__main__":
    earth = Body(Vector(3,4), 1, 1, 12)
    moon = Body(Vector(3.4,4.5), 0.16, 0.2, 6)
