import pygame

white = pygame.Color(255,255,255)

class Paddle:
    size = (15,60)

    def _init_(self,startx,starty):
        self.box = pygame.Rect(startx,starty,Paddle.size[0],Paddle.size[1])
        self.pos = [startx,starty]
        self.speed = 15

    def draw(self,window):
        pygame.draw.rect(window, white, self.box)
    #player
    def update(self, up,down):
        #movement
        if up: self.pos[1] -= self.speed;
        elif down:  self.pos[1] += self.speed;
        #border
        if(self.pos[1] < 0) : self.pos[1] = 0
        elif self.pos[1] > (480 - Paddle.size[1]): self.pos[1] = 480 - Paddle.size[1]

        #update
        self.box = pygame.Rect(self.pos[0],self.pos[1],Paddle.size[0],Paddle.size[1])

    #enemy
    def update1(self, pos):
        pos[1] += 5;
        #movement
        if pos[1] > self.pos[1] : self.pos[1] += self.speed
        elif pos[1] < self.pos[1] : self.pos[1] -= self.speed 
        #border
        if(self.pos[1] < 0) : self.pos[1] = 0
        elif self.pos[1] > (480 - Paddle.size[1]): self.pos[1] = 480 - Paddle.size[1]
        #update
        self.box = pygame.Rect(self.pos[0],self.pos[1],Paddle.size[0],Paddle.size[1])