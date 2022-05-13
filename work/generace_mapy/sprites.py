import pygame,random
pygame.init()

width,heigth = 23*32,14*32
screen = pygame.display.set_mode((width,heigth))

images = {"zeď_0" : pygame.image.load("data/textury_hry/zeď_0.png").convert(),
          "zeď_1" : pygame.image.load("data/textury_hry/zeď_1.png").convert(),
          "zeď_2" : pygame.image.load("data/textury_hry/zeď_2.png").convert(),
          "zeď_3" : pygame.image.load("data/textury_hry/zeď_3.png").convert(),
          
          "vnitřní_roh_0" : pygame.image.load("data/textury_hry/vnitřní_roh_0.png").convert(),
          "vnitřní_roh_1" : pygame.image.load("data/textury_hry/vnitřní_roh_1.png").convert(),
          "vnitřní_roh_2" : pygame.image.load("data/textury_hry/vnitřní_roh_2.png").convert(),
          "vnitřní_roh_3" : pygame.image.load("data/textury_hry/vnitřní_roh_3.png").convert(),
          
          
          "vnější_roh_0" : pygame.image.load("data/textury_hry/vnější_roh_0.png").convert(),
          "vnější_roh_1" : pygame.image.load("data/textury_hry/vnější_roh_1.png").convert(),
          "vnější_roh_2" : pygame.image.load("data/textury_hry/vnější_roh_2.png").convert(),
          "vnější_roh_3" : pygame.image.load("data/textury_hry/vnější_roh_3.png").convert(),
          
          "dveře_0" : pygame.image.load("data/textury_hry/dveře_0.png").convert(),
          "dveře_1" : pygame.image.load("data/textury_hry/dveře_1.png").convert(),
          "dveře_2" : pygame.image.load("data/textury_hry/dveře_2.png").convert(),
          "dveře_3" : pygame.image.load("data/textury_hry/dveře_3.png").convert(),
          
          "podlaha" : pygame.image.load("data/textury_hry/podlaha.png").convert(),
          "void" : pygame.image.load("data/textury_hry/void.png").convert()}

dekorace_0 = (pygame.image.load("data/decorations/missing_poster_0.png").convert(),
              pygame.image.load("data/decorations/nástěnka_0_0.png").convert(),
              pygame.image.load("data/decorations/nástěnka_1_0.png").convert(),
              pygame.image.load("data/decorations/Péťa_0.png").convert(),
              pygame.image.load("data/decorations/šipka_0.png").convert(),
              pygame.image.load("data/decorations/trofeje_0.png").convert())

dekorace_1 = (pygame.image.load("data/decorations/missing_poster_1.png").convert(),
              pygame.image.load("data/decorations/nástěnka_0_1.png").convert(),
              pygame.image.load("data/decorations/nástěnka_1_1.png").convert(),
              pygame.image.load("data/decorations/Péťa_1.png").convert(),
              pygame.image.load("data/decorations/šipka_1.png").convert(),
              pygame.image.load("data/decorations/trofeje_1.png").convert())

dekorace_2= (pygame.image.load("data/decorations/missing_poster_2.png").convert(),
              pygame.image.load("data/decorations/nástěnka_0_2.png").convert(),
              pygame.image.load("data/decorations/nástěnka_1_2.png").convert(),
              pygame.image.load("data/decorations/Péťa_2.png").convert(),
              pygame.image.load("data/decorations/šipka_2.png").convert(),
              pygame.image.load("data/decorations/trofeje_2.png").convert())

dekorace_3 = (pygame.image.load("data/decorations/missing_poster_3.png").convert(),
              pygame.image.load("data/decorations/nástěnka_0_3.png").convert(),
              pygame.image.load("data/decorations/nástěnka_1_3.png").convert(),
              pygame.image.load("data/decorations/Péťa_3.png").convert(),
              pygame.image.load("data/decorations/šipka_3.png").convert(),
              pygame.image.load("data/decorations/trofeje_3.png").convert())

