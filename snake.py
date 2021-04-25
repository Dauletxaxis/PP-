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
    self.c=0
    self.l1=[(100,100),(125,100),(150,100),(175,100),(200,100),(225,100),(250,100),(275,100)]
    self.l2=[(200,100),(225,100),(250,100),(275,100),(300,100),(325,100),(325,125),(325,150),(325,175),(325,200),(325,225),(325,250),(325,275),(325,300),(325,325)]
    self.l3=[(100,100),(125,100),(150,100),(175,100),(200,100),(225,100),(250,100),(275,100),(300,100),(325,100),(350,100),(100,300),(125,300),(150,300),(175,300),(200,300),(225,300),(250,300),(275,300),(325,300),(350,300),(225,125),(225,150),(225,175),(225,200),(225,225),(225,250),(225,275),(225,300)]
    self.levels=[self.l1,self.l2,self.l3]
    self.image=get_image('wall.png')

  def draw(self):
    for i in self.levels[self.c]:
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
    def draw(self):
        for i in self.b:
            
            pygame.draw.circle(scr,self.color,(i.x,i.y),5)


class snake2:
    def __init__(self):
        self.b=[Point(100,400),Point(90,400)]
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
    
S2=snake2()
S=snake()
F=food()
W=wall()
run=True
cnt=0
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
          if ev.key==pygame.K_x:
            S2.add()
          if ev.key==pygame.K_a:
            S2.v=-7
            S2.vx,S2.vy=S2.v,0
          if ev.key==pygame.K_d:
            S2.v=7
            S2.vx,S2.vy=S2.v,0
          if ev.key==pygame.K_w:
            S2.v=-7
            S2.vx,S2.vy=0,S2.v
          if ev.key==pygame.K_s:
            S2.v=7
            S2.vx,S2.vy=0,S2.v
            
    if S.head().x>F.c[0] and S.head().x<F.c[0]+20 and S.head().y>F.c[1] and S.head().y<F.c[1]+20:
      cnt+=1
      if S.v<0:
        S.v-=0.5
      if S.v>0:
        S.v+=0.5
      if cnt%10==0 and W.c<4:
        W.c+=1
      F.c=(random.randint(0,500),random.randint(0,500))

    if S2.head().x>F.c[0] and S2.head().x<F.c[0]+20 and S2.head().y>F.c[1] and S2.head().y<F.c[1]+20:
      cnt+=1
      if S.v<0:
        S.v-=0.5
      if S.v>0:
        S.v+=0.5
      if cnt%10==0 and W.c<4:
        W.c+=1
      F.c=(random.randint(0,500),random.randint(0,500))
    if W.c==0 and (S.head().x>85 or S2.head().x>85) and (S.head().x<315 or S2.head().x<315) and (S.head().y>85 or S2.head().y>85) and (S.head().y<140 or S2.head().y<140):
      run=False
    if W.c==1 and (S.head().x>185 or S2.head().x>185) and (S.head().x<365 or S2.head().x<365) and (S.head().y>85 or S2.head().y>85) and (S.head().y<140 or S2.head().y<140):
      run=False

    if W.c==1 and (S.head().x>310 or S2.head().x>310) and (S.head().x<365 or S2.head().x<365) and (S.head().y>85 or S2.head().y>85) and (S.head().y<365 or S2.head().y<365):
      run=False
    if W.c==2 and (S.head().x>85 or S2.head().x>85) and (S.head().x<365 or S2.head().x<365) and (S.head().y>85 or S2.head().y>85) and (S.head().y<140 or S2.head().y<140):
      run=False
    if W.c==2 and (S.head().x>85 or S2.head().x>85) and (S.head().x<365 or S2.head().x<365) and (S.head().y>285 or S2.head().y>285) and (S.head().y<340 or S2.head().y<340):
      run=False
    if W.c==2 and (S.head().x>210 or S2.head().x>210) and (S.head().x<265 or S2.head().x<265) and (S.head().y>85 or S2.head().y>85) and (S.head().y<340 or S2.head().y<340):
      run=False
    if W.c==0 and F.c[0]>85 and F.c[0]<315 and F.c[1]>85 and F.c[1]<140:
      F.c=(random.randint(0,480),random.randint(0,480))
    if W.c==1 and F.c[0]>185 and F.c[0]<365 and F.c[1]>85 and F.c[1]<140:
      F.c=(random.randint(0,480),random.randint(0,480))

    if W.c==1 and F.c[0]>310 and F.c[0]<365 and F.c[1]>85 and F.c[1]<365:
      F.c=(random.randint(0,480),random.randint(0,480))
    if W.c==2 and F.c[0]>85 and F.c[0]<365 and F.c[1]>85 and F.c[1]<140:
      F.c=(random.randint(0,480),random.randint(0,480))
    if W.c==2 and F.c[0]>85 and F.c[0]<365 and F.c[1]>285 and F.c[1]<340:
      F.c=(random.randint(0,480),random.randint(0,480))
    if W.c==2 and F.c[0]>210 and F.c[0]<265 and F.c[1] and F.c[1]:
      F.c=(random.randint(0,480),random.randint(0,480))

    if S2.head().x>S.head().x+10 and S2.head.x<S.head().x-10 and S2.head().y>S.head().y-10 and S2.head().y<S2.head().y+10:
      run=False

  
                      
    S.move()
    S2.move()
    scr.fill((255,255,255))
    W.draw()
    F.draw()
    S.draw()
    S2.draw()
    pygame.display.flip()
    pygame.time.Clock().tick(5)
pygame.quit()
