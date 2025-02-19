from config import *
from floor import *
from elevator import *


class Building:
    # Arrays that include the building's floors and the building's elevators
    def __init__(self):
        self.floors = [Floor(i) for i in range(NUMBER_OF_FLOORS)]
        self.elevators = [Elevator(i) for i in range(NUMBER_OF_ELEVATORS)]

    # Drawing the building on the screen by going through all the floors and all the elevators
    def draw(self, canvas):
        for floor in self.floors:
            floor.draw(canvas)

        for elevator in self.elevators:
            elevator.draw(canvas)
    #The function that checks if there is a call to the elevator, and if so it calls it.
    def call_elevator(self, pos):
        x, y = pos
        if (MARGIN <= x <= MARGIN + WIDTH_FLOOR and
                HEIGHT_WINDOW - NUMBER_OF_FLOORS * HEIGHT_FLOOR <= y <= HEIGHT_WINDOW):

            destination_floor = self.floors[(HEIGHT_WINDOW - y) / HEIGHT_FLOOR]

            if destination_floor.call_elevator(x, y):
                pass

    def update(self, delta_time):
        pass
