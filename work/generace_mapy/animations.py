import pygame
pygame.init()

def getImage(x, y, w, h, image):
    imageToReturn = pygame.Surface((w, h))
    imageToReturn.set_colorkey((0, 0, 0)) #!!!!!!!dá černou jako průhlednou!!!!!!!!!! (takže nepoužívat v texturách čistě černou(0, 0, 0))
    imageToReturn.blit(image, (0, 0), (x, y, w, h))
    return imageToReturn

player = pygame.image.load("data/textury_hrac/Player_sprite.png")

walk = 0
animStart = 0
animDiff = 0
lastMoveDiff = "player_f"
image = getImage(0, 96, 16, 32, player)

sideWalkingSpeed = 20 #rychlost přehrávání animací
updownWalkingSpeed = 100

def playerAnim(posX, posY, prevPosX, prevPosY,):
    global walk, animStart, animDiff, lastMoveDiff, image, sideWalkingSpeed, updownWalkingSpeed
    
    if (posX, posY) == (prevPosX, prevPosY): #pokud se hráč nehýbe tak budou aplikovány defaultní textury
        if lastMoveDiff == "player_r":
            image = getImage(48, 96, 16, 32, player)
        if lastMoveDiff == "player_l":
            image = getImage(16, 96, 16, 32, player)
        if lastMoveDiff == "player_f":
            image = getImage(0, 96, 16, 32, player)
        if lastMoveDiff == "player_b":
            image = getImage(32, 96, 16, 32, player)
    
    if posX < prevPosX: #pokud jde hráč do leva tak se bude přehrávat animace
        animStart = pygame.time.get_ticks() - animDiff
        if animStart > sideWalkingSpeed:
            animDiff = pygame.time.get_ticks()
            if (walk <= 9):
                image = getImage(16*walk, 32, 16, 32, player)
                walk += 1
            else:
                walk = 0
            lastMoveDiff = "player_l"
            
    if posX > prevPosX:#pokud jde hráč do prava tak se bude přehrávat animace
        animStart = pygame.time.get_ticks() - animDiff
        if animStart > sideWalkingSpeed:
            animDiff = pygame.time.get_ticks()
            if (walk <= 9):
                image = getImage(16*walk, 0, 16, 32, player)
                walk += 1
            else:
                walk = 0
            lastMoveDiff = "player_r"
            
    if posY < prevPosY:#pokud jde hráč nahoru tak se bude přehrávat animace
        animStart = pygame.time.get_ticks() - animDiff
        if animStart > updownWalkingSpeed:
            animDiff = pygame.time.get_ticks()
            if (walk <= 1):
                image = getImage(16*walk, 64, 16, 32, player)
                walk += 1
            else:
                walk = 0
            lastMoveDiff = "player_b"
            
    if posY > prevPosY: #pokud jde hráč dolů tak se bude přehrávat animace
        animStart = pygame.time.get_ticks() - animDiff
        if animStart > updownWalkingSpeed:
            animDiff = pygame.time.get_ticks()
            if (walk <= 1):
                image = getImage(16*walk+32, 64, 16, 32, player)
                walk += 1
            else:
                walk = 0
            lastMoveDiff = "player_f"
            
    return(image)




janitorApearingFront = (pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f.png").convert_alpha())

jWalk = 0
jApear = 0
jApearStart = 0
jApearDiff = 0
jAnimStart = 0
jAnimDiff = 0
jLastMoveDiff = "janitor_apear"
jImage = janitorApearingFront


jApearingAnimSpeed = 50
jSideWalkingSpeed = 20 #rychlost přehrávání animací
jupdownWalkingSpeed = 100

def janitorAnim():
    global jImage, jWalk, jApear, jApearStart, jApearDiff, jAnimStart, jAnimDiff, jLastMoveDiff, jApearingAnimSpeed, jSideWalkingSpeed, jupdownWalkingSpeed
    
    jApearStart = pygame.time.get_ticks() - jApearDiff
    if jApearStart > jApearingAnimSpeed:
        jApearDiff = pygame.time.get_ticks()
        if (jApear <= 53):
            image = pygame.Surface((42, 59))
            image.set_colorkey((0, 0, 0))
            image.blit(janitorApearingFront, (0, 0), (42*jApear, 0, 42, 59))
            jApear += 1
            jImage = image
        else:
            jApear = 0
    
    return jImage
        
# class janitorAnim:
#     def __init__(self):
#         True
#         
#     def get_janitorApearingAnim(posX, posY, prevPosX, prevPosY, apearing):
#         global jImage, jWalk, jApear, jApearStart, jApearDiff, jAnimStart, jAnimDiff, jLastMoveDiff, jApearingAnimSpeed, jSideWalkingSpeed, jupdownWalkingSpeed
#         
#         if True:
#             jApearStart = pygame.time.get_ticks() - jApearDiff
#             if jApearStart > jApearingAnimSpeed:
#                 jApearDiff = pygame.time.get_ticks()
#                 if (jApear <= 53):
#                     jApearSprite = pygame.Surface((42, 59))
#                     jApearSprite.blit(janitorApearingFront, (0, 0), (42*jApear, 0, 42, 59))
#                     jApearSprite.set_colorkey((0, 0, 0))
#                     jImage = jApearSprite
#                     return(jApearSprite)
#                     jApear += 1
#                     lastMoveDiff = "janitor_apear"
#                     print(jApear, jImage, janitorApearingFront)
#                 else:
#                     jApear = 0
