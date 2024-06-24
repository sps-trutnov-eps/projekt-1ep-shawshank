import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

import random
import os
import pygame
sys.path.insert(1,DATA_ROOT + '/')
import languages

pygame.mixer.init()

def vyberOtazekaspol(otazky,localized_text):
    nahodnaOtazka = random.choice(otazky)
    spravnaOdpoved = spravne_odpovedi[otazky.index(nahodnaOtazka)]
    spatnaOdpoved1 = spatne_odpovedi1[otazky.index(nahodnaOtazka)]
    spatnaOdpoved2 = spatne_odpovedi2[otazky.index(nahodnaOtazka)]

    font = pygame.font.SysFont("Consolas", 20)
    otazkaText = font.render(nahodnaOtazka, True, (255, 255, 255))
    spravnaOdpovedText = font.render(spravnaOdpoved, True, (255, 255, 255))
    spatnaOdpovedText1 = font.render(spatnaOdpoved1, True, (255, 255, 255))
    spatnaOdpovedText2 = font.render(spatnaOdpoved2, True, (255, 255, 255))

    spatnaOdpovedMainText = font.render(localized_text[0] + f"{spravnaOdpoved}", True, (255, 0, 0))
    spravnaOdpovedMainText = font.render(localized_text[1], True, (0, 255, 0))

    spravneTlacitko = random.choice(range(0,3))
    
    return otazkaText, (spravnaOdpovedText,spatnaOdpovedText1, spatnaOdpovedText2), (spatnaOdpovedMainText, spravnaOdpovedMainText), spravneTlacitko
    
