import pygame
import sys
import random
pygame.init()

v1,v2 = (500,500)
smer = ""

generování = True
obrazek = pygame.image.load("pixil-frame-0.png")

okno = pygame.display.set_mode((1000,1000))

while True:
    if generování:
        xs = random.randint(36,964)
        ys = random.randint(36,964)
        generování = False
    
    for udalost in pygame.event.get():
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_RIGHT:
                smer = "východ"
            if udalost.key == pygame.K_LEFT:
                smer = "západ"
            if udalost.key == pygame.K_DOWN:
                smer = "jih"
            if udalost.key == pygame.K_UP:
                smer = "sever"
    
    if smer is "sever":
        v2 = v2-0.5
    if smer is "jih":
        v2 = v2+0.5
    if smer is "východ":
        v1 = v1+0.5
    if smer is "západ":
        v1 = v1-0.5
    
    okno.fill((0,0,0))
    
    pygame.draw.rect(okno, (172, 106, 70), (v1,v2, 25,25))
    okno.blit(obrazek,(xs,ys, 25,25))
    
    pygame.display.update()
    
    if udalost.type is pygame.QUIT:
            pygame.quit()
            sys.exit()
    