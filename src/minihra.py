import pygame 
import random
import sys
import time

sirka_okno = 776
vyska_okno = 448
zelena = (124, 252, 0)

okno = pygame.display.set_mode((sirka_okno, vyska_okno))
pygame.init()

handle = open("otazky-dejepis.txt", "r", encoding = "utf-8")
vsechny_otazky = handle.read()
handle.close()

handle = open("odpovedi-dejepis.txt", "r", encoding = "utf-8")
vsechny_odpovedi = handle.read()
handle.close()

spravne_odpovedi = vsechny_odpovedi.strip().split("\n")
otazky= vsechny_otazky.strip().split("\n")

font = pygame.font.SysFont("timesnewroman", 20)
text = font.render(random.choice(otazky), True, (255, 255, 255))

while (True):
    udalosti = pygame.event.get()
    
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    okno.fill((70, 150, 0))
    pygame.display.update()

spravne_odpovedi = vsechny_odpovedi.strip().split("\n") 
otazky_dejepis = vsechny_otazky.strip().split("\n") 
 
font = pygame.font.SysFont("timesnewroman", 20) 
text = font.render(random.choice(otazky-dejepis), True, (255, 255, 255)) 
 
vyplneneTlacitko = random.choice(range(0,5)) 
print(vyplneneTlacitko) 
    
if u.type == pygame.MOUSEBUTTONDOWN and u.button == 1: 
    if vyplneneTlacitko == 0 and pygame.mouse.get_pos()[0] > moznostiPozice[0] and pygame.mouse.get_pos()[0] < moznostiPozice[0] + moznostiSirka[0] and pygame.mouse.get_pos()[1] > moznostiPozice[3] and pygame.mouse.get_pos()[1] < moznostiPozice[3] + moznostiSirka[1]: 
            print("Správně") 
    if vyplneneTlacitko == 1 and pygame.mouse.get_pos()[0] > moznostiPozice[1] and pygame.mouse.get_pos()[0] < moznostiPozice[1] + moznostiSirka[0] and pygame.mouse.get_pos()[1] > moznostiPozice[3] and pygame.mouse.get_pos()[1] < moznostiPozice[3] + moznostiSirka[1]: 
            print("Správně") 
    if vyplneneTlacitko == 2 and pygame.mouse.get_pos()[0] > moznostiPozice[2] and pygame.mouse.get_pos()[0] < moznostiPozice[2] + moznostiSirka[0] and pygame.mouse.get_pos()[1] > moznostiPozice[3] and pygame.mouse.get_pos()[1] < moznostiPozice[3] + moznostiSirka[1]: 
            print("Správně")     
pocet_otazek = 5 
 
print("1:") 
nahodna_otazka1 = random.choice(otazky) 
print(nahodna_otazka1) 
poradi_otazky1 = otazky.index(nahodna_otazka1) 
spravna_odpoved1 = spravne_odpovedi[poradi_otazky1] 
if spravna_odpoved1 == input() : 
    print("Správně")    
     
else: 
    print("ŠPATNĚ") 
     
print("2:") 
nahodna_otazka2 = random.choice(otazky) 
print(nahodna_otazka2) 
poradi_otazky2 = otazky.index(nahodna_otazka2) 
spravna_odpoved2 = spravne_odpovedi[poradi_otazky2] 
if spravna_odpoved2 == input() : 
    print("Správně") 
       
else: 
    print("ŠPATNĚ") 
     
print("3:") 
nahodna_otazka3 = random.choice(otazky) 
print(nahodna_otazka3) 
poradi_otazky3 = otazky.index(nahodna_otazka3) 
spravna_odpoved3 = spravne_odpovedi[poradi_otazky3] 
if spravna_odpoved3 == input() : 
    print("Správně") 
   
else: 
    print("ŠPATNĚ") 
     
print("4:") 
nahodna_otazka4 = random.choice(otazky) 
print(nahodna_otazka4) 
poradi_otazky4 = otazky.index(nahodna_otazka4) 
spravna_odpoved4 = spravne_odpovedi[poradi_otazky4] 
if spravna_odpoved4 == input() : 
    print("Správně") 
         
else: 
    print("ŠPATNĚ") 
     
print("5:") 
nahodna_otazka5 = random.choice(otazky) 
print(nahodna_otazka5) 
poradi_otazky5 = otazky.index(nahodna_otazka5) 
spravna_odpoved5 = spravne_odpovedi[poradi_otazky5] 
if spravna_odpoved5 == input() : 
    print("Správně") 

pygame.quit() 
sys.exit() 










