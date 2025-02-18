from config import *
from floor import *
from elevator import *


class Building:

    def __init__(self):
        self.floors = [Floor(i) for i in range(NUMBER_OF_FLOORS)]
        self.elevators = [Elevator(i) for i in range(NUMBER_OF_ELEVATORS)]

    def draw(self, canvas):
        for Floor in range(NUMBER_OF_FLOORS):
            Floor.draw(canvas)

        for Elevator in range(NUMBER_OF_ELEVATORS):
            Elevator.draw(canvas)

    def call_elevator(self, pos):
        x, y = pos
        if MARGIN <= x <= MARGIN + WIDTH_FLOOR
            and HEIGHT_WINDOW - NUMBER_OF_FLOORS * HEIGHT_FLOOR <= y <= HEIGHT_WINDOW:

            destination_floor = self.floors[(HEIGHT_WINDOW - y) / HEIGHT_FLOOR ]

            if destination_floor.call_elevator(destination_floor , x, y):
                    pass


def update(self, delta_time):
    pass