def main(language):
    global spravne_odpovedi, spatne_odpovedi1, spatne_odpovedi2
    theme = pygame.mixer.Sound(DATA_ROOT + "/data/music/minigame_theme.mp3")

    localized_text = languages.minigame_lang("lanka",language)
    opakovani=5
    
    sirka_okna = 736
    vyska_okna = 448

    cerna = (0, 0, 0)
    bila = (255, 255, 255)
    cervena = (255, 0, 0)
    zelena = (0, 255, 0)
    modra = (0, 0, 255)

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((sirka_okna, vyska_okna))

    moznostiPozice = (12, sirka_okna/3+9, sirka_okna/3*2+6, 300) #poziceX možnosti 1, poziceX možnosti 2, poziceX možnosti 3, poziceY všechny možnosti
    moznostiSirka = (sirka_okna/3-18, 125)

    if language == "ENG":
        #nacteni-otazek
        handle = open("./minihry/lanka/eng/otazky.txt", "r", encoding = "utf-8")
        vsechny_otazky = handle.read()
        handle.close()

        #nacteni-odpovedi
        handle = open("./minihry/lanka/eng/odpovedi.txt", "r", encoding = "utf-8")
        vsechny_odpovedi = handle.read()
        handle.close()

        #nacteni-spatnych-odpovedi
        handle = open("./minihry/lanka/eng/spatna_odpoved1.txt", "r", encoding = "utf-8")
        spatna_odpoved1 = handle.read()
        handle.close()

        handle = open("./minihry/lanka/eng/spatna_odpoved2.txt", "r", encoding = "utf-8")
        spatna_odpoved2 = handle.read()
        handle.close()
        
    else:
        #nacteni-otazek
        handle = open("./minihry/lanka/cze/otazky.txt", "r", encoding = "utf-8")
        vsechny_otazky = handle.read()
        handle.close()

        #nacteni-odpovedi
        handle = open("./minihry/lanka/cze/odpovedi.txt", "r", encoding = "utf-8")
        vsechny_odpovedi = handle.read()
        handle.close()

        #nacteni-spatnych-odpovedi
        handle = open("./minihry/lanka/cze/spatna_odpoved1.txt", "r", encoding = "utf-8")
        spatna_odpoved1 = handle.read()
        handle.close()

        handle = open("./minihry/lanka/cze/spatna_odpoved2.txt", "r", encoding = "utf-8")
        spatna_odpoved2 = handle.read()
        handle.close()

    timeOut = 0
    timeOut2 = 0

    #Rozdeleni-na-radky
    spravne_odpovedi = vsechny_odpovedi.strip().split("\n")
    otazky = vsechny_otazky.strip().split("\n")
    spatne_odpovedi1 = spatna_odpoved1.strip().split("\n")
    spatne_odpovedi2 = spatna_odpoved2.strip().split("\n")
    nahodnaOtazka = ""
    spatnaOdpoved1 = ""
    spatnaOdpoved2 = ""
    spravnaOdpoved = ""
    spravneTlacitko = 0
    spatnaOdpoved = 0

    otazkaText, (spravnaOdpovedText,spatnaOdpovedText1, spatnaOdpovedText2), (spatnaOdpovedMainText, spravnaOdpovedMainText), spravneTlacitko = vyberOtazekaspol(otazky,localized_text)
    spatnaOdpoved = 0
    
    pocetOdpovedi = 0
    pocetBodu = 0

    while(True):
        if not pygame.mixer.get_busy():
            theme.play()
        udalosti = pygame.event.get()
        screen.fill((50, 141, 176))
        
        for u in udalosti:
            if u.type == pygame.QUIT:
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
        
            if u.type == pygame.MOUSEBUTTONDOWN and u.button == 1:
                if pygame.mouse.get_pos()[0] > moznostiPozice[0] and pygame.mouse.get_pos()[0] < moznostiPozice[0] + moznostiSirka[0] and pygame.mouse.get_pos()[1] > moznostiPozice[3] and pygame.mouse.get_pos()[1] < moznostiPozice[3] + moznostiSirka[1]:
                    if timeOut < 1:
                        timeOut = 3500
                        if spravneTlacitko == 0:
                            spatnaOdpoved = 2
                            pocetBodu += 1
                        else:
                            spatnaOdpoved = 1
                        pocetOdpovedi += 1
                    
                if pygame.mouse.get_pos()[0] > moznostiPozice[1] and pygame.mouse.get_pos()[0] < moznostiPozice[1] + moznostiSirka[0] and pygame.mouse.get_pos()[1] > moznostiPozice[3] and pygame.mouse.get_pos()[1] < moznostiPozice[3] + moznostiSirka[1]:
                    if timeOut < 1:
                        timeOut = 3500
                        if spravneTlacitko == 1:
                            spatnaOdpoved = 2
                            pocetBodu += 1
                        else:
                            spatnaOdpoved = 1
                        pocetOdpovedi += 1
                        
                if pygame.mouse.get_pos()[0] > moznostiPozice[2] and pygame.mouse.get_pos()[0] < moznostiPozice[2] + moznostiSirka[0] and pygame.mouse.get_pos()[1] > moznostiPozice[3] and pygame.mouse.get_pos()[1] < moznostiPozice[3] + moznostiSirka[1]:
                    if timeOut < 1:
                        timeOut = 3500
                        if spravneTlacitko == 2:
                            spatnaOdpoved = 2
                            pocetBodu += 1
                        else:
                            spatnaOdpoved = 1
                        pocetOdpovedi += 1
        
        #otázka
        pygame.draw.rect(screen, (20, 121, 160), pygame.Rect(0, 0, sirka_okna, 100))
        #možnosti
        pygame.draw.rect(screen, (20, 121, 160), pygame.Rect(moznostiPozice[0], moznostiPozice[3], moznostiSirka[0], moznostiSirka[1]))
        pygame.draw.rect(screen, (20, 121, 160), pygame.Rect(moznostiPozice[1], moznostiPozice[3], moznostiSirka[0], moznostiSirka[1]))
        pygame.draw.rect(screen, (20, 121, 160), pygame.Rect(moznostiPozice[2], moznostiPozice[3], moznostiSirka[0], moznostiSirka[1]))
        #otazka otázek
        screen.blit(otazkaText, (sirka_okna/2 - otazkaText.get_rect().width/2, 100/2 - otazkaText.get_rect().height/2))
        #otazka odpovedi
        if spravneTlacitko == 0:
            screen.blit(spravnaOdpovedText, (moznostiPozice[0] + moznostiSirka[0]/2 - spravnaOdpovedText.get_rect().width/2, moznostiPozice[3] + moznostiSirka[1]/2 - spravnaOdpovedText.get_rect().height/2))
            screen.blit(spatnaOdpovedText1, (moznostiPozice[1] + moznostiSirka[0]/2 - spatnaOdpovedText1.get_rect().width/2, moznostiPozice[3] + moznostiSirka[1]/2 - spravnaOdpovedText.get_rect().height/2))
            screen.blit(spatnaOdpovedText2, (moznostiPozice[2] + moznostiSirka[0]/2 - spatnaOdpovedText2.get_rect().width/2, moznostiPozice[3] + moznostiSirka[1]/2 - spravnaOdpovedText.get_rect().height/2))
        if spravneTlacitko == 1 :
            screen.blit(spravnaOdpovedText, (moznostiPozice[1] + moznostiSirka[0]/2 - spravnaOdpovedText.get_rect().width/2, moznostiPozice[3] + moznostiSirka[1]/2 - spravnaOdpovedText.get_rect().height/2))
            screen.blit(spatnaOdpovedText1, (moznostiPozice[0] + moznostiSirka[0]/2 - spatnaOdpovedText1.get_rect().width/2, moznostiPozice[3] + moznostiSirka[1]/2 - spravnaOdpovedText.get_rect().height/2))
            screen.blit(spatnaOdpovedText2, (moznostiPozice[2] + moznostiSirka[0]/2 - spatnaOdpovedText2.get_rect().width/2, moznostiPozice[3] + moznostiSirka[1]/2 - spravnaOdpovedText.get_rect().height/2))
        if spravneTlacitko == 2:
            screen.blit(spravnaOdpovedText, (moznostiPozice[2] + moznostiSirka[0]/2 - spravnaOdpovedText.get_rect().width/2, moznostiPozice[3] + moznostiSirka[1]/2 - spravnaOdpovedText.get_rect().height/2))
            screen.blit(spatnaOdpovedText1, (moznostiPozice[0] + moznostiSirka[0]/2 - spatnaOdpovedText1.get_rect().width/2, moznostiPozice[3] + moznostiSirka[1]/2 - spravnaOdpovedText.get_rect().height/2))
            screen.blit(spatnaOdpovedText2, (moznostiPozice[1] + moznostiSirka[0]/2 - spatnaOdpovedText2.get_rect().width/2, moznostiPozice[3] + moznostiSirka[1]/2 - spravnaOdpovedText.get_rect().height/2))
        #spravne spatne
        if spatnaOdpoved == 1:
            screen.blit(spatnaOdpovedMainText, (sirka_okna/2 - spatnaOdpovedMainText.get_rect().width/2, vyska_okna/2 - spatnaOdpovedMainText.get_rect().height/2))
            nahodnaOtazka = random.choice(otazky)
            spravnaOdpoved = spravne_odpovedi[otazky.index(nahodnaOtazka)]
            spatnaOdpoved1 = spatne_odpovedi1[otazky.index(nahodnaOtazka)]
            spatnaOdpoved2 = spatne_odpovedi2[otazky.index(nahodnaOtazka)]
        elif spatnaOdpoved == 2:
            screen.blit(spravnaOdpovedMainText, (sirka_okna/2 - spravnaOdpovedMainText.get_rect().width/2, vyska_okna/2 - spravnaOdpovedMainText.get_rect().height/2))
            
        if timeOut > 0:
            timeOut -= 1
        if timeOut > 0:
            timeOut -= 1
           
        if timeOut == 0 and not spatnaOdpoved == 0:
            otazkaText, (spravnaOdpovedText,spatnaOdpovedText1, spatnaOdpovedText2), (spatnaOdpovedMainText, spravnaOdpovedMainText), spravneTlacitko = vyberOtazekaspol(otazky,localized_text)
            spatnaOdpoved = 0
        
        if pocetOdpovedi >= 5:
            theme.stop()
            if pocetBodu > 3:
                return True
            elif pocetBodu < 2:
                return False
        
            
        pygame.display.update()
        
