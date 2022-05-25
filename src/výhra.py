import pygame as pg
import sys
import time

pg.init()

def vyhrals(vyhral):
        BARVA_POZADI = (0, 0, 0)
        okno = pg.display.set_mode((736,448))
        pg.display.set_caption("Vyhráls")
        font = pg.font.SysFont("Comic Sans MS", 42)
        
        if vyhral:
            zprava = "Vzhráls."
        else:
            zprava = "Nevyhráls."
            
        while True:
            udalost = pg.event.get()
            stisknuto = pg.key.get_pressed()
            for u in udalost:
                if u.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif u.type == pg.KEYDOWN:
                    if u.key == pg.K_q:
                        return vyhral
                    if u.key == pg.K_m:
                        return "menu"
             
            time.sleep(0.5)
            
            if vyhral:
                barva_textu = (0, 255, 0)
            else:
                barva_textu = (255, 0, 0)
            
            vyhra = font.render(zprava, True, barva_textu)
            okno.fill(BARVA_POZADI)
            okno.blit(vyhra, (0,0))
            
            pg.display.update()
