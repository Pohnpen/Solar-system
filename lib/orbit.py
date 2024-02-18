# Orbit of the object in Solar system

import math
import pi
from vector import Vector

class Orbit():
    standardd_radian = 0.0

    def __init__(self,  center: Vector, distance: float, velocity: float):
        self.center = center
        self.distance = distance(
        self.velocity = velocity # radians per time (1 time) rad/hour

    def position_at(self, time=0.0):
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
