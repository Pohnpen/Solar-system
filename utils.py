from lib.constants import SIMULATION_SPEED_MODES

def change_simulation_speed(mode, current):
    # Returns the current sim speed if SIMULATION_SPEED_MODES are not out of bounds
    # mode is -1/+1/0 for decr/incr/pause
    if mode == 0:
        return 0
    new = SIMULATION_SPEED_MODES.index(current) + mode
    if new in range(len(SIMULATION_SPEED_MODES)):
        return SIMULATION_SPEED_MODES[new]
    return current