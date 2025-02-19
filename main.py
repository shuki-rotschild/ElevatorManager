import pygame

from config import *
from building import *

pygame.init()

# The production of the window
size = WIDTH_WINDOW, HEIGHT_WINDOW
canvas = pygame.display.set_mode(size)
pygame.display.set_caption("Mechanism for operating the elevators")

# Counting the time required to run the program

past_time = pygame.time.get_ticks()
print(past_time)

# Screen color


pygame.mixer.music.load(DING_IMAGE_PATH)

# An instance of a building class
building = Building()

#A boolean variable that determines whether the main loop will run
run = True

#main loop
while run:

    canvas.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            building.call_elevator(pos)

    building.draw(canvas)

    current_time = pygame.time.get_ticks()
    delta_time = current_time - past_time
    past_time = current_time
    building.update(delta_time)
    pygame.display.update()


    pygame.display.flip()