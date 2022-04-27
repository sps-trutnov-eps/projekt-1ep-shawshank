import pygame
import sys
from sprites import *

pygame.init()

RESOLUTION_X = 23*32
RESOLUTION_Y = 14*32
screen = pygame.display.set_mode((RESOLUTION_X, RESOLUTION_Y))

zdi = pygame.sprite.Group()
hraci = pygame.sprite.Group()
podlaha = pygame.sprite.Group()
dvere = pygame.sprite.Group()
mask = pygame.sprite.Group()

mapa = ((15,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (14,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8),
        (12,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,9))


for radek_ind,radek in enumerate(mapa):
    for symbol_ind,symbol in enumerate(radek):
        if symbol == 5:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_0"))
        elif symbol == 8:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_1"))
        elif symbol == 11:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_2"))
        elif symbol == 14:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_3"))
        elif symbol == 17:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"void"))
        elif symbol == 4:
            podlaha.add(zed((symbol_ind*32,radek_ind*32),"podlaha"))
        elif symbol == 13:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"vnejsi_roh_2")) 
        elif symbol == 16:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"vnější_roh_3")) 
        elif symbol == 10:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"vnější_roh_1")) 
        elif symbol == 7:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"vnější_roh_0"))
        elif symbol == 15:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_3"))
        elif symbol == 0:
            dvere.add(zed((symbol_ind*32,radek_ind*32),"dveře_0"))  
        elif symbol == 6:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_0"))
        elif symbol == 9:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_1"))
        elif symbol == 12:
            zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_2"))

playerPosX = 0
playerPosY = 0
hraci.add(hrac((playerPosX, playerPosY)))

mask.add(blackMask(RESOLUTION_X))
    
while True:
    pressedButton = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if (pressedButton[pygame.K_LEFT]):
        playerPosX -= 1
    if (pressedButton[pygame.K_RIGHT]):
        playerPosX += 1
    if (pressedButton[pygame.K_UP]):
        playerPosY -= 1
    if (pressedButton[pygame.K_DOWN]):
        playerPosY += 1
    
    hraci.update(playerPosX, playerPosY)
    
    zdi.draw(screen)
    podlaha.draw(screen)
    dvere.draw(screen)
    hraci.draw(screen)
    mask.update(screen, playerPosX, playerPosY)
    
    pygame.display.update()