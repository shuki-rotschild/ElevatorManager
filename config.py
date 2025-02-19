import pygame


# Building characteristics
NUMBER_OF_FLOORS = 70
NUMBER_OF_ELEVATORS = 3

# Window size
WIDTH_WINDOW = 1000
HEIGHT_WINDOW =600

# Floor size
WIDTH_FLOOR = 120
HEIGHT_FLOOR = 80
MARGIN = 10
ROOF_FLOOR = 7
BUTTON_RADIUS = 50

# elevator size
WIDTH_ELEVATOR = 60
HEIGHT_ELEVATOR = 80

# RGB for program colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SILVER = (0,128,128)

#Fixed times in the program
FLOOR_CROSSING_TIME = 500
FLOOR_WAITING_TIME = 2000
REFRESH_TIME = 60 # Every few milliseconds the main loop ran
DEAD_TIME = 10000 # The number of milliseconds after which the lifts dissipate on average

#The paths to the files required for the program
FLOOR_IMAGE_PATH = "resources/floor.jpeg"
ELEVATOR_IMAGE_PATH = "resources/elv.png"
DING_IMAGE_PATH = "resources/ding.mp3"