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




janitor = (pygame.image.load("data/textures_janitor/Janitor_sprite.png").convert_alpha())

jWalk = 0
jApear = 0
jApearStart = 0
jApearDiff = 0
jAnimStart = 0
jAnimDiff = 0
jLastMoveDiff = "janitor_f"
jImage = janitor


jApearingAnimSpeed = 50
jSideWalkingSpeed = 20 #rychlost přehrávání animací
jupdownWalkingSpeed = 100

def janitorAnim(posX, posY, prevPosX, prevPosY):
    global jImage, jWalk, jApear, jApearStart, jApearDiff, jAnimStart, jAnimDiff, jLastMoveDiff, jApearingAnimSpeed, jSideWalkingSpeed, jupdownWalkingSpeed
    
    if jLastMoveDiff == "janitor_apear":
        jApearStart = pygame.time.get_ticks() - jApearDiff
        if jApearStart > jApearingAnimSpeed:
            if jApear == 0 or jApear == 1 or jApear == 2 or jApear == 4 or jApear == 5 or jApear == 8 or jApear == 9 or jApear == 11 or jApear == 12:
                jApearDiff = pygame.time.get_ticks() + 500
            elif jApear == 15 or jApear == 52:
                jApearDiff = pygame.time.get_ticks() + 1000
            else:
                jApearDiff = pygame.time.get_ticks()
            if (jApear <= 53):
                jImage = getImage(42*jApear, 0, 42, 59, janitor)
                jApear += 1
            else:
                jLastMoveDiff == "janitor_f"
                jApear = 0
    else:    
        if (posX, posY) == (prevPosX, prevPosY): #pokud se hráč školník tak budou aplikovány defaultní textury
            if jLastMoveDiff == "janitor_r":
                jImage = getImage(84, 177, 42, 59, janitor)
            if jLastMoveDiff == "janitor_l":
                jImage = getImage(128, 177, 42, 59, janitor)
            if jLastMoveDiff == "janitor_f":
                jImage = getImage(0, 177, 42, 59, janitor)
            if jLastMoveDiff == "janitor_b":
                jImage = getImage(42, 177, 42, 59, janitor)

        if posX < prevPosX: #pokud jde školník do leva tak se bude přehrávat animace
            jAnimStart = pygame.time.get_ticks() - jAnimDiff
            if jAnimStart > jSideWalkingSpeed:
                jAnimDiff = pygame.time.get_ticks()
                if (jWalk <= 9):
                    jImage = getImage(42*jWalk, 59, 42, 59, janitor)
                    jWalk += 1
                else:
                    jWalk = 0
                jLastMoveDiff = "janitor_l"
                
        if posX > prevPosX:#pokud jde školník do prava tak se bude přehrávat animace
            jAnimStart = pygame.time.get_ticks() - jAnimDiff
            if jAnimStart > sideWalkingSpeed:
                jAnimDiff = pygame.time.get_ticks()
                if (jWalk <= 9):
                    jImage = getImage(42*jWalk, 118, 42, 59, janitor)
                    jWalk += 1
                else:
                    jWalk = 0
                jLastMoveDiff = "janitor_r"
                
        if posY < prevPosY:#pokud jde školník nahoru tak se bude přehrávat animace
            jAnimStart = pygame.time.get_ticks() - jAnimDiff
            if jAnimStart > updownWalkingSpeed:
                jAnimDiff = pygame.time.get_ticks()
                if (jWalk <= 1):
                    jImage = getImage(42*jWalk+252, 177, 42, 59, janitor)
                    jWalk += 1
                else:
                    jWalk = 0
                jLastMoveDiff = "janitor_b"
                
        if posY > prevPosY: #pokud jde školník dolů tak se bude přehrávat animace
            jAnimStart = pygame.time.get_ticks() - jAnimDiff
            if jAnimStart > updownWalkingSpeed:
                jAnimDiff = pygame.time.get_ticks()
                if (jWalk <= 1):
                    jImage = getImage(42*jWalk+168, 177, 42, 59, janitor)
                    jWalk += 1
                else:
                    jWalk = 0
                jLastMoveDiff = "janitor_f"
                
    return jImage