import pygame,random

from animations import playerAnim, janitorAnim
pygame.init()

width,heigth = 23*32,14*32
screen = pygame.display.set_mode((width,heigth))
pygame.display.set_caption("¤Útěk ze střední průmyslové Shawshank¤")

images = {"zeď_0" : pygame.image.load("../data/textury_hry/zeď_0.png").convert(),
          "zeď_1" : pygame.image.load("../data/textury_hry/zeď_1.png").convert(),
          "zeď_2" : pygame.image.load("../data/textury_hry/zeď_2.png").convert(),
          "zeď_3" : pygame.image.load("../data/textury_hry/zeď_3.png").convert(),
          
          "vnitřní_roh_0" : pygame.image.load("../data/textury_hry/vnitřní_roh_0.png").convert(),
          "vnitřní_roh_1" : pygame.image.load("../data/textury_hry/vnitřní_roh_1.png").convert(),
          "vnitřní_roh_2" : pygame.image.load("../data/textury_hry/vnitřní_roh_2.png").convert(),
          "vnitřní_roh_3" : pygame.image.load("../data/textury_hry/vnitřní_roh_3.png").convert(),
          
          
          "vnější_roh_0" : pygame.image.load("../data/textury_hry/vnější_roh_0.png").convert(),
          "vnější_roh_1" : pygame.image.load("../data/textury_hry/vnější_roh_1.png").convert(),
          "vnější_roh_2" : pygame.image.load("../data/textury_hry/vnější_roh_2.png").convert(),
          "vnější_roh_3" : pygame.image.load("../data/textury_hry/vnější_roh_3.png").convert(),
          
          "dveře_0" : pygame.image.load("../data/textury_hry/dveře_0.png").convert(),
          "dveře_1" : pygame.image.load("../data/textury_hry/dveře_1.png").convert(),
          "dveře_2" : pygame.image.load("../data/textury_hry/dveře_2.png").convert(),
          "dveře_3" : pygame.image.load("../data/textury_hry/dveře_3.png").convert(),
          
          "podlaha" : pygame.image.load("../data/textury_hry/podlaha.png").convert(),
          "void" : pygame.image.load("../data/textury_hry/void.png").convert(),
          
          "special_0" : pygame.image.load("../data/textury_hry/special_dveře_0.png").convert(),
          "special_1" : pygame.image.load("../data/textury_hry/special_dveře_1.png").convert(),
          "special_2" : pygame.image.load("../data/textury_hry/special_dveře_2.png").convert(),
          
          "podlaha_dark" : pygame.image.load("../data/textury_hry/dark_podlaha.png").convert(),
          "podlaha_dark_blood" : pygame.image.load("../data/textury_hry/podlaha.png").convert(),
          "podlaha_dark_blooood" : pygame.image.load("../data/textury_hry/podlaha.png").convert(),
          "podlaha_kachlicky" : pygame.image.load("../data/textury_hry/kachličky.png").convert(),
          
          "lavicka_horizontalni" : pygame.image.load("../data/textury_hry/horizontalni_lavicka_base.png").convert(),
          "lavicka_horizontalni_konec" : pygame.image.load("../data/textury_hry/horizontální_lavička.png").convert(),
          "lavicka_vertikalni" : pygame.image.load("../data/textury_hry/lavička_vertikální.png").convert(),
          "lavicka_vertikalni_konec1" : pygame.image.load("../data/textury_hry/lavička_vertikální_konec.png").convert(),
          "lavicka_vertikalni_konec2" : pygame.image.load("../data/textury_hry/lavička_vertikální_konec_1.png").convert(),
          
          "skrinka_vertikalni" : pygame.image.load("../data/textury_hry/horizontální_skříňka.png").convert(),
          "skrinka_vertikalni_spodek" : pygame.image.load("../data/textury_hry/horizontální_skříňka_spodek.png").convert(),
          "skrinka_vertikalni_vrsek" : pygame.image.load("../data/textury_hry/horizontální_skříňka_vršek.png").convert(),
          "skrinka_horizontalni" : pygame.image.load("../data/textury_hry/skříňka.png").convert(),
          "skrinka_horizontalni_otevrena" : pygame.image.load("../data/textury_hry/skříňka_otevřena.png").convert(),
          "skrinka_horizontalni_zamek" : pygame.image.load("../data/textury_hry/skříňka_se_zámkem.png").convert(),
          
          "kos" : pygame.image.load("../data/textury_hry/koš_šatní.png").convert(),
          
          "odpatkove_pytle" : pygame.image.load("../data/textury_hry/pytel_biologického_odpdu.png").convert(),
          
          "skrin" : pygame.image.load("../data/textury_hry/skříň.png").convert(),
          "skrin_bok" : pygame.image.load("../data/textury_hry/skříň_bok.png").convert(),
          
          #Proč se stoly píší slovensky ?
          "stul_dole" : pygame.image.load("../data/textury_hry/stool_školnikov_dole.png").convert(),
          "stul_hore" : pygame.image.load("../data/textury_hry/stool_školnikov_hore.png").convert(),
          "stul_stred" : pygame.image.load("../data/textury_hry/stool_školnikov_stred.png").convert(),}

