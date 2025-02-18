import pygame

from config import *

pygame.init()

#The production of the window
size = WIDTH_WINDOW, HEIGHT_WINDOW
canvas = pygame.display.set_mode(size)
pygame.display.set_caption("Mechanism for operating the elevators")

#Counting the time required to run the program
clock = pygame.time.Clock()
past_time = pygame.time.get_ticks()
print(past_time)

#Screen color
canvas.fill(WHITE)
#pygame.display.flip()

run = True

while run:


    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
    pygame.display.update()


