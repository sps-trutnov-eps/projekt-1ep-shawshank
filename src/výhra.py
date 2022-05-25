import pygame as pg
import sys
import time

pg.init()

def vyhrals(vyhral):
        BARVA_POZADI = (0, 0, 0)
        barva_zpravy = (0, 0, 0)
        barva_textu = (0, 0, 0)
        okno = pg.display.set_mode((736,448))
        pg.display.set_caption("Vyhráls")
        font = pg.font.SysFont("Comic Sans MS", 42)
        
        if vyhral:
            zprava = "Vzhráls."
        else:
            zprava = "Nevyhráls."
            
        nabidka = "q - odejít   m - \"menu\""
            
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
             
            
            if vyhral:
                if barva_zpravy == (0, 255, 0):
                    barva_zpravy = (255, 255, 0)
                else:
                    barva_zpravy = (0, 255, 0)
            else:
                if barva_zpravy == (255, 0, 0):
                    barva_zpravy = (255, 255, 0)
                else:
                    barva_zpravy = (255, 0, 0)
                    
            if barva_textu == (255, 255, 255):
                barva_textu = (255, 255, 0)
            else:
                barva_textu = (255, 255, 255)
            
            vyhra = font.render(zprava, True, barva_zpravy)
            text = font.render(nabidka, True, barva_textu)
            
            okno.fill(BARVA_POZADI)
            okno.blit(vyhra, (0,0))
            okno.blit(text, (0,50))
            
            pg.display.update()
