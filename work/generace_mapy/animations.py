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

sideWalkingSpeed = 20 #rychlost přehrávání animací
updownWalkingSpeed = 100

def playerAnim(posX, posY, prevPosX, prevPosY,):
    global walk, animStart, animDiff, lastMoveDiff, image, sideWalkingSpeed, updownWalkingSpeed
    
    if (posX, posY) == (prevPosX, prevPosY): #pokud se hráč nehýbe tak budou aplikovány defaultní textury
        if lastMoveDiff == "player_r":
            image = playerAngles[1]
        if lastMoveDiff == "player_l":
            image = playerAngles[2]
        if lastMoveDiff == "player_f":
            image = playerAngles[0]
        if lastMoveDiff == "player_b":
            image = playerAngles[3]
        
    if posX < prevPosX: #pokud jde hráč do leva tak se bude přehrávat animace
        animStart = pygame.time.get_ticks() - animDiff
        if animStart > sideWalkingSpeed:
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
        if animStart > sideWalkingSpeed:
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
        if animStart > updownWalkingSpeed:
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
        if animStart > updownWalkingSpeed:
            animDiff = pygame.time.get_ticks()
            if walk:
               image = playerFrontWalk[0]
               walk = False
            else:
               image = playerFrontWalk[1]
               walk = True
            lastMoveDiff = "player_f"
            
    return(image)


janitorApearingFront = (pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f1.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f2.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f3.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f4.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f5.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f6.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f7.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f9.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f10.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f12.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f13.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f14.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f15.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f16.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f17.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f18.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f19.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f20.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f21.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f22.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f23.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f24.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f25.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f26.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f27.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f28.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f29.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f30.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f31.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f32.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f33.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f34.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f35.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f36.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f37.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f38.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f39.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f40.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f41.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f42.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f43.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f44.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f45.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f46.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f47.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f48.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f49.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f50.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f51.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f52.png").convert_alpha(),
                        pygame.image.load("data/textures_janitor/JanitorApearing/janitorApearing_f53.png").convert_alpha())

jWalk = 0
jApear = 0
jApearStart = 0
jApearDiff = 0
jAnimStart = 0
jAnimDiff = 0
jLastMoveDiff = "janitor_apear"
#jImage = playerAngles[0]


jApearingAnimSpeed = 100
jSideWalkingSpeed = 20 #rychlost přehrávání animací
jupdownWalkingSpeed = 100
def janitorAnim(posX, posY, prevPosX, prevPosY, apearing):
    global jWalk, jApear, jApearStart, jApearDiff, jAnimStart, jAnimDiff, jLastMoveDiff, apearingAnimSpeed, sideWalkingSpeed, updownWalkingSpeed
    
    if apearing:
        jApearStart = pygame.time.get_ticks() - jApearDiff
        if jApearStart > jApearingAnimSpeed:
            jApearDiff = pygame.time.get_ticks()
            if jApear == 0:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 1:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 2:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 3:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 4:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 5:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 6:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 7:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 8:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 9:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 10:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 11:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 12:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 13:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 14:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 15:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 16:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 17:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 18:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 19:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 20:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 21:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 22:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 23:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 24:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 25:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 26:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 27:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 28:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 29:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 30:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 31:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 32:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 33:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 34:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 35:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 36:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 37:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 38:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 39:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 40:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 41:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 42:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 43:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 44:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 45:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 46:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 47:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 48:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 49:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 50:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 51:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 52:
               image = janitorApearingFront[jApear]
               jApear += 1
            elif jApear == 53:
               image = janitorApearingFront[jApear]
               jApear = 0
            lastMoveDiff = "player_l"       
    return(image)