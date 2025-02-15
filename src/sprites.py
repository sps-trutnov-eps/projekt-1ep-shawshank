import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

import pygame,random

from animations import playerAnim, janitorAnim, playerMenuAnim, janitorMenuAnim
pygame.init()

width,heigth = 23*32,14*32
screen = pygame.display.set_mode((width,heigth))
pygame.display.set_caption("¤ Útek ze stredni průmyslove Shawshank ¤")

images = {"zed_0" : pygame.image.load(DATA_ROOT + "/data/textury_hry/zed_0.png").convert(),
          "zed_1" : pygame.image.load(DATA_ROOT + "/data/textury_hry/zed_1.png").convert(),
          "zed_2" : pygame.image.load(DATA_ROOT + "/data/textury_hry/zed_2.png").convert(),
          "zed_3" : pygame.image.load(DATA_ROOT + "/data/textury_hry/zed_3.png").convert(),
          
          "vnitrni_roh_0" : pygame.image.load(DATA_ROOT + "/data/textury_hry/vnitrni_roh_0.png").convert(),
          "vnitrni_roh_1" : pygame.image.load(DATA_ROOT + "/data/textury_hry/vnitrni_roh_1.png").convert(),
          "vnitrni_roh_2" : pygame.image.load(DATA_ROOT + "/data/textury_hry/vnitrni_roh_2.png").convert(),
          "vnitrni_roh_3" : pygame.image.load(DATA_ROOT + "/data/textury_hry/vnitrni_roh_3.png").convert(),
          
          
          "vnejsi_roh_0" : pygame.image.load(DATA_ROOT + "/data/textury_hry/vnejsi_roh_0.png").convert(),
          "vnejsi_roh_1" : pygame.image.load(DATA_ROOT + "/data/textury_hry/vnejsi_roh_1.png").convert(),
          "vnejsi_roh_2" : pygame.image.load(DATA_ROOT + "/data/textury_hry/vnejsi_roh_2.png").convert(),
          "vnejsi_roh_3" : pygame.image.load(DATA_ROOT + "/data/textury_hry/vnejsi_roh_3.png").convert(),
          
          "dvere_0" : pygame.image.load(DATA_ROOT + "/data/textury_hry/dvere_0.png").convert(),
          "dvere_1" : pygame.image.load(DATA_ROOT + "/data/textury_hry/dvere_1.png").convert(),
          "dvere_2" : pygame.image.load(DATA_ROOT + "/data/textury_hry/dvere_2.png").convert(),
          "dvere_3" : pygame.image.load(DATA_ROOT + "/data/textury_hry/dvere_3.png").convert(),
          
          "podlaha" : pygame.image.load(DATA_ROOT + "/data/textury_hry/podlaha.png").convert(),
          "void" : pygame.image.load(DATA_ROOT + "/data/textury_hry/void.png").convert(),
          
          "special_0" : pygame.image.load(DATA_ROOT + "/data/textury_hry/special_dvere_0.png").convert(),
          "special_1" : pygame.image.load(DATA_ROOT + "/data/textury_hry/special_dvere_1.png").convert(),
          "special_2" : pygame.image.load(DATA_ROOT + "/data/textury_hry/special_dvere_2.png").convert(),
          
          "podlaha_dark" : pygame.image.load(DATA_ROOT + "/data/textury_hry/dark_podlaha.png").convert(),
          "podlaha_dark_blood" : pygame.image.load(DATA_ROOT + "/data/textury_hry/dark_podlaha_blood.png").convert(),
          "podlaha_dark_blooood" : pygame.image.load(DATA_ROOT + "/data/textury_hry/dark_podlaha_blooood.png").convert(),
          "podlaha_kachlicky" : pygame.image.load(DATA_ROOT + "/data/textury_hry/kachlicky.png").convert(),
          "podlaha_dark_flek" : pygame.image.load(DATA_ROOT + "/data/textury_hry/dark_podlaha_flek.png").convert(),
          "podlaha_dark_prkno" : pygame.image.load(DATA_ROOT + "/data/textury_hry/dark_podlaha_prkno.png").convert(),
        
          "lavicka_horizontalni" : pygame.image.load(DATA_ROOT + "/data/textury_hry/horizontalni_lavicka_base.png").convert(),
          "lavicka_horizontalni_konec_leva" : pygame.image.load(DATA_ROOT + "/data/textury_hry/horizontalni_lavicka.png").convert_alpha(),
          "lavicka_horizontalni_konec_prava" : pygame.transform.flip(pygame.image.load(DATA_ROOT + "/data/textury_hry/horizontalni_lavicka.png").convert_alpha(), True, False),
          "lavicka_vertikalni" : pygame.image.load(DATA_ROOT + "/data/textury_hry/lavicka_vertikalni.png").convert(),
          "lavicka_vertikalni_konec1" : pygame.image.load(DATA_ROOT + "/data/textury_hry/lavicka_vertikalni_konec.png").convert(),
          "lavicka_vertikalni_konec2" : pygame.image.load(DATA_ROOT + "/data/textury_hry/lavicka_vertikalni_konec_1.png").convert_alpha(),
          
          "skrinka_vertikalni" : pygame.image.load(DATA_ROOT + "/data/textury_hry/horizontalni_skrinka.png").convert(),
          "skrinka_vertikalni_spodek" : pygame.image.load(DATA_ROOT + "/data/textury_hry/horizontalni_skrinka_spodek.png").convert(),
          "skrinka_vertikalni_vrsek" : pygame.image.load(DATA_ROOT + "/data/textury_hry/horizontalni_skrinka_vrsek.png").convert_alpha(),
          "skrinka_horizontalni" : pygame.image.load(DATA_ROOT + "/data/textury_hry/skrinka.png").convert(),
          "skrinka_horizontalni_otevrena" : pygame.image.load(DATA_ROOT + "/data/textury_hry/skrinka_otevrena.png").convert(),
          "skrinka_horizontalni_zamek" : pygame.image.load(DATA_ROOT + "/data/textury_hry/skrinka_se_zamkem.png").convert(),
          
          "kos" : pygame.image.load(DATA_ROOT + "/data/textury_hry/kos_satni.png").convert_alpha(),
          
          "odpatkove_pytle_biologicke" : pygame.image.load(DATA_ROOT + "/data/textury_hry/pytel_biologickeho_odpdu.png").convert_alpha(),
          "odpatkove_pytle" : pygame.image.load(DATA_ROOT + "/data/textury_hry/pytel_normalni.png").convert_alpha(),
          
          "skrin" : pygame.image.load(DATA_ROOT + "/data/textury_hry/skrin.png").convert(),
          "skrin_bok" : pygame.image.load(DATA_ROOT + "/data/textury_hry/skrin_bok.png").convert(),
          
          #Proc se stoly pisi slovensky ?
          #Lip_se_to_pise
          "stul_dole" : pygame.image.load(DATA_ROOT + "/data/textury_hry/stool_skolnikov_dole.png").convert_alpha(),
          "stul_dole_normalni" : pygame.image.load(DATA_ROOT + "/data/textury_hry/stůl_skolnik_dolnicast_normalni.png").convert_alpha(),
          "stul_hore" : pygame.image.load(DATA_ROOT + "/data/textury_hry/stool_skolnikov_hore.png").convert_alpha(),
          "stul_hore_normalni" : pygame.image.load(DATA_ROOT + "/data/textury_hry/stůl_skolnik_hornicast_normalni.png").convert_alpha(),
          "stul_stred" : pygame.image.load(DATA_ROOT + "/data/textury_hry/stool_skolnikov_stred.png").convert_alpha(),
          "stul_stred_klic" : pygame.image.load(DATA_ROOT + "/data/textury_hry/stool_skolnikov_stred_klice.png").convert_alpha()}

