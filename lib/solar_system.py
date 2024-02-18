# Solar system

from constants import PREFIX

class Solar_system_body():
    density = None
    children = None
    distance_from_Sun = None
    ring_of_planet = None
    #distance_from_Sun_Unit = "AU"
    nick_name = None

    def __init__(self, mass, prefix="normal", distance_from_Sun):
        self.mass = self.(mass, prefix)
        self.distance_from_Sun = self.(distance_from_Sun, distance_from_Sun_Unit)

    def __str__(self, __class__):
        return f"{self.__class__} has {self.children}"

class Sun(Solar_system_body):
    density = "x"
    children = "8"

class Mercury(Solar_system_body):
    density = "x1"
    distance_from_Sun = "y AU"
    nick_name = "..."