dekorace_0 = (pygame.image.load("../data/decorations/missing_poster_0.png").convert(),
              pygame.image.load("../data/decorations/nástěnka_0_0.png").convert(),
              pygame.image.load("../data/decorations/nástěnka_1_0.png").convert(),
              pygame.image.load("../data/decorations/Péťa_0.png").convert(),
              pygame.image.load("../data/decorations/šipka_0.png").convert(),
              pygame.image.load("../data/decorations/trofeje_0.png").convert())

dekorace_1 = (pygame.image.load("../data/decorations/missing_poster_1.png").convert(),
              pygame.image.load("../data/decorations/nástěnka_0_1.png").convert(),
              pygame.image.load("../data/decorations/nástěnka_1_1.png").convert(),
              pygame.image.load("../data/decorations/Péťa_1.png").convert(),
              pygame.image.load("../data/decorations/šipka_1.png").convert(),
              pygame.image.load("../data/decorations/trofeje_1.png").convert())

dekorace_2= (pygame.image.load("../data/decorations/missing_poster_2.png").convert(),
              pygame.image.load("../data/decorations/nástěnka_0_2.png").convert(),
              pygame.image.load("../data/decorations/nástěnka_1_2.png").convert(),
              pygame.image.load("../data/decorations/Péťa_2.png").convert(),
              pygame.image.load("../data/decorations/šipka_2.png").convert(),
              pygame.image.load("../data/decorations/trofeje_2.png").convert())

dekorace_3 = (pygame.image.load("../data/decorations/missing_poster_3.png").convert(),
              pygame.image.load("../data/decorations/nástěnka_0_3.png").convert(),
              pygame.image.load("../data/decorations/nástěnka_1_3.png").convert(),
              pygame.image.load("../data/decorations/Péťa_3.png").convert(),
              pygame.image.load("../data/decorations/šipka_3.png").convert(),
              pygame.image.load("../data/decorations/trofeje_3.png").convert())

pygame.display.set_icon(images["special_1"])

class zed(pygame.sprite.Sprite):
    def __init__(self,pozice,textura,door_type):
        super().__init__()
        if "zeď" in textura:
            if random.randint(0,15): self.image = images[textura]
            else:
                if "0" in textura: self.image = random.choice(dekorace_0)
                elif "1" in textura: self.image = random.choice(dekorace_1)
                elif "2" in textura: self.image = random.choice(dekorace_2)
                else: self.image = random.choice(dekorace_3)
        elif "dveře" in textura:
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
        
class player_hitbox(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        self.image = pygame.image.load("../data/textury_hrac/player_hitbox.png").convert_alpha()
        self.hitBox = pygame.image.load("../data/textury_hrac/player_hitbox.png").convert_alpha()
        self.visibleHitBox = pygame.image.load("../data/textury_hrac/player_hitbox_visible.png").convert_alpha()
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
        self.textura = pygame.image.load("../data/hud/health_bar/health_bar.png").convert_alpha()
        self.rect = self.textura.get_rect()
        self.rect.center = pozice
        self.okno = okno
        self.border = pygame.image.load("../data/hud/health_bar/health_bar_border.png").convert_alpha()
        
    def vykresleni_baru(self):
        self.okno.blit(self.textura, self.rect)
        
    def vykresleni_borderu(self):
        self.okno.blit(self.border, self.rect)    

    def vykresleni_predelu(self, health_max, health):
        #health bar - výpočty segmentů
        health_bar_segments = health_max
        velikost_health_baru = self.rect.width
        jeden_segment = round(velikost_health_baru / health_bar_segments)
        x_segmentu = 268
        x_prazdneho_mista = 467 - jeden_segment
        
        #health bar - vykreslování předělů
        for predel in range(health_bar_segments - 1):
            pygame.draw.line(self.okno, (0, 0, 0), ((x_segmentu + jeden_segment),(12)),((x_segmentu + jeden_segment),(12+24)), 2)
            x_segmentu = x_segmentu + jeden_segment
        
        #health_bar - vykreslení prázdných míst health baru
        for mezera in range(health_max - health):
            pygame.draw.rect(self.okno, (0, 0, 0), (x_prazdneho_mista, 12, jeden_segment, 26))
            x_prazdneho_mista = x_prazdneho_mista - jeden_segment
