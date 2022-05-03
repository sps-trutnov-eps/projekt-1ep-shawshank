import random

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

print("Vítejte u ustního zkoušení ze zěměpisu")
print("Tak začneme")
znamka = 6
pocet_otazek=5

print("Otázka 1:")
nahodna_otazka1 = random.choice(otazky)
poradi_otazky = otazky.index(nahodna_otazka1)
input(nahodna_otazka1)
spravna_odpoved1 = (spravne_odpovedi[poradi_otazky])

if nahodna_otazka1 == (spravne_odpovedi[poradi_otazky]):
    print("Správně")
    znamka = znamka - 1
else:
    print("Špatně")
    print(spravna_odpoved1)
    
    
print("Otázka 2:")
nahodna_otazka2 = random.choice(otazky)
poradi_otazky = otazky.index(nahodna_otazka2)
input(nahodna_otazka2)
spravna_odpoved1 = (spravne_odpovedi[poradi_otazky])

if nahodna_otazka2 == (spravne_odpovedi[poradi_otazky]):
    print("Správně")
    znamka = znamka - 1
else:
    print("Špatně")
    print(spravna_odpoved1)    

print("Otázka 3:")
nahodna_otazka3 = random.choice(otazky)
poradi_otazky = otazky.index(nahodna_otazka3)
input(nahodna_otazka3)
spravna_odpoved1 = (spravne_odpovedi[poradi_otazky])

if nahodna_otazka3 == (spravne_odpovedi[poradi_otazky]):
    print("Správně")
    znamka = znamka - 1
else:
    print("Špatně")
    print(spravna_odpoved1)    

print("Otázka 4:")
nahodna_otazka4 = random.choice(otazky)
poradi_otazky = otazky.index(nahodna_otazka4)
input(nahodna_otazka4)
spravna_odpoved1 = (spravne_odpovedi[poradi_otazky])

if nahodna_otazka4 == (spravne_odpovedi[poradi_otazky]):
    print("Správně")
    znamka = znamka - 1
else:
    print("Špatně")
    print(spravna_odpoved1)    

print("Otázka 5:")
nahodna_otazka5 = random.choice(otazky)
poradi_otazky = otazky.index(nahodna_otazka5)
input(nahodna_otazka5)
spravna_odpoved1 = (spravne_odpovedi[poradi_otazky])

if nahodna_otazka5 == (spravne_odpovedi[poradi_otazky]):
    print("Správně")
    znamka = znamka - 1
else:
    print("Špatně")
    print(spravna_odpoved1)




if znamka == 6:
    print("Dostal jste za 5 <_>")
else:
    print("Dostal jste", znamka)



