from version import TITLE

from time import sleep

from lib.orbit import Orbit
from lib.vector import Vector

TIME_FACTOR = 1/(365)

if __name__ == "__main__":
    print(TITLE)

    earth = Orbit(Vector(0,0), distance=1.0, period=1.0)
    moon = Orbit(earth.orbital_position(), distance=0.002679, period=27/365)
    mars = Orbit(Vector(0,0), distance=1.52, period=779/365)

    while True:
        earth.move(TIME_FACTOR)
        moon.move(TIME_FACTOR)
        mars.move(TIME_FACTOR)
        print(f"Earth: {earth} ::: Moon {moon} ::: Mars {mars}")
        sleep(0.1)
