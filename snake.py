import pygame
import os
import random

pygame.init()

scr=pygame.display.set_mode((500,500))
pygame.display.set_caption('SNake')

_image_library = {}
def get_image(path):
  global _image_library
  image = _image_library.get(path)
  if image == None:
    canonicalized_path = path.replace('/', os.sep).replace('\'', os.sep)
    image = pygame.image.load(canonicalized_path)
    _image_library[path] = image
  return image

class wall:
  def __init__(self):
    self.l1=[(100,100),(125,100),(150,100),(175,100),(200,100),(225,100),(250,100),(275,100)]
    self.image=get_image('wall.png')

  def draw(self):
    for i in self.l1:
      scr.blit(self.image,i)
class food:
  def __init__(self):
    self.c=(random.randint(0,480),random.randint(0,480))
    self.image=get_image('food.jpg')

  def draw(self):
    scr.blit(self.image,self.c)
class Point:
  def __init__(self, _x: int, _y: int):
    self.x = _x
    self.y = _y
class snake:
    def __init__(self):
        self.b=[Point(200,200),Point(190,200)]
        self.v=7
        self.vx=self.v
        self.vy=0
        self.color=(0,0,0)
    def head(self):
        return self.b[0]

    def move(self):
        for i in range(len(self.b)-1,0,-1):
            self.b[i].x=self.b[i-1].x
            self.b[i].y=self.b[i-1].y
            
        if self.head().x>500:
            self.head().x=0
            
          

        self.head().x+=self.vx
        self.head().y+=self.vy

    def add(self):
        self.b.append(Point(0,0))
        
    def draw(self):
        for i in self.b:
            
            pygame.draw.circle(scr,self.color,(i.x,i.y),5)

S=snake()
F=food()
W=wall()
run=True

while run:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
          run=False
        if ev.type==pygame.KEYDOWN:
          if ev.key==pygame.K_SPACE:
            S.add()
          if ev.key==pygame.K_LEFT:
            S.v=-7
            S.vx,S.vy=S.v,0
          if ev.key==pygame.K_RIGHT:
            S.v=7
            S.vx,S.vy=S.v,0
          if ev.key==pygame.K_UP:
            S.v=-7
            S.vx,S.vy=0,S.v
          if ev.key==pygame.K_DOWN:
            S.v=7
            S.vx,S.vy=0,S.v
    if S.head().x>F.c[0] and S.head().x<F.c[0]+20 and S.head().y>F.c[1] and S.head().y<F.c[1]+20:
      F.c=(random.randint(0,500),random.randint(0,500))
                      
    S.move()          
    scr.fill((255,255,255))
    W.draw()
    F.draw()
    S.draw()
    pygame.display.flip()
    pygame.time.Clock().tick(5)
pygame.quit()
