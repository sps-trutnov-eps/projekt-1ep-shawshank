import random
import sys
import pygame

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

#nacteni-otazek
handle = open("otazky.txt", "r", encoding = "utf-8")
vsechny_otazky = handle.read()
handle.close()

#nacteni-odpovedi
handle = open("odpovedi.txt", "r", encoding = "utf-8")
vsechny_odpovedi = handle.read()
handle.close()

#nacteni-spatnych-odpovedi
handle = open("spatna_odpoved1.txt", "r", encoding = "utf-8")
spatna_odpoved1 = handle.read()
handle.close()

handle = open("spatna_odpoved2.txt", "r", encoding = "utf-8")
spatna_odpoved2 = handle.read()
handle.close()


#Rozdeleni-na-radky
spravne_odpovedi = vsechny_odpovedi.strip().split("\n")
otazky = vsechny_otazky.strip().split("\n")
spatne_odpovedi1 = spatna_odpoved1.strip().split("\n")
spatne_odpovedi2 = spatna_odpoved2.strip().split("\n")

nahodnaOtazka = random.choice(otazky)
spravnaOdpoved = spravne_odpovedi[otazky.index(nahodnaOtazka)]
spatnaOdpoved1 = spatne_odpovedi1[otazky.index(nahodnaOtazka)]
spatnaOdpoved2 = spatne_odpovedi2[otazky.index(nahodnaOtazka)]

font = pygame.font.SysFont("Consolas", 20)
otazkaText = font.render(nahodnaOtazka, True, (255, 255, 255))
spravnaOdpovedText = font.render(spravnaOdpoved, True, (255, 255, 255))
spatnaOdpovedText1 = font.render(spatnaOdpoved1, True, (255, 255, 255))
spatnaOdpovedText2 = font.render(spatnaOdpoved2, True, (255, 255, 255))

spatnaOdpovedMainText = font.render(f"Špatná odpověd, správně je: {spravnaOdpoved}", True, (255, 255, 255))

spravneTlacitko = random.choice(range(0,3))
print(spravneTlacitko)

spatnaOdpoved = False

while(True):
    udalosti = pygame.event.get()
    
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((50, 141, 176))
    
    if u.type == pygame.MOUSEBUTTONDOWN and u.button == 1:
        if pygame.mouse.get_pos()[0] > moznostiPozice[0] and pygame.mouse.get_pos()[0] < moznostiPozice[0] + moznostiSirka[0] and pygame.mouse.get_pos()[1] > moznostiPozice[3] and pygame.mouse.get_pos()[1] < moznostiPozice[3] + moznostiSirka[1]:
            if spravneTlacitko == 0:
                print("Správně")
            else:
                print("Špatně")
                spatnaOdpoved = True
            
        if pygame.mouse.get_pos()[0] > moznostiPozice[1] and pygame.mouse.get_pos()[0] < moznostiPozice[1] + moznostiSirka[0] and pygame.mouse.get_pos()[1] > moznostiPozice[3] and pygame.mouse.get_pos()[1] < moznostiPozice[3] + moznostiSirka[1]:
            if spravneTlacitko == 1:
                print("Správně")
            else:
                print("Špatně")
                spatnaOdpoved = True
                
        if pygame.mouse.get_pos()[0] > moznostiPozice[2] and pygame.mouse.get_pos()[0] < moznostiPozice[2] + moznostiSirka[0] and pygame.mouse.get_pos()[1] > moznostiPozice[3] and pygame.mouse.get_pos()[1] < moznostiPozice[3] + moznostiSirka[1]:
            if spravneTlacitko == 2:
                print("Správně")
            else:
                print("Špatně")
                spatnaOdpoved = True
    
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
    #sravne spatne
    if spatnaOdpoved == True:
        screen.blit(spatnaOdpovedMainText, (sirka_okna/2 - spatnaOdpovedMainText.get_rect().width/2, vyska_okna/2 - spatnaOdpovedMainText.get_rect().height/2))
        nahodnaOtazka = random.choice(otazky)
        spravnaOdpoved = spravne_odpovedi[otazky.index(nahodnaOtazka)]
        spatnaOdpoved1 = spatne_odpovedi1[otazky.index(nahodnaOtazka)]
        spatnaOdpoved2 = spatne_odpovedi2[otazky.index(nahodnaOtazka)]
    
    
    pygame.display.update()
    
    













#otázky
               
print("Vítejte u ustního zkoušení ze zěměpisu")
print("Tak začneme")
znamka = 6
pocet_otazek=5

print("Otázka 1:")
nahodna_otazka1 = random.choice(otazky)
print(nahodna_otazka1)
poradi_otazky1 = otazky.index(nahodna_otazka1)
spravna_odpoved1 = spravne_odpovedi[poradi_otazky1]
if spravna_odpoved1 == input() :
    print("Správně")
    znamka = znamka - 1
    
else:
    print("ŠPATNĚ")
    
  
    
print("Otázka 2:")
nahodna_otazka2 = random.choice(otazky)
print(nahodna_otazka2)
poradi_otazky2 = otazky.index(nahodna_otazka2)
spravna_odpoved2 = spravne_odpovedi[poradi_otazky2]
if spravna_odpoved2 == input() :
    print("Správně")
    znamka = znamka - 1
    
else:
    print("ŠPATNĚ")
    
print("Otázka 3:")
nahodna_otazka3 = random.choice(otazky)
print(nahodna_otazka3)
poradi_otazky3 = otazky.index(nahodna_otazka3)
spravna_odpoved3 = spravne_odpovedi[poradi_otazky3]
if spravna_odpoved3 == input() :
    print("Správně")
    znamka = znamka - 1
    
else:
    print("ŠPATNĚ")
    
print("Otázka 4:")
nahodna_otazka4 = random.choice(otazky)
print(nahodna_otazka4)
poradi_otazky4 = otazky.index(nahodna_otazka4)
spravna_odpoved4 = spravne_odpovedi[poradi_otazky4]
if spravna_odpoved4 == input() :
    print("Správně")
    znamka = znamka -1 
    
else:
    print("ŠPATNĚ")
    
print("Otázka 5:")
nahodna_otazka5 = random.choice(otazky)
print(nahodna_otazka5)
poradi_otazky5 = otazky.index(nahodna_otazka5)
spravna_odpoved5 = spravne_odpovedi[poradi_otazky5]
if spravna_odpoved5 == input() :
    print("Správně")
    znamka = znamka - 1
    
else:
    print("ŠPATNĚ")      
    
#konecna-znamka    
    
if znamka == 6 :
    print("Hodně špatný výkon, za 5 !!!")
else:
    print("Dostal si za", znamka)
    
if znamka < 5:
    život = True
else:
    život = False
      
if život == True:
    print("Super! Neumřel jsi!!!")
if život == False:
    print("Tak tady končíme...")


pygame.quit()
sys.exit()

    

