import sys
import os
import importlib
from generace_mapy import generate
from sprites import *
import time
from inventory import inventoryHasKey, inventoryHasBoots

minigames = []
try:
    path = os.path.join(os.getcwd()+"\\minihry")
    names = os.listdir(path)
except:
    path = os.path.join(os.getcwd()+"/minihry")
    names = os.listdir(path)

for name in names:
    if ".py" in name:
        minigames.append(importlib.import_module("minihry."+name.split(".")[0]))
    

pygame.init()
pygame.mixer.init()

#základní proměnné
game_map,master,minimap = generate()

clock = pygame.time.Clock()
hall = pygame.mixer.Sound("../data/music/þE_hALL.mp3")

cheat_timeout = 20
show_minimap = False
mimimap_pos = (width - len(game_map[0])*20,heigth - len(game_map)*12)
ukazatel = pygame.image.load("../data/hud/ukazatel_na_mapce.png").convert_alpha()
counter_texture = pygame.image.load("../data/hud/counter.png").convert_alpha()
counter_surface = counter_texture.get_rect()
clip = True
hitbox = False
show_minigame = True
player_x = 23 * 32 / 2
player_y = 14 * 32 / 2
player_speed = 3
health_max = health = 5
mozne_prechody = []
player_movable = True

default_time = 60
current_time = 60
time_background = pygame.Surface((60,54))
time_background.fill((0,28,32))
time_outground = pygame.Surface((65,59))
time_outground.fill("gray")

hrac_display_grp = pygame.sprite.Group()
hrac_hitbox_grp = pygame.sprite.Group()
postavy_display_grp = pygame.sprite.Group()
player_instance = player(player_x, player_y)
hrac_display_grp.add(player_instance)
player_hitbox_instance = player_hitbox(player_x, player_y)
hrac_hitbox_grp.add(player_hitbox_instance)
hrac_hitbox = hrac_hitbox_grp.sprites()[0]
health_bar = Health_bar((23*32/2, 24), screen)

#inventář
inventoryKey_grp = pygame.sprite.Group()
invKey = inventoryHasKey(23*32-32-16-16, 16+8)
inventoryKey_grp.add(invKey)
inventoryBoots_grp = pygame.sprite.Group()
invBoots = inventoryHasBoots(23*32-16-8, 16+8)
inventoryBoots_grp.add(invBoots)

current_position = master

skolnik = janitor(player_instance)
postavy_display_grp.add(skolnik)
menu_state = None

#výstup ze dveří
def vystup(pos):
    for line_ind,line in enumerate(game_map[pos[0]][pos[1]][0]):
        for symbol_ind,symbol in enumerate(line):
            if symbol == "1": return (symbol_ind*32+16,(line_ind+1)*32+16)
            elif symbol == "2": return ((symbol_ind-1)*32+16,line_ind*32+16)
            elif symbol == "3": return (symbol_ind*32+16,(line_ind-1)*32+16)
            elif symbol == "4": return ((symbol_ind+1)*32+16,line_ind*32+16)
##aktivace miniher
def play_minigame():
    hall.stop()
    if show_minigame:
        outcome = random.choice(minigames).main()
        screen = pygame.display.set_mode((width,heigth))
        pygame.display.set_caption("¤Útěk ze střední průmyslové Shawshank¤")
        player_hitbox_instance.rect.center = vystup(current_position)
        player_instance.rect.centerx = player_hitbox_instance.rect.centerx+4
        player_instance.rect.bottom = player_hitbox_instance.rect.bottom-2
        hall.play()
        if outcome: return health
        else: return health-1
    else:
        player_hitbox_instance.rect.center = vystup(current_position)
        player_instance.rect.centerx = player_hitbox_instance.rect.centerx+4
        player_instance.rect.bottom = player_hitbox_instance.rect.bottom-2
        hall.play()
        return health

