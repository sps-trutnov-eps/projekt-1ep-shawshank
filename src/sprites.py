import pygame
pygame.init()

screen = pygame.display.set_mode((23*32,14*32))

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