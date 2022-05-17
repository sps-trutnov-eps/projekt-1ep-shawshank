import pygame as pg
import sys

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
            
            vyhra = font.render(zprava, True, (255, 255, 255))
            okno.fill(BARVA_POZADI)
            okno.blit(vyhra, (0,0))
            
            pg.display.update()