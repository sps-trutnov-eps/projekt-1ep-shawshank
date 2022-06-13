import pygame
import random
import sys
pygame.init()
window = pygame.display.set_mode((640,480))
pygame.display.update()
pygame.display.set_caption("Šibenice")
game_over = False
slova = ["TABULE", "KRIDA",]
nahoda = random.choice(slova)
font2 = pygame.font.SysFont('forte', 50)
chyby = 0
spravne = 0
abeceda = [
    {"znak": "A", "stav": True , "stav2": True},
    {"znak": "B", "stav": True , "stav2": False},
    {"znak": "C", "stav": True , "stav2": False},
    {"znak": "D", "stav": True , "stav2": False},
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
znaky_nahoda = []
for pismeno in nahoda:
    znaky_nahoda.append({"znak": pismeno, "stav": False, "pripocteni": False})
    
while not game_over:
    stisk = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            quit()
    if stisk[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
        
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
            rozmery_pismene = font.size(pismeno["znak"])
        elif pismeno["stav"] == False:
            text = font.render("_",True,white)
            rozmery_pismene = font.size("_")
        textRect = text.get_rect()
        textRect.center = (rozmery_pismene[0]//2 + odsazeni, Y // 1.05)
        window.blit(text, textRect)
        odsazeni += rozmery_pismene[0] + 7.5
   
    odsazeni = 10
    for x in znaky_nahoda:
        if x["stav"] == True:
            text = font.render(x["znak"],True,white)
            rozmery_pismene = font.size(x["znak"])
        elif x["stav"] == False:
            text = font.render("_",True,white)
            rozmery_pismene = font.size("_")
        textRect = text.get_rect()
        textRect.center = (rozmery_pismene[0]//2 + odsazeni, Y // 2)
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
            if pismeno["stav2"] == False or pismeno["stav"] == False:
                pass
            elif pismeno["stav2"] == True and pismeno["stav"] == True:
                pozice = p
                nalezeno = False
                for znak in znaky_nahoda:
                    if znak["znak"] == pismeno["znak"]:
                        znak["stav"] = True
                        nalezeno = True
                    else:
                        pass
                if nalezeno == False:
                    chyby += 1
                break
        abeceda[pozice]["stav"] = False
    
        #VYKRESLENÍ ŠIBENICE
    if chyby >= 1:
        pygame.draw.line(window, white, (250, 400), (450, 400),5)
    if chyby >= 2:
        pygame.draw.line(window, white, (350, 400), (350, 100),5)
    if chyby >= 3:
        pygame.draw.line(window, white, (350, 102), (490, 102),5)
    if chyby >= 4:
        pygame.draw.line(window, white, (350, 180), (430, 102),5)
    if chyby >= 5:
        pygame.draw.line(window, white, (488, 102), (488, 140),5)
    if chyby >= 6:
        pygame.draw.circle(window, white, (488, 170), 30, 5)
    if chyby >= 7:
        pygame.draw.line(window, white, (488, 200), (488, 280), 5)
    if chyby >= 8:
        pygame.draw.line(window, white, (488, 200), (520, 260), 5)
    if chyby >= 9:
        pygame.draw.line(window, white, (488, 200), (456, 260), 5)
    if chyby >= 10: 
        pygame.draw.line(window, white, (488, 280), (520, 340), 5)
    if chyby >= 11:
        pygame.draw.line(window, white, (488, 280), (456, 340), 5)
        
        text = font2.render("Prohrál jsi", True, red)
        textRect.center = (320, 240)
        window.blit(text, textRect)
        
        #KONTROLA VÝHRY
    for znak in znaky_nahoda:
        if znak["stav"] == True and znak["pripocteni"] == False:
            spravne += 1
            znak["pripocteni"] = True
    if spravne == len(znaky_nahoda):
        text2 = font2.render("Vyhrál jsi", True, red)
        textRect.center = (320, 240)
        window.blit(text2, textRect)
       
    pygame.time.delay(60)
    pygame.display.update()
pygame.display.update() 