import pygame
pygame.init()

screen = pygame.display.set_mode((23*32,14*32))

class zed(pygame.sprite.Sprite):
    def __init__(self,pozice,textura):
        super().__init__()
        
        self.image = pygame.image.load(f"../data/textury_hry/{textura}.png").convert()
        self.rect = self.image.get_rect(topleft = (pozice))
        
class player(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        
        self.image = pygame.image.load("../data/textury_hrac/player_front.png").convert_alpha()
        self.rect = self.image.get_rect(center = (player_x, player_y))
        
    def update(self, player_x, player_y):
        self.rect.centerx = player_x
        self.rect.centery = player_y
        
class player_hitbox(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        
        self.image = pygame.image.load("../data/textury_hrac/player_hitbox.png").convert_alpha()
        self.hitBox = pygame.image.load("../data/textury_hrac/player_hitbox.png").convert_alpha()
        self.visibleHitBox = pygame.image.load("../data/textury_hrac/player_hitbox_visible.png").convert_alpha()
        self.rect = self.image.get_rect(center = (player_x, player_y + 12))
        
        self.hitbox = False
        
    def update(self, player_x, player_y):
        self.rect.centerx = player_x
        self.rect.centery = player_y + 12
    
    def showHitBox(self):
        if self.hitbox == False:
            self.hitbox = True
            self.image = self.visibleHitBox
            
    def hideHitBox(self):
        if self.hitbox == True:
            self.hitbox = False
            self.image = self.hitBox