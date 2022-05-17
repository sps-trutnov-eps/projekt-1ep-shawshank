import pygame
from animations import getImage
pygame.init()

inventoryImages = pygame.image.load("../data/inventory/inventory.png")
hasKeys = False
hasBoots = False
canGoOut = False

class inventoryHasKey(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = getImage(32, 0, 32, 32, inventoryImages)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def update(self):
        global hasKeys
        if hasKeys: hasKeys = False
        else: hasKeys = True

        if hasKeys:
            self.image = getImage(0, 0, 32, 32, inventoryImages)
        else:
            self.image = getImage(32, 0, 32, 32, inventoryImages)

class inventoryHasBoots(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = getImage(96, 0, 32, 32, inventoryImages)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def update(self):
        global hasBoots
        if hasBoots: hasBoots = False
        else: hasBoots = True

        if hasBoots:
            self.image = getImage(64, 0, 32, 32, inventoryImages)
        else:
            self.image = getImage(96, 0, 32, 32, inventoryImages)