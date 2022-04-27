import pygame
import sys

okno = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Trida")

x = 400
y = 550

x2 = 400
y2 = 10

width = 40
height = 55

r = 5
krida = pygame.image.load("krida.png")

run = True

while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        
        
libor = pygame.image.load("libor.png")
lavice = pygame.image.load("lavice.png")
tabule = pygame.image.load("tabule.png")
vyhled = pygame.image.load("okno.png")
hrac = pygame.image.load("hrac.png")
    
run = True

while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>200:
        x -= r
    
    if keys[pygame.K_RIGHT] and x<880-width:
        x += r
            
    okno.fill("white")
    
    okno.blit(tabule, (150, 40))
    okno.blit(libor, (900, 0))
    okno.blit(lavice, (200, 300))
    okno.blit(lavice, (500, 300))
    okno.blit(lavice, (800, 300))
    okno.blit(lavice, (200, 400))
    okno.blit(lavice, (800, 400))
    okno.blit(lavice, (500, 400))
    okno.blit(vyhled, (20, 500))
    okno.blit(vyhled, (20, 280))
    okno.blit(hrac, (x, y))
    okno.blit(krida, (400, 10))
    
    
    
              
    pygame.display.update()