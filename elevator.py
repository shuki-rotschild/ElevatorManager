from config import *


class Elevator:

    def __init__(self, num):
        self.num = num
        self.image = (pygame.transform.smoothscale(pygame.image.load(ELEVATOR_IMAGE_PATH),
                                                   (WIDTH_ELEVATOR, HEIGHT_ELEVATOR)))
        # An array that includes all the floors to which the elevator is supposed to reach in the future
        self.tasks = []
        # The time remaining until the elevator is at rest
        self.tasks_time = 0
        # The ratio of the width of the left side of the elevator in relation to the screen
        self.x = MARGIN + WIDTH_FLOOR + (self.num) * WIDTH_ELEVATOR
        # The ratio of the height of the elevator in relation to the screen
        self.y = HEIGHT_WINDOW - HEIGHT_ELEVATOR

    # The function that draws the elevator on the screen according to the image saved in the program
    def draw(self, canvas):
        canvas.blit(self.image, (self.x, self.y))

    def eta(self, destination_floor):
        eta = self.tasks_time
        if len(self.tasks) > 0:
            eta += abs(self.tasks[-1] - destination_floor) * FLOOR_CROSSING_TIME
        return eta

    def start_an_elevator(self, destination_floor):
        self.tasks.append(destination_floor)
        self.tasks_time += abs(self.tasks[-1] - destination_floor) * FLOOR_CROSSING_TIME + FLOOR_WAITING_TIME

    def update(self, delta_time):
        if len(self.tasks) == 0:
            return

        if HEIGHT_WINDOW - self.tasks[0] * HEIGHT_FLOOR < self.y:
            self.y += delta_time * (HEIGHT_FLOOR // FLOOR_CROSSING_TIME)

        if HEIGHT_WINDOW - self.tasks[0] * HEIGHT_FLOOR > self.y:
            self.y -= delta_time * (HEIGHT_FLOOR // FLOOR_CROSSING_TIME)
