import pygame
import sys
import random

BARVA_POZADI = (0, 20, 0)

pygame.init()

okno = pygame.display.set_mode((736,448))
pygame.display.set_caption("Minihra Martina Michálka")

seznam_zadani = ["test", "tset"]
zadani = seznam_zadani[random.randint(0,len(seznam_zadani))-1]

while True:
    udalost = pygame.event.get()
    stisknuto = pygame.key.get_pressed()
    
    for u in udalost:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    okno.fill(BARVA_POZADI)
    
    font = pygame.font.SysFont("Comic Sans MS", 42)
    uloha = font.render(zadani, True, (255, 255, 255))
    okno.blit(uloha, (0,0))
    
    ## ToDo input řešení
    
    pygame.display.update()