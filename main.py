import pygame

from config import *
from building import *

pygame.init()

# The production of the window
size = WIDTH_WINDOW, HEIGHT_WINDOW
canvas = pygame.display.set_mode(size)
pygame.display.set_caption("Mechanism for operating the elevators")

# Counting the time required to run the program
clock = pygame.time.Clock()
past_time = pygame.time.get_ticks()
print(past_time)

# Screen color
canvas.fill(WHITE)

# An instance of a building class
building = Building()

#A boolean variable that determines whether the main loop will run
run = True

#main loop
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

    building.draw(canvas)
    pygame.display.update()
