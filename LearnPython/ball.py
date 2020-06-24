import pygame

white = pygame.Color(255,255,255)
class Ball:
    size = 10
  

    def _init_(self, startx, starty):
        self.box = pygame.Rect(startx,starty,Ball.size,Ball.size)
        self.posx = startx
        self.posy = starty    
        self.speedx = 5
        self.speedy = 5
        
    def draw(self,window):
        pygame.draw.rect(window, white, self.box)

    def update(self):
       self.posx += self.speedx
       self.posy += self.speedy
       self.box = pygame.Rect(self.posx, self.posy, Ball.size,Ball.size)

       if(self.posx < 0 or self.posx > (640 - Ball.size)):
           self.speedx = -self.speedx

       if(self.posy < 0 or self.posy > (480 - Ball.size)):
          self.speedy = -self.speedy

