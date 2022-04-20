print("Vítejte u ustního zkoušení ze zěměpisu")
print("Tak začneme")
znamka = 6
pocet_otazek=5

odpoved = input("Otázka 1 : Jaké hlavní město má Česká Rebublika ?")
if odpoved == "Praha" or odpoved == "praha" :
    print("Správně !")
    znamka -= 1
else:
    print("Špatně")
    
odpoved1 = input("Otázka 2: Jaký je největší oceán na světě? ")
if odpoved1 == "Tichý oceán" or odpoved1 == "tichý oceán" or odpoved1 == "Pacifický oceán" or odpoved1 == "pacifický oceán" or odpoved1 == "Pacifik" or odpoved1 == "pacifik"or odpoved1 == "tichý" or odpoved1== "Tichý" or odpoved1 == "Pacifický" or odpoved1 == "pacifický" :
    print("Správně !")
    znamka -= 1
else:
    print("Špatně")
     
odpoved2 = input("Otázka 3: Jaké je hlavní město Spojených Států Amerických ? ")
if odpoved2 == "Washington D.C." or odpoved2 == "washington D.C." or odpoved2 == "washington d.c." or odpoved2 == "Washington d.c." or odpoved2 == "washington dc" or odpoved2 == "washington DC" or odpoved2== "Washington" or odpoved2== "washington" :
    print("Správně !")
    znamka -= 1
elif odpoved2 == "New York" or odpoved2 == "new york" :
    print("XD si dement")
else:
    print("Špatně")
    
odpoved3 = input("Otázka 4 : Ve kterém státě žije Papež ?")
if odpoved3 == "Vatikán" or odpoved3 == "vatikán" :
    print("Správně")
    znamka -= 1
else:
    print("Špatně")
    
odpoved4 = input("Otázka 5 : Jaká je nejvetší hora světa ? ")
if odpoved4 == "Mount Everest" or odpoved3 == "mount everest" or odpoved4== "Everest" or odpoved4 == "everest" or odpoved4 == " mount Everest" :
    print("Správně")
    znamka -= 1
else:
    print("Špatně")
    
if znamka == 6 :
    print("Dostal jste za 5")    
    
else:
    print("Dostal jste:")     
    print(znamka)    

