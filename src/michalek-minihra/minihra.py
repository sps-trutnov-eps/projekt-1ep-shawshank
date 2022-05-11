## ToDo input a kontrola řešení, časovač odpovědi
import pygame as pg
import sys
import random
import time

pg.init()

def mminihra():
    BARVA_POZADI = (0, 20, 0)
    okno = pg.display.set_mode((736,448))
    pg.display.set_caption("Minihra Martina Michálka")

    seznam_zadani = {"1 + 1 =":"2", "5 - 4 =":"1", "2*2":"4","28/4":"7","7*3":"21"}
    klice = list(seznam_zadani)
    notazek = random.randint(1, 5)

    while notazek > 0:
        zadani = random.choice(klice)
        klice.remove(zadani)
        reseni = seznam_zadani[zadani]
        odpovezeno = False
        spravneb = (0, 25, 0)
        odpoved = ""
        spravne = ""
        vysledek = True
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
                        
            if odpovezeno == True:
                if odpoved == reseni:
                    spravne = "Správně"
                    spravneb = (0, 255, 0)
                else:
                    spravne = "Špatně"
                    spravneb = (255, 0, 0)
                    vysledek = False
                    
            font = pg.font.SysFont("Comic Sans MS", 42)
            uloha = font.render(zadani, True, (255, 255, 255))
            odpovedin = font.render(odpoved, True, (255, 255, 255))
            spravneout = font.render(spravne, True, (spravneb))
            zbotazky = font.render(str(notazek), True, (255, 255, 0))
            
            okno.fill(BARVA_POZADI)
            okno.blit(uloha, (0,0))
            okno.blit(odpovedin, (0, 50))
            okno.blit(spravneout, (0, 108))
            okno.blit(zbotazky, (689, 0))
                
            pg.display.update()
        time.sleep(0.5)
        notazek = notazek - 1
    pg.quit()
    sys.exit()
    return vysledek