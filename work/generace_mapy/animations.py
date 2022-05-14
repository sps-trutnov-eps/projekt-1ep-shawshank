import pygame
pygame.init()

playerAngles = (pygame.image.load("data/textury_hrac/Player/Player_f.png").convert_alpha(),
               pygame.image.load("data/textury_hrac/Player/Player_r.png").convert_alpha(),
               pygame.image.load("data/textury_hrac/Player/Player_l.png").convert_alpha(),
               pygame.image.load("data/textury_hrac/Player/Player_b.png").convert_alpha())

playerFrontWalk = (pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_f/PlayerWalking_f1.png").convert_alpha(),
             pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_f/PlayerWalking_f2.png").convert_alpha())

backWalk = (pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_b/PlayerWalking_b1.png").convert_alpha(),
            pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_b/PlayerWalking_b2.png").convert_alpha())

playerLeftWalk = (pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l1.png").convert_alpha(),
            pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l2.png").convert_alpha(),
            pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l3.png").convert_alpha(),
            pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l4.png").convert_alpha(),
            pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l5.png").convert_alpha(),
            pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l6.png").convert_alpha(),
            pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l7.png").convert_alpha(),
            pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l8.png").convert_alpha(),
            pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l9.png").convert_alpha(),
            pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_l/PlayerWalking_l10.png").convert_alpha())

playerRightWalk = (pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r1.png").convert_alpha(),
             pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r2.png").convert_alpha(),
             pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r3.png").convert_alpha(),
             pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r4.png").convert_alpha(),
             pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r5.png").convert_alpha(),
             pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r6.png").convert_alpha(),
             pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r7.png").convert_alpha(),
             pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r8.png").convert_alpha(),
             pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r9.png").convert_alpha(),
             pygame.image.load("data/textury_hrac/PlayerWalking/PlayerWalking_r/PlayerWalking_r10.png").convert_alpha())

walk = 0
animStart = 0
animDiff = 0
lastMoveDiff = "player_f"
image = playerAngles[0]
def playerAnim(posX, posY, prevPosX, prevPosY,):
    global walk, animStart, animDiff, lastMoveDiff, image
    
    if (posX, posY) == (prevPosX, prevPosY): #pokud se hráč nehýbe tak budou aplikovány defaultní textury
        if lastMoveDiff == "player_f":
            image = playerAngles[0]
        if lastMoveDiff == "player_b":
            image = playerAngles[3]
        if lastMoveDiff == "player_r":
            image = playerAngles[1]
        if lastMoveDiff == "player_l":
            image = playerAngles[2]
        
    if posX < prevPosX: #pokud jde hráč do leva tak se bude přehrávat animace
        animStart = pygame.time.get_ticks() - animDiff
        if animStart > 20:
            animDiff = pygame.time.get_ticks()
            if walk == 0:
               image = playerLeftWalk[walk]
               walk += 1
            elif walk == 1:
               image = playerLeftWalk[walk]
               walk += 1
            elif walk == 2:
               image = playerLeftWalk[walk]
               walk += 1
            elif walk == 3:
               image = playerLeftWalk[walk]
               walk += 1
            elif walk == 4:
               image = playerLeftWalk[walk]
               walk += 1
            elif walk == 5:
               image = playerLeftWalk[walk]
               walk += 1
            elif walk == 6:
               image = playerLeftWalk[walk]
               walk += 1
            elif walk == 7:
               image = playerLeftWalk[walk]
               walk += 1
            elif walk == 8:
               image = playerLeftWalk[walk]
               walk += 1
            elif walk == 9:
               image = playerLeftWalk[walk]
               walk = 0
            lastMoveDiff = "player_l"       
    if posX > prevPosX:#pokud jde hráč do prava tak se bude přehrávat animace
        animStart = pygame.time.get_ticks() - animDiff
        if animStart > 20:
            animDiff = pygame.time.get_ticks()
            if walk == 0:
               image = playerRightWalk[walk]
               walk += 1
            elif walk == 1:
               image = playerRightWalk[walk]
               walk += 1
            elif walk == 2:
               image = playerRightWalk[walk]
               walk += 1
            elif walk == 3:
               image = playerRightWalk[walk]
               walk += 1
            elif walk == 4:
               image = playerRightWalk[walk]
               walk += 1
            elif walk == 5:
               image = playerRightWalk[walk]
               walk += 1
            elif walk == 6:
               image = playerRightWalk[walk]
               walk += 1
            elif walk == 7:
               image = playerRightWalk[walk]
               walk += 1
            elif walk == 8:
               image = playerRightWalk[walk]
               walk += 1
            elif walk == 9:
               image = playerRightWalk[walk]
               walk = 0
            lastMoveDiff = "player_r"
            
    if posY < prevPosY:#pokud jde hráč nahoru tak se bude přehrávat animace
        animStart = pygame.time.get_ticks() - animDiff
        if animStart > 100:
            animDiff = pygame.time.get_ticks()
            if walk:
               image = backWalk[0]
               walk = False
            else:
               image = backWalk[1]
               walk = True
            lastMoveDiff = "player_b"
    if posY > prevPosY: #pokud jde hráč dolů tak se bude přehrávat animace
        animStart = pygame.time.get_ticks() - animDiff
        if animStart > 100:
            animDiff = pygame.time.get_ticks()
            if walk:
               image = playerFrontWalk[0]
               walk = False
            else:
               image = playerFrontWalk[1]
               walk = True
            lastMoveDiff = "player_f"
            
    return(image)
