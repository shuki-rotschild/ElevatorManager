from config import *


class Floor:

    def __init__(self, num):
        self.num = num
        self.image = pygame.image.load(FLOOR_IMAGE_PATH)
        self.x = MARGIN
        self.y = HEIGHT_WINDOW - HEIGHT_FLOOR * self.num
        self.x_button_center = MARGIN + WIDTH_FLOOR / 2
        self.y_button_center = HEIGHT_WINDOW - self.num * HEIGHT_FLOOR + HEIGHT_FLOOR / 2
        self.button_color = BLACK

    # The function that draws the elevator on the screen according to the image saved in the program

    def draw(self, canvas):
        canvas.blit(self.image, (self.x , self.y))
        pygame.draw.rect(self.image , BLACK , (MARGIN, self.y + ROOF_FLOOR , WIDTH_FLOOR , self.y))
        pygame.draw.circle(self.image, BLACK, (self.x_button_center, self.y_button_center), BUTTON_RADIUS, width=2)

    #The function that checks if the button on the floor is pressed, and returns a boolean value.
    def call_elevator(self, x, y):
        an_elevator_arrives = False

        if abs(x - self.x_button_center) <= BUTTON_RADIUS and abs(y - self.y_button_center) <= BUTTON_RADIUS:
            an_elevator_arrives = True

        return an_elevator_arrives


    def update(self):
        pass
