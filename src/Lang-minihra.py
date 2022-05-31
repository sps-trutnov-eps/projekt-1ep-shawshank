import random



opakovat = 0
znamka = 1
vyhra = False



print("Výtej v minihře, ve které budeš muset napsat prvočíslo ve vybraném rozmezí")
print("Čekají na tebe čryři cvičení")
print("Maximálně můžeš udělat dvě chyby")
print("Jdeme na to!")



while opakovat < 4:
    
    rnd = (random.randint(1,10))
    
    opakovat = opakovat + 1
    
    
    
    if rnd == 1:
        
        print()
        print()
        print()
        
        akce1 = int(input("Napiš prvočíslo od 0 do 10: "))
        
        
    
        if akce1 == 2:
            print("Správná odpověd ")
            
        elif akce1 == 3:
            print("Správná odpověd ")
            
        elif akce1 == 5:
            print("Správná odpověd ")
            
        elif akce1 == 7:
            print("Správná odpověd ")



        else:
            print("Špatná odpověd ")
            znamka = znamka + 1
            
            print()
            
            print("řešení: ")
            x = (0)
            y = (10)
            for z in range(x, y+1):
                if z>1:
                    for i in range(2, z):
                        if(z%i) ==0:
                            break
                    else:
                        print(z)
                    
                    
                    
    elif rnd == 2:
        
        print()
        print()
        print()
        
        akce1 = int(input("Napiš prvočíslo od 10 do 20: "))
        
        
        
        if akce1 == 11:
            print("Správná odpověd ")

        elif akce1 == 13:
            print("Správná odpověd ")
            
        elif akce1 == 17:
            print("Správná odpověd ")
                
        elif akce1 == 19:
            print("Správná odpověd ")



        else:
            print("Špatná odpověd ")
            znamka = znamka + 1
            
            print()
            
            print("řešení: ")
            x = (10)
            y = (20)
            for z in range(x, y+1):
                if z>1:
                    for i in range(2, z):
                        if(z%i) ==0:
                            break
                    else:
                        print(z)



    elif rnd == 3:
        
        print()
        print()
        print()
        
        akce1 = int(input("Napiš prvočíslo od 20 do 30: "))
        
        
        
        if akce1 == 23:
            print("Správná odpověd ")

        elif akce1 == 29:
            print("Správná odpověd ")



        else:
            print("Špatná odpověd ")
            znamka = znamka + 1
            
            print()
            
            print("řešení: ")
            x = (20)
            y = (30)
            for z in range(x, y+1):
                if z>1:
                    for i in range(2, z):
                        if(z%i) ==0:
                            break
                    else:
                        print(z)
                    
                    
                    


    elif rnd == 4:
        
        print()
        print()
        print()
        
        akce1 = int(input("Napiš prvočíslo od 30 do 40: "))
        
        
        
        if akce1 == 31:
            print("Správná odpověd ")

        elif akce1 == 37:
            print("Správná odpověd ")



        else:
            print("Špatná odpověd ")
            znamka = znamka + 1
            
            print()
            
            print("řešení: ")
            x = (30)
            y = (40)
            for z in range(x, y+1):
                if z>1:
                    for i in range(2, z):
                        if(z%i) ==0:
                            break
                    else:
                        print(z)
                    
                    
                     
        
        
    elif rnd == 5:
        
        print()
        print()
        print()
        
        akce1 = int(input("Napiš prvočíslo od 40 do 50: "))
        
        
        
        if akce1 == 41:
            print("Správná odpověd ")

        elif akce1 == 43:
            print("Správná odpověd ")
            
        elif akce1 == 47:
            print("Správná odpověd ")



        else:
            print("Špatná odpověd ")
            znamka = znamka + 1
            
            print()
            
            print("řešení: ")
            x = (40)
            y = (50)
            for z in range(x, y+1):
                if z>1:
                    for i in range(2, z):
                        if(z%i) ==0:
                            break
                    else:
                        print(z)
                    
                    
                    
        
        
    elif rnd == 6:
        
        print()
        print()
        print()
        
        akce1 = int(input("Napiš prvočíslo od 50 do 60: "))
        
        
        
        if akce1 == 53:
            print("Správná odpověd ")

        elif akce1 == 59:
            print("Správná odpověd ")



        else:
            print("Špatná odpověd ")
            znamka = znamka + 1
            
            print()
            
            print("řešení: ")
            x = (50)
            y = (60)
            for z in range(x, y+1):
                if z>1:
                    for i in range(2, z):
                        if(z%i) ==0:
                            break
                    else:
                        print(z)
                    
                    
                     
        
        
    elif rnd == 7:
        
        print()
        print()
        print()
        
        akce1 = int(input("Napiš prvočíslo od 60 do 70: "))
        
        
        
        if akce1 == 61:
            print("Správná odpověd ")

        elif akce1 == 67:
            print("Správná odpověd ")



        else:
            print("Špatná odpověd ")
            znamka = znamka + 1
            
            print()
            
            print("řešení: ")
            x = (60)
            y = (70)
            for z in range(x, y+1):
                if z>1:
                    for i in range(2, z):
                        if(z%i) ==0:
                            break
                    else:
                        print(z)
                    
                    
                    
        
        
    elif rnd == 8:
        
        print()
        print()
        print()
        
        akce1 = int(input("Napiš prvočíslo od 70 do 80: "))
        
        
        
        if akce1 == 71:
            print("Správná odpověd ")

        elif akce1 == 73:
            print("Správná odpověd ")
            
        elif akce1 == 79:
            print("Správná odpověd ")



        else:
            print("Špatná odpověd ")
            znamka = znamka + 1
            
            print()
            
            print("řešení: ")
            x = (70)
            y = (80)
            for z in range(x, y+1):
                if z>1:
                    for i in range(2, z):
                        if(z%i) ==0:
                            break
                    else:
                        print(z)
                    
                    
                       
        
        
    elif rnd == 9:
        
        print()
        print()
        print()
        
        akce1 = int(input("Napiš prvočíslo od 80 do 90: "))
        
        
        
        if akce1 == 83:
            print("Správná odpověd ")
            
        elif akce1 == 89:
            print("Správná odpověd ")



        else:
            print("Špatná odpověd ")
            znamka = znamka + 1
            
            print()
            
            print("řešení: ")
            x = (80)
            y = (90)
            for z in range(x, y+1):
                if z>1:
                    for i in range(2, z):
                        if(z%i) ==0:
                            break
                    else:
                        print(z)



    elif rnd == 10:
        
        print()
        print()
        print()
        
        akce1 = int(input("Napiš prvočíslo od 90 do 100: "))
        
        
        
        if akce1 == 97:
            print("Správná odpověd ")



        else:
            print("Špatná odpověd ")
            znamka = znamka + 1
            
            print()
            
            print("řešení: ")
            x = (90)
            y = (100)
            for z in range(x, y+1):
                if z>1:
                    for i in range(2, z):
                        if(z%i) ==0:
                            break
                    else:
                        print(z)
                        
                    
                    
                    
else:
    print()
    print()
    print()
    
    print("Známka: ")
    print(znamka)
    
    
    
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