#vytvoření textu
def text(text_size, text, x, y, text_color, text_font, align, sysfont):
    if sysfont:
        font = pygame.font.SysFont(text_font, text_size)
    else:        
        font = pygame.font.Font(text_font, text_size)
    text = font.render(text, True, text_color)
    text_rect = text.get_rect()
    if align == "topleft":
        text_rect.topleft = (x,y)
    if align == "midtop":
        text_rect.midtop = (x,y)
    if align == "topright":
        text_rect.topright = (x,y)
    if align == "midleft":
        text_rect.midleft = (x,y)
    if align == "center":
        text_rect.center = (x,y)
    if align == "midright":
        text_rect.midright = (x,y)
    if align == "bottomleft":
        text_rect.bottomleft = (x,y)
    if align == "midbottom":
        text_rect.midbottom = (x,y)
    if align == "midright":
        text_rect.midright = (x,y)
        
    screen.blit(text, text_rect)
    return text_rect
    
    
#načtení zdí specificky
def random_zdi(mapka,ind,door):
    global mozne_prechody
    zdi = pygame.sprite.Group()
    for radek_ind,radek in enumerate(mapka):
        for symbol_ind,symbol in enumerate(radek):
            if symbol == "6":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_0",mapka[2][1]))
            elif symbol == "9":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_1",mapka[2][1]))
            elif symbol == "12":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_2",mapka[2][1]))
            elif symbol == "15":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"zeď_3",mapka[2][1])) 
            elif symbol == "7":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_0",mapka[2][1])) 
            elif symbol == "10":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_1",mapka[2][1]))
            elif symbol == "13":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_2",mapka[2][1])) 
            elif symbol == "16":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnitřní_roh_3",mapka[2][1]))  
            elif symbol == "8":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnější_roh_0",mapka[2][1]))  
            elif symbol == "11":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnější_roh_1",mapka[2][1]))  
            elif symbol == "14":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnější_roh_2",mapka[2][1]))
            elif symbol == "17":
                zdi.add(zed((symbol_ind*32,radek_ind*32),"vnější_roh_3",mapka[2][1]))
                
        if "1" in radek or "2" in radek or "3" in radek or "4" in radek:
            if door == "regular_door":
                mozne_prechody.append(ind)
    return zdi

#načtení obrazovek
def urceni_sprite_group(mapa):
    podlaha = pygame.sprite.Group()
    dvere = pygame.sprite.Group()
    for radek_ind,radek in enumerate(mapa[0]):
        for symbol_ind,symbol in enumerate(radek):
            if symbol == "18":
                podlaha.add(zed((symbol_ind*32,radek_ind*32),"void",mapa[2][1]))
            elif symbol == "5":
                podlaha.add(zed((symbol_ind*32,radek_ind*32),"podlaha",mapa[2][1]))
            elif symbol == "1":
                dvere.add(zed((symbol_ind*32,radek_ind*32),"dveře_0",mapa[2][1]))
            elif symbol == "2":
                dvere.add(zed((symbol_ind*32,radek_ind*32),"dveře_1",mapa[2][1]))
            elif symbol == "3":
                dvere.add(zed((symbol_ind*32,radek_ind*32),"dveře_2",mapa[2][1]))
            elif symbol == "4":
                dvere.add(zed((symbol_ind*32,radek_ind*32),"dveře_3",mapa[2][1]))
    return podlaha,dvere

wall_map = []
for line_ind,line in enumerate(game_map):
    new = []
    for something_ind,something in enumerate(line):
        if something != []:
            new.append(random_zdi(something[0],[line_ind,something_ind],something[2][1]))
        else: new.append(None)
    wall_map.append(new)
    
podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])
zdi = wall_map[current_position[0]][current_position[1]]

