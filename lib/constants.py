# Simulation Speed in hours per ingame seconds
SIMULATION_SPEED_MODES = [0, 1, 24, 7*24, 30*24, 365*24]

EARTH_HOURS_PER_EARTH_YEAR = 365*24

AU_IN_KM = 149597870.7
PX_PER_AU = 400

earth_radii_to_au = lambda er: er/AU_IN_KM

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (225, 225, 0)
BLUE = (0, 0, 225)
GREY = (128, 128, 128)
DARK_GREY = (64, 64, 64)
LIGTH_GREY = (99, 99 ,99)
RED = (225, 0, 0)
LIGTH_BROWN = (214, 181, 117)
BROWN = (94, 62, 23)

EARTH_MASS = 1 * ((5.972168) * 10**24) #kg


GRAVITATIONAL_CONSTANT = 6.674 * 10**-11 # N m**2 / kg**2