class zed(pygame.sprite.Sprite):
    def __init__(self,pozice,textura):
        super().__init__()
        if "zeď" in textura:
            if random.randint(0,15): self.image = images[textura]
            else:
                if "0" in textura: self.image = random.choice(dekorace_0)
                elif "1" in textura: self.image = random.choice(dekorace_1)
                elif "2" in textura: self.image = random.choice(dekorace_2)
                else: self.image = random.choice(dekorace_3)
        else: self.image = images[textura]
        self.rect = self.image.get_rect(topleft = (pozice))
        
class player(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        self.image = pygame.image.load("data/textury_hrac/player_front.png").convert_alpha()
        self.rect = self.image.get_rect(center = (player_x, player_y))
        
    def update(self, player_x, player_y):
        self.rect.centerx = player_x
        self.rect.centery = player_y
        
class player_hitbox(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        self.image = pygame.image.load("data/textury_hrac/player_hitbox.png").convert_alpha()
        self.hitBox = pygame.image.load("data/textury_hrac/player_hitbox.png").convert_alpha()
        self.visibleHitBox = pygame.image.load("data/textury_hrac/player_hitbox_visible.png").convert_alpha()
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
            
class Health_bar(pygame.sprite.Sprite):
    def __init__(self, pozice, okno):
        self.textura = pygame.image.load("data/health_bar/health_bar.png").convert_alpha()
        self.rect = self.textura.get_rect()
        self.rect.center = pozice
        self.okno = okno
        self.border = pygame.image.load("data/health_bar/health_bar_border.png").convert_alpha()
        
    def vykresleni_baru(self):
        self.okno.blit(self.textura, self.rect)
        
    def vykresleni_borderu(self):
        self.okno.blit(self.border, self.rect)    

    def vykresleni_predelu(self, health_max):
        #health bar - výpočty segmentů
        health_bar_segments = health_max
        velikost_health_baru = self.rect.width
        jeden_segment = round(velikost_health_baru / health_bar_segments)
        x_segmentu = 268
        x_prazdneho_mista = x_segmentu + (health_bar_segments - 1) * jeden_segment
        #print(jeden_segment)
        
        #health bar - vykreslování předělů
        for predel in range(health_bar_segments - 1):
            pygame.draw.line(self.okno, (0, 0, 0), ((x_segmentu + jeden_segment),(12)),((x_segmentu + jeden_segment),(12+24)), 2)
            x_segmentu = x_segmentu + jeden_segment
        
        #health_bar - vykreslení prázdných míst health baru
        if health == 5:
            return
        if health == 4:
            for prazdne_misto in range(health_bar_segments - 1):
                pygame.draw.rect(self.okno, (0, 0, 0), (x_prazdneho_mista, 12, jeden_segment, 26))
                x_prazdneho_mista = x_prazdneho_mista - 40
        if health == 3:
            for prazdne_misto in range(health_bar_segments - 2):
                pygame.draw.rect(self.okno, (0, 0, 0), (x_prazdneho_mista, 12, jeden_segment, 26))
                x_prazdneho_mista = x_prazdneho_mista - 40
        if health == 2:
            for prazdne_misto in range(health_bar_segments - 3):
                pygame.draw.rect(self.okno, (0, 0, 0), (x_prazdneho_mista, 12, jeden_segment, 26))
                x_prazdneho_mista = x_prazdneho_mista - 40
        if health == 1:
            for prazdne_misto in range(health_bar_segments - 4):
                pygame.draw.rect(self.okno, (0, 0, 0), (x_prazdneho_mista, 12, jeden_segment, 26))
                x_prazdneho_mista = x_prazdneho_mista - 40
        if health == 0:
            for prazdne_misto in range(health_bar_segments):
                pygame.draw.rect(self.okno, (0, 0, 0), (x_prazdneho_mista, 12, jeden_segment, 26))
                x_prazdneho_mista = x_prazdneho_mista - 40
            
        