#restart
def restart():
    global current_position,podlaha,dvere,zdi,minimap,game_map,wall_map,master
    game_map,master,minimap = generate()
    current_position = master
    player_hitbox_instance.rect.center = (width//2,heigth//2)
    
    wall_map = []
    for line_ind,line in enumerate(game_map):
        new = []
        for something_ind,something in enumerate(line):
            if something != []:
                new.append(random_zdi(something[0],[line_ind,something_ind],something[2][1]))
            else: new.append(None)
        wall_map.append(new)
        
    podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])
    zdi = wall_map[current_position[0]][current_position[1]]
    invKey.completed = True
    invBoots.completed = True
    inventoryKey_grp.update()
    inventoryBoots_grp.update()

#kód pro ztmavení obrazovky
fade = pygame.Surface((23*32, 14*32))
fade.fill("black")
pruhlednost = 0
pruhlednost_textu = 0
fade.set_alpha(pruhlednost)
fade_speed = 10

#gamestates
inGame = False
gameOver = False
inMenu = True
vyhra = False

#main loop
while True:
    #vypnutí
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            pygame.mixer.quit()
        if pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
            pygame.mixer.quit()
    
    if inMenu:
        screen.fill("black")
        
        #pohyb přetz tab
        if pressed[pygame.K_TAB] and cheat_timeout < 0:
            if pressed[pygame.K_RSHIFT] or pressed[pygame.K_LSHIFT]:
                if menu_state == None: menu_state = 2
                elif menu_state != 0: menu_state -= 1
                else: menu_state = 2
            else:
                if menu_state == None: menu_state = 0
                elif menu_state != 2: menu_state += 1
                else: menu_state = 0
            cheat_timeout = 10
        cheat_timeout -=1
        
        #povrchy
        txt_bg = pygame.image.load("../data/menu/text_bg.png").convert_alpha()
        txt_bg_rect = txt_bg.get_rect(topright=(23*32, 0))
        start_highlight = pygame.image.load("../data/menu/start_highlight.png").convert_alpha()
        start_highlight_rect = start_highlight.get_rect(topright=(23*32 - 8, 8))
        credits_highlight = pygame.image.load("../data/menu/credits_highlight.png").convert_alpha()
        credits_highlight_rect = credits_highlight.get_rect(topright=(23*32 - 10, 13))
        exit_highlight = pygame.image.load("../data/menu/exit_highlight.png").convert_alpha()
        exit_highlight_rect = exit_highlight.get_rect(topright=(23*32 - 15, 15))
        
        #vykreslování
        screen.blit(txt_bg, txt_bg_rect)
        text(50, "START", 23*32 - 225, 100, (255, 255, 255), "../data/fonts/ARCADECLASSIC.TTF", "topleft", False)
        text(50, "CREDITS", 23*32 - 225, 200, (255, 255, 255), "../data/fonts/ARCADECLASSIC.TTF", "topleft", False)
        text(50, "EXIT", 23*32 - 225, 300, (255, 255, 255), "../data/fonts/ARCADECLASSIC.TTF", "topleft", False)
        
        #kolize myši s tlačítky v menu
        if text(50, "START", 23*32 - 225, 100, (255, 255, 255), "../data/fonts/ARCADECLASSIC.TTF", "topleft", False).collidepoint(pygame.mouse.get_pos()) or menu_state == 0:
            screen.blit(start_highlight, start_highlight_rect)
            menu_state = 0
            
        if text(50, "CREDITS", 23*32 - 225, 200, (255, 255, 255), "../data/fonts/ARCADECLASSIC.TTF", "topleft", False).collidepoint(pygame.mouse.get_pos()) or menu_state == 1:
            screen.blit(credits_highlight, credits_highlight_rect)
            menu_state = 1
            
        if text(50, "EXIT", 23*32 - 225, 300, (255, 255, 255), "../data/fonts/ARCADECLASSIC.TTF", "topleft", False).collidepoint(pygame.mouse.get_pos()) or menu_state == 2:
            screen.blit(exit_highlight, exit_highlight_rect)
            menu_state = 2
            
        if (text(50, "START", 23*32 - 225, 100, (255, 255, 255), "../data/fonts/ARCADECLASSIC.TTF", "topleft", False).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) or ((pressed[pygame.K_KP_ENTER] or pressed[pygame.K_RETURN]) and menu_state == 0):
            inMenu = False
            inGame = True
            menu_state = None
            hall.play()
        
        if (text(50, "CREDITS", 23*32 - 225, 200, (255, 255, 255), "../data/fonts/ARCADECLASSIC.TTF", "topleft", False).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) or ((pressed[pygame.K_KP_ENTER] or pressed[pygame.K_RETURN]) and menu_state == 1):
            print("Zde budou kredity")
            menu_state = None
        

        if (text(50, "EXIT", 23*32 - 225, 300, (255, 255, 255), "../data/fonts/ARCADECLASSIC.TTF", "topleft", False).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) or ((pressed[pygame.K_KP_ENTER] or pressed[pygame.K_RETURN]) and menu_state == 2):
            pygame.quit()
            pygame.mixer.quit()
            sys.exit()
    
    elif inGame:
        #cheaty
        if pressed[pygame.K_h] and cheat_timeout < 0:
            if hitbox == False:
                hitbox = True
                player_hitbox_instance.showHitBox()
            else:
                hitbox = False
                player_hitbox_instance.hideHitBox()
            cheat_timeout = 20
                
        if pressed[pygame.K_n] and cheat_timeout < 0:
            if clip: clip = False
            else: clip = True
            cheat_timeout = 20
            
        if pressed[pygame.K_m] and cheat_timeout < 0:
            if show_minimap: show_minimap = False
            else: show_minimap = True
            cheat_timeout = 20
            
        if pressed[pygame.K_g] and cheat_timeout < 0:
            health = 0
            cheat_timeout = 20
        
        if pressed[pygame.K_t] and cheat_timeout < 0:
            current_time = default_time
            cheat_timeout = 20
            
        if pressed[pygame.K_1] and cheat_timeout < 0:
            inventoryKey_grp.update()
            cheat_timeout = 20
            
        if pressed[pygame.K_2] and cheat_timeout < 0:
            inventoryBoots_grp.update()
            cheat_timeout = 20
            
        if pressed[pygame.K_3] and cheat_timeout < 0:
            inGame = False
            vyhra = True
            cheat_timeout = 20
            hall.stop()
            
        if pressed[pygame.K_p] and cheat_timeout < 0:
            if show_minigame == False:
                show_minigame = True
            else:
                show_minigame = False
            cheat_timeout = 20
        cheat_timeout -= 1
        
        #pohyb
        posun_x = 0
        posun_y = 0
        if player_movable:
            if pressed[pygame.K_a]:
                posun_x -= player_speed
                image = "player_l"
            if pressed[pygame.K_d]:
                posun_x += player_speed
                image = "player_r"
            if pressed[pygame.K_w]:
                posun_y -= player_speed
                image = "player_b"
            if pressed[pygame.K_s]:
                posun_y += player_speed
                image = "player_f"
            
            player_hitbox_instance.posun_x(posun_x)

        #kolize se zdmi
        if clip:
            for wall in zdi:
                if wall.rect.collidepoint(player_hitbox_instance.rect.topleft) or wall.rect.collidepoint(player_hitbox_instance.rect.bottomleft):
                    player_hitbox_instance.rect.left = wall.rect.right+1
                if wall.rect.collidepoint(player_hitbox_instance.rect.topright) or wall.rect.collidepoint(player_hitbox_instance.rect.bottomright):
                    player_hitbox_instance.rect.right = wall.rect.left-1
                    
        player_hitbox_instance.posun_y(posun_y)
            
        if clip:
            for wall in zdi:
                if wall.rect.collidepoint(player_hitbox_instance.rect.topleft) or wall.rect.collidepoint(player_hitbox_instance.rect.topright):
                    player_hitbox_instance.rect.top = wall.rect.bottom+1
                if wall.rect.collidepoint(player_hitbox_instance.rect.bottomleft) or wall.rect.collidepoint(player_hitbox_instance.rect.bottomright):
                    player_hitbox_instance.rect.bottom = wall.rect.top-1
        
        #pohyb mezi obrazovkami
        if player_hitbox_instance.rect.left < 0:
            player_hitbox_instance.rect.right = width
            current_position[1] -=1
            podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])
            zdi = wall_map[current_position[0]][current_position[1]]
        elif player_hitbox_instance.rect.right > width:
            player_hitbox_instance.rect.left = 0
            current_position[1] +=1
            podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])
            zdi = wall_map[current_position[0]][current_position[1]]
        elif player_hitbox_instance.rect.top < 0:
            player_hitbox_instance.rect.bottom = heigth
            current_position[0] -=1
            podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])
            zdi = wall_map[current_position[0]][current_position[1]]
        elif player_hitbox_instance.rect.bottom > heigth:
            player_hitbox_instance.rect.top = 0
            current_position[0] +=1
            podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])
            zdi = wall_map[current_position[0]][current_position[1]]
            
        #zbytek pohybu
        player_instance.rect.centerx = player_hitbox_instance.rect.centerx
        player_instance.rect.bottom = player_hitbox_instance.rect.bottom+1
        
        #kolize s dvermi
        if pygame.sprite.spritecollide(hrac_hitbox, dvere, False):
            for door in dvere:
                if door.door_type == "regular_door":
                    health = play_minigame()
                    current_time = default_time
                elif door.door_type == "KEY_ROOM":
                    player_hitbox_instance.rect.center = vystup(current_position)
                    player_instance.rect.centerx = player_hitbox_instance.rect.centerx+4
                    player_instance.rect.bottom = player_hitbox_instance.rect.bottom-2
                    if not invKey.completed: inventoryKey_grp.update()
                elif door.door_type == "LOCKER_ROOM":
                    player_hitbox_instance.rect.center = vystup(current_position)
                    player_instance.rect.centerx = player_hitbox_instance.rect.centerx+4
                    player_instance.rect.bottom = player_hitbox_instance.rect.bottom-2
                    if not invBoots.completed and invKey.completed: inventoryBoots_grp.update()
                elif door.door_type == "EXIT":
                    player_hitbox_instance.rect.center = vystup(current_position)
                    player_instance.rect.centerx = player_hitbox_instance.rect.centerx+4
                    player_instance.rect.bottom = player_hitbox_instance.rect.bottom-2
                    if invBoots.completed:
                        inGame = False
                        vyhra = True
                        hall.stop()
        
        #vykreslování
        screen.fill("black")
        zdi.draw(screen)
        podlaha.draw(screen)
        dvere.draw(screen)
        if show_minimap:
            screen.blit(minimap,mimimap_pos)
            screen.blit(ukazatel,(current_position[1]*20+mimimap_pos[0],current_position[0]*12+mimimap_pos[1]))
        hrac_display_grp.update()
        hrac_display_grp.draw(screen)
        hrac_hitbox_grp.draw(screen)
        health_bar.vykresleni_baru()
        health_bar.vykresleni_predelu(health_max, health)
        health_bar.vykresleni_borderu()
        inventoryKey_grp.draw(screen)
        inventoryBoots_grp.draw(screen)
        counter_surface.topleft = (8,6)
        screen.blit(counter_texture, counter_surface)
        
        #časomíra
        current_time -= 0.016
        if current_time > 21: text(30, (str(int(current_time))), 24, 25, "gray", "rockwellcondensedtučné", "center", True)
        elif current_time > 0 : text(30, (str(int(current_time))), 24, 25, "red", "rockwellcondensedtučné", "center", True)
        else:
            hall.stop()
            if not skolnik.completed:
                postavy_display_grp.update()
                postavy_display_grp.draw(screen)
                player_movable = False
            else:
                current_position = random.choice(mozne_prechody)
                podlaha,dvere = urceni_sprite_group(game_map[current_position[0]][current_position[1]])
                zdi = wall_map[current_position[0]][current_position[1]]
                
                player_movable = True
                skolnik.completed = False
                health = play_minigame()
                current_time = default_time
        
        #prohra
        if health == 0:
            g_over_font = pygame.font.Font("../data/fonts/ARCADECLASSIC.TTF", 125)
            return_font = pygame.font.Font("../data/fonts/ARCADECLASSIC.TTF", 50)
            g_over_font_render = g_over_font.render("GAME OVER", True, (255, 0, 0))
            return_font_render = return_font.render("PRESS   ENTER", True, (100, 0, 0))
            g_over_font_rect = g_over_font_render.get_rect(center=(23*32/2, 14*32/2))
            return_font_rect = return_font_render.get_rect(center=(23*32/2, 14*32/2 + 75))
            g_over_font_render.set_alpha(0)
            return_font_render.set_alpha(0)
            
            while pruhlednost <= 12:
                pruhlednost += 0.1
                pruhlednost_textu += 1.5
                fade.set_alpha(pruhlednost)
                g_over_font_render.set_alpha(pruhlednost_textu)
                return_font_render.set_alpha(pruhlednost_textu)
                screen.blit(fade, (0, 0))
                screen.blit(g_over_font_render, g_over_font_rect)
                screen.blit(return_font_render, return_font_rect)
                pygame.display.update()
                pygame.time.wait(fade_speed)
            
            health = -1
            inGame = False
            gameOver = True
            hall.stop()
            pruhlednost = 255
            fade.set_alpha(pruhlednost)
            g_over_font_render.set_alpha(pruhlednost)
            return_font_render.set_alpha(pruhlednost)
            
        #školník
        if current_time == 0:
            x_hrace = player_instance.prevPosX
            y_hrace = player_instance.prevPosY
            janitor(x_hrace, y_hrace)
            
    if gameOver:
        pruhlednost = 0
        if pressed[pygame.K_RETURN]:
            gameOver = False
            inMenu = True
            restart()
            current_time = default_time
            health = health_max
    
    #vyhra
    if vyhra:
        BARVA_POZADI = (0, 0, 0)
        barva_zpravy = (0, 0, 0)
        barva_textu = (0, 0, 0)
        okno = pygame.display.set_mode((736,448))
        font = pygame.font.SysFont("Comic Sans MS", 42)
        
        if not gameOver:
            zprava = "Vyhráls."
        else:
            zprava = "Nevyhráls."
            
        pygame.display.set_caption(zprava)

            
        nabidka = "q - odejít   m - \"menu\""
            
        while vyhra:
            udalost = pygame.event.get()
            stisknuto = pygame.key.get_pressed()
            for u in udalost:
                if u.type == pygame.QUIT:
                    pygame.quit()
                    pygame.mixer.quit()
                    sys.exit()
                    
                elif u.type == pygame.KEYDOWN:
                    if u.key == pygame.K_q:
                        pygame.quit()
                        pygame.mixer.quit()
                        sys.exit()
                    if u.key == pygame.K_m:
                        inMenu = True
                        vyhra = False
                        
            time.sleep(0.05)
            
            if barva_zpravy == (0, 255, 0):
                barva_zpravy = (255, 255, 0)
            else:
                barva_zpravy = (0, 255, 0)  
            if barva_textu == (255, 255, 255):
                barva_textu = (255, 255, 0)
            else:
                barva_textu = (255, 255, 255)
            
            vyhra_text = font.render(zprava, True, barva_zpravy)
            text_vyhra = font.render(nabidka, True, barva_textu)
            
            okno.fill(BARVA_POZADI)
            okno.blit(vyhra_text, (0,0))
            okno.blit(text_vyhra, (0,50))
            
            pygame.display.update()
        else:
            restart()
            current_time = default_time
            health = health_max
    pygame.display.update()
    clock.tick(60)