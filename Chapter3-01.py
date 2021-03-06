import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
background = pygame.image.load(background_image_filename).convert()
clock = pygame.time.Clock()

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if event.type == KEYDOWN:
        if event.key == K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
                print "into full screen mode"
                screen = pygame.display.set_mode((640,480), FULLSCREEN, 32)
            else:
                print "out of full screen mode"
                screen = pygame.display.set_mode((640,480), 0, 32)

        # emergency exit!
        if event.key == K_q:
            pygame.quit()
            quit()

    screen.blit(background, (0,0))
    pygame.display.update()
    clock.tick(5)