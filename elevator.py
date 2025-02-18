




from config import *


class Elevator:

    def __init__(self, num):
        self.num = num
        self.image = pygame.transform.smoothscale(pygame.image.load(ELEVATOR_IMAGE_PATH),
    (WIDTH_ELEVATOR , HEIGHT_ELEVATOR))
        self.tasks = []
        self.tasks_time = 0
        self.x = MARGIN + WIDTH_FLOOR + self.num * WIDTH_ELEVATOR
        self.y = HEIGHT_WINDOW

    def draw(self, canvas):

        canvas.blit(self.image, (self.x , self.y))

    def eta (self):

        pass

    def update(self):
        pass
