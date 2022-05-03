import random

#nacteni-otazek
handle = open("otazky.txt", "r", encoding = "utf-8")
vsechny_otazky = handle.read()
handle.close()

#nacteni-odpovedi
handle = open("odpovedi.txt", "r", encoding = "utf-8")
vsechny_odpovedi = handle.read()
handle.close()

spravna_odpoved = vsechny_odpovedi.strip().split("\n")
otazky= vsechny_otazky.strip().split("\n")

print("Vítejte u ustního zkoušení ze zěměpisu")
print("Tak začneme")
znamka = 6
pocet_otazek=5

print("Otázka 1: ")
input(random.choice(otazky))
print(random.choice(spravna_odpoved))



if znamka == 6:
    print("Dostal jste za 5 <_>")
else:
    print("Dostal jste", znamka)



