import pygame
import random

pygame.init()


screen = pygame.display.set_mode((500,500))
run=True

c1=[0,0]
c2=[0,0]
screen.fill((0,0,0))

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run=False
    if event.type==pygame.MOUSEBUTTONDOWN:
      c1[0]=pygame.mouse.get_pos()[0]
      c1[1]=pygame.mouse.get_pos()[1]
    if event.type == pygame.MOUSEMOTION:
      c2[0]=pygame.mouse.get_pos()[0]
      c2[1]=pygame.mouse.get_pos()[1]
      if c1[0]!=0 and c1[1]!=0:
        pygame.draw.line(screen,(0,0,255), (c1[0],c1[1]), (c2[0],c2[1]), 1)
        c1=c2
    if event.type==pygame.MOUSEBUTTONUP:
      c1[0]=0
      c1[1]=0

  pygame.display.flip()
  pygame.time.Clock().tick(60)

pygame.quit()
