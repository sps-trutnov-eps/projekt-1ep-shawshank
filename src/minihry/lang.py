import pygame as pg
import sys
import random
import time

pg.init()
pg.mixer.init()

def main():
    theme = pg.mixer.Sound("../data/music/minigame_theme.mp3") 
    opakovat = 0
    znamka = 1
    vyhra = True

    UKOL="Prvočíslo"
    BARVA_POZADI = (0, 20, 0)
    okno = pg.display.set_mode((736,448))
    pg.display.set_caption(UKOL)
    ukol_barva = (255, 255, 255)
    font = pg.font.SysFont("Comic Sans MS", 42)

    def reseni(x, y):
        prvocisla = ""
        for z in range(x, y+1):
                if z>1:
                    for i in range(2, z):
                        if(z%i) ==0:
                            break
                    else:
                        prvocisla = prvocisla + str(z) + "  "
        odpocet = True
        while odpocet:
            titul = font.render("Špatně- řešení:", True, (255, 255, 255))
            outreseni = font.render(prvocisla, True, (255, 255, 255))
            okno.fill(BARVA_POZADI)
            okno.blit(outreseni, (0, 50))
            okno.blit(titul, (0, 0))
            pg.display.update()
            time.sleep(5)
            odpocet = False
                    
    def otazka(zacatek, konec, odpovedi):
        odpovezeno = False
        odpoved = ""
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
            
            if odpovezeno == True:
                try:
                    if int(odpoved) in odpovedi:
                        return True
                        
                    else:
                        reseni(zacatek, konec)
                        return False
                except:
                    reseni(zacatek, konec)
                    return False
                
            okno.fill(BARVA_POZADI)
            okno.blit(odpovedin, (0, 50))
            okno.blit(uloha, (0,0))

            pg.display.update()

    while opakovat < 4:
        if not pg.mixer.get_busy():
            theme.play()
        rnd = (random.randint(1,10))
        
        opakovat = opakovat + 1
        
        if rnd == 1:
            vyhra = vyhra and otazka(0, 10, (2, 3, 5, 7))                    
                        
        elif rnd == 2:
            vyhra = vyhra and otazka(10, 20, (11, 13, 17, 19))

        elif rnd == 3:
            vyhra = vyhra and otazka(20, 30, (23, 29))
            
        elif rnd == 4:
            vyhra = vyhra and otazka(30, 40, (31, 37))
            
        elif rnd == 5:
            vyhra = vyhra and otazka(40, 50, (41, 43, 47))
            
        elif rnd == 6:
            vyhra = vyhra and otazka(50, 60, (53, 59))
            
        elif rnd == 7:
            vyhra = vyhra and otazka(60, 70, (61, 67))
            
        elif rnd == 8:
            vyhra = vyhra and otazka(70, 80, (71, 73, 79))
            
        elif rnd == 9:
            vyhra = vyhra and otazka(80, 90, (83, 89))

        elif rnd == 10:
            vyhra = vyhra and otazka(90, 100, (97, random.randint(1000, 10000000)))
                        
    theme.stop()
    return vyhra