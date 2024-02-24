# Orbit of the object in Solar system

from math import pi, sin, cos
from .vector import Vector
from .constants import GRAVITATIONAL_CONSTANT

class Orbit():
    standardd_radian = 0.0

    def __init__(self, center: Vector, distance, period, angle=0.0):
        self.center = center    # Barycenter of the or bit
        self.distance = distance # Apsis of a circular orbit in AU
        self.period = period # time (1 Earth Year) for one revolution (2*pi) in radians
        self.current_angle = angle # current angle in radians


    def position_at(self, period=2*pi):
        # DEPRECATED! TODO: DELETE
        # return the Vector position on the orbital plane at time
        start = (self.center.x * cos(2 * pi)) * self.distance ,  (self.center.y * sin(2 * pi)) * self.distance
        return start
        # 50/t
        # t = 0.61
        # 50/23.61
        # # 50/(23.61 % 50


    def orbital_position(self):
        # returns the vector position of the orbit at a certain angle in radians
        return self.center.angular_displacement(self.distance, self.current_angle)

    def move(self, delta_time):
        self.current_angle += (2*pi)*(delta_time/self.period)

    def __str__(self):
        #return str(self.current_angle)
        return str(self.orbital_position())
