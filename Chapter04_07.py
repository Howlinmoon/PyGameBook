import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Random Pixel generation, non-locking

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    
    rand_color = (randint(0,255), randint(0,255), randint(0,255))
    for _ in xrange(100):
        rand_pos = (randint(0,639), randint(0, 479))
        screen.set_at(rand_pos, rand_color)
        
    pygame.display.update()
    
    