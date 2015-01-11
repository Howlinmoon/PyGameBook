# Chapter 3 example 7, Scrolly Message test
background_image_filename = "sushiplate.jpg"
SCREEN_SIZE = (640, 480)

message = "    This is a demonstration of the scrolly message script.   "

import pygame
from pygame.locals import *

pygame.init()
gameDisplay = pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF)
font = pygame.font.SysFont("arial", 80)
text_surface = font.render(message, True, (0, 0, 255))

x = 0
y =  ( SCREEN_SIZE[1] - text_surface.get_height() ) / 2
background = pygame.image.load(background_image_filename).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        
    gameDisplay.blit(background, (0,0))
    
    x -= 2
    if x < -text_surface.get_width():
        x = 0
        
    gameDisplay.blit(text_surface, (x,y))
    gameDisplay.blit(text_surface, (x+text_surface.get_width(), y))
    pygame.display.flip()
        