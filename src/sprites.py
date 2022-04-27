import pygame
pygame.init()

class zed(pygame.sprite.Sprite):
    def __init__(self,pozice,textura):
        super().__init__()
        
        self.image = pygame.image.load(f"../data/textury_hry/{textura}.png").convert()
        self.rect = self.image.get_rect(topleft = (pozice))
        
class hrac(pygame.sprite.Sprite):
    def __init__(self, pozice):
        super().__init__()
        
        self.image = pygame.image.load("../data/textury_hrac/player_front.png").convert_alpha()
        self.rect = self.image.get_rect(center = (pozice))
        
    def update(self, poziceX, poziceY):
        self.rect.centerx = poziceX
        self.rect.centery = poziceY
        
class blackMask(pygame.sprite.Sprite):
    def __init__(self, RESOLUTION_X):
        super().__init__()
        
        self.maskRadius = RESOLUTION_X*1.2
        self.maskWidth = RESOLUTION_X*1.15
        
    def update(self, surface, positionX, positionY):
        self.mask = pygame.draw.circle(surface, (0, 0, 0), (positionX, positionY), self.maskRadius, int(self.maskWidth))