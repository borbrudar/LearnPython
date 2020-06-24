import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAY = pygame.display.set_mode((200,200))

FPS = pygame.time.Clock()
FPS.tick(60)

#game loop
while True:
     #quit the game
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
    #update
    pygame.display.update()

    #draw
    c1 = pygame.Color(255,0,0)
    pygame.draw.circle(DISPLAY, c1, (200,50), 30)
