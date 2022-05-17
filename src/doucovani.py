import pygame
import sys
pygame.init()

v1,v2 = (500,500)
smer = ""


okno = pygame.display.set_mode((1000,1000))
while True:
    okno.fill((0,0,0))
    had = pygame.draw.rect(okno, (172, 106, 70), (v1,v2, 25,25))
    if smer is "sever":
        v2 = v2-0.5
    if smer is "jih":
        v2 = v2+0.5
    if smer is "východ":
        v1 = v1+0.5
    if smer is "západ":
        v1 = v1-0.5
        
    
    pygame.display.update()
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
                 
            
        if udalost.type is pygame.QUIT:
            pygame.quit()
            sys.exit()
    

