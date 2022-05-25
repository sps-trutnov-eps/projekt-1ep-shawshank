import pygame as pg
import random
import sys
import time

sirka_okno = 776
vyska_okno = 448

pygame.init() 
okno = pygame.display.set_mode((sirka_okno, vyska_okno)) 

zelena = (0,255,0)
cervena = (255,0,0)
modra = (0,0,255)
fialova = (0,0,128)
bila = (255,255,255)
cerna = (0,0,0)
ruzova = (255,200,200)


otazky = ["Kdy začala druhá světová válka?";
          "Kdy vzniklo Československo?",
          "Kdo postavil Karlštejn?",
          "Jak se jmenoval konkurenční rod Přemyslovců?",
          "Jak se jmenoval poslední Přemyslovec?",
          "Kdo byl prezidentem USA během občanské války?",
          "V jakém roce vznikl Sovětský svaz?",
          "Kdo byl první prezident České republiky?",
          "Kde byl upálen Jan Hus?",
          "Na jakého panovníka byl spáchán atentát v Sarajevu?"
          ]

 data = list(otazky)
 otazka = random.randit  (1, 6)
 

otazky = random.choice(data)
        data.remove(otazky)


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
    zprava_na_obrazovce("Ustní zkoušení", zelena, -230)
    zprava_na_obrazovce(otazky (1, 10), zelena, -100)
    zprava_na_obrazovce("", zelena, 130)
    pygame.display.update()
    

 












