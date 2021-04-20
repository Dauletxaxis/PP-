import pygame
import math
class Cor:
    def __init__(self, p=(0,0)):
        self.x=p[0]
        self.y=p[1]
    def __mul__(self, scalar):
        return Cor((self.x*scalar, self.y*scalar))
    def __add__(self,an):
        return Cor((self.x+an.x,self.y+an.y))
    def __sub__(self,an):
        return Cor((self.x-an.x,self.y-an.y))
    def __len__(self):
        return int(math.sqrt(self.x**2+self.y**2))
    def __div__(self,sc):
        return Cor((self.x/sc,self.y/sc))
    def cr(self):
        return (self.x,self.y)
def draw(surf,col,st,end,w=1,dl=4):
    of=Cor(st)
    tr=Cor(end)
    dis=tr-of
    d=len(dis)
    un=dis.__div__(d)
    for i in range(0,int(d/dl),2):
        start=of+(un*i *dl)
        end=of+(un*(i+1)*dl)
        pygame.draw.line(surf,col,start.cr(),end.cr(),w)
pygame.init()
scr=pygame.display.set_mode((400,300))
run=True
while run:
    draw(scr,(0,255,0),(0,0),(100,100),1)
    pygame.display.flip()
        
