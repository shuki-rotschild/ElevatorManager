from config import *


class Floor:

    def __init__(self, num):
        self.num = num
        self.image = pygame.transform.smoothscale (pygame.image.load(FLOOR_IMAGE_PATH) , (WIDTH_FLOOR , HEIGHT_FLOOR))
        self.x = MARGIN
        self.y = HEIGHT_WINDOW - HEIGHT_FLOOR * (self.num +1)
        self.x_button_center = MARGIN + WIDTH_FLOOR / 2
        self.y_button_center = HEIGHT_WINDOW - self.num * HEIGHT_FLOOR + HEIGHT_FLOOR / 2
        self.button_color = GREEN

        self.an_elevator_arrives = False
        self.timm_elevator_arrives = None
    # The function that draws the elevator on the screen according to the image saved in the program

    def draw(self, canvas):
        #pygame.draw.circle(self.image, SILVER, (self.x_button_center, self.y_button_center), BUTTON_RADIUS)
        #pygame.draw.circle(self.image, BLACK, (self.x_button_center, self.y_button_center), BUTTON_RADIUS, width = 2)
        #a= pygame.draw.rect(self.image , BLACK , (MARGIN, self.y + ROOF_FLOOR , WIDTH_FLOOR , self.y))
        # draw floor number
        font = pygame.font.Font(None, 20)
        num = str(self.num)
        button_num = font.render(num, True, BLACK)
        button_num_rect = button_num.get_rect()
        button_num_rect.center = self.x_button_center , self.y_button_center
        self.image.blit(button_num, button_num_rect)
        canvas.blit(self.image, (self.x, self.y))

        spacer_rect = pygame.Rect(self.x , self.y, WIDTH_FLOOR, ROOF_FLOOR)
        pygame.draw.rect(canvas, BLACK, spacer_rect)

        #pygame.draw.circle(self.image, BLACK, (self.x_button_center, self.y_button_center), BUTTON_RADIUS, width=2)

    #The function that checks if the button on the floor is pressed, and returns a boolean value.
    def call_elevator(self, x, y):
        an_elevator_arrives = False




        if abs(x - self.x_button_center) <= BUTTON_RADIUS and abs(y - self.y_button_center) <= BUTTON_RADIUS:
            an_elevator_arrives = True



        return an_elevator_arrives


    def update(self , delta_time):
        if self.an_elevator_arrives:
            self.button_color = RED
            self.timm_elevator_arrives -= delta_time

            if self.timm_elevator_arrives <=0:
                pygame.mixer.music.play()