dekorace_0 = (pygame.image.load(DATA_ROOT + "/data/decorations/missing_poster_0.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/nastenka_0_0.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/nastenka_1_0.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/Peta_0.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/sipka_0.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/trofeje_0.png").convert())

dekorace_1 = (pygame.image.load(DATA_ROOT + "/data/decorations/missing_poster_1.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/nastenka_0_1.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/nastenka_1_1.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/Peta_1.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/sipka_1.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/trofeje_1.png").convert())

dekorace_2= (pygame.image.load(DATA_ROOT + "/data/decorations/missing_poster_2.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/nastenka_0_2.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/nastenka_1_2.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/Peta_2.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/sipka_2.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/trofeje_2.png").convert())

dekorace_3 = (pygame.image.load(DATA_ROOT + "/data/decorations/missing_poster_3.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/nastenka_0_3.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/nastenka_1_3.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/Peta_3.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/sipka_3.png").convert(),
              pygame.image.load(DATA_ROOT + "/data/decorations/trofeje_3.png").convert())

pygame.display.set_icon(images["special_0"])

class zed(pygame.sprite.Sprite):
    def __init__(self,pozice,textura,door_type):
        super().__init__()
        self.textura = textura
        if "zed" in textura:
            if random.randint(0,15): self.image = images[textura]
            else:
                if "0" in textura: self.image = random.choice(dekorace_0)
                elif "1" in textura: self.image = random.choice(dekorace_1)
                elif "2" in textura: self.image = random.choice(dekorace_2)
                else: self.image = random.choice(dekorace_3)
        elif "dvere" in textura:
            if door_type == "EXIT":
                if "0" in textura: self.image = images["special_0"]
                elif "1" in textura: self.image = pygame.transform.rotate(images["special_0"],-90)
                elif "2" in textura: self.image = pygame.transform.rotate(images["special_0"],180)
                elif "3" in textura: self.image = pygame.transform.rotate(images["special_0"],90)
            elif door_type == "KEY_ROOM":
                if "0" in textura: self.image = images["special_1"]
                elif "1" in textura: self.image = pygame.transform.rotate(images["special_1"],-90)
                elif "2" in textura: self.image = pygame.transform.rotate(images["special_1"],180)
                elif "3" in textura: self.image = pygame.transform.rotate(images["special_1"],90)
            elif door_type == "LOCKER_ROOM":
                if "0" in textura: self.image = images["special_2"]
                elif "1" in textura: self.image = pygame.transform.rotate(images["special_2"],-90)
                elif "2" in textura: self.image = pygame.transform.rotate(images["special_2"],180)
                elif "3" in textura: self.image = pygame.transform.rotate(images["special_2"],90)
            else: self.image = images[textura]
        else: self.image = images[textura]
        self.rect = self.image.get_rect(topleft = (pozice))
        self.door_type = door_type
        if door_type == "master": self.door_type = "regular_door"
        
