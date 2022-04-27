import pygame
import sys

okno = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Libor")

libor = pygame.image.load("libor.png")
lavice = pygame.image.load("lavice.png")
tabule = pygame.image.load("tabule.png")
vyhled = pygame.image.load("okno.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    okno.fill("white")
    
    okno.blit(tabule, (150, 40))
    okno.blit(libor, (900, 0))
    okno.blit(lavice, (200, 300))
    okno.blit(lavice, (500, 300))
    okno.blit(lavice, (800, 300))
    okno.blit(lavice, (200, 500))
    okno.blit(lavice, (800, 500))
    okno.blit(lavice, (500, 500))
    okno.blit(vyhled, (20, 500))
    okno.blit(vyhled, (20, 280))
   
    
    
              
    pygame.display.update()