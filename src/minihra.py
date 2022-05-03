import pygame


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
    zprava_na_obrazovce("Vítej na hodině matematiky", zelena, -230)
    zprava_na_obrazovce("Cílem hry je spočítat všechny příklady", zelena, -200)
    zprava_na_obrazovce("Stistknutím S spustíte hru, Stisknutím Q vypnete hru", zelena, -30)
    pygame.display.update()
    
okno.fill(255, 255, 255)
pygame.display.update()
 













