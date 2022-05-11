import random
import sys
import pygame

sirka_okna = 800
vyska_okna = 600

cerna = (0, 0, 0)
bila = (255, 255, 255)
cervena = (255, 0, 0)
zelena = (0, 255, 0)
modra = (0, 0, 255)

pygame.init()
okno = pygame.display.set_mode((sirka_okna, vyska_okna))
pygame.display.set_caption("Zeměpis")


#nacteni-otazek
handle = open("otazky.txt", "r", encoding = "utf-8")
vsechny_otazky = handle.read()
handle.close()

#nacteni-odpovedi
handle = open("odpovedi.txt", "r", encoding = "utf-8")
vsechny_odpovedi = handle.read()
handle.close()

#Rozdeleni-na-radky
spravne_odpovedi = vsechny_odpovedi.strip().split("\n")
otazky= vsechny_otazky.strip().split("\n")

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

while True:
    okno.fill(bila)
    pygame.display.update()


pygame.quit()
sys.exit()

    

