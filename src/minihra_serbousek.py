import pygame
import random
pygame.init()
window = pygame.display.set_mode((640,480))
pygame.display.update()
pygame.display.set_caption("Šibenice")
game_over = False
slova = ["tabule", "krida"]
nahoda = random.choice(slova)
abeceda = [
    {"znak": "A", "stav": True , "stav2": True},
    {"znak": "B", "stav": True , "stav2": False},
    {"znak": "C", "stav": True , "stav2": False},
    {"znak": "D", "stav": False , "stav2": False},
    {"znak": "E", "stav": True , "stav2": False},
    {"znak": "F", "stav": True , "stav2": False},
    {"znak": "G", "stav": True , "stav2": False},
    {"znak": "H", "stav": True , "stav2": False},
    {"znak": "I", "stav": True , "stav2": False},
    {"znak": "J", "stav": True , "stav2": False},
    {"znak": "K", "stav": True , "stav2": False},
    {"znak": "L", "stav": True , "stav2": False},
    {"znak": "M", "stav": True , "stav2": False},
    {"znak": "N", "stav": True , "stav2": False},
    {"znak": "O", "stav": True , "stav2": False},
    {"znak": "P", "stav": True , "stav2": False},
    {"znak": "Q", "stav": True , "stav2": False},
    {"znak": "R", "stav": True , "stav2": False},
    {"znak": "S", "stav": True , "stav2": False},
    {"znak": "T", "stav": True , "stav2": False},
    {"znak": "U", "stav": True , "stav2": False},
    {"znak": "V", "stav": True , "stav2": False},
    {"znak": "W", "stav": True , "stav2": False},
    {"znak": "X", "stav": True , "stav2": False},
    {"znak": "Y", "stav": True , "stav2": False},
    {"znak": "Z", "stav": True , "stav2": False}
    ]
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            quit()
    color = (0,44,0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    X = 640
    Y = 480
    window.fill(color)
    font = pygame.font.SysFont('forte', 26)
    odsazeni = 10
        #VYKRESLOVANI
    for pismeno in abeceda:
        if pismeno["stav"] == True:
            if pismeno["stav2"] == False:
                text = font.render(pismeno["znak"],True,white)
            elif pismeno["stav2"] == True:
                text = font.render(pismeno["znak"],True,red)
        elif pismeno["stav"] == False:
            text = font.render("_",True,white)
        textRect = text.get_rect()
        rozmery_pismene = font.size(pismeno["znak"])
        textRect.center = (rozmery_pismene[0]//2 + odsazeni, Y // 1.05)
        window.blit(text, textRect)
        odsazeni += rozmery_pismene[0] + 7.5
    stisk = pygame.key.get_pressed()
        #OVLÁDÁNÍ DOPRAVA
    if stisk[pygame.K_RIGHT]:
        for p, pismeno in enumerate(abeceda):
            if pismeno["stav2"] == False:
                pass
            elif pismeno["stav2"] == True:
                pozice = p
                break
        abeceda[pozice]["stav2"] = False
        if pozice == 25:
            abeceda[0]["stav2"] = True
        else:
            abeceda[pozice+1]["stav2"] = True
                
        #OVLÁDÁNÍ DOLEVA
    if stisk[pygame.K_LEFT]:
        for p, pismeno in enumerate(abeceda):
            if pismeno["stav2"] == False:
                pass
            elif pismeno["stav2"] == True:
                pozice = p
                break
        abeceda[pozice]["stav2"] = False
        if pozice == 0:
            abeceda[25]["stav2"] = True
        else:
            abeceda[pozice-1]["stav2"] = True
            
        #POUŽÍVÁNÍ PÍSMEN
    if stisk[pygame.K_SPACE]:
        for p, pismeno in enumerate(abeceda):
            if pismeno["stav2"] == False:
                pass
            elif pismeno["stav2"] == True:
                pozice = p
                break
        abeceda[pozice]["stav"] = False
    
        
        
    pygame.time.delay(60)
    pygame.display.update()   