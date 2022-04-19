import pygame
import sys
from sprites import *

pygame.init()

zdi = pygame.sprite.Group()
hraci = pygame.sprite.Group()
podlaha = pygame.sprite.Group()
dvere = pygame.sprite.Group()

mapa = ((17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,15,0,6,17,14,4,4,8,17,17,17,17,17),
        (5,5,5,5,5,16,4,4,7,5,16,4,7,5,16,4,4,7,5,5,5,5,5),
        (4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4),
        (4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4),
        (11,11,11,11,11,13,4,4,10,11,11,11,11,11,13,4,4,10,11,11,11,11,11),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17))


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

hraci.add(hrac())
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
    screen.fill("black")
    zdi.draw(screen)
    podlaha.draw(screen)
    dvere.draw(screen)
    hraci.draw(screen)
    pygame.display.update()