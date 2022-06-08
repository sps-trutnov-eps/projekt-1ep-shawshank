import random



opakovat = 0
znamka = 1
vyhra = False



def odpoved(x, y):
    print("řešení: ")
    for z in range(x, y+1):
        if z>1:
            for i in range(2, z):
                if(z%i) ==0:
                    break
            else:
                print(z)
                
def otazka(zacatek, konec, odpovedi):
    print("\n\n\n")
    
    akce = int(input("Napiš prvočíslo od " + str(zacatek) + " do " + str(konec) + ": "))

    if akce in odpovedi:
        print("Správná odpověd ")
        
    else:
        print("Špatná odpověd \n")
        znamka = znamka + 1
        
        odpoved(zacatek, konec)                    




print("Výtej v minihře, ve které budeš muset napsat prvočíslo ve vybraném rozmezí")
print("Čekají na tebe čryři cvičení")
print("Maximálně můžeš udělat dvě chyby")
print("Jdeme na to!")



while opakovat < 4:
    
    rnd = (random.randint(1,10))
    
    opakovat = opakovat + 1
    
    if rnd == 1:
        otazka(0, 10, (2, 3, 5, 7))                    
                    
    elif rnd == 2:
        otazka(10, 20, (11, 13, 17, 19))

    elif rnd == 3:
        otazka(20, 30, (23, 29))
        
    elif rnd == 4:
        otazka(30, 40, (31, 37))
        
    elif rnd == 5:
        otazka(40, 50, (41, 43, 47))
        
    elif rnd == 6:
        otazka(50, 60, (53, 59))
        
    elif rnd == 7:
        otazka(60, 70, (61, 67))
        
    elif rnd == 8:
        otazka(70, 80, (71, 73, 79))
        
    elif rnd == 9:
        otazka(80, 90, (83, 89))

    elif rnd == 10:
        otazka(90, 100, (97, random.randint(1000, 10000000)))
                    
else:
    print("\n\n\nZnámka: " + str(znamka))    
    
    
if znamka == 1:
    print("Výborně, úspěšně jsi dokončil minihru s plným počtem bodů!")
    vyhra = True

if znamka == 2:
    vyhra = True
    print("Výborně, úspěšně jsi dokončil minihru!")
    
if znamka == 3:
    vyhra = False
    print("Bohužel, k výhře ti chyběl jeden bod")
    
if znamka == 4:
    vyhra = False
    print("Bohužel, ale to ti stačit nebude")

if znamka == 5:
    vyhra = False
    print("To se ti nepovedlo, nezískal jsi ani jeden bod")