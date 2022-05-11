import pygame
import random

sirka_okno = 800
vyska_okno = 600

pygame.init() 
okno = pygame.display.set_mode((sirka_okno, vyska_okno)) 

zelena = (0,255,0)
cervena = (255,0,0)
modra = (0,0,255)
fialova = (0,0,128)
bila = (255,255,255)
cerna = (0,0,0)
ruzova = (255,200,200)


maly_font = pygame.font.SysFont("timesnewroman", 25)
stredni_font = pygame.font.SysFont("timesnewroman", 50)
velky_font = pygame.font.SysFont("timesnewroman", 85)

def textove_objekty(text, barva, velikost = "malá"):    
    
    if velikost == "malá":
        textSurface = maly_font.render(text, True, barva)
    if velikost == "střední":
        textSurface = stredni_font.render(text, True, barva)
    if velikost == "velká":
        textSurface = velky_font.render(text, True, barva)
    
    return textSurface, textSurface.get_rect()

def zprava_na_obrazovce(zprava, barva, y_displace = 0, velikost = "malá"):
    textSurf, textRect = textove_objekty(zprava, barva, velikost)
    textRect.center = (int(sirka_okno / 2), int(vyska_okno / 2)+y_displace)
    okno.blit(textSurf, textRect)

while True:
    zprava_na_obrazovce("Počítání příkladů", zelena, -230)
    zprava_na_obrazovce("Máš 3 životy, pokud je ztratíš tak si prohrál", zelena, -200)
    zprava_na_obrazovce("Stiskněte ENTER pro zapnutí hry", zelena, -30)
    pygame.display.update()
    
handle = open("příklady.txt","r", encoding = "utf-8")
priklady = handle.read()
print(priklady)
handle.close()


handle = open("výsledky.txt","r", encoding = "utf-8")
vysledky = handle.read()
handle.close()


spravne_vysledky = vysledky.strip().split("\n")
vsechny_priklady = priklady.strip().split("\n")

nahodny_priklad1 = random.choice(vsechny_priklady)
print(nahodny_priklad1)
poradi_prikladu1 = vsechny_priklady.index(nahodny_priklad1)
spravny_vysledek1 = vysledky[poradi_prikladu1]
if spravny_vysledek1 == input ():
    print ("Správně")
    
else:
    print ("Špatně")  
okno.fill(255, 255, 255)
pygame.display.update()
 













