import pygame
import random
import os

pygame.init()
Clock=pygame.time.Clock()

scr=pygame.display.set_mode((400,600))
pygame.display.set_caption(('danger drive'))

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\'', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

background=['AnimatedStreet2.png','bg2.jpg']

        
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.im=get_image('coin.png')
        self.surf=pygame.Surface((30,30))
        self.rect=self.surf.get_rect(center=(random.randint(15,385),552))

        
                                       

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.im=get_image('Player.png')
        self.surf=pygame.Surface((44,96))
        self.rect=self.surf.get_rect(center=(200,552))
        self.dim=0

    def move(self):
        kb=pygame.key.get_pressed()
        if kb[pygame.K_LEFT] and self.rect.left>0:
            self.rect.move_ip(-5,0)
        if kb[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        if self.rect.right>400:
            self.rect.center=(0,552)
            self.dim+=1

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.im=get_image('Enemy.png')
        self.surf=pygame.Surface((48,93))
        self.rect=self.surf.get_rect(center=(random.randint(0,356),0))
    def move(self):
        self.rect.move_ip(0,random.randint(1,5))
        if self.rect.top>600:
            self.rect.top=0
            self.rect.center=(random.randint(0,356),0)
cnt=0
font=pygame.font.SysFont('Verdana', 20)
E=Enemy()
P=Player()
C=Coin()
Coins=pygame.sprite.Group()
Coins.add(C)
G=pygame.sprite.Group()
G.add(E)
A=pygame.sprite.Group()
A.add(E)
A.add(P)
run=True
while run:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            run=False
        if ev.type==pygame.KEYDOWN:
            if ev.key==pygame.K_UP:
                A.add(Enemy())
    scr.blit(get_image(background[P.dim]),(0,0))
    Font=font.render('score:{score}'.format(score=cnt),True,(0,0,0))
    scr.blit(Font, (300,100))
    for en in A:
        scr.blit(en.im,en.rect)
        en.move()
    for m in Coins:
        scr.blit(m.im,m.rect)
    if pygame.sprite.spritecollideany(P,G):
        run=False
    if pygame.sprite.spritecollideany(P,Coins):
        C.rect.center=(random.randint(15,385),552)
        cnt+=1
    pygame.display.update()
    Clock.tick(60)
pygame.quit()

    
    
