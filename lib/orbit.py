# Orbit of the object in Solar system

from math import pi
from vector import Vector
from constants import GRAVITATIONAL_CONSTANT

class Orbit():
    standardd_radian = 0.0

    def __init__(self,  center: Vector, distance: float, period: float):
        self.center = center
        self.distance = distance
        self.period = period # radians per time (1 time) rad/hour

    def position_at(self, period=0.0*pi):
        # return the Vector position on the orbital plane at time
        start = self.center * self.distance
        return
        # 50/t
        # t = 0.61
        # 50/23.61
        # # 50/(23.61 % 50


    def circumference(self, pi=3.14):
        #circumference =
        pass
