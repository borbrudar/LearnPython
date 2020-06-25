import pygame, sys, os
import ball, paddle
import font
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((640,480))
pygame.display.set_caption("Python Pong")

FPS = 30 
Frame = pygame.time.Clock()

b = ball.Ball()
b._init_(320,0)
pad = paddle.Paddle()
pad._init_(50,200)
enemy = paddle.Paddle()
enemy._init_(575,200)

up,down = 0,0

score1,score2 = 0,0

#game loop
while True:
    window.fill(pygame.Color(0,0,0))
     #quit the game
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            os._exit(1)
    #keys
    up,down = 0,0
    keys=pygame.key.get_pressed()
    if keys[K_UP]:
        up = 1
    if keys[K_DOWN]:
        down = 1


    #update
    sc = b.update(pad.box, enemy.box)
    pad.update(up,down)
    enemy.update1(b.box)

    #scores
    if(sc == 1) : score1 += 1
    elif(sc == 2): score2 += 1

    #draw
    b.draw(window)
    pad.draw(window)
    enemy.draw(window)

    #scores draw
    font.text_to_screen(window, '{0}'.format(score1), 160, 30)
    font.text_to_screen(window, '{0}'.format(score2), 480, 30)

    pygame.display.update()
    Frame.tick(FPS)
