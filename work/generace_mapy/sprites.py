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
    def __init__(self, player_x, player_y, imageType):
        super().__init__()
        self.angles = (pygame.image.load("data/textury_hrac/Player/Player_f.png").convert_alpha(),
                       pygame.image.load("data/textury_hrac/Player/Player_r.png").convert_alpha(),
                       pygame.image.load("data/textury_hrac/Player/Player_l.png").convert_alpha(),
                       pygame.image.load("data/textury_hrac/Player/Player_b.png").convert_alpha(),)
        
        #textury animací
        self.frontWalk = (pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_f/PlayerWalking_f1.png").convert_alpha(),
                          pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_f/PlayerWalking_f2.png").convert_alpha(),)

        self.backWalk = (pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_b/PlayerWalking_b1.png").convert_alpha(),
                          pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_b/PlayerWalking_b2.png").convert_alpha(),)

        self.leftWalk = (pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l1.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l2.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l3.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l4.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l5.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l6.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l7.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l8.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l9.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l10.png").convert_alpha(),)

        self.leftWalk = (pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r1.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r2.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r3.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r4.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r5.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r6.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r7.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r8.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r9.png").convert_alpha(),
                         pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r10.png").convert_alpha(),)
        self.walk = 0
        self.animStart = 0
        self.animDiff = 0
        self.lastMoveDiff = "player_f"
        
        self.image = self.angles[0]
        
        self.rect = self.image.get_rect(center = (player_x, player_y))
        
        self.prevPosX = self.rect.centerx
        self.prevPosY = self.rect.centery
        
    def update(self, imageType, anim):
        
        if self.rect.center == (self.prevPosX, self.prevPosY): #pokud se hráč nehýbe tak budou aplikovány defaultní textury
            if self.lastMoveDiff == "player_f":
                self.image = self.angles[0]
            if self.lastMoveDiff == "player_b":
                self.image = self.angles[3]
            if self.lastMoveDiff == "player_r":
                self.image = self.angles[1]
            if self.lastMoveDiff == "player_l":
                self.image = self.angles[2]
            
        if self.rect.centerx < self.prevPosX: #pokud jde hráč do leva tak se bude přehrávat animace
            self.animStart = pygame.time.get_ticks() - self.animDiff
            if self.animStart > 100:
                self.animDiff = pygame.time.get_ticks()
                if self.walk == 0:
                   self.image = self.leftWalk[self.walk]
                   self.walk += 1
                elif self.walk == 1:
                   self.image = self.leftWalk[self.walk]
                   self.walk += 1
                elif self.walk == 2:
                   self.image = self.leftWalk[self.walk]
                   self.walk += 1
                elif self.walk == 3:
                   self.image = self.leftWalk[self.walk]
                   self.walk += 1
                elif self.walk == 4:
                   self.image = self.leftWalk[self.walk]
                   self.walk += 1
                elif self.walk == 5:
                   self.image = self.leftWalk[self.walk]
                   self.walk += 1
                elif self.walk == 6:
                   self.image = self.leftWalk[self.walk]
                   self.walk += 1
                elif self.walk == 7:
                   self.image = self.leftWalk[self.walk]
                   self.walk += 1
                elif self.walk == 8:
                   self.image = self.leftWalk[self.walk]
                   self.walk += 1
                elif self.walk == 9:
                   self.image = self.leftWalk[self.walk]
                   self.walk += 1
                elif self.walk == 10:
                   self.image = self.leftWalk[self.walk]
                   self.walk += 1
                self.lastMoveDiff = "player_l"       
        if self.rect.centerx > self.prevPosX:#pokud jde hráč do prava tak se bude přehrávat animace
            self.animStart = pygame.time.get_ticks() - self.animDiff
            if self.animStart > 100:
                self.animDiff = pygame.time.get_ticks()
                if self.walk:
                   self.image = self.rightWalk[0]
                   self.walk = False
                else:
                   self.image = self.rightWalk[1]
                   self.walk = True
                self.lastMoveDiff = "player_r"
                
        if self.rect.centery < self.prevPosY:#pokud jde hráč nahoru tak se bude přehrávat animace
            self.animStart = pygame.time.get_ticks() - self.animDiff
            if self.animStart > 100:
                self.animDiff = pygame.time.get_ticks()
                if self.walk:
                   self.image = self.backWalk[0]
                   self.walk = False
                else:
                   self.image = self.backWalk[1]
                   self.walk = True
                self.lastMoveDiff = "player_b"
        if self.rect.centery > self.prevPosY: #pokud jde hráč dolů tak se bude přehrávat animace
            self.animStart = pygame.time.get_ticks() - self.animDiff
            if self.animStart > 100:
                self.animDiff = pygame.time.get_ticks()
                if self.walk:
                   self.image = self.frontWalk[0]
                   self.walk = False
                else:
                   self.image = self.frontWalk[1]
                   self.walk = True
                self.lastMoveDiff = "player_f"
        
        self.prevPosX = self.rect.centerx
        self.prevPosY = self.rect.centery
        
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