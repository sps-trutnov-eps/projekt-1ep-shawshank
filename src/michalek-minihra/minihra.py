## ToDo input a kontrola řešení, časovač odpovědi
import pygame
import sys
import random

BARVA_POZADI = (0, 20, 0)

pygame.init()
input_active = True

okno = pygame.display.set_mode((736,448))
pygame.display.set_caption("Minihra Martina Michálka")

seznam_zadani = {"1 + 1 =":"2", "5 - 4 =":"1"}
odpoved = ""
spravne = ""
spravneb = (0, 25, 0)
notazek = random.randint(1, 5)

while notazek > 0:
    zadani = random.choice(list(seznam_zadani))
    reseni = seznam_zadani[zadani]
    whpriklad = True
    while whpriklad:
        udalost = pygame.event.get()
        stisknuto = pygame.key.get_pressed()
        
        for u in udalost:
            if u.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif u.type == pygame.KEYDOWN and input_active:
                if u.key == pygame.K_RETURN:
                    input_active = False
                elif u.key == pygame.K_BACKSPACE:
                    if len(odpoved)>0:
                        odpoved = odpoved[:-1]
                else:
                    odpoved += u.unicode
                    
        if input_active == False:
            if odpoved == reseni:
                spravne = "Správně"
                spravneb = (0, 255, 0)
            else:
                spravne = "Špatně"
                spravneb = (255, 0, 0)
            whpriklad = False
                
                
                
        font = pygame.font.SysFont("Comic Sans MS", 42)
        uloha = font.render(zadani, True, (255, 255, 255))
        odpovedin = font.render(odpoved, True, (255, 255, 255))
        spravneout = font.render(spravne, True, (spravneb))
        zbotazky = font.render(str(notazek), True, (255, 255, 0))
        
        okno.fill(BARVA_POZADI)
        okno.blit(uloha, (0,0))
        okno.blit(odpovedin, (0, 50))
        okno.blit(spravneout, (0, 108))
        okno.blit(zbotazky, (650, 0))
            
        pygame.display.update()
    notazek = notazek - 1
print("konec")
pygame.quit()
sys.exit()