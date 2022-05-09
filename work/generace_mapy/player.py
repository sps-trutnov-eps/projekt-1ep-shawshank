import pygame, sys
from generace_mapy import game_map,master
from sprites import *
pygame.init()

#základní proměnné
clock = pygame.time.Clock()

hitbox = False
player_x = 23 * 32 / 2
player_y = 14 * 32 / 2
player_speed = 3

hrac_display_grp = pygame.sprite.Group()
hrac_hitbox_grp = pygame.sprite.Group()
player_instance = player(player_x, player_y)
hrac_display_grp.add(player_instance)
player_hitbox_instance = player_hitbox(player_x, player_y)
hrac_hitbox_grp.add(player_hitbox_instance)
hrac_hitbox = hrac_hitbox_grp.sprites()[0]

current_position = master

#načtení obrazovek
def urceni_sprite_group(mapa):
    zdi = pygame.sprite.Group()
    podlaha = pygame.sprite.Group()
    dvere = pygame.sprite.Group()
    for radek_ind,radek in enumerate(mapa[0]):
        for symbol_ind,symbol in enumerate(radek):
            if symbol == "6":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_0"))
            elif symbol == "9":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_1"))
            elif symbol == "12":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_2"))
            elif symbol == "15":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_3"))
            elif symbol == "18":
                podlaha.add(zed((symbol_ind*32,radek_ind*32),"void"))
            elif symbol == "5":
                podlaha.add(zed((symbol_ind*32,radek_ind*32),"podlaha")) 
            elif symbol == "7":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_0")) 
            elif symbol == "10":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_1"))
            elif symbol == "13":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_2")) 
            elif symbol == "16":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_3"))  
            elif symbol == "8":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnější_roh_0"))  
            elif symbol == "11":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnější_roh_1"))  
            elif symbol == "14":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnější_roh_2"))
            elif symbol == "17":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnější_roh_3"))
            elif symbol == "1":
                dvere.add(zed((symbol_ind*32,radek_ind*32),"dveře_0"))
            elif symbol == "2":
                dvere.add(zed((symbol_ind*32,radek_ind*32),"dveře_1"))
            elif symbol == "3":
                dvere.add(zed((symbol_ind*32,radek_ind*32),"dveře_2"))
            elif symbol == "4":
                dvere.add(zed((symbol_ind*32,radek_ind*32),"dveře_3"))
    return zdi,podlaha,dvere

zdi,podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])

#main loop
while True:
    #vypnutí
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    
    #ukázka hitboxu
    if pressed[pygame.K_j]:
        if hitbox == False:
            hitbox = True
            player_hitbox_instance.showHitBox()
    if pressed[pygame.K_h]:
        if hitbox == True:
            hitbox = False
            player_hitbox_instance.hideHitBox()
    
    #pohyb
    posun_x = 0
    posun_y = 0
    
    if pressed[pygame.K_w]:
        posun_y -= player_speed
    if pressed[pygame.K_s]:
        posun_y += player_speed
    if pressed[pygame.K_a]:
        posun_x -= player_speed
    if pressed[pygame.K_d]:
        posun_x += player_speed
    
    player_hitbox_instance.posun_x(posun_x)

    #kolize se zdmi
    for wall in zdi:
        if wall.rect.collidepoint(player_hitbox_instance.rect.topleft) or wall.rect.collidepoint(player_hitbox_instance.rect.bottomleft):
            player_hitbox_instance.rect.left = wall.rect.right+1
        if wall.rect.collidepoint(player_hitbox_instance.rect.topright) or wall.rect.collidepoint(player_hitbox_instance.rect.bottomright):
            player_hitbox_instance.rect.right = wall.rect.left-1
            
    player_hitbox_instance.posun_y(posun_y)
    
    for wall in zdi:
        if wall.rect.collidepoint(player_hitbox_instance.rect.topleft) or wall.rect.collidepoint(player_hitbox_instance.rect.topright):
            player_hitbox_instance.rect.top = wall.rect.bottom+1
        if wall.rect.collidepoint(player_hitbox_instance.rect.bottomleft) or wall.rect.collidepoint(player_hitbox_instance.rect.bottomright):
            player_hitbox_instance.rect.bottom = wall.rect.top-1
    
    #pohyb mezi obrazovkami
    if player_hitbox_instance.rect.left < 0:
        player_hitbox_instance.rect.right = width
        current_position[1] -=1
        zdi,podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])
    elif player_hitbox_instance.rect.right > width:
        player_hitbox_instance.rect.left = 0
        current_position[1] +=1
        zdi,podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])
    elif player_hitbox_instance.rect.top < 0:
        player_hitbox_instance.rect.bottom = heigth
        current_position[0] -=1
        zdi,podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])
    elif player_hitbox_instance.rect.bottom > heigth:
        player_hitbox_instance.rect.top = 0
        current_position[0] +=1
        zdi,podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])
    
    #zbytek pohybu
    player_instance.rect.centerx = player_hitbox_instance.rect.centerx
    player_instance.rect.bottom = player_hitbox_instance.rect.bottom
        
    #kolize s dvermi
    if pygame.sprite.spritecollide(hrac_hitbox, dvere, False):
        print(dvere.sprites().index(pygame.sprite.spritecollide(hrac_hitbox, dvere, False)[0]))
    
    #vykreslování
    screen.fill("black")
    zdi.draw(screen)
    podlaha.draw(screen)
    dvere.draw(screen)
    hrac_display_grp.draw(screen)
    hrac_hitbox_grp.draw(screen)
    
    pygame.display.update()
    clock.tick(60)