class player(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        
        self.prevPosX = player_x
        self.prevPosY = player_y
        
        self.image = playerAnim(player_x, player_y, self.prevPosX, self.prevPosY)
        self.rect = self.image.get_rect()
        self.rect.center = (player_y, player_x)
        
        self.prevPosX = self.rect.centerx
        self.prevPosY = self.rect.centery
        
    def update(self):
        
        self.image = playerAnim(self.rect.centerx, self.rect.centery, self.prevPosX, self.prevPosY)
        
        self.prevPosX = self.rect.centerx
        self.prevPosY = self.rect.centery
        
class menuPlayer(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        
        self.image = playerMenuAnim(100, 200)
        self.rect = self.image.get_rect()
        self.rect.center = (player_y, player_x)
        
    def update(self):
        self.image = playerMenuAnim(100, 200)
        
class menuJanitor(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        
        self.image = janitorMenuAnim(300, 400)
        self.rect = self.image.get_rect()
        self.rect.center = (player_y, player_x)
        
    def update(self):
        self.image = janitorMenuAnim(300, 400)
        
class player_hitbox(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        self.image = pygame.image.load(DATA_ROOT + "/data/textury_hrac/player_hitbox.png").convert_alpha()
        self.hitBox = pygame.image.load(DATA_ROOT + "/data/textury_hrac/player_hitbox.png").convert_alpha()
        self.visibleHitBox = pygame.image.load(DATA_ROOT + "/data/textury_hrac/player_hitbox_visible.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (width//2,heigth//2)
        self.hitbox = False
        
    def posun_x(self, player_x):
        self.rect.centerx += player_x
    def posun_y(self,player_y):
        self.rect.centery += player_y
    
    def showHitBox(self):
        if self.hitbox == False:
            self.hitbox = True
            self.image = self.visibleHitBox
            
    def hideHitBox(self):
        if self.hitbox == True:
            self.hitbox = False
            self.image = self.hitBox
            
class janitor(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        
        self.player = player
        self.prevPosX = player.prevPosX
        self.prevPosY = player.prevPosY
        
        self.image, self.completed = janitorAnim(self.prevPosX, self.prevPosY, self.prevPosX, self.prevPosY)
        self.rect = self.image.get_rect()
        self.rect.center = (self.prevPosY, self.prevPosX)
        
        self.prevPosX = self.rect.centerx
        self.prevPosY = self.rect.centery
        
    def update(self):
        
        self.image, self.completed = janitorAnim(self.rect.centerx, self.rect.centery, self.prevPosX, self.prevPosY)
        
        self.prevPosX = self.rect.centerx = self.player.prevPosX
        self.prevPosY = self.rect.centery = self.player.prevPosY
            
class Health_bar(pygame.sprite.Sprite):
    def __init__(self, pozice, okno):
        self.textura = pygame.image.load(DATA_ROOT + "/data/hud/health_bar/health_bar.png").convert_alpha()
        self.rect = self.textura.get_rect()
        self.rect.center = pozice
        self.okno = okno
        self.border = pygame.image.load(DATA_ROOT + "/data/hud/health_bar/health_bar_border.png").convert_alpha()
        
    def vykresleni_baru(self):
        self.okno.blit(self.textura, self.rect)
        
    def vykresleni_borderu(self):
        self.okno.blit(self.border, self.rect)    

    def vykresleni_predelu(self, health_max, health):
        #health bar - výpocty segmentů
        health_bar_segments = health_max
        velikost_health_baru = self.rect.width
        jeden_segment = round(velikost_health_baru / health_bar_segments)
        x_segmentu = 268
        x_prazdneho_mista = 467 - jeden_segment
        
        #health bar - vykreslovani predelů
        for predel in range(health_bar_segments - 1):
            pygame.draw.line(self.okno, (0, 0, 0), ((x_segmentu + jeden_segment),(12)),((x_segmentu + jeden_segment),(12+24)), 2)
            x_segmentu = x_segmentu + jeden_segment
        
        #health_bar - vykresleni prazdných mist health baru
        for mezera in range(health_max - health):
            pygame.draw.rect(self.okno, (0, 0, 0), (x_prazdneho_mista, 12, jeden_segment, 26))
            x_prazdneho_mista = x_prazdneho_mista - jeden_segment
