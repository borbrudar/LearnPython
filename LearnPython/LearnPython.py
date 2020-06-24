import pygame, sys, os
import ball
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((640,480))
pygame.display.set_caption("Python Pong")

FPS = 30 
Frame = pygame.time.Clock()

b = ball.Ball()
b._init_(320,0)

#game loop
while True:
    window.fill(pygame.Color(0,0,0))
     #quit the game
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            os._exit(1)
    #update
    b.update()

    #draw
    b.draw(window)


    pygame.display.update()
    Frame.tick(FPS)
