import pygame as pg
import sys
import random
import time

pg.init()

opakovat = 0
znamka = 1
vyhra = False

UKOL="Prvočíslo"
BARVA_POZADI = (0, 20, 0)
okno = pg.display.set_mode((736,448))
pg.display.set_caption(UKOL)
ukol_barva = (255, 255, 255)
font = pg.font.SysFont("Comic Sans MS", 42)

def reseni(x, y):

    print("řešení: ")
    for z in range(x, y+1):
        if z>1:
            for i in range(2, z):
                if(z%i) ==0:
                    break
            else:
                print(z)
                
    pg.display.update()
                
def otazka(zacatek, konec, odpovedi):
    while not odpovezeno:
        udalost = pg.event.get()
        stisknuto = pg.key.get_pressed()
        for u in udalost:
            if u.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif u.type == pg.KEYDOWN and not odpovezeno:
                if u.key == pg.K_RETURN:
                    odpovezeno = True
                elif u.key == pg.K_BACKSPACE:
                    if len(odpoved)>0:
                        odpoved = odpoved[:-1]
                else:
                    odpoved += u.unicode
    
    
    
    uloha = font.render("Napiš prvočíslo od " + str(zacatek) + " do " + str(konec) + ": ", True, (255, 255, 255))
    odpovedin = font.render(odpoved, True, (255, 255, 255))
    
    if int(uloha) in odpovedi:
    vysledek = "Správná odpověd "
        
    else:
        vysledek = "Špatná odpověd \n"
        znamka = znamka + 1
        
        reseni(zacatek, konec)
        
    pg.display.update()




print("Výtej v minihře, ve které budeš muset napsat prvočíslo ve vybraném rozmezí")
print("Čekají na tebe čryři cvičení")
print("Maximálně můžeš udělat dvě chyby")
print("Jdeme na to!")



while opakovat < 4:
    
    rnd = (random.randint(1,10))
    
    opakovat = opakovat + 1
    
    if rnd == 1:
        otazka(0, 10, (2, 3, 5, 7))                    
                    
    elif rnd == 2:
        otazka(10, 20, (11, 13, 17, 19))

    elif rnd == 3:
        otazka(20, 30, (23, 29))
        
    elif rnd == 4:
        otazka(30, 40, (31, 37))
        
    elif rnd == 5:
        otazka(40, 50, (41, 43, 47))
        
    elif rnd == 6:
        otazka(50, 60, (53, 59))
        
    elif rnd == 7:
        otazka(60, 70, (61, 67))
        
    elif rnd == 8:
        otazka(70, 80, (71, 73, 79))
        
    elif rnd == 9:
        otazka(80, 90, (83, 89))

    elif rnd == 10:
        otazka(90, 100, (97, random.randint(1000, 10000000)))
                    
else:
    print("\n\n\nZnámka: " + str(znamka))    
    
    
if znamka == 1:
    print("Výborně, úspěšně jsi dokončil minihru s plným počtem bodů!")
    vyhra = True

if znamka == 2:
    vyhra = True
    print("Výborně, úspěšně jsi dokončil minihru!")
    
if znamka == 3:
    vyhra = False
    print("Bohužel, k výhře ti chyběl jeden bod")
    
if znamka == 4:
    vyhra = False
    print("Bohužel, ale to ti stačit nebude")

if znamka == 5:
    vyhra = False
    print("To se ti nepovedlo, nezískal jsi ani jeden bod")