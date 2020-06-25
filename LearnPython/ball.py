import pygame

white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)

class Ball:
    size = 10
  
    def _init_(self, startx, starty):
        self.box = pygame.Rect(startx,starty,Ball.size,Ball.size)
        self.pos = [startx,starty]  #0 - x, 1- y
        self.speed = [10,10] #same here
        self.prevPos = self.pos
        #multiple boxes
        self.bb1 = pygame.Rect(startx, starty, Ball.size - 2,2) #top
        self.bb2 = pygame.Rect(startx, starty + Ball.size - 2, Ball.size,2) #bottom
        self.bb3 = pygame.Rect(startx, starty, 2,Ball.size - 2)    #left
        self.bb4 = pygame.Rect(startx + Ball.size, starty, 2,Ball.size - 2) ##right
        
    def draw(self,window):
        pygame.draw.rect(window, white, self.box)

       #pygame.draw.rect(window, red, self.bb1)
       #pygame.draw.rect(window, red, self.bb2)
       #pygame.draw.rect(window, red, self.bb3)
       #pygame.draw.rect(window, red, self.bb4)

    def update(self, pad):
       self.prevPos = self.pos

       if self.pos[0] < 0 or self.pos[0] > (640 - Ball.size):
           self.speed[0] = -self.speed[0]

       if self.pos[1] < 0 or self.pos[1] > (480 - Ball.size):
          self.speed[1] = -self.speed[1]

       #paddle collision
       if self.bb1.colliderect(pad) or self.bb2.colliderect(pad):
           self.pos = self.prevPos
           self.speed[0] = -self.speed[0]
       elif self.bb3.colliderect(pad) or self.bb4.colliderect(pad):
           self.pos = self.prevPos
           self.speed[1] = -self.speed[1]   
           
       #pos etc
       self.pos[0] += self.speed[0]
       self.pos[1] += self.speed[1]
       self.box = pygame.Rect(self.pos[0], self.pos[1], Ball.size,Ball.size)

       #boxes
       self.bb1 = pygame.Rect(self.pos[0] + 1,self.pos[1],Ball.size - 3,2)
       self.bb2 = pygame.Rect(self.pos[0] + 1, self.pos[1] + Ball.size - 3, Ball.size,2) #bottom
       self.bb3 = pygame.Rect(self.pos[0], self.pos[1] + 1, 2,Ball.size - 3)    #left
       self.bb4 = pygame.Rect(self.pos[0] + Ball.size, self.pos[1] + 1, 2,Ball.size - 3) ##right


